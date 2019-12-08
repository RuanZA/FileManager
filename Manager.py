'''TODO
neeed to sort files by extension
add simalar extensions to same folder
organise file types in differant folders
'''

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import mimetypes
import os
import json
import time




class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            #if (mimetypes.guess_type(filename) == )
            new_dest = folder_dest + '/' + filename
            os.rename(src, new_dest)

folder_to_track = "C:\\Users\\PeeWeeZA\\Desktop\\one"
folder_dest = "C:\\Users\\PeeWeeZA\\Desktop\\two"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()