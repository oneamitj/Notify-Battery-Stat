#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
from threading import Thread
import gobject
import os

gobject.threads_init()


class Battery:
    #global label
    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()
        global check
        self.check = 1

    def status(self):
        global label
        global check
        self.check = 0
        while(1):
            per = os.popen('upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E "state|time\ to\ | percentage| capacity"').read()
            '''parse = ["state:","time to full:","percentage:"," "]
            for i in parse:
            	per = per.replace(i,"")
            '''
            self.label.set_text(per)
            if self.check==1:
                return

    def __init__(self):
        global label
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_keep_above(True)
        self.window.set_title("Battery Indicator")
        self.window.set_default_size(20,50)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        self.label = gtk.Label()

        self.window.add(self.label)

        self.label.show()

        t=Thread(target=self.status,args=())
        t.start()

        self.window.show()

    def main(self):
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    battery = Battery()
    battery.main()


'''#gnome-session-quit
#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import os
from threading import Thread
import gobject
gobject.threads_init()

def destroy(self):
    gtk.main_quit()
    global check
    check = 1


def status():
    global per, check
    check=0
    while(1):
        per = os.popen('upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E "state|to\ full|percentage| time\ to\ empty"').read()
        label.set_text(per)
        if check==1:
            return

def main():
    t=Thread(target=start,args=())
    t.start()

def start():
    global per
    global label
    per= "1"
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_keep_above(True)
    window.set_title("Battery Indicator")
    window.set_default_size(20,50)

    #window.connect("delete_event", delete_event)

    window.connect("destroy", destroy)

    window.set_border_width(10)

    #label = gtk.Button(per)
    #label.connect("clicked", callback)

    label = gtk.Label()

    window.add(label)

    label.show()

    #button.show()

    window.show()

    t=Thread(target=status,args=())
    t.start()
    gtk.main()

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_keep_above(True)
    window.set_default_size(200,250)
    #button=gtk.Button("Button")

    per=os.system('bash stat.sh')
    label = gtk.Label(per)
    #window.add(button)
    window.add(label)
    label.show()
    #button.show()
    window.show()
    gtk.main()
    

if __name__ == "__main__": main()
'''