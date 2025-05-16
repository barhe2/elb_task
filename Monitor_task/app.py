import psutil
import time
import logging
import configparser
import smtplib
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')  # Read the configuration from config.ini

CPU_THRESHOLD = config.getint('monitor', 'cpu_threshold', fallback=80)
LOG_FILE = config.get('monitor', 'log_file', fallback='cpu_monitor.log')
SLEEP_INTERVAL = config.getint('monitor', 'sleep_interval', fallback=5)

# Email configuration
EMAIL_ALERT = config.getboolean('alert', 'email_alert', fallback=False)
SMTP_SERVER = config.get('email', 'smtp_server', fallback='')
SMTP_PORT = config.getint('email', 'smtp_port', fallback=587)
SMTP_USERNAME = config.get('email', 'smtp_username', fallback='')
SMTP_PASSWORD = config.get('email', 'smtp_password', fallback='')
SENDER_EMAIL = config.get('email', 'sender_email', fallback='')
RECEIVER_EMAIL = config.get('email', 'receiver_email', fallback='')

#Logs
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_cpu_usage():
    #Get current CPU usage as %
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        return cpu_percent
    except Exception as e:
        logging.error(f"Error getting CPU usage: {e}")
        return None


def send_log_alert(message):
    #Logs the alert message.
    logging.warning(message)
    print(f"ALERT: {message}")  #print to console


def send_email_alert(subject, body):
    if not EMAIL_ALERT:
        logging.info("Email alerts are disabled in the configuration.")
        return

    if not all([SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SENDER_EMAIL, RECEIVER_EMAIL]):
        logging.error("Email configuration is incomplete. Please check config.ini.")
        return

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() 
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECEIVER_EMAIL
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        logging.info(f"Email alert sent to {RECEIVER_EMAIL} with subject: {subject}")
    except Exception as e:
        logging.error(f"Error sending email alert: {e}")


def main():
    #function to non-stop monitor CPU usage and reports alerts.
    logging.info("CPU monitoring service started.")

    while True:
        cpu_usage = get_cpu_usage()

        if cpu_usage is not None:
            logging.info(f"Current CPU usage: {cpu_usage}%")

            if cpu_usage > CPU_THRESHOLD:
                alert_message = f"CPU usage exceeded {CPU_THRESHOLD}%: {cpu_usage}%"
                send_log_alert(alert_message)

                if EMAIL_ALERT:
                    email_subject = f"CPU Usage Alert - Exceeded {CPU_THRESHOLD}%"
                    email_body = f"The CPU usage on the system has exceeded the threshold of {CPU_THRESHOLD}%. Current usage is {cpu_usage}% at {time.strftime('%Y-%m-%d %H:%M:%S')}.\n\nPlease investigate."
                    send_email_alert(email_subject, email_body)

        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()