"""
All of the JavaScript classes used by pyJsConsole.

© Anime no Sekai
"""

#from .execute_js import evaluate, switch_to_alert
from .execute_js import evaluate
from .. import browser
from ..exceptions import *

#import lifeeasy

import random
import string

list_of_variables = []

def createRandomString(length):
    """
    Creates a random string which hasn't been already created\n
    Useful for random variable and ID names.
    """
    global list_of_variables
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    if result_str in list_of_variables:
        result_str = createRandomString(length)
    return result_str

class _Math():
    '''
    According to w3schools.com\n
    The JavaScript Math object allows you to perform mathematical tasks on numbers.
    '''
    # Math.E
    E = evaluate('Math.E')

    # Math.PI
    PI = evaluate('Math.PI')

    # Math.SQRT2
    SQRT2 = evaluate('Math.SQRT2')

    # Math.SQRT1_2
    SQRT1_2 = evaluate('Math.SQRT1_2')

    # Math.LN2
    LN2 = evaluate('Math.LN2')

    # Math.LN10
    LN10 = evaluate('Math.LN10')

    # Math.LOG2E
    LOG2E = evaluate('Math.LOG2E')

    # Math.LOG10E
    LOG10E = evaluate('Math.LOG10E')
    
    # Math.round()
    def round(self, number):
        '''
        According to w3schools.com\n
        Math.round(x) returns the value of x rounded to its nearest integer.
        '''
        return evaluate(f'Math.round({str(number)})')

    # Math.pow()
    def pow(self, number1, number2):
        '''
        According to w3schools.com\n
        Math.pow(x, y) returns the value of x to the power of y.
        '''
        return evaluate(f'Math.pow({str(number1)}, {str(number2)})')

    # Math.sqrt()
    def sqrt(self, number):
        '''
        According to w3schools.com\n
        Math.sqrt(x) returns the square root of x.
        '''
        return evaluate(f'Math.sqrt({str(number)})')

    # Math.abs()
    def abs(self, number):
        '''
        According to w3schools.com\n
        Math.abs(x) returns the absolute (positive) value of x.
        '''
        return evaluate(f'Math.abs({str(number)})')

    # Math.ceil()
    def ceil(self, number):
        '''
        According to w3schools.com\n
        Math.ceil(x) returns the value of x rounded up to its nearest integer.
        '''
        return evaluate(f'Math.ceil({str(number)})')

    # Math.floor()
    def floor(self, number):
        '''
        According to w3schools.com\n
        Math.floor(x) returns the value of x rounded down to its nearest integer.
        '''
        return evaluate(f'Math.floor({str(number)})')

    # Math.sin()
    def sin(self, number):
        '''
        According to w3schools.com\n
        Math.sin(x) returns the sine (a value between -1 and 1) of the angle x (given in radians).\n
        If you want to use degrees instead of radians, you have to convert degrees to radians:\n
        Angle in radians = Angle in degrees x PI / 180.
        '''
        return evaluate(f'Math.sin({str(number)})')

    # Math.sinh()
    def sinh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic sine of x.
        '''
        return evaluate(f'Math.sinh({str(number)})')

    # Math.asin()
    def asin(self, number):
        '''
        According to w3schools.com\n
        Returns the arcsine of x, in radians.
        '''
        return evaluate(f'Math.asin({str(number)})')

    # Math.asinh()
    def asinh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic arcsine of x.
        '''
        return evaluate(f'Math.asinh({str(number)})')
    
    # Math.cos()
    def cos(self, number):
        '''
        According to w3schools.com\n
        Math.cos(x) returns the cosine (a value between -1 and 1) of the angle x (given in radians).\n
        If you want to use degrees instead of radians, you have to convert degrees to radians:\n
        Angle in radians = Angle in degrees x PI / 180.
        '''
        return evaluate(f'Math.cos({str(number)})')
    
    # Math.cosh()
    def cosh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic cosine of x.
        '''
        return evaluate(f'Math.cosh({str(number)})')
    
    # Math.acos()
    def acos(self, number):
        '''
        According to w3schools.com\n
        Returns the arccosine of x, in radians.
        '''
        return evaluate(f'Math.acos({str(number)})')
    
    # Math.acosh()
    def acosh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic arccosine of x.
        '''
        return evaluate(f'Math.acosh({str(number)})')

    # Math.min()
    def min(self, list_of_number):
        '''
        According to w3schools.com\n
        Math.min() can be used to find the lowest value in a list of arguments.
        '''
        return evaluate(f'Math.min({str(list_of_number)[1:][:-1]})')
    
    # Math.max()
    def max(self, list_of_number):
        '''
        According to w3schools.com\n
        Math.max() can be used to find the highest value in a list of arguments.
        '''
        return evaluate(f'Math.max({str(list_of_number)[1:][:-1]})')

    # Math.random()
    def random(self):
        '''
        According to w3schools.com\n
        Math.random() returns a random number between 0 (inclusive), and 1 (exclusive).
        '''
        return evaluate(f'Math.random()')

    # Math.tan()
    def tan(self, number):
        '''
        According to w3schools.com\n
        Returns the tangent of an angle.
        '''
        return evaluate(f'Math.tan({str(number)})')

    # Math.tanh()
    def tanh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic tangent of a number.
        '''
        return evaluate(f'Math.tanh({str(number)})')
    
    # Math.atan()
    def atan(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic tangent of a number.
        '''
        return evaluate(f'Math.atan({str(number)})')
    
    # Math.atan2()
    def atan2(self, number1, number2):
        '''
        According to w3schools.com\n
        Returns the arctangent of the quotient of its arguments.
        '''
        return evaluate(f'Math.atan2({str(number1)}, {str(number2)})')
    
    # Math.atan2()
    def atanh(self, number):
        '''
        According to w3schools.com\n
        Returns the hyperbolic arctangent of x.
        '''
        return evaluate(f'Math.atan2({str(number)})')

    # Math.cbrt()
    def cbrt(self, number):
        '''
        According to w3schools.com\n
        Returns the cubic root of x.
        '''
        return evaluate(f'Math.cbrt({str(number)})')

    # Math.exp()
    def exp(self, number):
        '''
        According to w3schools.com\n
        Returns the value of E^x.
        '''
        return evaluate(f'Math.exp({str(number)})')

    # Math.log()
    def log(self, number):
        '''
        According to w3schools.com\n
        Returns the natural logarithm (base E) of x.
        '''
        return evaluate(f'Math.log({str(number)})')

    # Math.trunc():
    def trunc(self, number):
        '''
        According to w3schools.com\n
        Returns the integer part of a number (x).
        '''
        return evaluate(f'Math.trunc({str(number)})')


