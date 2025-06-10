# Import necessary libraries
import os  # For accessing environment variables and operating system functions
import smtplib  # For sending emails using SMTP protocol
from email.mime.text import MIMEText  # For creating email text content
from email.mime.multipart import MIMEMultipart  # For creating multi-part email messages
from email.utils import formatdate  # For properly formatting dates in email headers
from getpass import getpass  # For securely getting password input (hides typing)
import re  # For regular expressions (email validation)

def validate_email(email):
    """Check if an email address is properly formatted using regex pattern matching"""
    # This pattern checks for standard email format: name@domain.tld
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Return True if the email matches the pattern, False otherwise
    return re.match(pattern, email) is not None # makes the return value a boolean instead of string

def get_email_credentials():
    """
    Safely get email credentials either from environment variables or user input
    Returns a tuple containing (email_address, password)
    """
    # Try to get credentials from environment variables first (more secure)
    email = os.getenv('SMTP_EMAIL')  # Get email from SMTP_EMAIL environment variable
    password = os.getenv('SMTP_PASSWORD')  # Get password from SMTP_PASSWORD environment variable
    
    # This "if"-statement will handle when the os.getenv variable is not set
    # In our code, environment variables aren't set, instead of setting we ask user for input
    if not email or not password:
        print("Environment variables not found. Please enter your credentials:")
        
        # Keep asking for email until a valid one is provided
        while True:
            email = input("Email address: ").strip()  # Get email input
            if validate_email(email):  # Check if email is valid
                break  # Exit loop if valid
            print("Invalid email format. Please try again.")  # Show error if invalid
        
        # Get password securely (input won't be shown on screen)
        password = getpass("Password (input hidden): ").strip()
    
    # Return the collected credentials
    return email, password

def send_bulk_emails(sender_email, sender_password, recipients, subject, message_body, smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send emails to multiple recipients using SMTP protocol
    Parameters:
        sender_email: Your email address
        sender_password: Your email password
        recipients: List of email addresses to send to
        subject: Email subject line
        message_body: Content of the email
        smtp_server: Mail server address (default: Gmail)
        smtp_port: Connection port (default: 587 for TLS encryption)
    """
    
    # First check if any recipient emails are invalid
    invalid_emails = [email for email in recipients if not validate_email(email)]
    if invalid_emails:
        print(f"Warning: These recipient emails appear invalid: {', '.join(invalid_emails)}")
        proceed = input("Continue anyway? (y/n): ").lower()  # Ask user if they want to proceed
        if proceed != 'y':  # If not 'y', cancel sending
            print("Email sending cancelled.")
            return
    
    try:
        # Create a connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS encryption for secure connection
            server.starttls()
            
            # Login to the email account
            server.login(sender_email, sender_password)
            
            # Send email to each recipient
            for recipient in recipients:
                try:
                    # Create a new email message container
                    msg = MIMEMultipart()
                    
                    # Set email headers
                    msg['From'] = sender_email  # Who the email is from
                    msg['To'] = recipient  # Who the email is to
                    msg['Date'] = formatdate(localtime=True)  # Current date/time
                    msg['Subject'] = subject  # Email subject
                    
                    # Attach the message body as plain text
                    msg.attach(MIMEText(message_body, 'plain'))
                    
                    # Send the email
                    server.sendmail(sender_email, recipient, msg.as_string())
                    print(f"Email sent to: {recipient}")
                    
                except Exception as e:
                    # If sending to one recipient fails, continue with others
                    print(f"Failed to send to {recipient}: {str(e)}")
                    continue
            
        # This prints when all emails are sent successfully
        print("Email sending process completed.")
        
    except Exception as e:
        # This catches any major errors in the sending process
        print(f"Error occurred: {str(e)}")

# This runs when the script is executed directly (not imported as a module)
if __name__ == "__main__":
    print("=== Bulk Email Sender ===")
    
    # Step 1: Get email credentials securely
    sender_email, sender_password = get_email_credentials()
    
    # Step 2: Get list of recipients
    print("\nEnter recipient email addresses (separated by commas):")
    recipients_input = input("Recipients: ").strip()  # Get user input
    # Split input by commas, remove whitespace, and ignore empty entries
    recipients = [email.strip() for email in recipients_input.split(',') if email.strip()]
    
    # Check if we have at least one recipient
    if not recipients:
        print("No valid recipients provided. Exiting.")
        exit()  # Quit the program if no recipients
    
    # Step 3: Get email subject
    subject = input("Subject: ").strip()
    
    # Step 4: Get email message body
    print("Message body (press Enter then Ctrl+D on empty line to finish):")
    message_lines = []  # Store each line of the message
    while True:
        try:
            line = input()  # Get each line of input
        except EOFError:  # When user presses Ctrl+D
            break  # Exit the input loop
        message_lines.append(line)  # Add the line to our message
    
    # Combine all lines into a single message body
    message_body = '\n'.join(message_lines)
    
    # Step 5: Show confirmation before sending
    print(f"\nAbout to send to {len(recipients)} recipients:")
    print(f"Subject: {subject}")
    print("Message:")
    print(message_body)
    confirm = input("\nConfirm sending? (y/n): ").lower()  # Get confirmation
    
    # Step 6: Send emails if confirmed
    if confirm == 'y':
        send_bulk_emails(
            sender_email=sender_email,
            sender_password=sender_password,
            recipients=recipients,
            subject=subject,
            message_body=message_body
        )
    else:
        print("Email sending cancelled.")