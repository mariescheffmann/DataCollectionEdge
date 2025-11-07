from Data import Data
from opcua import Client
from dotenv import load_dotenv
import os
import time

class OpcUaClient:
    def __init__(self, realTimeDatabase, interval, addresses):
        self.realTimeDatabase = realTimeDatabase
        self.interval = interval
        self.addresses = addresses

        load_dotenv()
        url = os.getenv("OPC_UA_URL")
        if not url:
            raise ValueError("OPC_UA_URL is not set in .env")

        self.client = Client(url)

        self.variables = {item["name"]: item["address"] for item in addresses}

    def start(self):
        try:
            self.client.connect()
            print("Connected to server")

            while True:
                for node_name, node_id in self.variables.items():
                    node = self.client.get_node(node_id)
                    value = node.get_value()

                    data = Data(node_name, value, self.realTimeDatabase)
                    data.prepareData()
                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("Client stopped by user")
        finally:
            self.client.disconnect()
