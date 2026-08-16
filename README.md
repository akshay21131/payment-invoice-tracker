# Payment & Invoice Tracker

An automated payment tracking system that reads invoice data from Excel/CSV, flags overdue payments, generates color-coded MIS status reports, and sends email alerts for overdue accounts.

## Features
- Automated tracking: reads invoice data and calculates days overdue
- Color-coded Excel reports (Red = Overdue, Yellow = Due Soon, Green = Paid)
- Email alerts via SMTP for overdue invoices
- MIS summary with total counts and overdue amounts

## Tech Stack
Python 3, Pandas, OpenPyXL, SMTP

## Project Structure

    payment-invoice-tracker/
    ├── data/payments.csv
    ├── src/
    │   ├── tracker.py
    │   ├── report.py
    │   └── notifier.py
    ├── output/status_report.xlsx
    ├── requirements.txt
    └── README.md

## How to Run

    pip install -r requirements.txt
    cd src
    python tracker.py
    python report.py
    python notifier.py

## Use Case
Designed to reduce manual reconciliation effort in payment tracking workflows — commonly needed in finance operations, MIS reporting, and vendor payment management.

## Author
Akshay Kumar | GitHub: akshay21131
