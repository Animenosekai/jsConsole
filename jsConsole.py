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

def clearInterval(intervalID):
    JSClass.clearInterval(intervalID)

def clearTimeout(timeoutID):
    JSClass.clearTimeout(timeoutID)

def eval(code_to_execute, return_value=False):
    JSClass.evaluate(code_to_execute, return_value=return_value)

def setInterval(function, milliseconds):
    JSClass.setInterval(function, milliseconds)

def setTimeout(function, milliseconds):
    JSClass.setTimeout(function, milliseconds)