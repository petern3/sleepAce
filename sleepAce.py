import os, datetime, threading, time

switch_off = datetime.time(20, 0)
end_bound = datetime.time(22, 30)
early = datetime.time(20, 0)
now = datetime.datetime.now()

def shutdown():
    import ctypes  # An included library with Python install.
    a = ctypes.windll.user32.MessageBoxW(0, "Do you really need to be browsing still?", "Sleep pro", 0)
    if a == 1 and end_bound > now.time()  > switch_off:
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

print('hi')
time.sleep(1)

i = 0
while end_bound > now.time() > early and i < 200:
    time.sleep(60)
    if end_bound > now.time() > switch_off:
        t = threading.Thread(target=shutdown)
        t.start()
    i += 1
