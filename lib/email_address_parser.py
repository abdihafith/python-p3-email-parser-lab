# your code goes here!
import re
class EmailAddressParser:
    email_address = r"[a-z]([A-Za-z0-9])+[\.]{0,1}([A-Za-z0-9])+@[a-z]+.[a-z]{2,}"
    email_regex = re.compile(email_address)

    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        emails = re.split(r"\s|,", self.addresses)

        unique_emails = set()
        for email in emails:
            if self.email_regex.fullmatch(email):
                unique_emails.add(email)

        return sorted(list(unique_emails))