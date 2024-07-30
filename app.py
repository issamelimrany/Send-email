import smtplib
import ssl
from email.message import EmailMessage
import mimetypes
import os

# Define email sender and receiver
email_sender = os.environ.get('EMAIL_SENDER')
email_password = os.environ.get('EMAIL_PASSWORD')

# Add SSL ( of security)
context = ssl.create_default_context()

def send_email(email_receiver, subject, body, pdf_path=None, is_html=False): 
    em = EmailMessage()
    
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    
    if is_html:
        em.add_alternative(body, subtype='html')
    else:
        em.set_content(body)
    
    # Attach PDF if provided
    if pdf_path:
        # Guess the MIME type and subtype
        mime_type, _ = mimetypes.guess_type(pdf_path)
        mime_type, mime_subtype = mime_type.split('/')
        
        with open(pdf_path, 'rb') as pdf_file:
            em.add_attachment(pdf_file.read(),
                              maintype=mime_type,
                              subtype=mime_subtype,
                              filename=os.path.basename(pdf_path))
    
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())