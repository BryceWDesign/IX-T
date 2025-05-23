# IX-T Dashboard

## Overview

This dashboard provides real-time visualization and monitoring of the IX-T Ambient Energy Loop simulation metrics. It aims to present clear, actionable insights on system performance, efficiency, and energy flow for researchers and engineers.

## Setup Instructions

1. **Prerequisites**

   - Python 3.8+ installed
   - `Flask` or equivalent web server (if hosting API locally)
   - JSON API serving metrics at the configured endpoint (default: `http://localhost:5000/api/metrics`)
   - Web browser (Chrome, Firefox, Edge recommended)

2. **Installation**

   - Clone this repository or ensure the `dashboard` folder is included.
   - Install dependencies:
     ```bash
     pip install flask flask-cors
     ```
   - Configure your data source and widgets in `dashboard_config.yaml`.

3. **Running the Dashboard**

   - Start your metric API server.
   - Run the dashboard frontend server (implementation dependent).
   - Open the dashboard URL in your browser.
   - Data will refresh automatically based on `refresh_interval_seconds`.

## Usage

- Monitor voltage, efficiency, and loss in real-time.
- Receive notifications for abnormal states (warning/critical).
- Customize widgets and data sources via `dashboard_config.yaml`.

## Contribution Guidelines

- Use clear and descriptive commits.
- Follow PEP8 style guidelines for Python scripts.
- Document any changes to configuration or code.
- Submit pull requests for new features or bug fixes.

## Contact

For further assistance contact the author please VIA Github. 

---

Thank you for exploring the IX-T project dashboard!

