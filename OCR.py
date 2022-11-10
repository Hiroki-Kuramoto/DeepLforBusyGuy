import pyocr
import pyocr.builders
from PIL import Image

def main():
    img = Image.open("Image_path")
    doc = image2doc(img, "eng")

def image2doc(img:Image, OCR_LANG):
    """
     using OCR, extract documents from the image
    """
    tools = pyocr.get_available_tools()
    if len(tools) == 0: 
        raise Exception("image2doc >>\033[31m No OCR tool found\033[0m")
    tool = tools[0]
    langs = tool.get_available_languages()
    if OCR_LANG not in langs:
        raise Exception("image2doc >>\033[31m The OCR tool does not support English\033[0m")
    lang = OCR_LANG
    
    doc = tool.image_to_string(img,lang=lang,builder=pyocr.builders.TextBuilder())
    
    return doc

if __name__ == "__main__":
    main()
