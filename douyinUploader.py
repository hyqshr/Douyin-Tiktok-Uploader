import platform
import time
import webbrowser

import pyautogui

def open_chrome_with_url(url):
    system_name = platform.system()
    if system_name == 'Darwin':
        # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif system_name == 'Windows':
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    else:
        print("Unknown system. Unable to open chrome")
        return None

    webbrowser.get(chrome_path).open(url)
    print(f"Chrome opened with url: {url}")

DarkMode = False
class DouyinUploader:
    entrance_button = '发布作品.png'
    upload_button = '上传视频.png'
    file_search_bar = '搜索栏.png' if not DarkMode else '搜索栏-dark.png'
    video = '视频.png' if not DarkMode else '视频-dark.png'
    url = 'https://creator.douyin.com/creator-micro/home'
    publish = '发布.png'

    open_chrome_with_url(url)
    time.sleep(5)

    @classmethod
    def upload_video_douyin(cls):
        # 1. Click on the entrance button
        entrance_x, entrance_y = pyautogui.locateCenterOnScreen(cls.entrance_button, confidence=.5)
        pyautogui.moveTo(cls.entrance_button, duration=1)
        pyautogui.leftClick(entrance_x, entrance_y)
        pyautogui.leftClick(entrance_x, entrance_y)
        time.sleep(2)
        # 2. choose file to upload
        upload_button_x, upload_button_y = pyautogui.locateCenterOnScreen(cls.upload_button, confidence=.5)
        pyautogui.moveTo(cls.upload_button, duration=1)
        pyautogui.leftClick(upload_button_x, upload_button_y)
        pyautogui.leftClick(upload_button_x, upload_button_y)

        # 3. search in search bar 
        time.sleep(1)
        searchbar_x, searchbar_y = pyautogui.locateCenterOnScreen(cls.file_search_bar, confidence=.7)
        pyautogui.moveTo(cls.file_search_bar)
        pyautogui.leftClick(searchbar_x, searchbar_y)
        pyautogui.write("the_only_filename.mp4")

        # 4. find the video, have to be unique filename in you system
        time.sleep(1)
        video_x, video_y = pyautogui.locateCenterOnScreen(cls.video)
        pyautogui.moveTo(cls.video)
        pyautogui.leftClick(video_x, video_y)
        pyautogui.leftClick(video_x, video_y)
        pyautogui.press('enter')
        time.sleep(1)

        # larger the video, the longer it take to upload
        time.sleep(15)
        pyautogui.scroll(-100)

        publish_x, publish_y = pyautogui.locateCenterOnScreen(cls.publish)
        print(publish_x, publish_y)
        pyautogui.moveTo(cls.publish)
        time.sleep(1)
        pyautogui.leftClick(publish_x, publish_y)
        time.sleep(1)
        pyautogui.click(clicks=2, interval=0.1)


if __name__ == '__main__':
    DouyinUploader.upload_video_douyin()