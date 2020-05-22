from Settings import Settings
from Listener import Listener
from GUI import App
from kthread import KThread
from utils import watch_handle
import sys

settings = Settings()
listener = Listener(settings)
gui = App(settings, listener)

thread = KThread(target=lambda: watch_handle(gui.main_frame.DACTIVE))
thread.start()

gui.mainloop()
settings.save()
thread.terminate()
listener.thread.terminate()
sys.exit()
