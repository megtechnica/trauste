import re
from message_request_main import find_zip_code

class SMS_Msg_Request:
    def __init__(self, sender_num, msg_body):
        self.sender_num = sender_num
        self.msg_body = msg_body
        self.return_msg = ''
    def check_if_valid_msg(self):
        ## this regular expression will check to see if self.msg_body has 5 digits at the beginning
        ## and MWFTV at the end.
        ## M = Male     W = Woman   F = Family  T = Trans   V = Veteran
        if re.search(r"^\d{5}.\Z[MmWwFfTtVv]$", msg_body):  
            self.zip_code = re.search(r"^\d{5}", zip_code)
            self.character = re.search(r"\Z[MWFTV]", zip_code)
            self.is_valid = True
        else:
            self.is_valid = False

