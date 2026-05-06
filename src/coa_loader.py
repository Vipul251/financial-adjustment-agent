import pandas as pd

def load_coa(file):
    df = pd.read_csv(file)
    
    # Normalize account codes
    df['account_code'] = df['account_code'].astype(str).str.strip()
    
    return set(df['account_code'])