class _Console():
    """
    According to MDN\n
    The console object provides access to the browser's debugging console (e.g. the Web Console in Firefox).\n
    The specifics of how it works varies from browser to browser, but there is a de facto set of features that are typically provided.\n

    The console object can be accessed from any global object.\n
    Window on browsing scopes and WorkerGlobalScope as specific variants in workers via the property console.\n
    It's exposed as Window.console, and can be referenced as simply console.
    """
    def log(self, element, pythonConsole=True):
        """
        According to MDN\n
        The Console method log() outputs a message to the web console.\n
        The message may be a single string (with optional substitution values), or it may be any one or more JavaScript objects.
        """
        if type(element) == type('hey'):
            newelement = str(element).replace('"', '\\"')
            evaluate(f'console.log("{newelement}")', return_value=False)
        elif type(element) == type(1) or type(element) == type(1.1):
            evaluate(f'console.log({str(element)})', return_value=False)
        else:
            newelement = str(element).replace('"', '\\"')
            evaluate(f'console.log("{newelement}")', return_value=False)
        if pythonConsole:
            print(element)

    def assertJS(self, assertion, message):
        """
        According to MDN\n
        The console.assert() method writes an error message to the console if the assertion is false.\n
        If the assertion is true, nothing happens.
        """
        evaluate(f'console.asset({str(assertion).lower()}, "{str(message)}")', return_value=False)

    def clear(self):
        """
        According to MDN\n
        The console.clear() method clears the console if the environment allows it.
        """
        evaluate('console.clear()', return_value=False)

    def count(self, label=''):
        """
        According to MDN\n
        The console.count() method logs the number of times that this particular call to count() has been called.
        """
        if label != '':
            evaluate(f'console.count("{str(label)}")', return_value=False)
        else:
            evaluate('console.count()', return_value=False)

    def countReset(self, label=""):
        """
        According to MDN\n
        Resets the value of the counter with the given label.
        """
        if label != '':
            evaluate(f'console.countReset("{str(label)}")', return_value=False)
        else:
            evaluate('console.countReset()', return_value=False)
    
    def debug(self, message):
        """
        According to MDN\n
        The console method debug() outputs a message to the web console at the "debug" log level.\n
        The message is only displayed to the user if the console is configured to display debug output.
        """
        evaluate(f'console.debug("{str(message)}")', return_value=False)
    
    def dir(self, object):
        """
        According to MDN\n
        The Console method dir() displays an interactive list of the properties of the specified JavaScript object.\n
        The output is presented as a hierarchical listing with disclosure triangles that let you see the contents of child objects.

        In other words, console.dir() is the way to see all the properties of a specified JavaScript object in console by which the developer can easily get the properties of the object.
        """
        evaluate(f'console.dir({str(object)})', return_value=False)
    
    def dirxml(self, object):
        """
        According to MDN\n
        Displays an interactive tree of the descendant elements of the specified XML/HTML element.\n
        If it is not possible to display as an element the JavaScript Object view is shown instead.\n
        The output is presented as a hierarchical listing of expandable nodes that let you see the contents of child nodes.
        """
        evaluate(f'console.dirxml({str(object)})', return_value=False)


    def error(self, message):
        """
        According to MDN\n
        Outputs an error message to the Web Console.
        """
        evaluate(f'console.error("{str(message)}")', return_value=False)

    def exception(self, message):
        """
        According to MDN\n
        Outputs an error message to the Web Console.
        """
        evaluate(f'console.error("{str(message)}")', return_value=False)
    
    def group(self, label=''):
        """
        According to MDN\n
        Creates a new inline group in the Web Console log.\n
        This indents following console messages by an additional level, until console.groupEnd() is called.
        """
        if label != "":
            evaluate(f'console.group("{str(label)}")', return_value=False)
        else:
            evaluate('console.group()', return_value=False)
    
    def groupCollapsed(self, label=''):
        """
        According to MDN\n
        Creates a new inline group in the Web Console.\n
        Unlike console.group(), however, the new group is created collapsed.\n
        The user will need to use the disclosure button next to it to expand it, revealing the entries created in the group.\n

        Call console.groupEnd() to back out to the parent group.
        """
        if label != "":
            evaluate(f'console.groupCollapsed("{str(label)}")', return_value=False)
        else:
            evaluate('console.groupCollapsed()', return_value=False)

    def groupEnd(self):
        """
        According to MDN\n
        Exits the current inline group in the Web Console.
        """
        evaluate('console.groupEnd()', return_value=False)

    def info(self, message):
        """
        According to MDN\n
        The console.info() method outputs an informational message to the Web Console.\n
        In Firefox, a small "i" icon is displayed next to these items in the Web Console's log.
        """
        evaluate(f'console.info("{str(message)}")', return_value=False)

    def profile(self, profileName=''):
        """
        According to MDN\n
        Starts recording a performance profile (for example, the Firefox performance tool).

        You can optionally supply an argument to name the profile and this then enables you to stop only that profile if multiple profiles being recorded.\n
        See Console.profileEnd() to see how this argument is interpreted.

        To stop recording call Console.profileEnd().
        """
        if profileName != '':
            evaluate(f'console.profile("{str(profileName)}")', return_value=False)
        else:
            evaluate(f'console.profile()', return_value=False)


    def profileEnd(self, profileName=''):
        """
        According to MDN\n
        The profileEnd method stops recording a profile previously started with Console.profile().\n

        You can optionally supply an argument to name the profile.\n
        Doing so enables you to stop only that profile if you have multiple profiles being recorded.\n

        ・ if Console.profileEnd() is passed a profile name, and it matches the name of a profile being recorded, then that profile is stopped.\n
        ・ if Console.profileEnd() is passed a profile name and it does not match the name of a profile being recorded, no changes will be made.\n
        ・ if Console.profileEnd() is not passed a profile name, the most recently started profile is stopped.
        """
        if profileName != '':
            evaluate(f'console.profileEnd("{str(profileName)}")', return_value=False)
        else:
            evaluate(f'console.profileEnd()', return_value=False)

    def table(self, object):
        """
        According to MDN\n
        Displays tabular data as a table.\n

        This function takes one mandatory argument data, which must be an array or an object, and one additional optional parameter columns.\n

        It logs data as a table.\n
        Each element in the array (or enumerable property if data is an object) will be a row in the table.\n

        The first column in the table will be labeled (index).\n
        If data is an array, then its values will be the array indices.\n
        If data is an object, then its values will be the property names.\n
        Note that (in Firefox) console.table is limited to displaying 1000 rows (first row is the labeled index).
        """
        evaluate(f'console.table({str(object)})', return_value=False)

    def time(self, label=''):
        """
        According to MDN\n
        Starts a timer you can use to track how long an operation takes.\n
        You give each timer a unique name, and may have up to 10,000 timers running on a given page.\n
        When you call console.timeEnd() with the same name, the browser will output the time, in milliseconds, that elapsed since the timer was started.
        """
        if label != "":
            evaluate(f'console.time("{str(label)}")', return_value=False)
        else:
            evaluate('console.time()', return_value=False)

    def timeEnd(self, label=''):
        """
        According to MDN\n
        Stops a timer that was previously started by calling console.time().
        """
        if label != "":
            evaluate(f'console.timeEnd("{str(label)}")', return_value=False)
        else:
            evaluate('console.timeEnd()', return_value=False)

    def timeLog(self, label=''):
        """
        According to MDN\n
        Logs the current value of a timer that was previously started by calling console.time() to the console.
        """
        if label != "":
            evaluate(f'console.timeLog("{str(label)}")', return_value=False)
        else:
            evaluate('console.timeLog()', return_value=False)

    def timeStamp(self, label=''):
        """
        According to MDN\n
        Adds a single marker to the browser's Performance or Waterfall tool.\n
        This lets you correlate a point in your code with the other events recorded in the timeline, such as layout and paint events.\n

        You can optionally supply an argument to label the timestamp, and this label will then be shown alongside the marker.
        """
        if label != "":
            evaluate(f'console.timeStamp("{str(label)}")', return_value=False)
        else:
            evaluate('console.timeStamp()', return_value=False)

    def trace(self, message=''):
        """
        According to MDN\n
        The console interface's trace() method outputs a stack trace to the Web Console.
        """
        if message != "":
            evaluate(f'console.timeStamp("{str(message)}")', return_value=False)
        else:
            evaluate('console.timeStamp()', return_value=False)

    def warn(self, message):
        """
        According to MDN\n
        Outputs a warning message to the Web Console.
        """
        evaluate(f'console.warn("{str(message)}")', return_value=False)

class _Screen():
    """
    According to MDN\n
    The Screen interface represents a screen, usually the one on which the current window is being rendered, and is obtained using window.screen.\n

    Note that browsers determine which screen to report as current by detecting which screen has the center of the browser window.
    """

    class _ScreenOrientation():
        def __init__(self):
            self.angle = evaluate('screen.orientation.angle')
            self.onchange = evaluate('screen.orientation.onchange')
            self.type = evaluate('screen.orientation.type')

    width = evaluate('screen.width')
    height = evaluate('screen.height')
    availWidth = evaluate('screen.availWidth')
    availHeight = evaluate('screen.availHeight')
    colorDepth = evaluate('screen.colorDepth')
    pixelDepth = evaluate('screen.pixelDepth')
    orientation = _ScreenOrientation()

    def lockOrientation(self):
        evaluate('screen.lockOrientation()', return_value=False)
    
    def unlockOrientation(self):
        evaluate('screen.unlockOrientation()', return_value=False)
    

