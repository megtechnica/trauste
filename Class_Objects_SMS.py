
class SMS_Msg_Request:
    def __init__(self, sender_num, msg_body):
        self.sender_num = sender_num
        self.msg_body = msg_body
        self.return_msg = ''

