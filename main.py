from Settings import Settings
from Listener import Listener
from GUI import GUI
import win32gui
from kthread import KThread
from utils import watch_handle
import sys

handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
print(handle)
settings = Settings()
listener = Listener(settings, handle)
gui = GUI(settings, listener)

handle_thread = KThread(target=lambda: watch_handle(listener, settings, gui.DACTIVE))
handle_thread.start()

gui.mainloop()
settings.save()
listener.thread.terminate()
handle_thread.terminate()
sys.exit()
