
class Notifier:
    def __init__(self,sender_id, **kwargs):
        self.sender_id = sender_id
        super().__init__(**kwargs)

    def send(self,message):
        return f"[Notifier {self.sender_id}] general broadcast: {message}"

class EmailNotifier(Notifier):
    def __init__(self,email_server, **kwargs):
        self.email_server = email_server
        super().__init__(**kwargs)

    def send(self, message):
        return super().send(message)