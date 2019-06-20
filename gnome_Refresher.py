# Version 0.1 by Ashley W.
# Used to automate restarting the GNOME desktop

import sys
import time
import easygui
from pykeyboard import PyKeyboard

k = PyKeyboard()

easygui.msgbox("This will refresh the GNOME Desktop. Click OK to continue..", title="GNOME Refresher", ok_button="OK")
k.press_keys([k.alt_key, k.function_keys[2]])
time.sleep(1)
k.tap_key('r')
k.tap_key(k.enter_key)
time.sleep(5)
easygui.msgbox("GNOME has been refreshed. Click below to close.", title="GNOME Refresher", ok_button="Close")
