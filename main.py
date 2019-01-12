import serial.tools.list_ports

def serial_ports():

    # produce a list of all serial ports. The list contains a tuple with the port number, 
    # description and hardware address
    #
    ports = list(serial.tools.list_ports.comports())  
    print(ports)
    # return the port if 'USB' is in the description 
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no

print(serial_ports())
