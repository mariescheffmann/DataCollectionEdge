import paho.mqtt.client as mqtt
import os
import ssl

class MqttPublisher:
    def __init__(self):
        self.client = mqtt.Client(client_id=os.getenv("CLIENT_ID"))
        self.client.tls_set(
            ca_certs="/Edge/certs/ca.crt",
            certfile="/Edge/certs/edge-client.crt",
            keyfile="/Edge/certs/edge-client.key",
            tls_version=ssl.PROTOCOL_TLSv1_2
        )
        self.client.tls_insecure_set(True)

        self.client.connect(os.getenv("BROKER"), int(os.getenv("PORT")), 60)

    def publish(self, message, topic_start, topic_suffix):
        client_id = os.getenv("CLIENT_ID")
        topic = f"{topic_start}/{client_id}/{topic_suffix}"
        self.client.publish(topic, message)
        print(message, topic)
