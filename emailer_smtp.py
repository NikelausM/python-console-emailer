import argparse, re, getpass, smtplib, ssl
from enum import Enum, IntEnum

# Encryption types
class Encryption(Enum):
    """Enumerate email encryption types

    Specifies the types of email encryption available.
    """
    SSL = "ssl"
    TLS = "tls"

# Emails with GMAIL
# port 465 for SSL encryption
# port 587 for TLS encryption
class Port(IntEnum):
    SSL = 465
    TLS = 587

# Emailer class
class Emailer:
    def validateEmail(self, email):
        if(re.match(r"[^@]+@[^@]+\.[^@]+", email)):
            return True
        else:
            print("invalid email")
            return False

    def get_user_credentials(self):

        """Prompt user for their email credentials"""
        isValidEmail = False
        while(not isValidEmail):
            self.sender_email = input("Please enter your email (e.g., john@gmail.com): ")
            isValidEmail = self.validateEmail(self.sender_email)

        # Get password
        self.sender_pass = getpass.getpass("enter your password: ")

    def set_display_name(self):
        """Set optional display name"""
        option = input(f"Do you want to include a display name for the email (email will show as from {self.sender_email} otherwise [y/n]: ").lower()
        isInputValid = False
        while(not isInputValid):
            if(option == "y"):
                self.sender_display_name = input("Please enter your display name: ")
                self.message = f"From: {self.sender_display_name} <{self.sender_email}>\n"

                isInputValid = True
            elif(option == "n"):
                self.message = ""
                isInputValid = True
            else:
                option = input( "Invalid input, please enter 'y' for yes or 'n' for no: ").lower()

    def create_html_body(self):
        html = "MIME-Version: 1.0\n"
        html += "Content-Type: text/html\n"
        html += input("Please enter the html you would like to send in the email (e.g., <h1> Hello, </h1> <p Nice to talk to you!</p>): ")
        return html

    def create_text_body(self):
        text = "Content-Type: text/plain\n"
        isDone = False
        text = ""
        while(not isDone):
            response = input(r"Please enter a line of text you would like to send in the email (e.g., Nice talking to you!). When you are done, please enter 'quit': ")
            if(response == "quit"):
                isDone = True
            else:
                text += response + "\r\n"
        return text

    def create_body(self):
        hasChosen = False
        while(not hasChosen):
            choice = input("Would you like to send an text [text] or html [html] email? ")
            if(choice == "text"):
                self.body = self.create_text_body()
                hasChosen = True
            elif(choice == "html"):
                self.body = self.create_html_body()
                hasChosen = True
            else:
                print("please enter a valid input [text or html]")

    def create_email(self):
        """Create an email"""
        self.set_display_name()

        # Get receiver email
        isValidEmail = False
        while(not isValidEmail):
            self.receiver_email = input("please enter the receiver's email (e.g., john@gmail.com): ")
            isValidEmail = self.validateEmail(self.receiver_email)

        # Create email content    
        self.subject    = "Subject: " + input("Please enter email subject: ") + "\n"

        # Create email body
        self.create_body()

        self.message    += self.subject + self.body

    def send_ssl_email(self):
        """Send an SSL encrypted email"""
        print("sending ssl email")
        # Connect
        # Create a secure SSL context
        context_ssl = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", context=context_ssl) as server:
            server.login(self.sender_email, self.sender_pass)
            server.sendmail(self.sender_email, self.receiver_email, self.message)

    def send_tls_email(self):
        """Send a TLS encrypted email"""
        print("sending tls email")
        # Connect 
        with smtplib.SMTP("smtp.gmail.com", port=int(Port.TLS)) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_pass)
                server.sendmail(self.sender_email, self.receiver_email, self.message)

    def send_email(self, encryption_type):
        """Send email with user specified encryption type
        
        Keyword arguments:
        encryption_type (Encryption): the type of email encryption (default SSL)
        """
        try:
            if(not isinstance(encryption_type, Encryption)):
                raise TypeError("Invalid email encryption type")
            if(encryption_type == Encryption.SSL):
                self.send_ssl_email()
            elif(encryption_type == Encryption.TLS):
                self.send_tls_email()
        except:
            raise
        else:
            print("email sent")

if __name__ == "__main__":
    # parse user arguments
    parser = argparse.ArgumentParser(description="Send email")
    required = parser.add_argument_group("required arguments")
    required.add_argument("-e", "--encryption", type=str, help="email encryption type", required=True)
    args = parser.parse_args()

    # Get encryption type
    encryption_type = Encryption(args.encryption)

    # Send email
    emailer = Emailer()
    emailer.get_user_credentials()
    emailer.create_email()
    emailer.send_email(encryption_type)