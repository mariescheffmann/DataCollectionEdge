from Data import Data
from opcua import Client, ua
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

        self.variables = {
            item["name"]: {
                "address": item["address"],
                "tag": item.get("tag")
            }
            for item in addresses
        }

    def start(self):
        try:
            self.client.connect()
            print("Connected to server")

            while True:
                for node_name, node_info in self.variables.items():
                    node = self.client.get_node(node_info.get("address"))
                    tag = node_info.get("tag")

                    data_value = node.get_data_value()
                    source_timestamp = data_value.SourceTimestamp

                    try:
                        value = node.get_value()
                    except ua.UaStatusCodeError as e:
                        print(f"Node {node} does not exist: {e}")

                    data = Data(node_name, value, self.realTimeDatabase, timestamp=source_timestamp, tag=tag)
                    data.prepareData()
                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("Client stopped by user")
        finally:
            self.client.disconnect()
