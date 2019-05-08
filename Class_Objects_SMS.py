import re
import HTTP_Requests

class SMS_Msg_Request:
    def __init__(self, sender_num, msg_body):
        self.sender_num = sender_num
        self.msg_body = msg_body
        self.return_msg = ''
    def check_if_valid_msg(self):
        ## this regular expression will check to see if self.msg_body has 5 digits at the beginning
        ## and MWFTV at the end.
        ## M = Male     W = Woman   F = Family  T = Trans   V = Veteran
        if re.search("^\d{5}.\Z[MmWwFfTtVv]$"):  
            self.zip_code = re.search("^\d{5}")
            self.character = re.search("\Z[MWFTV]")
        else:
            self.return_msg = 'Hello {0}, please review your message for errors: {1}'.format(self.sender_num, self.msg_body)

