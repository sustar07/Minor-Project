import re
from datetime import datetime
import subprocess

class SMSExtractor:
    def __init__(self):
        pass

    def get_sms(self):
        try:
            query = "adb shell content query --uri content://sms --projection _id,address,date,body"
            result = subprocess.run(query, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else ""
        except Exception as e:
            return str(e)

    def parse_sms_dump(self, sms_dump):
        messages = sms_dump.strip().split("\n")
        if not messages:
            return []
        
        first_message = messages[0]  # Get only the first row (Row 0)
        date_match = re.search(r"date=(\d+)", first_message)
        body_match = re.search(r"body=(.*)", first_message)
        address_match = re.search(r"address=(\S+)", first_message)
        
        if date_match and body_match and address_match:
            timestamp = int(date_match.group(1)) / 1000  # Convert to seconds
            return [{
                "time": datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')},
                {"address": address_match.group(1)},
                {"body": body_match.group(1).strip()
            }]
        
        return []

    def get_latest_sms(self):
        sms_dump = self.get_sms()
        return self.parse_sms_dump(sms_dump)

# Example usage
# extractor = SMSExtractor()
# latest_sms = extractor.get_latest_sms()
# print(latest_sms)

