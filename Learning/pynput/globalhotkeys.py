from pynput.keyboard import HotKey,GlobalHotKeys,Listener
def on_activate():
    print('Global hotkey activated!') #What to do when hotkey is pressed
# def for_canonical(f): #Required for using HotKey + Listener
#     return lambda k: f(l.canonical(k))
hotkey = HotKey( #Creating a hotkey
    HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)


def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

# with Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)) as l:
#     l.join()


#Working with multiple global hotkeys

with GlobalHotKeys({ #Using a dictionary to pass
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as g: 
    g.join()
