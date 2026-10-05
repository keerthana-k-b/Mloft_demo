import cv2
import numpy as np
from PIL import Image

def resize_long_side(img, target_long=1200):
    h, w = img.shape[:2]
    if h >= w:
        new_h = target_long
        new_w = int(round(w * (target_long / h)))
    else:
        new_w = target_long
        new_h = int(round(h * (target_long / w)))
    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)

def save_dual_format(bgr_img, base_path_no_ext, jpg_quality=95, webp_quality=92):
    resized_bgr = resize_long_side(bgr_img, 1200)
    rgb_img = cv2.cvtColor(resized_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    pil_img.save(f"{base_path_no_ext}.jpg", 'JPEG', quality=jpg_quality, optimize=True)
    pil_img.save(f"{base_path_no_ext}.webp", 'WEBP', quality=webp_quality, method=6)
    print(f"Updated: {base_path_no_ext}")

# 1. Perfect engagement-02:
img1 = cv2.imread("assets/reference/new/Screenshot 2026-10-01 150237.png")
h1, w1 = img1.shape[:2]
mask1 = np.zeros((h1, w1), dtype=np.uint8)
# Cover entire upper-right watermark zone
mask1[30:155, 345:430] = 255
# Using cv2.INPAINT_NS with radius 5 produces a completely smooth bokeh gradient
clean1 = cv2.inpaint(img1, mask1, 5, cv2.INPAINT_NS)
save_dual_format(clean1, "assets/images/engagement-02")

# 2. Perfect roja-02:
img14 = cv2.imread("assets/reference/new/Screenshot 2026-10-04 173928.png")
h14, w14 = img14.shape[:2]
mask14 = np.zeros((h14, w14), dtype=np.uint8)
roi14_crop = img14[455:500, 150:215]
gray14_crop = cv2.cvtColor(roi14_crop, cv2.COLOR_BGR2GRAY)
# Catch all letter and shadow pixels with threshold > 125
white_letters = (gray14_crop > 125).astype(np.uint8) * 255
white_letters = cv2.dilate(white_letters, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=2)
mask14[455:500, 150:215] = white_letters
clean14 = cv2.inpaint(img14, mask14, 3, cv2.INPAINT_NS)
save_dual_format(clean14, "assets/images/roja-02")

print("Perfect patches done!")
