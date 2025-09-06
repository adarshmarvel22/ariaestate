from channels.consumer import SyncConsumer


class researchConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass