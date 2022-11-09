import os
from PIL import ImageGrab
from PIL import Image
import datetime


def logger(img:Image):
    LOGGING_DIR = "./logs"
    if not(os.path.exists(LOGGING_DIR)):
        os.mkdir(LOGGING_DIR)
    dt_now = datetime.datetime.now()
    dt_now = str(dt_now).replace(":", "-")
    dt_now = str(dt_now).replace(".", "-")
    img.save(f"{LOGGING_DIR}/{dt_now}.png")

def getScreenshot(boundingBox)-> Image:
    screen = ImageGrab.grab()
    # trim the image
    img = screen.crop(boundingBox)

    logger(img)
    return img
