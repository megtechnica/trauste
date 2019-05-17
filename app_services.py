import re

def check_if_valid(message_contents):
    msg_body = message_contents["text"]
    msg_body_re = re.compile(msg_body, re.IGNORECASE)
    if msg_body_re.search("\d{5}\s[MFWTV]{1}") == True:
        msg_zip_code = msg_body_re.search("\d{5}")
        msg_character = msg_body_re.search("\s[MWTFV]")
        