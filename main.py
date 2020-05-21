from Settings import Settings
from Listener import Listener
from Gui import App
import win32gui
from kthread import KThread
from utils import watch_handle
import sys

handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
print(handle)
settings = Settings()
listener = Listener(settings, handle)
gui = App(settings, listener)

handle_thread = KThread(
    target=lambda: watch_handle(listener, settings, gui.main_frame.DACTIVE)
)
handle_thread.start()

gui.mainloop()
settings.save()
listener.thread.terminate()
handle_thread.terminate()
sys.exit()
