# CPU Monitoring Service

## Overview

This project implements a service that continuously monitors CPU usage and sends alerts when a threshold is exceeded.

## Features

* **Real-time CPU Usage Monitoring.** 
* **Updates every 5 seconds.**
* **Configurable Alert Threshold (default: 80%).**
* **Multiple Alerting Methods:** Email, Logging, System Notifications.
* **Outpots logs into file "cpu_monitor.log".**
* **Cross-Platform Compatibility (Python + `psutil`).**
* **Runs as a background service.**

## Prerequisites

* **Python 3.x.**
* **`psutil`:** Installed automatically by the `setup.sh` script.
* **Optional dependencies for specific alert methods (see full README for details).**

## Installation and Running

Run the `setup.sh` script to create a virtual environment, install dependencies, and start the monitoring service:

#./setup.sh