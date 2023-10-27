'''Скрыть окно консоли'''
from pyvirtualdisplay import Display
import win32gui, win32con

def hide_all_windows():
    display = Display(visible=0, size=(800, 600))
    display.start()

    # pip install pywin32
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
