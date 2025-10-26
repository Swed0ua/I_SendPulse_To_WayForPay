# I_SendPulse_To_WayForPay - Setup and Autostart Guide

## Overview
Integration service connecting WayForPay payment system with SendPulse email marketing platform.

## Files
- Main entry point: `main.py`
- Configuration: `config/config.py`
- Port: 5060 (default)

---

## Linux/Unix Autostart Setup

### 1. Create systemd service file

```bash
sudo nano /etc/systemd/system/AC_I_SendPulse_To_WayForPay.service
```

### 2. Service file content

**Note**: Update paths below with your actual project directory.

```ini
[Unit]
Description=I SendPulse To WayForPay Service
After=network.target
Wants=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/path/to/I_SendPulse_To_WayForPay
Environment=PATH=/path/to/I_SendPulse_To_WayForPay/venv/bin
Environment=PYTHONPATH=/path/to/I_SendPulse_To_WayForPay
ExecStart=/path/to/I_SendPulse_To_WayForPay/venv/bin/python main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=AC_I_SendPulse_To_WayForPay

# Security settings
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/path/to/I_SendPulse_To_WayForPay

[Install]
WantedBy=multi-user.target
```

### 3. Initialize and enable service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable autostart
sudo systemctl enable AC_I_SendPulse_To_WayForPay

# Start service
sudo systemctl start AC_I_SendPulse_To_WayForPay

# Check status
sudo systemctl status AC_I_SendPulse_To_WayForPay
```

---

## Service Management Commands

### Start service
```bash
sudo systemctl start AC_I_SendPulse_To_WayForPay
```

### Stop service
```bash
sudo systemctl stop AC_I_SendPulse_To_WayForPay
```

### Restart service
```bash
sudo systemctl restart AC_I_SendPulse_To_WayForPay
```

### Check status
```bash
sudo systemctl status AC_I_SendPulse_To_WayForPay
```

### View logs
```bash
# Follow logs in real-time
sudo journalctl -u AC_I_SendPulse_To_WayForPay -f

# View last 50 log entries
sudo journalctl -u AC_I_SendPulse_To_WayForPay -n 50

# View all logs
sudo journalctl -u AC_I_SendPulse_To_WayForPay
```

---

## Verification

### Check if API is responding
```bash
curl -X POST http://localhost:5060/proccessInvoice
```

### Check if process is running
```bash
ps aux | grep "python main.py"
```

### Check if port is open
```bash
netstat -tulpn | grep 5060
```

### List all services
```bash
sudo systemctl list-units --type=service
```

---

## Manual Start (Development)

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Ensure config/config.py file exists with proper configuration

# Run the service
python main.py
```

---

## Configuration

Edit `config/config.py` with the following settings:

```python
SP_REST_API_ID = 'your_api_id'
SP_REST_API_SECRET = 'your_api_secret'
SP_TOKEN_STORAGE = 'file'
SP_ADDRESSBOOK_ID = 'your_addressbook_id'
```

---

## API Endpoint

### POST /proccessInvoice

Accepts payment data from WayForPay and adds contacts to SendPulse.

**Request format:**
- Content-Type: `application/json` or form-data with JSON string
- Body: `{"email": "user@example.com", "phone": "+380123456789"}`

**Response:**
```json
{
  "status": "success",
  "sendpulse_response": {...}
}
```

---