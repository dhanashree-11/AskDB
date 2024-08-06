# AskDB
AskDB is a web application designed to convert natural language questions into SQL queries, providing quick data access. The application features multilingual support, displays the used query for retrieving results, allows downloading query results as CSV files, and maintains a query history to enhance user experience.

## Features
- Converts user input in natural language into SQL queries.
- Displays the SQL query that was used to retrieve the result from the database.
- Allows users to download query results as CSV files.
- Maintains Query History
- Multilingual Support

## Installation

To get started with AskDB, follow these steps:

1. **Clone the Repository**
   
   ```bash
   
   git clone https://github.com/yourusername/AskDB.git

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    
3. **Install the Required Packages**:
   
    ```bash
    pip install -r requirements.txt

## Setup

### API Keys

Obtain API keys for Google PaLM2 and any other services you might be using. Store them in a `.env` file in the root directory:

1. Create a `.env` file in the root directory of your project.
2. Add your API keys to the `.env` file:

   ```env
   GOOGLE_PALM2_API_KEY=your_api_key

Streamlit Configuration: Configure Streamlit settings if needed in config.toml.
