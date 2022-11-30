#pip install pyautogui
import pyautogui
import time
from PIL import Image
#pip install imagehash
import imagehash
hash = imagehash.average_hash(Image.open('data/test/imagehash.png'))
print(hash)
#ffd7918181c9ffff
otherhash = imagehash.average_hash(Image.open('data/test/peppers.png'))
print(otherhash)
#9f172786e71f1e00
print(hash == otherhash)
#False
print(hash - otherhash)  # hamming distance
#33
