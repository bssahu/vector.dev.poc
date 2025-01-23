import time
import random
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    format='%(message)s',  # Only output the message, no extra formatting
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Sample application names and error messages
APPS = ["web-server", "auth-service", "payment-api", "user-service"]
ERROR_TYPES = ["ValidationError", "TimeoutError", "DatabaseError", "AuthenticationError"]
ERROR_MESSAGES = [
    "Failed to process request",
    "Connection timed out",
    "Invalid input parameters",
    "Database connection failed",
    "Authentication token expired"
]

def generate_log_entry():
    app = random.choice(APPS)
    error_type = random.choice(ERROR_TYPES)
    message = random.choice(ERROR_MESSAGES)
    severity = random.choice(["ERROR", "WARN", "INFO"])
    
    log_entry = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "app": app,
        "error_type": error_type,
        "message": message,
        "severity": severity,
        "request_id": f"req_{random.randint(1000, 9999)}",
        "user_id": f"user_{random.randint(1, 100)}",
        "metadata": {
            "host": f"server-{random.randint(1, 5)}",
            "environment": "production"
        }
    }
    
    return log_entry

def main():
    while True:
        log_entry = generate_log_entry()
        print(json.dumps(log_entry), flush=True)  # Print directly to stdout
        time.sleep(random.uniform(0.1, 2))

if __name__ == "__main__":
    main() 