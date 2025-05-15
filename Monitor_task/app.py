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

# Email Configuration
EMAIL_ALERT = config.getboolean('alert', 'email_alert', fallback=False)
SMTP_SERVER = config.get('email', 'smtp_server', fallback='')
SMTP_PORT = config.getint('email', 'smtp_port', fallback=587)
SMTP_USERNAME = config.get('email', 'smtp_username', fallback='')
SMTP_PASSWORD = config.get('email', 'smtp_password', fallback='')
SENDER_EMAIL = config.get('email', 'sender_email', fallback='')
RECEIVER_EMAIL = config.get('email', 'receiver_email', fallback='')

#Logs Setup 
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


def send_alert(message):
    #Logs the alert message.
    logging.warning(message)
    print(f"ALERT: {message}")  # Also print to console


def main():
    #function to non-stop monitor CPU usage and reports alerts.
    logging.info("CPU monitoring service started.")

    while True:
        cpu_usage = get_cpu_usage()

        if cpu_usage is not None:
            logging.info(f"Current CPU usage: {cpu_usage}%")

            if cpu_usage > CPU_THRESHOLD:
                alert_message = f"CPU usage exceeded {CPU_THRESHOLD}%: {cpu_usage}%"
                send_alert(alert_message)

        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()