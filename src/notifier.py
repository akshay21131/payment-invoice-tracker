"""Payment & Invoice Tracker - Email Notifier"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from tracker import load_payments, flag_overdue

SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "recipient@example.com"
SEND_EMAILS = False

def build_email_body(overdue_df):
    if len(overdue_df) == 0:
        return "<p>No overdue payments. All clear!</p>"
    html = """
    <html><body>
    <h2>Overdue Payment Alert</h2>
    <p>The following invoices are overdue and require immediate attention:</p>
    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;">
    <tr style="background-color:#1F4E78;color:white;">
        <th>Invoice ID</th><th>Client</th><th>Amount (Rs.)</th><th>Days Overdue</th>
    </tr>
    """
    for _, row in overdue_df.iterrows():
        html += f"""
        <tr>
            <td>{row['Invoice_ID']}</td>
            <td>{row['Client_Name']}</td>
            <td>{row['Amount']:,.2f}</td>
            <td style="color:red;font-weight:bold;">{row['Days_Overdue']}</td>
        </tr>
        """
    total = overdue_df['Amount'].sum()
    html += f"""
    </table>
    <p><strong>Total Overdue Amount: Rs. {total:,.2f}</strong></p>
    <p>Please follow up with the respective clients.</p>
    </body></html>
    """
    return html

def send_email(subject, html_body):
    msg = MIMEMultipart('alternative')
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(html_body, 'html'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
    print(f"Email sent to {RECIPIENT_EMAIL}")

def notify_overdue():
    df = load_payments(os.path.join('..', 'data', 'payments.csv'))
    df = flag_overdue(df)
    overdue_df = df[df['Flag'] == 'OVERDUE']
    if len(overdue_df) == 0:
        print("No overdue payments. Nothing to send.")
        return
    subject = f"Payment Alert: {len(overdue_df)} Overdue Invoice(s)"
    html_body = build_email_body(overdue_df)
    if SEND_EMAILS:
        send_email(subject, html_body)
    else:
        print("="*70)
        print("EMAIL PREVIEW (Demo Mode - not actually sent)")
        print("="*70)
        print(f"Subject: {subject}")
        print(f"Would be sent to: {RECIPIENT_EMAIL}")
        print(f"Overdue count: {len(overdue_df)}")
        print(f"Total overdue: Rs. {overdue_df['Amount'].sum():,.2f}")
        print("="*70)

if __name__ == "__main__":
    notify_overdue()
