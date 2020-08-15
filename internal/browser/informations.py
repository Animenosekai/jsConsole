"""
All of the informations about the current pyJsConsole instance.

© Anime no Sekai - 2020
"""

drivername = ''
connected = False

def set_connection_status(status):
    global connected
    connected = status
    return connected

def set_drivername(name):
    global drivername
    drivername = name
    return drivername