class _History():
    """
    According to MDN\n
    The History interface allows manipulation of the browser session history, that is the pages visited in the tab or frame that the current page is loaded in.
    """

    length = evaluate('history.length')
    scrollRestoration = evaluate('history.scrollRestoration')
    state = evaluate('history.state')

    def back(self):
        """
        According to MDN\n
        This asynchronous method goes to the previous page in session history, the same action as when the user clicks the browser's Back button.\n
        Equivalent to history.go(-1).
        """
        evaluate('history.back()', return_value=False)

    def forward(self):
        """
        According to MDN\n
        This asynchronous method goes to the next page in session history, the same action as when the user clicks the browser's Forward button; this is equivalent to history.go(1)
        """
        evaluate('history.forward()', return_value=False)

    def go(self, number=''):
        """
        According to MDN\n
        Asynchronously loads a page from the session history, identified by its relative location to the current page, for example -1 for the previous page or 1 for the next page.\n
        If you specify an out-of-bounds value (for instance, specifying -1 when there are no previously-visited pages in the session history), this method silently has no effect.\n
        Calling go() without parameters or a value of 0 reloads the current page.\n
        Internet Explorer lets you specify a string, instead of an integer, to go to a specific URL in the history list.
        """
        evaluate(f'hitory.go({str(number)})', return_value=False)

    def pushState(self, state, title, url=""):
        """
        According to MDN\n
        Pushes the given data onto the session history stack with the specified title (and, if provided, URL).\n
        The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized.\n
        Note that all browsers but Safari currently ignore the title parameter.
        """
        if url != "":
            evaluate(f'history.pushState("{str(state)}", "{str(title)}", "{str(url)}")')
        else:
            evaluate(f'history.pushState("{str(state)}", "{str(title)}")')

    def replaceState(self, state, title, url=""):
        """
        According to MDN\n
        Updates the most recent entry on the history stack to have the specified data, title, and, if provided, URL.\n
        The data is treated as opaque by the DOM; you may specify any JavaScript object that can be serialized.\n
        Note that all browsers but Safari currently ignore the title parameter.
        """
        if url != "":
            evaluate(f'history.replaceState("{str(state)}", "{str(title)}", "{str(url)}")')
        else:
            evaluate(f'history.replaceState("{str(state)}", "{str(title)}")')


class _Navigator():
    """
    According to MDN\n
    The Navigator interface represents the state and the identity of the user agent.\n
    It allows scripts to query it and to register themselves to carry on some activities.\n

    A Navigator object can be retrieved using the read-only window.navigator property.  
    """

    class _UserActivation():
        hasBeenActive = evaluate('navigator.userActivation.hasBeenActive')
        isActive = evaluate('navigator.userActivation.isActive')

    class _NetworkInformation():
        """
        According to MDN\n
        The NetworkInformation interface provides information about the connection a device is using to communicate with the network and provides a means for scripts to be notified if the connection type changes.\n
        The NetworkInformation interfaces cannot be instantiated.\n
        It is instead accessed through the connection property of the Navigator interface.
        """
        downlink = evaluate('navigator.connection.downlink')
        effectiveType = evaluate('navigator.connection.effectiveType')
        onchange = evaluate('navigator.connection.onchange')
        rtt = evaluate('navigator.connection.rtt')
        saveData = evaluate('navigator.connection.saveData')

    class _MediaSession():
        """
        According to MDN\n
        The MediaSession interface of the Media Session API allows a web page to provide custom behaviors for standard media playback interactions, and to report metadata that can be sent by the user agent to the device or operating system for presentation in standardized user interface elements.\n

        For example, a smartphone might have a standard panel in its lock screen that provides controls for media.\n
        A browser on that device might deliver the metadata provided by calling MediaSession to the device in order to be controllable using the global user interface.
        """
        metadata = evaluate('navigator.mediaSession.metadata')
        playbackState = evaluate('navigator.mediaSession.playbackState')


    def __init__(self):
        class _MimeType():
            """
            According to MDN\n
            The MimeType interface provides contains information about a MIME type associated with a particular plugin.\n
            NavigatorPlugins.mimeTypes returns an array of this object.
            """
            def __init__(self, path):
                self.description = evaluate(path + '.description')
                self.suffixes = evaluate(path + '.suffixes')
                self.type = evaluate(path + '.type')
        
        class _Plugin():
            """
            According to MDN\n
            The Plugin interface provides information about a browser plugin.
            """
            def __init__(self, path):
                class _MimeType():
                    """
                    According to MDN\n
                    The MimeType interface provides contains information about a MIME type associated with a particular plugin.\n
                    NavigatorPlugins.mimeTypes returns an array of this object.
                    """
                    def __init__(self, path):
                        self.description = evaluate(path + '.description')
                        self.suffixes = evaluate(path + '.suffixes')
                        self.type = evaluate(path + '.type')

                self.description = evaluate(path + '.description')
                self.filename = evaluate(path + '.filename')
                self.length = evaluate(path + '.length')
                self.name = evaluate(path + '.name')
                list_of_element = []
                for number in range(int(self.length)):
                    newMimeElement = _MimeType(path + f'[{str(number)}]')
                    list_of_element.append(newMimeElement)
                self.MimeType = list_of_element

        self.plugins = []
        for number in range(int(evaluate('navigator.plugins.length'))):
            newPluginElement = _Plugin(f'navigator.plugins[{str(number)}]')
            self.plugins.append(newPluginElement)

        self.mimeTypes = []
        for number in range(int(evaluate('navigator.mimeTypes.length'))):
            newMimeElement = _MimeType(f'navigator.mimeTypes[{str(number)}]')
            self.mimeTypes.append(newMimeElement)
        
        self.languages = []
        for number in range(int(evaluate('navigator.languages.length'))):
            self.languages.append(evaluate(f'navigator.languages[{str(number)}]'))

    cookieEnabled = evaluate('navigator.cookieEnabled')
    appName = evaluate('navigator.appName')
    appCodeName = evaluate('navigator.appCodeName')
    product = evaluate('navigator.product')
    productSub = evaluate('navigator.productSub')
    appVersion = evaluate('navigator.appVersion')
    userAgent = evaluate('navigator.userAgent')
    platform = evaluate('navigator.platform')
    language = evaluate('navigator.language')
    onLine = evaluate('navigator.onLine')
    doNotTrack = evaluate('navigator.doNotTrack')
    maxTouchPoints = evaluate('navigator.maxTouchPoints')
    hardwareConcurrency = evaluate('navigator.hardwareConcurrency')
    vendor = evaluate('navigator.vendor')
    vendorSub = evaluate('navigator.vendorSub')
    userActivation = _UserActivation()

    def javaEnabled(self):
        """
        According to MDN\n
        Returns a Boolean flag indicating whether the host browser is Java-enabled or not.
        """
        return evaluate('navigator.javaEnabled()')

def setTimeout(function, milliseconds):
    """
    According to w3schools\n
    Executes a function, after waiting a specified number of milliseconds.

    > Returns an identifier for the timeout process (called timeoutID in the arguments of clearTimeout())
    """
    return evaluate(f'setTimeout("{str(function)}", {str(milliseconds)})')

def setInterval(function, milliseconds):
    """
    According to w3schools\n
    Same as setTimeout(), but repeats the execution of the function continuously.

    > Returns an identifier for the interval process (called intervalID in the arguments of clearInterval())
    """
    return evaluate(f'setInterval({str(function)}, {str(milliseconds)})')

def clearTimeout(timeoutID):
    """
    According to w3schools\n
    The clearTimeout() method stops the execution of the function specified in setTimeout().
    """
    evaluate(f'clearTimeout({str(timeoutID)})', return_value=False)

def clearInterval(intervalID):
    """
    According to w3schools\n
    The clearInterval() method stops the executions of the function specified in the setInterval() method.
    """
    evaluate(f'clearInterval({str(intervalID)})', return_value=False)

