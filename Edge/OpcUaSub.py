from opcua import Client, ua
import time
import os
import json
from dotenv import load_dotenv
from Data import EventPayload
from datetime import datetime

class SubscriptionHandler(object):
    def __init__(self, machine_id, event_templates):
        self.machine_id = machine_id
        self.event_templates = event_templates
        self.address_to_template = {}
        for event_config in event_templates:
            for addr_info in event_config.get("opcua_addresses", []):
                self.address_to_template[addr_info["address"]] = event_config

    def datachange_notification(self, node, val, data):
        opcua_address = node.nodeid.to_string()
        event_match = self.address_to_template.get(opcua_address)

        sql_config = event_match.get("sql_config")

        if not sql_config:
            print(f"No sql_config found for address {opcua_address}")
            return

        eventPayload = EventPayload(
            self.machine_id,
            event_match["event_name"],
            val,
            sql_config,
            data.monitored_item.Value.SourceTimestamp
        )
        eventPayload.sendData()


class OpcUaSub:
    def __init__(self, machine_id, event_templates):
        load_dotenv()
        url = os.getenv("OPC_UA_URL")
        if not url:
            raise ValueError("OPC_UA_URL is not set in .env")

        self.client = Client(url)
        self.machine_id = machine_id
        self.event_templates = event_templates

        self.addresses_to_subscribe = {}
        for event_config in event_templates:
            for addr_info in event_config.get("opcua_addresses", []):
                self.addresses_to_subscribe[addr_info["address"]] = addr_info["name"]

    def start(self):
        try:
            self.client.connect()
            print(f"--- SQL Subscriptions Startet for Maskine ID: {self.machine_id} ---")

            handler = SubscriptionHandler(self.machine_id, self.event_templates)
            sub = self.client.create_subscription(500, handler)

            for address, name in self.addresses_to_subscribe.items():
                node = self.client.get_node(address)
                handle = sub.subscribe_data_change(node)
                print(f"Subscribed: {name} ({address})")

            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"Subscription client for {self.machine_id} stoppet af bruger.")
        except Exception as e:
            print(f"Error i OpcUaSub for {self.machine_id}: {e}")
        finally:
            if 'sub' in locals():
                sub.unsubscribe(handle)
            if self.client:
                self.client.disconnect()
