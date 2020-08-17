"""
pyJsConsole wrapper.

© Anime no Sekai - 2020
"""

import internal.javascript.classes as JSClass

console = JSClass._Console()
document = JSClass._Document()
history = JSClass._History
Math = JSClass._Math()
navigator = JSClass._Navigator
screen = JSClass._Screen()
window = JSClass._Window()

'''
import threading
from lifeeasy import sleep

def reloadElements():
    global console
    global document
    global history
    global navigator
    global screen
    global window
    lastURL = 'data:,'
    while True:
        sleep(0.1)
        try:
            if JSClass.evaluate('window.location.href') != lastURL:
                document = JSClass._Document()
                window = JSClass._Window()
                lastURL = JSClass.evaluate('window.location.href')
        except:
            break

thread = threading.Thread(target=reloadElements)
thread.daemon = True
thread.start()
'''

def newDocument():
    return JSClass._Document()

def newWindow():
    return JSClass._Window()

def fresh():
    return (JSClass._Document(), JSClass._Window())

def clearInterval(intervalID):
    JSClass.clearInterval(intervalID)

def clearTimeout(timeoutID):
    JSClass.clearTimeout(timeoutID)

def evaluate(code_to_execute, return_value=False):
    JSClass.evaluate(code_to_execute, return_value=return_value)

def setInterval(function, milliseconds):
    JSClass.setInterval(function, milliseconds)

def setTimeout(function, milliseconds):
    JSClass.setTimeout(function, milliseconds)
