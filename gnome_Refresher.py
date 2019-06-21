# Version 0.2 by Ashley Watson
# Used to automate restarting the GNOME desktop
#
# Changelog
# V0.1 - Initial release
# V0.2 - Graphical prompt to confirm user action

import sys
import time
import easygui
from pykeyboard import PyKeyboard

k = PyKeyboard()

msg = "This will refresh the GNOME Desktop. Click OK to continue or Cancel to close without refreshing"
title = "GNOME Refresher"
if easygui.ccbox(msg, title):   # shows a Continue / Cancel box
    pass    # user chose Continue
else:   # user chose Cancel
    sys.exit(0)

k.press_keys([k.alt_key, k.function_keys[2]])
time.sleep(1)
k.tap_key('r')
k.tap_key(k.enter_key)
time.sleep(5)
easygui.msgbox("GNOME has been refreshed. Click below to close.", title="GNOME Refresher", ok_button="Close")
