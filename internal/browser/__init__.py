"""
Browser Element.

© Anime no Sekai - 2020
"""
import psutil

from .launch import start
from .config import browsername, layer

browser = start()

def kill():
    """
    Kills the browser process in use.
    """
    from .informations import connected, set_connection_status, drivername
    if layer == 'Selenium':
        if connected:
            if browsername == 'Chrome' or browsername == 'Firefox':
                driver_process = psutil.Process(browser.service.process.pid)
                if driver_process.is_running():
                    process = driver_process.children()
                    if process:
                        process = process[0]
                        if process.is_running():
                            browser.quit()
                        else:
                            process.kill()
                    set_connection_status(False)