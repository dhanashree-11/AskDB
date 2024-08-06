from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sentencepiece

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text.strip()

# Function to retrieve query from the database
def read_sql_query(sql, conn):
    try:
        df_result = pd.read_sql_query(sql, conn)
    except Exception as e:
        df_result = pd.DataFrame()
        st.error(f"Error executing SQL query: {e}")
    return df_result

# Function to generate a prompt based on the DataFrame's schema
def generate_prompt(table_name, df):
    columns = ', '.join(df.columns)
    prompt = f"""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name {table_name} and has the following columns - {columns}.
    For example,
    Example 1 - How many entries of records are present?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM {table_name};
    Example 2 - Tell me all the entries where column X has value Y?, 
    the SQL command will be something like this: SELECT * FROM {table_name} WHERE X="Y";
    Note: The SQL code should not have ``` in the beginning or end and the word "sql" in the output.
    """
    return prompt

# Function to translate text to the target language
def translate_text(text, target_language='en'):
    if target_language == 'en':
        return text  # No translation needed for English
    
    # Load and use a translation model here (assuming a function for translation exists)
    # Example function - replace with actual implementation
    # translated_text = some_translation_function(text, target_language)
    return text  # Placeholder return for non-English translations

# Streamlit App
st.set_page_config(page_title="AskDB", layout="centered")

# Center align title and description with green title and bold text
st.markdown("""
<style>
    .title {
        color: #4CAF50;
        font-size: 4em;
        text-align: center;
        font-weight: bold;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AskDB</div>', unsafe_allow_html=True)
st.markdown("""
<div class="description">
    Welcome to AskDB, Get answer to all your questions !
</div>
""", unsafe_allow_html=True)

# Custom CSS for better styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
    }
    .stTextInput input {
        border: 2px solid #4CAF50;
        border-radius: 4px;
    }
    .stAlert {
        border-radius: 12px;
    }
    .clear-history-button {
        background-color: transparent;
        border: none;
        color: red;
        cursor: pointer;
        font-size: 16px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 0.8rem;
    }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

st.sidebar.header("User Input")
question = st.sidebar.text_input("Enter your question here:", key="input")

# Language selection with full names
language_options = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German'
}

target_language_code = st.sidebar.selectbox(
    "Select target language:",
    options=list(language_options.keys()),
    format_func=lambda code: language_options[code]
)

target_language = target_language_code

# Option to upload multiple Excel or CSV files
uploaded_files = st.sidebar.file_uploader("Upload Excel or CSV files", type=["xlsx", "csv"], accept_multiple_files=True, key="file_uploader")

if st.sidebar.button("Ask the question", key="ask_button"):
    table_name = "USER_DATA"
    conn = None
    all_dfs = []
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_extension = uploaded_file.name.split(".")[-1]
            if file_extension == "xlsx":
                df = pd.read_excel(uploaded_file)
            elif file_extension == "csv":
                df = pd.read_csv(uploaded_file)
            else:
                st.error(f"Unsupported file type: {uploaded_file.name}.")
                df = None
            
            if df is not None:
                all_dfs.append(df)
            else:
                st.error(f"Failed to read the file {uploaded_file.name}.")
        
        if all_dfs:
            combined_df = pd.concat(all_dfs, ignore_index=True)  # Combine all DataFrames
            conn = sqlite3.connect(":memory:")
            combined_df.to_sql(table_name, conn, index=False, if_exists='replace')
            prompt = generate_prompt(table_name, combined_df)
        else:
            st.error("No valid files were uploaded.")
            prompt = ""
    else:
        st.error("Please upload at least one Excel or CSV file.")
        prompt = ""
    
    if prompt:
        if target_language != 'en':
            with st.spinner("Translating question..."):
                translated_question = translate_text(question, target_language)
        else:
            translated_question = question
        
        with st.spinner("Generating SQL query..."):
            response = get_gemini_response(translated_question, prompt)
            st.code(response, language='sql')
        
        if conn:
            with st.spinner("Executing SQL query..."):
                df_result = read_sql_query(response, conn)
                conn.close()
            
            if not df_result.empty:
                st.success("Query executed successfully!")
                st.subheader("Query Results")
                st.dataframe(df_result)

                # Visualization
                st.subheader("Visualizations")
                
                if not df_result.select_dtypes(include='number').empty:
                    # Matplotlib Visualization
                    st.subheader("Matplotlib Visualization")
                    fig, ax = plt.subplots()
                    df_result.plot(kind='bar', ax=ax)
                    st.pyplot(fig)
                else:
                    st.warning("No numeric data available for Matplotlib visualization.")

                if not df_result.select_dtypes(include='number').empty:
                    # Seaborn Visualization
                    st.subheader("Seaborn Visualization")
                    fig, ax = plt.subplots()
                    sns.barplot(data=df_result)
                    st.pyplot(fig)
                else:
                    st.warning("No numeric data available for Seaborn visualization.")
                
                if not df_result.select_dtypes(include='number').empty:
                    # Plotly Visualization
                    st.subheader("Plotly Visualization")
                    numeric_cols = df_result.select_dtypes(include='number').columns
                    if len(numeric_cols) >= 2:
                        fig = px.bar(df_result, x=numeric_cols[0], y=numeric_cols[1])
                        st.plotly_chart(fig)
                    else:
                        st.warning("Not enough numeric columns for Plotly visualization.")
                else:
                    st.warning("No numeric data available for Plotly visualization.")

                # Download results as CSV
                csv = df_result.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download results as CSV",
                    data=csv,
                    file_name='query_results.csv',
                    mime='text/csv',
                )
                
                # Maintain query history
                if 'query_history' not in st.session_state:
                    st.session_state['query_history'] = []
                st.session_state.query_history.append((question, response))

            else:
                st.warning("No results found or an error occurred with the query.")

# Sidebar: Query History and Clear History Button
if 'query_history' in st.session_state:
    st.sidebar.subheader("Query History")
    query_history = st.session_state.query_history
    for idx, (q, r) in enumerate(query_history):
        with st.sidebar.expander(f"Query {idx + 1}"):
            st.write(f"Question: {q}")
            st.code(r, language='sql')

    # Button to clear all history with transparent background
    if st.sidebar.button("Clear Query History", key="clear_history"):
        st.session_state['query_history'] = []
        st.sidebar.success("Query history cleared.")

st.sidebar.markdown("""
#### Example Questions:
- How many entries of records are present?
- Tell me all the entries where column X has value Y.
""")

# Footer
st.markdown("""
    <div class="footer">
        Developed by Team Code Clan For Woodpecker Hackathon
    </div>
""", unsafe_allow_html=True)
