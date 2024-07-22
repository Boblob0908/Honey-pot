import pyinotify
from telethon import TelegramClient
from telethon import sync, events
import requests

# You can find API ID and API Hash info from 'https://my.telegram.org/auyh'

api_id = "Your telegram API ID"

api_hash = 'Your telegram API Hash'

client = TelegramClient('Bot' , api_id,api_hash)

client.start()

digs = client.get_dialogs()

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        client.send_message('Someone got access to the file!!')
    def process_IN_ATTRIB(self,event):
        client.send_message('Someone changed the file!!')
    def process_IN_CLOSE_WRITE(self , event):
        client.send_message('Someone changed the file!!')
    def process_IN_CLOSE_NOWRITE(self , event):
        client.send_message('Someone just red no changed the file!!')
    def process_IN_CREATE(self , event):
        client.send_message('Someone did a copy of the file!!')
    def process_IN_DELETE(self , event):
        client.send_message('Someone deleted the file!!')
    def process_IN_MODIFY(self , event):
        client.send_message('Someone modifyied the file!!')
    def process_IN_OPEN(self , event):
        client.send_message('Someone open the file!!')

def main():
    wm = pyinotify.WatchManager()
    wm.add_watch('path way to honeyPot', pyinotify.All_EVENTS, rec=True)
    eh=MyEventHandler()
    notifier=pyinotify.Notifier(wm,eh)
    notifier.loop()

if __name___== '__main__':
    main()