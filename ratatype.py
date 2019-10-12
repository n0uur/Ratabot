""" ratatype bot """
from time import sleep, time
import re

import selenium.webdriver as webdriver
import lxml.html as lh
import lxml.html.clean as clean

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def main():
    """ main function """
    browser = webdriver.Chrome()
    browser.get("https://www.ratatype.com/typing-test/test/")

    print("Loading page...")

    button = browser.find_element_by_xpath("//button[@class='submit gr']")
    button.click()

    sleep(1)
    print("Page loaded!")
    sleep(1)

    textarea = browser.find_element_by_xpath("//textarea[@spellcheck='false']")

    a_element = browser.page_source
    l_element = a_element.split('\n')
    maintext = [i for i in l_element if 'mainTxt' in i][0].strip(' ').split("</span>")

    print("Getting article...")
    sleep(1)

    words_data = []
    for i in range(len(maintext)):
        if maintext[i].find("</div>") != -1:
            continue
        if maintext[i].find("wgreen") != -1:
            words_data.append(maintext[i].replace('<div class="mainTxt"><span class="wgreen">', ""))
        else:
            words_data.append(maintext[i].replace('<span class="wblack">', ""))
    typing = ""
    for i in range(len(words_data)):
        typing += str(words_data[i])
    print(typing)
    time_sec_count = 5
    print("START IN:")
    while time_sec_count != 0:
        print(time_sec_count)
        time_sec_count -= 1
        sleep(1)
    for i in range(8):
        textarea.send_keys("a")
        sleep(0.2)
        textarea.send_keys("\b")
        sleep(0.2)
    for character in typing:
        textarea.send_keys(character)
        sleep(0.26)
    print("Finished! Login to your Facebook")
    print("Made by n0uur [Krittanut Siripornnoppakhun, KMITL]")
    input("\nPress enter to end this program..")
main()
