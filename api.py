import logging
import traceback
from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='api.log', level=logging.DEBUG)

@app.route('/api/test-smtp-login', methods=['POST'])
def test_smtp_login():
    try:
        data = request.get_json()
        smtp_host = data['smtp_host']
        smtp_port = data['smtp_port']
        smtp_username = data['smtp_username']
        smtp_password = data['smtp_password']

        # Your existing code
        def test_smtp_login(smtp_host, smtp_port, smtp_username, smtp_password):
            try:
                # Connect to the SMTP server
                server = smtplib.SMTP(smtp_host, smtp_port)
                server.starttls()  # Enable TLS encryption for secure connection

                # Login to the SMTP server
                server.login(smtp_username, smtp_password)

                # Close the connection
                server.quit()

                return True  # Login successful
            except smtplib.SMTPAuthenticationError:
                return False  # Invalid login credentials
            except Exception as e:
                logging.exception('An error occurred')  # Log the exception
                return False  # Other error occurred

        # Test SMTP login
        result = test_smtp_login(smtp_host, smtp_port, smtp_username, smtp_password)

        if result:
            response = {'message': 'SMTP login successful.'}
        else:
            response = {'message': 'SMTP login failed.'}

        return jsonify(response)
    except Exception as e:
        logging.exception('An error occurred')  # Log the exception
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
