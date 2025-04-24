# Setting Up and Running the Application

## Create and Activate a Virtual Environment
```bash
# For Linux/macOS
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Launch the Application
```bash
cd src/app
streamlit run app.py
```