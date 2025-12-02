from OpcUaClient import OpcUaClient
from OpcUaSub import OpcUaSub
import json
import threading

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
