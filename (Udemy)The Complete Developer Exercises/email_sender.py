import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def send_bulk_emails(sender_email, sender_password, recipients, subject, message_body, smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send emails to multiple recipients using SMTP.
    
    Parameters:
        sender_email (str): Your email address
        sender_password (str): Your email password or app password
        recipients (list): List of recipient email addresses
        subject (str): Email subject
        message_body (str): Email body content
        smtp_server (str): SMTP server address (default: 'smtp.gmail.com')
        smtp_port (int): SMTP server port (default: 587 for TLS)
    """
    
    try:
        # Create SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure TLS
        server.login(sender_email, sender_password)
        
        # Send email to each recipient
        for recipient in recipients:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject
            
            # Attach message body
            msg.attach(MIMEText(message_body, 'plain'))
            
            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to: {recipient}")
            
        # Close the SMTP connection
        server.quit()
        print("All emails sent successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Email configuration
    YOUR_EMAIL = "your_email@gmail.com"
    YOUR_PASSWORD = "your_password_or_app_password"  # For Gmail, use an App Password if 2FA is enabled
    RECIPIENTS = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
    SUBJECT = "Important Announcement"
    MESSAGE = """Hello,

This is a test email sent using Python's smtplib.

Best regards,
Your Name"""

    # Send emails
    send_bulk_emails(YOUR_EMAIL, YOUR_PASSWORD, RECIPIENTS, SUBJECT, MESSAGE)