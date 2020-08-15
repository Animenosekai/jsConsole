"""
Executing JavaScript on the browser.

© Anime no Sekai - 2020
"""


from ..browser import browser
from ..browser import config
from ..exceptions import BrowserError

def evaluate(command, return_value=True):
    if config.layer == 'Selenium':
        if return_value:
            return browser.execute_script('return ' + command)
        else:
            browser.execute_script(command)
    elif config.layer == 'Pyppeteer':
        if return_value:
            return browser.evaluate(command)
        else:
            browser.evaluate(command)
    else:
        raise BrowserError(f'There is an error with the layer: {config.layer}')

def switch_to_alert():
    if config.layer == 'Selenium':
        browser.switch_to.alert