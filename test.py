from jsConsole import *
from lifeeasy import sleep

#window.open('https://www.google.com/', '_self')
console.log('Opening page')
window.open('http://127.0.0.1:5500/', '_self')
console.log('Get loading screen by ID')
loadingscreenElement = document.getElementById('loadingscreen')
console.log('Create Element')
newelement = document.createElement('div')
console.log('ID')
newelement.id = 'heyheyid'
console.log('ClassList')
console.log(newelement._calling_method)
newelement.classList.add('heyheyheyclass')
console.log('appendChild')
loadingscreenElement.appendChild(newelement)

sleep(60)
window.close()