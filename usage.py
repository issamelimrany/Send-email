from app import send_email

# Set the subject of the email
subject = 'Test email'

# Read the HTML content from the file
with open('index.html', 'r') as file:
    body = file.read()

email_receiver = 'skyzlim1@gmail.com'
pdf_file_path = "test.pdf"



send_email(email_receiver, subject, body, pdf_file_path, is_html=True)