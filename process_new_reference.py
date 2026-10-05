import os
import cv2
import json
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
    
    jpg_path = f"{base_path_no_ext}.jpg"
    webp_path = f"{base_path_no_ext}.webp"
    
    pil_img.save(jpg_path, 'JPEG', quality=jpg_quality, optimize=True)
    pil_img.save(webp_path, 'WEBP', quality=webp_quality, method=6)
    print(f"Saved: {os.path.basename(jpg_path)} & {os.path.basename(webp_path)} ({resized_bgr.shape[1]}x{resized_bgr.shape[0]})")
    return jpg_path, webp_path, resized_bgr.shape[1], resized_bgr.shape[0]

def inpaint_region(img, mask, radius=3, method=cv2.INPAINT_TELEA):
    return cv2.inpaint(img, mask, radius, method)

results = []

# =========================================================================
# 1. Screenshot 2026-10-01 150237.png -> engagement-02
# =========================================================================
src_1 = "assets/reference/new/Screenshot 2026-10-01 150237.png"
img_1 = cv2.imread(src_1)
h1, w1 = img_1.shape[:2]
mask_1 = np.zeros((h1, w1), dtype=np.uint8)

# Lion logo + "M. LOFT" + "BY JOEL JACOB MATHEW" in top-right bokeh green foliage
roi_1 = img_1[30:155, 345:430]
gray_1 = cv2.cvtColor(roi_1, cv2.COLOR_BGR2GRAY)
bright_1 = (gray_1 > 160).astype(np.uint8) * 255
dilated_1 = cv2.dilate(bright_1, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
mask_1[30:155, 345:430] = dilated_1
clean_1 = inpaint_region(img_1, mask_1, radius=4, method=cv2.INPAINT_TELEA)

jpg1, webp1, rw1, rh1 = save_dual_format(clean_1, "assets/images/engagement-02")
results.append({
    "target": "engagement-02",
    "source": src_1,
    "category": "Engagement & Reception",
    "title": "Aurelia Floral Organza Lehenga",
    "resolution": f"{rw1}x{rh1}",
    "cleaning": "Inpainted M. LOFT lion emblem and branding text from upper-right foliage; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 2. Screenshot 2026-10-04 173353.png -> engagement-03
# =========================================================================
src_2 = "assets/reference/new/Screenshot 2026-10-04 173353.png"
img_2 = cv2.imread(src_2)
clean_2 = img_2[1:-1, 1:-1].copy()
jpg2, webp2, rw2, rh2 = save_dual_format(clean_2, "assets/images/engagement-03")
results.append({
    "target": "engagement-03",
    "source": src_2,
    "category": "Engagement & Sangeet",
    "title": "Samira Fuchsia Zari Bridal Lehenga",
    "resolution": f"{rw2}x{rh2}",
    "cleaning": "Trimmed 1px border; pristine photograph with zero watermarks; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 3. Screenshot 2026-10-04 173439.png -> handwork-03
# =========================================================================
src_3 = "assets/reference/new/Screenshot 2026-10-04 173439.png"
img_3 = cv2.imread(src_3)
h3, w3 = img_3.shape[:2]
mask_3 = np.zeros((h3, w3), dtype=np.uint8)

# M LOFT text on plain silk fabric: y: 185..230, x: 165..275
roi_text_3 = img_3[185:230, 165:275]
gray_text_3 = cv2.cvtColor(roi_text_3, cv2.COLOR_BGR2GRAY)
dark_text_3 = (gray_text_3 < 165).astype(np.uint8) * 255
dil_text_3 = cv2.dilate(dark_text_3, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=2)
mask_3[185:230, 165:275] = dil_text_3

# Bottom-left Instagram tag icon
roi_tag = img_3[h3-50:h3, 0:60]
tag_gray = cv2.cvtColor(roi_tag, cv2.COLOR_BGR2GRAY)
tag_mask = (tag_gray > 180).astype(np.uint8) * 255
tag_mask = cv2.dilate(tag_mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=3)
mask_3[h3-50:h3, 0:60] = tag_mask

clean_3 = inpaint_region(img_3, mask_3, radius=3, method=cv2.INPAINT_TELEA)
jpg3, webp3, rw3, rh3 = save_dual_format(clean_3, "assets/images/handwork-03")
results.append({
    "target": "handwork-03",
    "source": src_3,
    "category": "Handwork Details",
    "title": "Atelier Zardozi Handloom Artistry",
    "resolution": f"{rw3}x{rh3}",
    "cleaning": "Inpainted 'M LOFT' gold text from silk canvas; removed bottom-left Instagram tag icon; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 4. Screenshot 2026-10-04 173501.png -> pavithrappattu-02
# =========================================================================
src_4 = "assets/reference/new/Screenshot 2026-10-04 173501.png"
img_4 = cv2.imread(src_4)
h4, w4 = img_4.shape[:2]
mask_4 = np.zeros((h4, w4), dtype=np.uint8)
# Bottom pagination dots: y: h4-30..h4-5, x: w4//2-40..w4//2+40
mask_4[h4-30:h4-5, w4//2-45:w4//2+45] = 255
clean_4 = inpaint_region(img_4, mask_4, radius=4, method=cv2.INPAINT_TELEA)

jpg4, webp4, rw4, rh4 = save_dual_format(clean_4, "assets/images/pavithrappattu-02")
results.append({
    "target": "pavithrappattu-02",
    "source": src_4,
    "category": "Pavithrappattu",
    "title": "Vrinda Emerald & Maroon Heritage Silk",
    "resolution": f"{rw4}x{rh4}",
    "cleaning": "Inpainted bottom Instagram carousel pagination dots on solid studio backdrop; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 5. Screenshot 2026-10-04 173550.png -> christian-bride-03
# =========================================================================
src_5 = "assets/reference/new/Screenshot 2026-10-04 173550.png"
img_5 = cv2.imread(src_5)
# Crop top 25px dark foliage to remove external photographer watermark
clean_5 = img_5[25:, :].copy()
jpg5, webp5, rw5, rh5 = save_dual_format(clean_5, "assets/images/christian-bride-03")
results.append({
    "target": "christian-bride-03",
    "source": src_5,
    "category": "Christian Bride",
    "title": "Celeste Pearl-Work Bridal Saree",
    "resolution": f"{rw5}x{rh5}",
    "cleaning": "Cropped top 25px dark foliage to exclude photographer watermark; preserved full bride portrait; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 6. Screenshot 2026-10-04 173612.png -> engagement-04
# =========================================================================
src_6 = "assets/reference/new/Screenshot 2026-10-04 173612.png"
img_6 = cv2.imread(src_6)
clean_6 = img_6[1:-1, 1:-1].copy()
jpg6, webp6, rw6, rh6 = save_dual_format(clean_6, "assets/images/engagement-04")
results.append({
    "target": "engagement-04",
    "source": src_6,
    "category": "Engagement & Reception",
    "title": "Althea Emerald Velvet Embroidered Lehenga",
    "resolution": f"{rw6}x{rh6}",
    "cleaning": "Trimmed 1px border; pristine studio portrait; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 7. Screenshot 2026-10-04 173706.png -> hindu-bride-02
# =========================================================================
src_7 = "assets/reference/new/Screenshot 2026-10-04 173706.png"
img_7 = cv2.imread(src_7)
clean_7 = img_7[1:-1, 1:-1].copy()
jpg7, webp7, rw7, rh7 = save_dual_format(clean_7, "assets/images/hindu-bride-02")
results.append({
    "target": "hindu-bride-02",
    "source": src_7,
    "category": "Hindu Bride",
    "title": "Ananya Saffron Bridal Veil Editorial",
    "resolution": f"{rw7}x{rh7}",
    "cleaning": "Trimmed 1px boundary; clean editorial photography; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 8. Screenshot 2026-10-04 173718.png -> hindu-bride-03
# =========================================================================
src_8 = "assets/reference/new/Screenshot 2026-10-04 173718.png"
img_8 = cv2.imread(src_8)
clean_8 = img_8[1:-1, 1:-1].copy()
jpg8, webp8, rw8, rh8 = save_dual_format(clean_8, "assets/images/hindu-bride-03")
results.append({
    "target": "hindu-bride-03",
    "source": src_8,
    "category": "Hindu Bride",
    "title": "Mayura Tangerine Kanchipuram Silk",
    "resolution": f"{rw8}x{rh8}",
    "cleaning": "Trimmed 1px boundary; pristine photo content; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 9. Screenshot 2026-10-04 173728.png -> hindu-bride-04
# =========================================================================
src_9 = "assets/reference/new/Screenshot 2026-10-04 173728.png"
img_9 = cv2.imread(src_9)
clean_9 = img_9[1:-1, 1:-1].copy()
jpg9, webp9, rw9, rh9 = save_dual_format(clean_9, "assets/images/hindu-bride-04")
results.append({
    "target": "hindu-bride-04",
    "source": src_9,
    "category": "Hindu Bride",
    "title": "Kalyani Temple Gold Silk Ensemble",
    "resolution": f"{rw9}x{rh9}",
    "cleaning": "Trimmed 1px boundary; pristine ceremonial portrait; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 10. Screenshot 2026-10-04 173807.png -> engagement-05
# =========================================================================
src_10 = "assets/reference/new/Screenshot 2026-10-04 173807.png"
img_10 = cv2.imread(src_10)
# Crop top 25px to exclude photographer text without affecting mirror or bride
clean_10 = img_10[25:, :].copy()
jpg10, webp10, rw10, rh10 = save_dual_format(clean_10, "assets/images/engagement-05")
results.append({
    "target": "engagement-05",
    "source": src_10,
    "category": "Engagement & Reception",
    "title": "Ivory Silk Mirror Heirloom Lehenga",
    "resolution": f"{rw10}x{rh10}",
    "cleaning": "Cropped top 25px to exclude photographer text watermark; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 11. Screenshot 2026-10-04 173828.png -> white-gown-02
# =========================================================================
src_11 = "assets/reference/new/Screenshot 2026-10-04 173828.png"
img_11 = cv2.imread(src_11)
h11, w11 = img_11.shape[:2]
mask_11 = np.zeros((h11, w11), dtype=np.uint8)
# Tag icon in bottom-left corner
mask_11[h11-40:h11, 5:45] = 255
clean_11 = inpaint_region(img_11, mask_11, radius=4, method=cv2.INPAINT_TELEA)

jpg11, webp11, rw11, rh11 = save_dual_format(clean_11, "assets/images/white-gown-02")
results.append({
    "target": "white-gown-02",
    "source": src_11,
    "category": "White Gowns & Western Bridal",
    "title": "Giselle Beaded Cathedral Cape Gown",
    "resolution": f"{rw11}x{rh11}",
    "cleaning": "Inpainted bottom-left Instagram user-tag badge from cobblestones; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 12. Screenshot 2026-10-04 173852.png -> christian-bride-04
# =========================================================================
src_12 = "assets/reference/new/Screenshot 2026-10-04 173852.png"
img_12 = cv2.imread(src_12)
clean_12 = img_12[1:-1, 1:-1].copy()
jpg12, webp12, rw12, rh12 = save_dual_format(clean_12, "assets/images/christian-bride-04")
results.append({
    "target": "christian-bride-04",
    "source": src_12,
    "category": "Christian Bride",
    "title": "Evangeline Antique Gold Tissue Zari Saree",
    "resolution": f"{rw12}x{rh12}",
    "cleaning": "Trimmed 1px edge boundary; pristine church architectural portrait; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 13. Screenshot 2026-10-04 173908.png -> white-gown-03
# =========================================================================
src_13 = "assets/reference/new/Screenshot 2026-10-04 173908.png"
img_13 = cv2.imread(src_13)
h13, w13 = img_13.shape[:2]
mask_13 = np.zeros((h13, w13), dtype=np.uint8)
# Pagination dots in bottom center
mask_13[h13-30:h13-5, w13//2-45:w13//2+45] = 255
clean_13 = inpaint_region(img_13, mask_13, radius=4, method=cv2.INPAINT_TELEA)

jpg13, webp13, rw13, rh13 = save_dual_format(clean_13, "assets/images/white-gown-03")
results.append({
    "target": "white-gown-03",
    "source": src_13,
    "category": "White Gowns & Western Bridal",
    "title": "Rosalind Pearl Tassel Champagne Gown",
    "resolution": f"{rw13}x{rh13}",
    "cleaning": "Inpainted bottom Instagram carousel pagination dots on gravel ground; resized to 1200px long side",
    "status": "Approved"
})

# =========================================================================
# 14. Screenshot 2026-10-04 173928.png -> roja-02
# =========================================================================
src_14 = "assets/reference/new/Screenshot 2026-10-04 173928.png"
img_14 = cv2.imread(src_14)
h14, w14 = img_14.shape[:2]
mask_14 = np.zeros((h14, w14), dtype=np.uint8)

# M LOFT watermark across pleats: y: 455..500, x: 150..215
roi14_crop = img_14[455:500, 150:215]
gray14_crop = cv2.cvtColor(roi14_crop, cv2.COLOR_BGR2GRAY)
white_letters = (gray14_crop > 170).astype(np.uint8) * 255
white_letters = cv2.dilate(white_letters, cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)), iterations=2)
mask_14[455:500, 150:215] = white_letters

clean_14 = inpaint_region(img_14, mask_14, radius=2, method=cv2.INPAINT_NS)
jpg14, webp14, rw14, rh14 = save_dual_format(clean_14, "assets/images/roja-02")
results.append({
    "target": "roja-02",
    "source": src_14,
    "category": "Roja & Festive Silk",
    "title": "Charulata Chartreuse & Plum Zari Saree",
    "resolution": f"{rw14}x{rh14}",
    "cleaning": "Inpainted white 'M LOFT' watermark text from lower green silk pleats; resized to 1200px long side",
    "status": "Approved"
})

# Save new batch manifest
with open("crop_sources_new_batch.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

# Clean up temporary test files
for tmp in ["roi3_mloft.png", "roi14_mloft.png", "roi1_lion.png", "test_clean3.png", "test_clean14.png", "test_clean1.png", "test_roi.py", "test_inpaint_precise.py", "test_inpaint_lion.py", "inspect_coords.py"]:
    if os.path.exists(tmp):
        try:
            os.remove(tmp)
        except:
            pass

print(f"\nAll {len(results)} clean images processed and saved to assets/images with 1200px long side!")
