from OpcUaClient import OpcUaClient
from OpcUaSub import OpcUaSub
import json
import threading

print('Hello World!')

with open("Config/config.json", "r", encoding="utf-8") as f:
    configData = json.load(f)

for filename in configData.get("realtimeConfigs", []):
    with open("Config/"+filename, "r", encoding="utf-8") as fi:
        data = json.load(fi)

        opcua = OpcUaClient(True, data["interval"], data["addresses"])
        t = threading.Thread(target=opcua.start)
        t.start()

for filename in configData.get("sqlConfigs", []):
    with open("Config/"+filename, "r", encoding="utf-8") as fi:
        data = json.load(fi)

        opcua = OpcUaSub(data["machineId"], data["events"])
        t = threading.Thread(target=opcua.start)
        t.start()

# from MqttPublisher import MqttPublisher
# import random
# import time
# import json

# try:
#     mqtt = MqttPublisher()
#     while True:
#         temperatur = round(random.uniform(20.0, 25.0), 2)
#         humidity = round(random.uniform(40.0, 60.0), 2)

#         # JSON i DataPoint-format
#         temp_data = {
#             "tag": "fisk",
#             "name": "temperature",
#             "value": temperatur
#         }

#         humidity_data = {
#             "tag": "hej",
#             "name": "humidity",
#             "value": humidity,
#             "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
#         }

#         # Send til MQTT
#         mqtt.publish(json.dumps(temp_data), "data", "influx")
#         mqtt.publish(json.dumps(humidity_data), "data", "influx")

#         time.sleep(5)
# except KeyboardInterrupt:
#     print("Stopper publisher...")
#     client.disconnect()
