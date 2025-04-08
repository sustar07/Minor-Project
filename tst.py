from sms import SMSExtractor

extractor = SMSExtractor()
latest_sms = extractor.get_latest_sms()

print(latest_sms)  # Prints the latest SMS as a list
