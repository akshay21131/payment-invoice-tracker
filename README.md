# Payment & Invoice Tracker

An automated payment tracking system that reads invoice data from CSV, flags overdue payments, generates color-coded MIS-style Excel reports, and previews email alerts for overdue accounts.

## Features

- Reads invoice/payment records from CSV
- Automatically calculates days overdue
- Flags invoices as PAID, OVERDUE, DUE SOON, or PENDING
- Generates a color-coded Excel report using OpenPyXL
- Creates a summary sheet with invoice counts and overdue amount
- Previews email alerts for overdue payments using SMTP logic
- Useful for payment review, finance operations, MIS reporting, and follow-up tracking

## Tech Stack

- Python 3
- Pandas
- OpenPyXL
- SMTP / Email MIME (built-in)

## Project Structure

    payment-invoice-tracker/
    ├── data/
    │   └── payments.csv           # Invoice records (input)
    ├── src/
    │   ├── tracker.py             # Core logic + terminal summary
    │   ├── report.py              # Excel report generator
    │   └── notifier.py            # Email notification preview
    ├── output/
    │   └── status_report.xlsx     # Generated report (auto-created)
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Prerequisites

- Python 3.8 or higher
- pip (comes with Python)
- Git

Verify installation:

    python --version
    pip --version
    git --version

## How to Run on Any System

### Step 1 — Clone the repository

    git clone https://github.com/akshay21131/payment-invoice-tracker.git
    cd payment-invoice-tracker

### Step 2 — Install dependencies

    pip install -r requirements.txt

### Step 3 — Run the scripts (from inside src folder)

    cd src

**View terminal summary of all invoices:**

    python tracker.py

**Generate the color-coded Excel report:**

    python report.py

The report will be saved to output/status_report.xlsx with two tabs:
- Payment Status (full data with color-coded rows)
- Summary (quick metrics view)

**Preview email alerts for overdue invoices:**

    python notifier.py

By default runs in demo mode (prints preview only).

### Step 4 — Enable Real Email Sending (Optional)

Open src/notifier.py and update these lines:

    SENDER_EMAIL = "your-email@gmail.com"
    SENDER_PASSWORD = "your-app-password"
    RECIPIENT_EMAIL = "recipient@example.com"
    SEND_EMAILS = True

Note: For Gmail, you need an App Password (not your regular password). Generate one at: https://support.google.com/accounts/answer/185833

## Sample Data

The included data/payments.csv has 10 sample invoices covering paid, overdue, and pending statuses. Replace with your own data using the same column structure:

| Column | Type | Description |
|--------|------|-------------|
| Invoice_ID | Text | Unique invoice identifier |
| Client_Name | Text | Client or vendor name |
| Amount | Number | Invoice amount |
| Due_Date | Date (YYYY-MM-DD) | Payment due date |
| Status | Text | Paid or Pending |
| Notes | Text | Optional notes |

## Use Case

Designed to reduce manual reconciliation effort in payment tracking workflows — commonly needed in:
- Finance operations
- MIS reporting
- Vendor payment management
- Accounts receivable follow-up
- Procurement coordination

## Author

**Akshay Kumar**  
GitHub: https://github.com/akshay21131
