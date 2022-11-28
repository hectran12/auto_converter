import os, Home, time
from helper import *
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

while True:
    clear()
    # Detect your ip to display content
    helper = Helper()
    langCode = helper.detect_language_code()
    if langCode == None:
        langCode = 'en'

    # Home
    home = Home.Home(languge=langCode)
    home.welcome()
    number = home.Menu()

    # func
    if number == 1:
        checkFunc = home.setting_menu_1()
        if checkFunc == False:
            print('....')
            time.sleep(2)  
        else:
            home.function1()
