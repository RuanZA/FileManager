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
            # if (mimetypes.guess_type(filename) == )
            if filename.endswith('.exe'):
                new_dest = folder_exe + '/' + filename
            elif filename.endswith('.jpg') or filename.endswith('.gif') or filename.endswith('.png'):
                new_dest = folder_img + '/' + filename
            elif filename.endswith('.zip'):
                new_dest = folder_zip + '/' + filename
            else:
                new_dest = folder_unkown + '/' + filename

            os.rename(src, new_dest)


folder_to_track = "E:\\Downloads"
folder_exe = "E:\\downloads organized\\exe"
folder_img = "E:\\downloads organized\\images"
folder_zip = "E:\\downloads organized\\zips"
folder_unkown = "E:\\downloads organized\\unkown"
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