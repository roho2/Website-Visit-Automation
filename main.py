import webbrowser
import time
import keyboard


count = 0
urls = ['https://stackoverflow.com/users/13492699/boxman07']

while count < 10:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        keyboard.press_and_release('Control+W')
        count += 1