class _Window():
    """
    According to MDN\n

    The Window interface represents a window containing a DOM document; the document property points to the DOM document loaded in that window.\n
    A window for a given document can be obtained using the document.defaultView property.\n

    A global variable, window, representing the window in which the script is running, is exposed to JavaScript code.\n

    The Window interface is home to a variety of functions, namespaces, objects, and constructors which are not necessarily directly associated with the concept of a user interface window.\n
    However, the Window interface is a suitable place to include these items that need to be globally available.\n
    Many of these are documented in the JavaScript Reference and the DOM Reference.\n

    In a tabbed browser, each tab is represented by its own Window object; the global window seen by JavaScript code running within a given tab always represents the tab in which the code is running.\n
    That said, even in a tabbed browser, some properties and methods still apply to the overall window that contains the tab, such as resizeTo() and innerHeight.\n
    Generally, anything that can't reasonably pertain to a tab pertains to the window instead.
    """

    class _Location():
        """
        According to MDN\n
        The Window.location read-only property returns a Location object with information about the current location of the document.\n

        Though Window.location is a read-only Location object, you can also assign a DOMString to it.\n
        This means that you can work with location as if it were a string in most cases: location = 'http://www.example.com' is a synonym of location.href = 'http://www.example.com'.
        """
        href = evaluate('window.location.href')
        hostname = evaluate('window.location.hostname')
        pathname = evaluate('window.location.pathname')
        protocol = evaluate('window.location.protocol')
        port = evaluate('window.location.port')

        def assign(self, URL):
            """
            According to MDN\n
            Loads the resource at the URL provided in parameter.
            """
            return evaluate(f'window.location.assign("{str(URL)}"")', return_value=False)

        def reload(self):
            """
            According to MDN\n
            Reloads the current URL, like the Refresh button.
            """
            return evaluate(f'window.location.reload()', return_value=False)

        def replace(self, URL):
            """
            According to MDN\n
            Replaces the current resource with the one at the provided URL (redirects to the provided URL).\n
            The difference from the assign() method and setting the href property is that after using replace() the current page will not be saved in session History, meaning the user won't be able to use the back button to navigate to it.
            """
            return evaluate(f'window.location.replace("{str(URL)}"")', return_value=False)

        def toString(self):
            """
            According to MDN\n
            Returns a USVString containing the whole URL.\n
            It is a synonym for HTMLHyperlinkElementUtils.href, though it can't be used to modify the value.
            """
            return evaluate(f'window.location.toString()')

    innerHeight = evaluate('window.innerHeight')
    innerWidth = evaluate('window.innerWidth')
    location = _Location()
    screen = _Screen()
    history = _History()
    navigator = _Navigator()
    console = _Console()

    def close(self):
        """
        According to MDN\n
        Closes the current window.
        """
        evaluate('window.close()', return_value=False)

    def kill(self):
        """
        pyJsConsole specific command.\n
        Kills the browser process.
        """
        browser.kill()

    def open(self, URL, windowName='', windowFeatures=''):
        """
        According to MDN\n
        The Window interface's open() method loads the specified resource into the new or existing browsing context (window, <iframe> or tab) with the specified name.\n
        If the name doesn't exist, then a new browsing context is opened in a new tab or a new window, and the specified resource is loaded into it.
        """
        return evaluate(f'window.open("{str(URL)}", "{str(windowName)}", "{str(windowFeatures)}")', return_value=False)
    
    def moveTo(self, x, y):
        """
        According to MDN\n
        Moves the window to the specified coordinates.
        """
        return evaluate(f'window.moveTo("{str(x)}", "{str(y)}")', return_value=False)
    
    def resizeTo(self, width, height):
        """
        According to MDN\n
        Dynamically resizes window.
        """
        return evaluate(f'window.resizeTo("{str(width)}", "{str(height)}")', return_value=False)

    def alert(self, text):
        """
        According to MDN\n
        Displays an alert dialog.
        """
        try:
            evaluate(f'window.alert("{str(text)}")', return_value=False)
        except:
            pass

    def confirm(self, text):
        """
        According to MDN\n
        Displays a dialog with a message that the user needs to respond to.
        """
        try:
            evaluate(f'a = window.confirm("{str(text)}")', return_value=False)
            return evaluate('a')
        except:
            return False

    def prompt(self, text):
        """
        According to MDN\n
        Returns the text entered by the user in a prompt dialog.
        """
        try:
            evaluate(f'a = window.prompt("{str(text)}")', return_value=False)
            return evaluate('a')
        except:
            return False

    def setTimeout(self, function, milliseconds):
        """
        According to w3schools\n
        Executes a function, after waiting a specified number of milliseconds.

        > Returns an identifier for the timeout process (called timeoutID in the arguments of clearTimeout())
        """
        return evaluate(f'setTimeout("{str(function)}", {str(milliseconds)})')

    def setInterval(self, function, milliseconds):
        """
        According to w3schools\n
        Same as setTimeout(), but repeats the execution of the function continuously.

        > Returns an identifier for the interval process (called intervalID in the arguments of clearInterval())
        """
        return evaluate(f'setInterval("{str(function)}", {str(milliseconds)})')

    def clearTimeout(self, timeoutID):
        """
        According to w3schools\n
        The clearTimeout() method stops the execution of the function specified in setTimeout().
        """
        evaluate(f'clearTimeout({str(timeoutID)})', return_value=False)

    def clearInterval(self, intervalID):
        """
        According to w3schools\n
        The clearInterval() method stops the executions of the function specified in the setInterval() method.
        """
        evaluate(f'clearInterval({str(intervalID)})', return_value=False)

class _Attribute():
    def __init__(self):
        self._calling_method = ''

    @property
    def calling_method(self):
        return self._calling_method
    @calling_method.setter
    def calling_method(self, value):
        self._calling_method = value

        self._name = evaluate(self._calling_method + '.name')
        self._namespaceURI = evaluate(self._calling_method + '.namespaceURI')
        self._localName = evaluate(self._calling_method + '.localName')
        self._prefix = evaluate(self._calling_method + '.prefix')
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = self._calling_method + '.ownerElement'
        self._ownerElement = newDOMElement
        self._specified = evaluate(self._calling_method + '.specified')
        self._value = evaluate(self._calling_method + '.value')


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        raise ReadOnlyError('<document.name> is a read-only property.')

    @property
    def namespaceURI(self):
        return self._namespaceURI
    @namespaceURI.setter
    def namespaceURI(self, value):
        raise ReadOnlyError('<document.namespaceURI> is a read-only property.')

    @property
    def localName(self):
        return self._localName
    @localName.setter
    def localName(self, value):
        raise ReadOnlyError('<document.localName> is a read-only property.')

    @property
    def prefix(self):
        return self._prefix
    @prefix.setter
    def prefix(self, value):
        raise ReadOnlyError('<document.prefix> is a read-only property.')

    @property
    def ownerElement(self):
        return self._ownerElement
    @ownerElement.setter
    def ownerElement(self, value):
        raise ReadOnlyError('<document.ownerElement> is a read-only property.')

    @property
    def specified(self):
        return self._specified
    @specified.setter
    def specified(self, value):
        raise ReadOnlyError('<document.specified> is a read-only property.')

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        evaluate(self._calling_method + f'.value = "{str(value)}"', return_value=False)
        self._value = value

