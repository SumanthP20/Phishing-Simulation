

# Ethical Phishing Simulation Platform (Python Flask MVP)
# This script provides a minimal functional skeleton to start building your phishing simulation platform.

from flask import Flask, request, render_template_string, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import uuid

app = Flask(__name__)

# Simple SQLite database initialization for targets and tracking
conn = sqlite3.connect('phishing_simulation.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS targets (id TEXT, email TEXT, clicked INTEGER)''')
conn.commit()

# Email sending configuration (adjust as needed)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'youremail@gmail.com'  # Replace with your email
SMTP_PASS = 'yourpassword'          # Replace with your password

# Simple HTML landing page
landing_page = """
<!DOCTYPE html>
<html>
<head><title>Phishing Simulation</title></head>
<body>
<h2>This was a Phishing Simulation Test!</h2>
<p>You clicked the link in the simulated phishing email.</p>
<p>Always verify sender and URL before clicking links in emails.</p>
</body>
</html>
"""

@app.route('/')
def index():
    return '''
    <h2>Ethical Phishing Simulation Platform</h2>
    <form method="POST" action="/send">
      Target Email: <input type="email" name="email" required>
      <button type="submit">Send Phishing Simulation</button>
    </form>
    '''

@app.route('/send', methods=['POST'])
def send_email():
    target_email = request.form['email']
    unique_id = str(uuid.uuid4())
    
    cursor.execute("INSERT INTO targets (id, email, clicked) VALUES (?, ?, ?)", (unique_id, target_email, 0))
    conn.commit()

    # Create phishing email content
    phishing_link = request.url_root + 'phish/' + unique_id
    message = MIMEMultipart("alternative")
    message["Subject"] = "Important Update - Action Required"
    message["From"] = SMTP_USER
    message["To"] = target_email

    html_content = f"""
    <html>
      <body>
        <p>Dear User,<br>
           Please review the urgent update by clicking the link below:<br>
           <a href="{phishing_link}">Review Update</a>
        </p>
      </body>
    </html>
    """
    part = MIMEText(html_content, "html")
    message.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, target_email, message.as_string())
        return "Phishing simulation email sent successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"

@app.route('/phish/<id>')
def phish_landing(id):
    cursor.execute("UPDATE targets SET clicked = 1 WHERE id = ?", (id,))
    conn.commit()
    return render_template_string(landing_page)

@app.route('/report')
def report():
    cursor.execute("SELECT email, clicked FROM targets")
    data = cursor.fetchall()
    report_html = '<h2>Phishing Simulation Report</h2><table border="1"><tr><th>Email</th><th>Clicked</th></tr>'
    for row in data:
        report_html += f"<tr><td>{row[0]}</td><td>{'Yes' if row[1] else 'No'}</td></tr>"
    report_html += '</table>'
    return report_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
