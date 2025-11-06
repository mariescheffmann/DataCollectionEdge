from opcua import Client
from dotenv import load_dotenv
import os
import time


load_dotenv()
url = os.getenv("OPC_UA_URL")
if not url:
    raise ValueError("OPC_UA_URL is not set in .env")

client = Client(url)

variables = {
    "ServerStatus": "ns=2;i=2",
    "CurrentTime": "ns=2;i=3",
}

try:
    client.connect()
    print("Connected to server")

    while True:
        for name, node_id in variables.items():
            node = client.get_node(node_id)
            value = node.get_value()
            print(f"{name}: {value}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Client stopped by user")
finally:
    client.disconnect()