class _DOMElement():
    def __init__(self):
        self._calling_method = ''

    @property
    def calling_method(self):
        return self._calling_method

    @calling_method.setter
    def calling_method(self, value):
        self._calling_method = value
        self._id = evaluate(value + '.id')
        self._innerHTML = evaluate(value + '.innerHTML')
        self._innerText = evaluate(value + '.innerText')
        self._style = evaluate(value + '.style')
        self._textContent = evaluate(value + '.textContent')
        self._title = evaluate(value + '.title')

        self._accessKey = evaluate(value + '.accessKey')
        self._childElementCount = evaluate(value + '.childElementCount')
        self._className = evaluate(value + '.className')
        self._clientHeight = evaluate(value + '.clientHeight')
        self._clientLeft = evaluate(value + '.clientLeft')
        self._clientTop = evaluate(value + '.clientTop')
        self._clientWidth = evaluate(value + '.clientWidth')
        self._contentEditable = evaluate(value + '.contentEditable')
        self._dir = evaluate(value + '.dir')
        self._isContentEditable = evaluate(value + '.isContentEditable')
        self._lang = evaluate(value + '.lang')
        self._nodeName = evaluate(value + '.nodeName')
        self._nodeType = evaluate(value + '.nodeType')
        self._nodeValue = evaluate(value + '.nodeValue')
        self._offsetHeight = evaluate(value + '.offsetHeight')
        self._offsetWidth = evaluate(value + '.offsetWidth')
        self._offsetLeft = evaluate(value + '.offsetLeft')
        self._offsetParent = evaluate(value + '.offsetParent')
        self._offsetTop = evaluate(value + '.offsetTop')
        self._outerHTML = evaluate(value + '.outerHTML')
        self._outerText = evaluate(value + '.outerText')
        self._scrollHeight = evaluate(value + '.scrollHeight')
        self._scrollLeft = evaluate(value + '.scrollLeft')
        self._scrollTop = evaluate(value + '.scrollTop')
        self._scrollWidth = evaluate(value + '.scrollWidth')
        self._tabIndex = evaluate(value + '.tabIndex')
        self._tagName = evaluate(value + '.tagName')

        length = evaluate(value + '.childNodes.length')
        list_of_dom = []
        for number in range(int(length)):
            newDOMElement = _DOMElement()
            newDOMElement._calling_method = value + f'.childNodes[{str(number)}]'
            list_of_dom.append(newDOMElement)
        self._childNodes = list_of_dom

        length = evaluate(value + '.children.length')
        list_of_dom = []
        for number in range(int(length)):
            newDOMElement = _DOMElement()
            newDOMElement._calling_method = value + f'.children[{str(number)}]'
            list_of_dom.append(newDOMElement)
        self._children = list_of_dom

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.firstChild'
        self._firstChild = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.firstElementChild'
        self._firstElementChild = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.lastChild'
        self._lastChild = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.lastElementChild'
        self._lastElementChild = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.nextSibling'
        self._nextSibling = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.nextElementSibling'
        self._nextElementSibling = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.parentNode'
        self._parentNode = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.parentElement'
        self._parentElement = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.previousSibling'
        self._previousSibling = newDOMElement

        newDOMElement = _DOMElement()
        newDOMElement._calling_method = value + '.previousElementSibling'
        self._previousElementSibling = newDOMElement


        class _ClassList(object):
            def __init__(self, domobject):
                self.domobject = domobject
            
            def add(self, className):
                evaluate(self.domobject._calling_method + f'.classList.add("{str(className)}")', return_value=False)

            def remove(self, className):
                evaluate(self.domobject._calling_method + f'.classList.remove("{str(className)}")', return_value=False)
            
            def toggle(self, className):
                evaluate(self.domobject._calling_method + f'.classList.toggle("{str(className)}")', return_value=False)

            def contains(self, className):
                return evaluate(self.domobject._calling_method + f'.classList.contains("{str(className)}")')
                
            def item(self, index):
                return evaluate(self.domobject._calling_method + f'.classList.index("{str(index)}")')

        self.classList = _ClassList(self)


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        evaluate(self._calling_method + f'.id = "{str(value)}"', return_value=False)
        self._calling_method = f'document.getElementById("{str(value)}")'
        self._id = value

    @property
    def innerHTML(self):
        return self._innerHTML
    @innerHTML.setter
    def innerHTML(self, value):
        evaluate(self._calling_method + f'.innerHTML = "{str(value)}"', return_value=False)
        self._innerHTML = value

    @property
    def innerText(self):
        """
        Hey Hey
        """
        return self._innerText
    @innerText.setter
    def innerText(self, value):
        evaluate(self._calling_method + f'.innerText = "{str(value)}"', return_value=False)
        self._innerText = value

    @property
    def style(self):
        return self._style
    @style.setter
    def style(self, value):
        evaluate(self._calling_method + f'.style = "{str(value)}"', return_value=False)
        self._style = value

    @property
    def textContent(self):
        return self._textContent
    @textContent.setter
    def textContent(self, value):
        evaluate(self._calling_method + f'.textContent = "{str(value)}"', return_value=False)
        self._textContent = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        evaluate(self._calling_method + f'.title = "{str(value)}"', return_value=False)
        self._title = value

    @property
    def accessKey(self):
        return self._accessKey
    @accessKey.setter
    def accessKey(self, value):
        evaluate(self._calling_method + f'.accessKey = "{str(value)}"', return_value=False)
        self._accessKey = value

    @property
    def childElementCount(self):
        return self._childElementCount
    @childElementCount.setter
    def childElementCount(self, value):
        evaluate(self._calling_method + f'.childElementCount = "{str(value)}"', return_value=False)
        self._childElementCount = value

    @property
    def className(self):
        return self._className
    @className.setter
    def className(self, value):
        evaluate(self._calling_method + f'.className = "{str(value)}"', return_value=False)
        self._className = value

    @property
    def clientHeight(self):
        return self._clientHeight
    @clientHeight.setter
    def clientHeight(self, value):
        evaluate(self._calling_method + f'.clientHeight = "{str(value)}"', return_value=False)
        self._clientHeight = value

    @property
    def clientLeft(self):
        return self._clientLeft
    @clientLeft.setter
    def clientLeft(self, value):
        evaluate(self._calling_method + f'.clientLeft = "{str(value)}"', return_value=False)
        self._clientLeft = value

    @property
    def clientTop(self):
        return self._clientTop
    @clientTop.setter
    def clientTop(self, value):
        evaluate(self._calling_method + f'.clientTop = "{str(value)}"', return_value=False)
        self._clientTop = value

    @property
    def clientWidth(self):
        return self._clientWidth
    @clientWidth.setter
    def clientWidth(self, value):
        evaluate(self._calling_method + f'.clientWidth = "{str(value)}"', return_value=False)
        self._clientWidth = value

    @property
    def contentEditable(self):
        return self._contentEditable
    @contentEditable.setter
    def contentEditable(self, value):
        evaluate(self._calling_method + f'.contentEditable = "{str(value)}"', return_value=False)
        self._contentEditable = value

    @property
    def dir(self):
        return self._dir
    @dir.setter
    def dir(self, value):
        evaluate(self._calling_method + f'.dir = "{str(value)}"', return_value=False)
        self._dir = value

    @property
    def isContentEditable(self):
        return self._isContentEditable
    @isContentEditable.setter
    def isContentEditable(self, value):
        evaluate(self._calling_method + f'.isContentEditable = "{str(value)}"', return_value=False)
        self._isContentEditable = value

    @property
    def lang(self):
        return self._lang
    @lang.setter
    def lang(self, value):
        evaluate(self._calling_method + f'.lang = "{str(value)}"', return_value=False)
        self._lang = value

    @property
    def nodeName(self):
        return self._nodeName
    @nodeName.setter
    def nodeName(self, value):
        evaluate(self._calling_method + f'.nodeName = "{str(value)}"', return_value=False)
        self._nodeName = value

    @property
    def nodeType(self):
        return self._nodeType
    @nodeType.setter
    def nodeType(self, value):
        evaluate(self._calling_method + f'.nodeType = "{str(value)}"', return_value=False)
        self._nodeType = value

    @property
    def nodeValue(self):
        return self._nodeValue
    @nodeValue.setter
    def nodeValue(self, value):
        evaluate(self._calling_method + f'.nodeValue = "{str(value)}"', return_value=False)
        self._nodeValue = value

    @property
    def offsetHeight(self):
        return self._offsetHeight
    @offsetHeight.setter
    def offsetHeight(self, value):
        evaluate(self._calling_method + f'.offsetHeight = "{str(value)}"', return_value=False)
        self._offsetHeight = value

    @property
    def offsetWidth(self):
        return self._offsetWidth
    @offsetWidth.setter
    def offsetWidth(self, value):
        evaluate(self._calling_method + f'.offsetWidth = "{str(value)}"', return_value=False)
        self._offsetWidth = value

    @property
    def offsetLeft(self):
        return self._offsetLeft
    @offsetLeft.setter
    def offsetLeft(self, value):
        evaluate(self._calling_method + f'.offsetLeft = "{str(value)}"', return_value=False)
        self._offsetLeft = value

    @property
    def offsetParent(self):
        return self._offsetParent
    @offsetParent.setter
    def offsetParent(self, value):
        evaluate(self._calling_method + f'.offsetParent = "{str(value)}"', return_value=False)
        self._offsetParent = value

    @property
    def offsetTop(self):
        return self._offsetTop
    @offsetTop.setter
    def offsetTop(self, value):
        evaluate(self._calling_method + f'.offsetTop = "{str(value)}"', return_value=False)
        self._offsetTop = value

    @property
    def outerHTML(self):
        return self._outerHTML
    @outerHTML.setter
    def outerHTML(self, value):
        evaluate(self._calling_method + f'.outerHTML = "{str(value)}"', return_value=False)
        self._outerHTML = value

    @property
    def outerText(self):
        return self._outerText
    @outerText.setter
    def outerText(self, value):
        evaluate(self._calling_method + f'.outerText = "{str(value)}"', return_value=False)
        self._outerText = value

    @property
    def scrollHeight(self):
        return self._scrollHeight
    @scrollHeight.setter
    def scrollHeight(self, value):
        evaluate(self._calling_method + f'.scrollHeight = "{str(value)}"', return_value=False)
        self._scrollHeight = value

    @property
    def scrollLeft(self):
        return self._scrollLeft
    @scrollLeft.setter
    def scrollLeft(self, value):
        evaluate(self._calling_method + f'.scrollLeft = "{str(value)}"', return_value=False)
        self._scrollLeft = value

    @property
    def scrollTop(self):
        return self._scrollTop
    @scrollTop.setter
    def scrollTop(self, value):
        evaluate(self._calling_method + f'.scrollTop = "{str(value)}"', return_value=False)
        self._scrollTop = value

    @property
    def scrollWidth(self):
        return self._scrollWidth
    @scrollWidth.setter
    def scrollWidth(self, value):
        evaluate(self._calling_method + f'.scrollWidth = "{str(value)}"', return_value=False)
        self._scrollWidth = value

    @property
    def tabIndex(self):
        return self._tabIndex
    @tabIndex.setter
    def tabIndex(self, value):
        evaluate(self._calling_method + f'.tabIndex = "{str(value)}"', return_value=False)
        self._tabIndex = value

    @property
    def tagName(self):
        return self._tagName
    @tagName.setter
    def tagName(self, value):
        evaluate(self._calling_method + f'.tagName = "{str(value)}"', return_value=False)
        self._tagName = value

    

    @property
    def childNodes(self):
        return self._childNodes
    @childNodes.setter
    def childNodes(self, value):
        evaluate(self._calling_method + f'.childNodes = "{str(value)}"', return_value=False)
        self._childNodes = value

    @property
    def children(self):
        return self._children
    @children.setter
    def children(self, value):
        evaluate(self._calling_method + f'.children = "{str(value)}"', return_value=False)
        self._children = value

    @property
    def firstChild(self):
        return self._firstChild
    @firstChild.setter
    def firstChild(self, value):
        evaluate(self._calling_method + f'.firstChild = "{str(value)}"', return_value=False)
        self._firstChild = value

    @property
    def firstElementChild(self):
        return self._firstElementChild
    @firstElementChild.setter
    def firstElementChild(self, value):
        evaluate(self._calling_method + f'.firstElementChild = "{str(value)}"', return_value=False)
        self._firstElementChild = value

    @property
    def lastChild(self):
        return self._lastChild
    @lastChild.setter
    def lastChild(self, value):
        evaluate(self._calling_method + f'.lastChild = "{str(value)}"', return_value=False)
        self._lastChild = value

    @property
    def lastElementChild(self):
        return self._lastElementChild
    @lastElementChild.setter
    def lastElementChild(self, value):
        evaluate(self._calling_method + f'.lastElementChild = "{str(value)}"', return_value=False)
        self._lastElementChild = value

    @property
    def nextSibling(self):
        return self._nextSibling
    @nextSibling.setter
    def nextSibling(self, value):
        evaluate(self._calling_method + f'.nextSibling = "{str(value)}"', return_value=False)
        self._nextSibling = value

    @property
    def nextElementSibling(self):
        return self._nextElementSibling
    @nextElementSibling.setter
    def nextElementSibling(self, value):
        evaluate(self._calling_method + f'.nextElementSibling = "{str(value)}"', return_value=False)
        self._nextElementSibling = value

    @property
    def parentNode(self):
        return self._parentNode
    @parentNode.setter
    def parentNode(self, value):
        evaluate(self._calling_method + f'.parentNode = "{str(value)}"', return_value=False)
        self._parentNode = value

    @property
    def parentElement(self):
        return self._parentElement
    @parentElement.setter
    def parentElement(self, value):
        evaluate(self._calling_method + f'.parentElement = "{str(value)}"', return_value=False)
        self._parentElement = value

    @property
    def previousSibling(self):
        return self._previousSibling
    @previousSibling.setter
    def previousSibling(self, value):
        evaluate(self._calling_method + f'.previousSibling = "{str(value)}"', return_value=False)
        self._previousSibling = value

    @property
    def previousElementSibling(self):
        return self._previousElementSibling
    @previousElementSibling.setter
    def previousElementSibling(self, value):
        evaluate(self._calling_method + f'.previousElementSibling = "{str(value)}"', return_value=False)
        self._previousElementSibling = value
    

    def addEventListener(self, eventListener, function):
        evaluate(self._calling_method + f'.addEventListener("{str(eventListener)}, {str(function)}")', return_value=False)

    def appendChild(self, DOMElement):
        evaluate(self._calling_method + f'.appendChild({DOMElement._calling_method})', return_value=False)

    def blur(self):
        evaluate(self._calling_method + '.blur()', return_value=False)
    
    def click(self):
        evaluate(self._calling_method + '.click()', return_value=False)
    
    def cloneNode(self):
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = self._calling_method
        return newDOMElement
    
    def compareDocumentPosition(self, DOMElement):
        evaluate('var element = ' + DOMElement._calling_method, return_value=False)
        return evaluate(self._calling_method + '.compareDocumentPosition(element)')
    
    def contains(self, DOMElement):
        evaluate('var element = ' + DOMElement._calling_method, return_value=False)
        return evaluate(self._calling_method + '.contains(element)')
    
    def exitFullscreen(self):
        evaluate(self._calling_method + '.exitFullscreen()', return_value=False)
    
    def focus(self):
        evaluate(self._calling_method + '.focus()', return_value=False)
    
    def getAttribute(self, attributeName):
        return evaluate(self._calling_method + f'.getAttribute("{str(attribute)}")')
    
    def getAttributeNode(self, attributeName):
        newAttributeElement = _Attribute()
        newAttributeElement.calling_method = self._calling_method + f'.getAttributeNode("{str(attribute)}")'
        return newAttributeElement
    
    def getBoundingClientRect(self):
        return evaluate(self._calling_method + '.getBoundingClientRect()')

    def getElementsByClassName(self, className):
        length = evaluate(self._calling_method + f'.getElementsByClassName({className}).length')
        list_of_dom = []
        for number in range(int(length)):
            newDOMElement = _DOMElement()
            newDOMElement._calling_method = self._calling_method + f'.getElementsByClassName({className})[{str(number)}]'
            list_of_dom.append(newDOMElement)
        return list_of_dom

    def getElementsByTagName(self, className):
        length = evaluate(self._calling_method + f'.getElementsByTagName({className}).length')
        list_of_dom = []
        for number in range(int(length)):
            newDOMElement = _DOMElement()
            newDOMElement._calling_method = self._calling_method + f'.getElementsByTagName({className})[{str(number)}]'
            list_of_dom.append(newDOMElement)
        return list_of_dom

    def hasAttribute(self, attribute):
        return evaluate(self._calling_method + f'.hasAttribute("{str(attribute)}")')
    
    def hasAttributes(self, attributes):
        return evaluate(self._calling_method + f'.hasAttributes("{str(attributes)}")')
    
    def hasChildNodes(self):
        return evaluate(self._calling_method + '.hasChildNodes()')
    
    def insertAdjacentElement(self, position, DOMElement):
        evaluate(self._calling_method + f'.insertAdjacentElement("{str(position)}","{str(DOMElement._calling_method)}")', return_value=False)
    
    def insertAdjacentHTML(self, position, html):
        evaluate(self._calling_method + f'.insertAdjacentHTML("{str(position)}","{str(html)}")', return_value=False)
    
    def insertAdjacentText(self, position, text):
        evaluate(self._calling_method + f'.insertAdjacentText("{str(position)}","{str(text)}")', return_value=False)
    
    def insertBefore(self, newDOMElement, positionDOMElement):
        evaluate(self._calling_method + f'.insertAdjacentText("{str(newDOMElement._calling_method)}","{str(positionDOMElement._calling_method)}")', return_value=False)
    
    def isEqualNode(self, DOMElement):
        evaluate(self._calling_method + f'.isEqualNode("{str(DOMElement._calling_method)}")')
        
    def isSameNode(self, DOMElement):
        if DOMElement.calling_method == self._calling_method:
            return True
        
    def isSupported(self, feature, version):
        return evaluate(self._calling_method + f'.isSupported("{str(feature)}","{str(version)}")')
    
    def normalize(self):
        evaluate(self._calling_method + '.normalize()')

    def querySelector(self, query):
        newDOMElement = _DOMElement()
        newDOMElement._calling_method = self._calling_method + f'.querySelector("{str(query)}")'
        return newDOMElement

    def querySelectorAll(self, query):
        length = evaluate(self._calling_method + f'.querySelectorAll("{query}").length')
        list_of_dom = []
        for number in range(int(length)):
            newDOMElement = _DOMElement()
            newDOMElement._calling_method = self._calling_method + f'.querySelectorAll("{query}")[{str(number)}]'
            list_of_dom.append(newDOMElement)
        return list_of_dom

    def remove(self):
        evaluate(self._calling_method + '.remove()', return_value=False)
    
    def removeAttribute(self, attributeName):
        evaluate(self._calling_method + f'.removeAttribute("{str(attributeName)}")', return_value=False)
    
    def removeChild(self, DOMElement):
        evaluate(self._calling_method + f'.removeChild("{str(DOMElement._calling_method)}")', return_value=False)
    
    def removeEventListener(self, eventListener):
        evaluate(self._calling_method + f'.removeEventListener("{str(eventListener)}")', return_value=False)
    
    def replaceChild(self, DOMElement, DOMElementToReplace):
        evaluate(self._calling_method + f'.replaceChild("{str(DOMElement._calling_method)}", "{str(DOMElementToReplace._calling_method)}")', return_value=False)
    
    def requestFullscreen(self):
        evaluate(self._calling_method + '.requestFullscreen()', return_value=False)
    
    def scrollIntoView(self, alignTo=False):
        if alignTo:
            evaluate(self._calling_method + '.scrollIntoView(alignTo=true)', return_value=False)
        else:
            evaluate(self._calling_method + '.scrollIntoView()', return_value=False)

    def setAttribute(self, attributeName, attributeValue):
        evaluate(self._calling_method + f'.setAttribute("{str(attributeName)}", "{str(attributeValue)}")', return_value=False)
    
    def toString(self):
        return evaluate(self._calling_method + '.toString()')
    
    
