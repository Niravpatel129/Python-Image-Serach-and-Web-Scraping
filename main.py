import cv2
import pyautogui
import pytesseract
import bs4 as bs
from urllib.request import urlopen, Request
import webbrowser
from helper import *


class Rainbow:
    def __init__(self):
        self.f = open('helloworld.html', 'w')
        self.f.write(html_header)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
        self.config = '-l eng --oem 1 --psm 3'
        self.img = "C:\\Users\\Nirav\\PycharmProjects\\RainbowScriptUpdate\\newdownload.png"  # change this url later

    def locate_sword(self):
        self.redsword = pyautogui.locateOnScreen('redsword.png', grayscale=True)
        self.bluesword = pyautogui.locateOnScreen('bluesword.png', grayscale=True)
        if self.redsword or self.bluesword:
            print("SWORD FOUND!")
            return True
        else:
            return False

    def take_screenshot(self):
        pyautogui.screenshot('newdownload.png', region=(466, 334, 470, 500))
        print("screenshot!")
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
        config = ('-l eng --oem 1 --psm 3')

        # Read image from disk

        self.im = cv2.imread(self.img, cv2.IMREAD_COLOR)
        self.im = cv2.resize(self.im, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Run tesseract OCR on image
        self.text = pytesseract.image_to_string(self.im, config=config)
        self.textArray = self.text.split()
        print(self.textArray)
        return self.textArray

    def load_names(self):
        for person in self.textArray:
            request = Request(
                'https://r6.tracker.network/profile/pc/' + person,
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'})
            try:
                html = urlopen(request).read().decode()
                rank = True
            except Exception:
                html = "<div class'trn-card__content trn-card--light pt8 pb8'><img title='not Ranked Yet..'></img></div>"
                rank = False

            soup = bs.BeautifulSoup(html, 'lxml')

            if self.textArray[5] is person:
                self.f.write("""</div>
                <div class="column"">""")

            print(person + " Rank: ")
            self.f.write('<p><b>')
            self.f.write(person + "\n")
            self.f.write('</b>')
            if not soup.find_all('div', class_='trn-card__content trn-card--light pt8 pb8'):
                print('Not ranked yet.')
                print()
                self.f.write('<img src="https://game-rainbow6.ubi.com/assets/images/season5-rank0-hd.a1bedded1a.svg"">')
            for table in soup.find_all('div', class_='trn-card__content trn-card--light pt8 pb8'):
                self.f.write("<img src='")

                for img in table.find_all('img'):
                    if rank:
                        print(img.get('title'))
                        self.f.write(img.get('src'))
                        self.f.write("'>")
                    else:
                        print('Not ranked yet.')
                        self.f.write(img.get('src'))
                        self.f.write("'>")
                    print()

                if table.find_all('img') == []:
                    self.f.write('https://game-rainbow6.ubi.com/assets/images/season5-rank0-hd.a1bedded1a.svg')
                    self.f.write("'>")
                    print('Not ranked yet.')
                    print()
                    # f.write('Not ranked yet.')
                    self.f.write('</p>')
            self.load_winrate(soup)
            print()
        self.f.write("""</div></div></html>""")

    def load_winrate(self, person):
        values = person.find(attrs={'data-stat': 'RankedWLRatio'})
        self.f.write('<p class="winrate">')
        if values is not None:
            values = values.string
            print(values)
            self.f.write(values)
        else:
            print('0 %')
            self.f.write('0%')
        self.f.write('</p>')


r = Rainbow()
while not r.locate_sword():
    r.locate_sword()

r.take_screenshot()
r.load_names()
webbrowser.open_new_tab(url)

