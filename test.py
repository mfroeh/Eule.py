from Settings import Settings
from Listener import Listener
from GUI import GUI
import win32gui
from kthread import KThread
from utils import watch_handle
import sys
from time import sleep

handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
print(handle)

while True:
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    resolution = (x2 - x1, y2 - y1)
    print(resolution)
    sleep(1)
settings = Settings()
listener = Listener(settings, handle)
gui = GUI(settings, listener)

handle_thread = KThread(target=lambda: watch_handle(listener, settings, gui.BV_DACTIVE))
handle_thread.start()

gui.mainloop()
settings.save()
listener.thread.terminate()
handle_thread.terminate()
sys.exit()


#### Cube Conv sm not fast
#
# send_mouse(handle, 'RM', 1425 + j * 50, 580 + i * 50)  # Item
# macro_sleep(0.1)
# send_mouse(handle, 'LM', 710, 840)  # Fill
# send_mouse(handle, 'LM', 250, 830)  # Transmute
# macro_sleep(0.1)
# send_mouse(handle, 'LM', 580, 850)  # Backwards
# send_mouse(handle, 'LM', 850, 850)  # Forwards
