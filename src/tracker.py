"""Payment & Invoice Tracker - Core Logic"""
import pandas as pd
from datetime import datetime
import os

def load_payments(file_path):
    df = pd.read_csv(file_path)
    df['Due_Date'] = pd.to_datetime(df['Due_Date'])
    return df

def flag_overdue(df):
    today = pd.Timestamp(datetime.now().date())
    df['Days_Overdue'] = (today - df['Due_Date']).dt.days
    def get_flag(row):
        if row['Status'] == 'Paid':
            return 'PAID'
        elif row['Days_Overdue'] > 0:
            return 'OVERDUE'
        elif row['Days_Overdue'] >= -3:
            return 'DUE SOON'
        else:
            return 'PENDING'
    df['Flag'] = df.apply(get_flag, axis=1)
    return df

def print_summary(df):
    print("\n" + "="*70)
    print("PAYMENT STATUS SUMMARY")
    print("="*70)
    total = len(df)
    paid = len(df[df['Flag'] == 'PAID'])
    overdue = len(df[df['Flag'] == 'OVERDUE'])
    due_soon = len(df[df['Flag'] == 'DUE SOON'])
    pending = len(df[df['Flag'] == 'PENDING'])
    print(f"Total Invoices:     {total}")
    print(f"Paid:               {paid}")
    print(f"Overdue:            {overdue}")
    print(f"Due Soon (3 days):  {due_soon}")
    print(f"Pending (future):   {pending}")
    overdue_amount = df[df['Flag'] == 'OVERDUE']['Amount'].sum()
    print(f"\nTotal Overdue Amount: Rs. {overdue_amount:,.2f}")
    if overdue > 0:
        print("\n--- OVERDUE INVOICES ---")
        overdue_df = df[df['Flag'] == 'OVERDUE'][['Invoice_ID', 'Client_Name', 'Amount', 'Days_Overdue']]
        print(overdue_df.to_string(index=False))
    print("="*70 + "\n")

if __name__ == "__main__":
    file_path = os.path.join('..', 'data', 'payments.csv')
    df = load_payments(file_path)
    df = flag_overdue(df)
    print_summary(df)