# document Element Class
class _Document():
    """
    According to MDN\n
    The Document interface represents any web page loaded in the browser and serves as an entry point into the web page's content, which is the DOM tree.\n
    The DOM tree includes elements such as <body> and <table>, among many others.\n
    It provides functionality globally to the document, like how to obtain the page's URL and create new elements in the document.
    """

########## METHODS/FUNCTIONS
    def __init__(self):
        ###
        self._anchors = evaluate('document.anchors')
        self._body = evaluate('document.body')
        self._characterSet = evaluate('document.characterSet')
        self._compatMode = evaluate('document.compatMode')
        self._contentType = evaluate('document.contentType')
        self._doctype = evaluate('document.doctype')
        self._documentElement = evaluate('document.documentElement')
        self._documentURI = evaluate('document.documentURI')
        self._embeds = evaluate('document.embeds')
        self._fonts = evaluate('document.fonts')
        self._forms = evaluate('document.forms')
        self._head = evaluate('document.head')
        self._hidden = evaluate('document.hidden')
        self._images = evaluate('document.images')
        self._implementation = evaluate('document.implementation')
        self._lastStyleSheetSet = evaluate('document.lastStyleSheetSet')
        self._links = evaluate('document.links')
        self._plugins = evaluate('document.plugins')
        self._featurePolicy = evaluate('document.featurePolicy')
        self._preferredStyleSheetSet = evaluate('document.preferredStyleSheetSet')
        self._scripts = evaluate('document.scripts')
        self._scrollingElement = evaluate('document.scrollingElement')
        self._selectedStyleSeetSet = evaluate('document.selectedStyleSeetSet')
        self._styleSheetSets = evaluate('document.styleSheetSets')
        self._timeline = evaluate('document.timeline')
        self._undoManager = evaluate('document.undoManager')
        self._visibilityState = evaluate('document.visibilityState')
        self._childElementCount = evaluate('document.childElementCount')
        self._children = evaluate('document.children')
        self._firstElementChild = evaluate('document.firstElementChild')
        self._lastElementChild = evaluate('document.lastElementChild')
        try:
            self._cookie = evaluate('document.cookie')
        except:
            self._cookie = None
        self._defaultView = _Window()
        self._designMode = evaluate('document.designMode')
        self._dir = evaluate('document.dir')
        self._domain = evaluate('document.domain')
        self._lastModified = evaluate('document.lastModified')
        self._location = evaluate('document.location')
        self._readyState = evaluate('document.readyState')
        self._referrer = evaluate('document.referrer')
        self._title = evaluate('document.title')
        self._URL = evaluate('document.URL')
        self._activeElement = evaluate('document.activeElement')
        self._fullscreenElement = evaluate('document.fullscreenElement')
        self._pointerLockElement = evaluate('document.pointerLockElement')
        self._styleSheets = evaluate('document.styleSheets')



    def getElementById(self, id):
        """
        According to MDN\n
        Returns an object reference to the identified element.
        """
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementById("{str(id)}")'
        return newDOMElement
    
    def getElementsByClassName(self, className):
        """
        According to MDN\n
        Returns a list of elements with the given class name.
        """
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementsByClassName("{str(className)}")'
        return newDOMElement
    
    def getElementsByName(self, name):
        """
        According to MDN\n
        Returns a list of elements with the given name.
        """
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementsByName("{str(name)}")'
        return newDOMElement
    
    def getElementsByTagName(self, tagName):
        """
        According to MDN\n
        Returns a list of elements with the given tag name.
        """
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementsByTagName("{str(tagName)}")'
        return newDOMElement
    
    def getElementsByTagNameNS(self, tagName):
        """
        According to MDN\n
        Returns a list of elements with the given tag name and namespace.
        """
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementsByTagNameNS("{str(tagName)}")'
        return newDOMElement

    def createElement(self, type):
        """
        According to MDN\n
        Creates a new element with the given tag name.
        """
        variable_name = str(createRandomString(12))
        evaluate(f'document.getElementsByTagName("html")[0].insertAdjacentHTML("beforeend", "<{type} id=\\"python_animenosekai_{variable_name}\\"></{type}>")', return_value=False)
        newDOMElement = _DOMElement()
        newDOMElement.calling_method = f'document.getElementById("python_animenosekai_{variable_name}")'
        return newDOMElement




