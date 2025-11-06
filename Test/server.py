# -*- coding: utf-8 -*-

from opcua import Server
import time

# Opret server
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")  # lokal endpoint

# Opret et namespace
uri = "http://example.org"
idx = server.register_namespace(uri)

# Opret en folder og nogle variabler
objects = server.get_objects_node()
myobj = objects.add_object(idx, "MyObject")
var1 = myobj.add_variable(idx, "ServerStatus", "Running")
var2 = myobj.add_variable(idx, "CurrentTime", time.strftime("%H:%M:%S"))

# Gør variabler skrivbare
var1.set_writable()
var2.set_writable()

# Start server
server.start()
print("Server started at {}".format(server.endpoint))

try:
    while True:
        # Opdater tiden hvert sekund
        var2.set_value(time.strftime("%H:%M:%S"))
        time.sleep(1)
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    server.stop()
