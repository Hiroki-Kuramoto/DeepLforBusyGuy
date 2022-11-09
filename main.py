from getScreen import getScreenshot
from PIL import Image

import sys
# pip install pyautogui
import pyautogui
import time
# pip install keyboard
import keyboard

# pip install pytesseract
from OCR import image2doc

# pip install deepl
import deepl

DEEPL_KEY = "fa64391c-a63c-170c-0dd7-cf9bc6fec5e6:fx"

def main():
    """
    get leftTop coordinates
    """
    print("\033[32m\033[1m topLeft\033[0m : \033[32mposition cursor and press [Enter].\033[0m")
    point = ""
    while True:
        # interrupt processing
        if keyboard.is_pressed("enter"):
            break
        print("\b"*len(point),end="")
        print(" "*len(point),end="")
        print("\b"*len(point),end="",flush=True)
        point = str(pyautogui.position())
        print(point, end="", flush=True)
        time.sleep(0.01)
    print("Enter was pressed >> ", end="")
    topLeft = pyautogui.position()
    print(f"topLeft = {topLeft}")
    time.sleep(1)
    """
    get bottomRight coordinates
    """
    print("\033[32m\033[1m bottomRight\033[0m : \033[32mposition cursor and press [Enter].\033[0m")
    point = ""
    while True:
        # interrupt processing
        if keyboard.is_pressed("enter"):
            break
        print("\b"*len(point),end="")
        print(" "*len(point),end="")
        print("\b"*len(point),end="",flush=True)
        point = str(pyautogui.position())
        print(point, end="", flush=True)
        time.sleep(0.01)
    print("Enter was pressed >> ", end="")
    bottomRight = pyautogui.position()
    print(f"bottomRight = {bottomRight}")

    XYXY = (topLeft.x*2, topLeft.y*2, bottomRight.x*2, bottomRight.y*2)
    print(f"{XYXY =}")
    print("main >> All setups completed.")
    # stdinを1行だけクリアする
    sys.stdin.read(1)

    while True:
        input("\033[32m>> Press [Enter].\033[0m")
        img:Image = getScreenshot(XYXY)
        doc:str   = image2doc(img)
        assert type(doc) == str, "Type Error: image2doc() returned non-string type."
        doc = doc.replace(" "*2, " ")
        docs = doc.split("\n\n")
        docs = list(map(lambda x: x.replace("\n"," "), docs))
        doc  = "\n\n".join(docs)
        # print(f"\n\033[33m{doc}\033[0m\n")
        result = translator.translate_text(doc, source_lang="EN", target_lang="JA").text
        print(f"\033[3m{result}\033[0m")
        time.sleep(1)
        sys.stdin.flush()


if __name__ == "__main__":
    try:
        translator = deepl.Translator(DEEPL_KEY) 
    except:
        raise("DeepL authorization failed. Please check the api_key.")
    main()