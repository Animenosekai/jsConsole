"""
Browser Launcher for pyJsConsole.

© Anime no Sekai - 2020
"""
import asyncio
import threading

from .config import *
from .informations import *
from ..exceptions import BrowserError

async def _launchpyppeteer():
    """
    Internal Function to launch pyppeteer
    """
    from pyppeteer import launch
    try:
        browser = await launch()
    except:
        if executable_path == '':
            browser = await launch(
                handleSIGINT=False,
                handleSIGTERM=False,
                handleSIGHUP=False,
                headless=True,
                args=['--no-sandbox']
            )
        else:
            browser = await launch(
                handleSIGINT=False,
                handleSIGTERM=False,
                handleSIGHUP=False,
                headless=True,
                args=['--no-sandbox'],
                executablePath=executable_path
            )
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(timeout=0)
    return page

def _launchselenium():
    from selenium import webdriver
    if browsername.lower() == 'chrome':
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if headless:
            chrome_options.headless = True
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-extensions")
        if no_sandbox:
            chrome_options.add_argument("--no-sandbox")
        if executable_path == '':
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
        set_drivername('chromedriver')
        set_connection_status(True)
    
    elif browsername.lower() == 'firefox':
        pass

    elif browsername.lower() == 'phantom' or browsername.lower() == 'phantomjs':
        pass

    else:
        raise BrowserError(f'{browsername} is not supported yet.')

    return driver

def start():
    if layer == 'Pyppeteer':
        if isinstance(threading.current_thread(), threading._MainThread):
            #print('Main Thread')
            event_loop = asyncio.get_event_loop()
            instances = event_loop.run_until_complete(_launchpyppeteer())
            set_connection_status(True)
        else:
            #print('Not Main Thread')
            asyncio.set_event_loop(asyncio.new_event_loop())
            event_loop = asyncio.get_event_loop()
            instances = event_loop.run_until_complete(_launchpyppeteer())
            set_connection_status(True)
        return instances
    elif layer == 'Selenium':
        return _launchselenium()
    else:
        raise BrowserError(f'{layer} is not supported yet.')