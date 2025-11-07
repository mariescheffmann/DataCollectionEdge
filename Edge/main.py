from OpcUaClient import OpcUaClient
import json
import threading

with open("Config/config.json", "r", encoding="utf-8") as f:
    configData = json.load(f)

for filename in configData["configs"]:
    with open("Config/"+filename, "r", encoding="utf-8") as fi:
        data = json.load(fi)

        opcua = OpcUaClient(data["realTimeDatabase"], data["interval"], data["addresses"])
        t = threading.Thread(target=opcua.start)
        t.start()
