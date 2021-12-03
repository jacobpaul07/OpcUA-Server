import random

from opcua import Server
from random import randint
import time
from opc_server import mainfunction
import threading

try:
    server = Server()
    url = "opc.tcp://0.0.0.0:122"
    server.set_endpoint(url)
    booleanvalue = ["True", "False"]
    qualitycodelist = ["", ""]
    name = "OPC_SIMULATION_SERVER"
    addspace = server.register_namespace(name)

    node = server.get_objects_node()

    Param = node.add_object(addspace, "Parameters")

    cyclestart_status = Param.add_variable("ns=3;i=1001", "Cycle Start Staus", 0)
    downntimereasoncode = Param.add_variable("ns=3;i=1002", "Down Time Reason Code", 0)
    downtimestatus = Param.add_variable("ns=3;i=1003", "Down Time Status", 0)
    emgstopstatus = Param.add_variable("ns=3;i=1004", "Emergency Stop Status", 0)
    idealcycletime = Param.add_variable("ns=3;i=1005", "Ideal Cycle Time", 0)
    jobid = Param.add_variable("ns=3;i=1007", "Job ID", 0)
    machineid = Param.add_variable("ns=3;i=1006", "Machine ID", 0)
    operatorid = Param.add_variable("ns=3;i=1012", "Operator ID", 0)
    poweronstatus = Param.add_variable("ns=3;i=1016", "Power On Status", 0)
    productionstart = Param.add_variable("ns=3;i=1017", "Production Start", 0)
    qualitycode = Param.add_variable("ns=3;i=1018", "Quality Code", 0)
    shiftid = Param.add_variable("ns=3;i=1019", "Shift ID", 0)

    cyclestart_status.set_writable()
    downntimereasoncode.set_writable()
    downtimestatus.set_writable()
    emgstopstatus.set_writable()
    idealcycletime.set_writable()
    jobid.set_writable()
    machineid.set_writable()
    operatorid.set_writable()
    poweronstatus.set_writable()
    productionstart.set_writable()
    qualitycode.set_writable()
    shiftid.set_writable()

    server.start()
    print("Server started at {}".format(url))
    while True:
        thread = threading.Thread(
        target=mainfunction,
        args=(cyclestart_status,downntimereasoncode,downtimestatus, emgstopstatus, idealcycletime,jobid,machineid, operatorid, poweronstatus, productionstart, qualitycode,shiftid)
        )
        thread.start()
        time.sleep(5)
        

except Exception as ex:
    print("Error in opcServer: ", ex)

