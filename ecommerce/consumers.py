from channels.consumer import SyncConsumer


class ecommerceConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass