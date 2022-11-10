from getScreen import getScreenshot
from PIL import Image

# pip install pyautogui
import pyautogui
import time
# pip install keyboard
import keyboard

# pip install pytesseract
from OCR import image2doc

# pip install deepl
import deepl

# for summarize
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

DEEPL_KEY = "your Deepl API key"

def main():
    while True:
        """
        get leftTop coordinates
        """
        print("\033[32m\033[1m topLeft\033[0m : \033[32mposition cursor and press [SPACE].\033[0m",end=" ")
        point = ""
        while True:
            # interrupt processing
            if keyboard.is_pressed("space"):
                break
            print("\b"*len(point),end="")
            print(" "*len(point),end="")
            print("\b"*len(point),end="",flush=True)
            point = str(pyautogui.position())
            print(point, end="", flush=True)
            time.sleep(0.01)
        print("\n[SPACE] was pressed >> ", end="")
        topLeft = pyautogui.position()
        print(f"topLeft = {topLeft}")
        time.sleep(1)
        """
        get bottomRight coordinates
        """
        print("\033[32m\033[1m bottomRight\033[0m : \033[32mposition cursor and press [SPACE].\033[0m",end=" ")
        point = ""
        while True:
            # interrupt processing
            if keyboard.is_pressed("space"):
                break
            print("\b"*len(point),end="")
            print(" "*len(point),end="")
            print("\b"*len(point),end="",flush=True)
            point = str(pyautogui.position())
            print(point, end="", flush=True)
            time.sleep(0.01)
        print("\n[SPACE] was pressed >> ", end="")
        bottomRight = pyautogui.position()
        print(f"bottomRight = {bottomRight}")

        XYXY = (topLeft.x*2, topLeft.y*2, bottomRight.x*2, bottomRight.y*2)
        # print(f"{XYXY =}")
        # print("main >> All setups completed.")


        img:Image = getScreenshot(XYXY)
        doc:str   = image2doc(img)
        assert type(doc) == str, "Type Error: image2doc() returned non-string type."
        doc = doc.replace(" "*2, " ")
        docs = doc.split("\n\n")
        docs = list(map(lambda x: x.replace("\n"," "), docs))
        doc  = "\n\n".join(docs)
        # print(f"\n\033[33m{doc}\033[0m\n")
        result = translator.translate_text(doc, source_lang="EN", target_lang="JA").text
        print(f"\n* * * * * * * * * * * * * * * * * * * *\n\033[33m{result}\033[0m\n* * * * * * * * * * * * * * * * * * * *\n")

        # summarize the english document (i.e., doc) to 2 sentences.
        auto_abstractor = AutoAbstractor()
        auto_abstractor.tokenizable_doc = MeCabTokenizer()
        auto_abstractor.delimiter_list = [".", "\n"]
        # Object of abstracting and filtering document.
        abstractable_doc = TopNRankAbstractor()
        # Summarize document.
        result_dict = auto_abstractor.summarize(doc, abstractable_doc)
        # Output result.
        summary = result_dict["summarize_result"][0]
        result = translator.translate_text(summary, source_lang="EN", target_lang="JA").text
        print(f"\033[2mSummary >> {result}\033[0m")


if __name__ == "__main__":
    try:
        translator = deepl.Translator(DEEPL_KEY) 
    except:
        raise("DeepL authorization failed. Please check the api_key.")
    main()