########### PROPERTIES
##### READ-ONLY
    @property
    def anchors(self):
        return self._anchors
    @anchors.setter
    def anchors(self, value):
        raise ReadOnlyError('<document.anchors> is a read-only property.')

    @property
    def characterSet(self):
        return self._characterSet
    @characterSet.setter
    def characterSet(self, value):
        raise ReadOnlyError('<document.characterSet> is a read-only property.')

    @property
    def compatMode(self):
        return self._compatMode
    @compatMode.setter
    def compatMode(self, value):
        raise ReadOnlyError('<document.compatMode> is a read-only property.')

    @property
    def contentType(self):
        return self._contentType
    @contentType.setter
    def contentType(self, value):
        raise ReadOnlyError('<document.contentType> is a read-only property.')

    @property
    def doctype(self):
        return self._doctype
    @doctype.setter
    def doctype(self, value):
        raise ReadOnlyError('<document.doctype> is a read-only property.')

    @property
    def documentElement(self):
        return self._documentElement
    @documentElement.setter
    def documentElement(self, value):
        raise ReadOnlyError('<document.documentElement> is a read-only property.')

    @property
    def documentURI(self):
        return self._documentURI
    @documentURI.setter
    def documentURI(self, value):
        raise ReadOnlyError('<document.documentURI> is a read-only property.')

    @property
    def embeds(self):
        return self._embeds
    @embeds.setter
    def embeds(self, value):
        raise ReadOnlyError('<document.embeds> is a read-only property.')

    @property
    def forms(self):
        return self._forms
    @forms.setter
    def forms(self, value):
        raise ReadOnlyError('<document.forms> is a read-only property.')

    @property
    def head(self):
        return self._head
    @head.setter
    def head(self, value):
        raise ReadOnlyError('<document.head> is a read-only property.')

    @property
    def hidden(self):
        return self._hidden
    @hidden.setter
    def hidden(self, value):
        raise ReadOnlyError('<document.hidden> is a read-only property.')

    @property
    def images(self):
        return self._images
    @images.setter
    def images(self, value):
        raise ReadOnlyError('<document.images> is a read-only property.')

    @property
    def implementation(self):
        return self._implementation
    @implementation.setter
    def implementation(self, value):
        raise ReadOnlyError('<document.implementation> is a read-only property.')

    @property
    def lastStyleSheetSet(self):
        return self._lastStyleSheetSet
    @lastStyleSheetSet.setter
    def lastStyleSheetSet(self, value):
        raise ReadOnlyError('<document.lastStyleSheetSet> is a read-only property.')

    @property
    def links(self):
        return self._links
    @links.setter
    def links(self, value):
        raise ReadOnlyError('<document.links> is a read-only property.')

    @property
    def plugins(self):
        return self._plugins
    @plugins.setter
    def plugins(self, value):
        raise ReadOnlyError('<document.plugins> is a read-only property.')

    @property
    def featurePolicy(self):
        return self._featurePolicy
    @featurePolicy.setter
    def featurePolicy(self, value):
        raise ReadOnlyError('<document.featurePolicy> is a read-only property.')

    @property
    def preferredStyleSheet(self):
        return self._preferredStyleSheet
    @preferredStyleSheet.setter
    def preferredStyleSheet(self, value):
        raise ReadOnlyError('<document.preferredStyleSheet> is a read-only property.')

    @property
    def scripts(self):
        return self._scripts
    @scripts.setter
    def scripts(self, value):
        raise ReadOnlyError('<document.scripts> is a read-only property.')

    @property
    def scrollingElement(self):
        return self._scrollingElement
    @scrollingElement.setter
    def scrollingElement(self, value):
        raise ReadOnlyError('<document.scrollingElement> is a read-only property.')

    @property
    def selectedStyleSheetSet(self):
        return self._selectedStyleSheetSet
    @selectedStyleSheetSet.setter
    def selectedStyleSheetSet(self, value):
        raise ReadOnlyError('<document.selectedStyleSheetSet> is a read-only property.')

    @property
    def styleSheetSets(self):
        return self._styleSheetSets
    @styleSheetSets.setter
    def styleSheetSets(self, value):
        raise ReadOnlyError('<document.styleSheetSets> is a read-only property.')

    @property
    def timeline(self):
        return self._timeline
    @timeline.setter
    def timeline(self, value):
        raise ReadOnlyError('<document.timeline> is a read-only property.')

    @property
    def undoManager(self):
        return self._undoManager
    @undoManager.setter
    def undoManager(self, value):
        raise ReadOnlyError('<document.undoManager> is a read-only property.')

    @property
    def visibilityState(self):
        return self._visibilityState
    @visibilityState.setter
    def visibilityState(self, value):
        raise ReadOnlyError('<document.visibilityState> is a read-only property.')

    @property
    def childElementCount (self):
        return self._childElementCount 
    @childElementCount .setter
    def childElementCount (self, value):
        raise ReadOnlyError('<document.childElementCount > is a read-only property.')

    @property
    def children(self):
        return self._children
    @children.setter
    def children(self, value):
        raise ReadOnlyError('<document.children> is a read-only property.')

    @property
    def firstElementChild(self):
        return self._firstElementChild
    @firstElementChild.setter
    def firstElementChild(self, value):
        raise ReadOnlyError('<document.firstElementChild> is a read-only property.')

    @property
    def lastElementChild(self):
        return self._lastElementChild
    @lastElementChild.setter
    def lastElementChild(self, value):
        raise ReadOnlyError('<document.lastElementChild> is a read-only property.')

    @property
    def defaultView(self):
        return self._defaultView
    @defaultView.setter
    def defaultView(self, value):
        raise ReadOnlyError('<document.defaultView> is a read-only property.')

    @property
    def dir(self):
        return self._dir
    @dir.setter
    def dir(self, value):
        raise ReadOnlyError('<document.dir> is a read-only property.')

    @property
    def lastModified(self):
        return self._lastModified
    @lastModified.setter
    def lastModified(self, value):
        raise ReadOnlyError('<document.lastModified> is a read-only property.')

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        raise ReadOnlyError('<document.location> is a read-only property.')

    @property
    def readyState(self):
        return self._readyState
    @readyState.setter
    def readyState(self, value):
        raise ReadOnlyError('<document.readyState> is a read-only property.')

    @property
    def referrer(self):
        return self._referrer
    @referrer.setter
    def referrer(self, value):
        raise ReadOnlyError('<document.referrer> is a read-only property.')

    @property
    def URL(self):
        return self._URL
    @URL.setter
    def URL(self, value):
        raise ReadOnlyError('<document.URL> is a read-only property.')

    @property
    def activeElement(self):
        return self._activeElement
    @activeElement.setter
    def activeElement(self, value):
        raise ReadOnlyError('<document.activeElement> is a read-only property.')

    @property
    def fullscreenElement(self):
        return self._fullscreenElement
    @fullscreenElement.setter
    def fullscreenElement(self, value):
        raise ReadOnlyError('<document.fullscreenElement> is a read-only property.')

    @property
    def pointerLockElement(self):
        return self._pointerLockElement
    @pointerLockElement.setter
    def pointerLockElement(self, value):
        raise ReadOnlyError('<document.pointerLockElement> is a read-only property.')

    @property
    def styleSheets(self):
        return self._styleSheets
    @styleSheets.setter
    def styleSheets(self, value):
        raise ReadOnlyError('<document.styleSheets> is a read-only property.')



##### NOT READ-ONLY
    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value
        evaluate(f'document.body = "{value}"', return_value=False)

    @property
    def fonts(self):
        return self._fonts
    @fonts.setter
    def fonts(self, value):
        self._fonts = value
        evaluate(f'document.fonts = "{value}"', return_value=False)

    @property
    def selectedStyleSheetSet(self):
        return self._selectedStyleSheetSet
    @selectedStyleSheetSet.setter
    def selectedStyleSheetSet(self, value):
        self._selectedStyleSeetSet = value
        evaluate(f'document.selectedStyleSheetSet = "{value}"', return_value=False)

    @property
    def cookie(self):
        return self._cookie
    @cookie.setter
    def cookie(self, value):
        self._cookie = value
        evaluate(f'document.cookie = "{value}"', return_value=False)

    @property
    def designMode(self):
        return self._designMode
    @designMode.setter
    def designMode(self, value):
        self._designMode = value
        evaluate(f'document.designMode = "{value}"', return_value=False)

    @property
    def domain(self):
        return self._domain
    @domain.setter
    def domain(self, value):
        self._domain = value
        evaluate(f'document.domain = "{value}"', return_value=False)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value
        evaluate(f'document.title = "{value}"', return_value=False)