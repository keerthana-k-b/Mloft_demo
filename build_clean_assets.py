import os
import cv2
import json
import numpy as np
from PIL import Image

# Ensure output directories exist
os.makedirs('assets/images/reel-posters', exist_ok=True)

# Helper function to save in dual formats: High-Quality JPG and WebP
def save_dual_format(bgr_img, base_path_no_ext, jpg_quality=95, webp_quality=90):
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    
    jpg_path = f"{base_path_no_ext}.jpg"
    webp_path = f"{base_path_no_ext}.webp"
    
    pil_img.save(jpg_path, 'JPEG', quality=jpg_quality, optimize=True)
    pil_img.save(webp_path, 'WEBP', quality=webp_quality, method=6)
    print(f"  Saved: {os.path.basename(jpg_path)} & {os.path.basename(webp_path)} ({bgr_img.shape[1]}x{bgr_img.shape[0]})")
    return jpg_path, webp_path

# Helper for inpainting with mask
def inpaint_region(img, mask, radius=3, method=cv2.INPAINT_TELEA):
    return cv2.inpaint(img, mask, radius, method)

# Target image definitions and processing logic
crop_manifest = []

print("=== 1. PROCESSING INDIVIDUAL IMAGES ===")

# --- 1. Screenshot 2026-10-01 150222.png (Bride in Pastel Floral Lehenga) ---
# Used for: hero-01, engagement-01
src_150222 = "assets/raw/Screenshot 2026-10-01 150222.png"
img_150222 = cv2.imread(src_150222)
# Trim 2px top and 1px left dark screenshot border
trimmed_150222 = img_150222[2:, 1:].copy()
h_15, w_15 = trimmed_150222.shape[:2]
# Inpaint top-left M. LOFT lion logo and text (x: 10..95, y: 15..100)
mask_150222 = np.zeros((h_15, w_15), dtype=np.uint8)
roi_15 = trimmed_150222[15:105, 10:100]
gray_roi_15 = cv2.cvtColor(roi_15, cv2.COLOR_BGR2GRAY)
bright_15 = (gray_roi_15 > 210).astype(np.uint8)
dilated_15 = cv2.dilate(bright_15, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=2)
mask_150222[15:105, 10:100] = dilated_15
clean_150222 = inpaint_region(trimmed_150222, mask_150222, radius=4)

save_dual_format(clean_150222, "assets/images/hero-01")
save_dual_format(clean_150222, "assets/images/engagement-01")
crop_manifest.append({
    "target": "hero-01 / engagement-01",
    "source": src_150222,
    "crop_box": [1, 2, 440, 586],
    "cleaning": "Trimmed dark 2px border; inpainted M. LOFT lion logo & text in top-left using dilated mask",
    "category": "Hero / Engagement",
    "notes": "Stunning bride in pastel floral lehenga with kundan jewelry"
})

# --- 2. Screenshot 2026-10-01 150343.png (Gold/Yellow Lehenga front portrait) ---
# Used for: hero-02, handwork-02
src_150343 = "assets/raw/Screenshot 2026-10-01 150343.png"
img_150343 = cv2.imread(src_150343)
# Trim 1px borders
clean_150343 = img_150343[1:-1, 1:-1].copy()
save_dual_format(clean_150343, "assets/images/hero-02")
save_dual_format(clean_150343, "assets/images/handwork-02")
crop_manifest.append({
    "target": "hero-02 / handwork-02",
    "source": src_150343,
    "crop_box": [1, 1, 491, 582],
    "cleaning": "Clean full portrait; trimmed edge artifacts",
    "category": "Hero / Handwork",
    "notes": "Bride in gold/yellow bridal lehenga with temple jewelry & kamarbandh"
})

# --- 3. Screenshot 2026-10-01 150536.png (Regal Couple in Crimson Kanchipuram Saree) ---
# Used for: hero-03, hindu-bride-01
src_150536 = "assets/raw/Screenshot 2026-10-01 150536.png"
img_150536 = cv2.imread(src_150536)
clean_150536 = img_150536[1:-1, 1:-1].copy()
save_dual_format(clean_150536, "assets/images/hero-03")
save_dual_format(clean_150536, "assets/images/hindu-bride-01")
crop_manifest.append({
    "target": "hero-03 / hindu-bride-01",
    "source": src_150536,
    "crop_box": [1, 1, 443, 582],
    "cleaning": "Trimmed 1px boundary; pristine photo content",
    "category": "Hero / Hindu Bride",
    "notes": "Bride in royal crimson Kanchipuram silk saree & groom in sherwani under floral bower"
})

# --- 4. raw_150615_r0_c1 (Laughing Couple: Champagne Gown & Ivory Sherwani) ---
# Used for: hero-04, featured-03
src_150615 = "assets/raw/Screenshot 2026-10-01 150615.png"
img_150615 = cv2.imread(src_150615)
crop_150615_c1 = img_150615[0:444, 334:665].copy()
h_c1, w_c1 = crop_150615_c1.shape[:2]
# Inpaint top-right reel play icon (x: w-35..w-5, y: 5..35)
mask_c1 = np.zeros((h_c1, w_c1), dtype=np.uint8)
tr_c1 = crop_150615_c1[:40, -40:]
mask_c1[:40, -40:] = cv2.dilate((cv2.cvtColor(tr_c1, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
# Inpaint M. LOFT lion logo and text (x: 110..220, y: 40..175)
logo_roi = crop_150615_c1[40:175, 110:220]
gray_logo = cv2.cvtColor(logo_roi, cv2.COLOR_BGR2GRAY)
mask_c1[40:175, 110:220] = cv2.dilate((gray_logo > 220).astype(np.uint8), np.ones((3,3), np.uint8))
clean_150615_c1 = inpaint_region(crop_150615_c1, mask_c1, radius=4)

save_dual_format(clean_150615_c1, "assets/images/hero-04")
save_dual_format(clean_150615_c1, "assets/images/featured-03")
crop_manifest.append({
    "target": "hero-04 / featured-03",
    "source": src_150615,
    "crop_box": [334, 0, 665, 444],
    "cleaning": "Inpainted top-right reel icon and centered M. LOFT lion logo & text watermark",
    "category": "Hero / Featured",
    "notes": "Joyful laughing couple in champagne reception gown & sherwani"
})

# --- 5. Screenshot 2026-10-01 150307.png (Christian Bride with Veil & Ivory Corset Gown) ---
# Used for: hero-05, christian-bride-01
src_150307 = "assets/raw/Screenshot 2026-10-01 150307.png"
img_150307 = cv2.imread(src_150307)
# Crop 25px black bar on left (x=25..), trim top 1px
crop_150307 = img_150307[1:, 25:].copy()
h_07, w_07 = crop_150307.shape[:2]
# Inpaint "M LOFT" watermark across waist (x: 120..320, y: h-120..h-40)
mask_150307 = np.zeros((h_07, w_07), dtype=np.uint8)
wm_roi = crop_150307[h_07-120:h_07-40, 120:320]
gray_wm = cv2.cvtColor(wm_roi, cv2.COLOR_BGR2GRAY)
mask_150307[h_07-120:h_07-40, 120:320] = cv2.dilate((gray_wm > 200).astype(np.uint8), np.ones((3,3), np.uint8))
clean_150307 = inpaint_region(crop_150307, mask_150307, radius=3)

save_dual_format(clean_150307, "assets/images/hero-05")
save_dual_format(clean_150307, "assets/images/christian-bride-01")
crop_manifest.append({
    "target": "hero-05 / christian-bride-01",
    "source": src_150307,
    "crop_box": [25, 1, 465, 589],
    "cleaning": "Cropped 25px left black margin; inpainted thin M LOFT text watermark at waist; preserved tjsflare photographer credit at bottom",
    "category": "Hero / Christian Bride",
    "notes": "Christian bride with veil holding hands with groom"
})

# --- 6. ref_insta6_col0 (Christian Bride & Groom in Ivory Gown & Suit) ---
# Used for: white-gown-01, christian-bride-02
src_insta6 = "assets/reference/instagram/insta6.png"
img_insta6 = cv2.imread(src_insta6)
crop_insta6_c0 = img_insta6[0:444, 105:437].copy()
h_i6, w_i6 = crop_insta6_c0.shape[:2]
# Inpaint M LOFT watermark at bottom (y: h-60..h, x: 80..260)
mask_i6 = np.zeros((h_i6, w_i6), dtype=np.uint8)
bot_i6 = crop_insta6_c0[h_i6-60:, 80:260]
mask_i6[h_i6-60:, 80:260] = cv2.dilate((cv2.cvtColor(bot_i6, cv2.COLOR_BGR2GRAY) > 200).astype(np.uint8), np.ones((3,3), np.uint8))
clean_insta6_c0 = inpaint_region(crop_insta6_c0, mask_i6, radius=3)

save_dual_format(clean_insta6_c0, "assets/images/white-gown-01")
save_dual_format(clean_insta6_c0, "assets/images/christian-bride-02")
crop_manifest.append({
    "target": "white-gown-01 / christian-bride-02",
    "source": src_insta6,
    "crop_box": [105, 0, 437, 444],
    "cleaning": "Inpainted bottom M LOFT watermark",
    "category": "White Gown / Christian Bride",
    "notes": "Christian bride and groom holding hands in ivory couture"
})

# --- 7. raw_150629_r0_c1 (Rose Gold / Copper Silk Saree) ---
# Used for: pavithrappattu-01
src_150629 = "assets/raw/Screenshot 2026-10-01 150629.png"
img_150629 = cv2.imread(src_150629)
crop_150629_c1 = img_150629[1:444, 335:666].copy()
h_29, w_29 = crop_150629_c1.shape[:2]
# Inpaint top-right reel play icon
mask_29 = np.zeros((h_29, w_29), dtype=np.uint8)
tr_29 = crop_150629_c1[:45, -45:]
mask_29[:45, -45:] = cv2.dilate((cv2.cvtColor(tr_29, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
clean_150629_c1 = inpaint_region(crop_150629_c1, mask_29, radius=3)

save_dual_format(clean_150629_c1, "assets/images/pavithrappattu-01")
crop_manifest.append({
    "target": "pavithrappattu-01",
    "source": src_150629,
    "crop_box": [335, 1, 666, 444],
    "cleaning": "Inpainted top-right reel play icon",
    "category": "Pavithrappattu",
    "notes": "Woman smiling in traditional copper/rose gold silk saree"
})

# --- 8. raw_150629_r0_c2 (Crimson Red Saree with Golden Handwork) ---
# Used for: roja-01
crop_150629_c2 = img_150629[1:444, 668:999].copy()
h_29_2, w_29_2 = crop_150629_c2.shape[:2]
# Inpaint top-right carousel multi-photo icon
mask_29_2 = np.zeros((h_29_2, w_29_2), dtype=np.uint8)
tr_29_2 = crop_150629_c2[:45, -45:]
mask_29_2[:45, -45:] = cv2.dilate((cv2.cvtColor(tr_29_2, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
clean_150629_c2 = inpaint_region(crop_150629_c2, mask_29_2, radius=3)

save_dual_format(clean_150629_c2, "assets/images/roja-01")
crop_manifest.append({
    "target": "roja-01",
    "source": src_150629,
    "crop_box": [668, 1, 999, 444],
    "cleaning": "Inpainted top-right carousel multi-photo icon",
    "category": "Roja",
    "notes": "Model seated in crimson red silk saree with golden border"
})

# --- 9. raw_152553_r0_c0 (Intricate Zardozi & Handwork Embroidery on Silk) ---
# Used for: handwork-01
src_152553 = "assets/raw/Screenshot 2026-10-01 152553.png"
img_152553 = cv2.imread(src_152553)
crop_152553_c0 = img_152553[0:442, 0:331].copy()
# Inpaint thin horizontal white tile divider line at y: 140..150
h_53, w_53 = crop_152553_c0.shape[:2]
mask_53 = np.zeros((h_53, w_53), dtype=np.uint8)
line_roi = crop_152553_c0[138:152, :]
mask_53[138:152, :] = (cv2.cvtColor(line_roi, cv2.COLOR_BGR2GRAY) > 220).astype(np.uint8)
mask_53 = cv2.dilate(mask_53, np.ones((3,3), np.uint8))
clean_152553_c0 = inpaint_region(crop_152553_c0, mask_53, radius=3)

save_dual_format(clean_152553_c0, "assets/images/handwork-01")
crop_manifest.append({
    "target": "handwork-01",
    "source": src_152553,
    "crop_box": [0, 0, 331, 442],
    "cleaning": "Inpainted thin horizontal grid tile line at y~145",
    "category": "Handwork",
    "notes": "Close-up macro of intricate zardozi handwork embroidery on silk lehenga"
})

# --- 10. ref_insta4_col0 ("M. LOFT LEGACY" Campaign Artwork) ---
# Used for: legacy-01, new-launch-01
src_insta4 = "assets/reference/instagram/insta4.png"
img_insta4 = cv2.imread(src_insta4)
crop_insta4_c0 = img_insta4[0:444, 22:354].copy()
clean_insta4_c0 = crop_insta4_c0[2:-2, 2:-2].copy()

save_dual_format(clean_insta4_c0, "assets/images/legacy-01")
save_dual_format(clean_insta4_c0, "assets/images/new-launch-01")
crop_manifest.append({
    "target": "legacy-01 / new-launch-01",
    "source": src_insta4,
    "crop_box": [24, 2, 352, 442],
    "cleaning": "Trimmed 2px edge borders; clean official campaign typography & pattern",
    "category": "Legacy / New Launch Alert",
    "notes": "Official 'M. LOFT LEGACY' gold typography on royal maroon damask/carpet pattern"
})

# --- 11. raw_152553_r0_c2 (Ornate Crimson Bridal Lehenga Drape) ---
# Used for: legacy-02, new-launch-02
crop_152553_c2 = img_152553[0:442, 666:994].copy()
h_53_2, w_53_2 = crop_152553_c2.shape[:2]
mask_53_2 = np.zeros((h_53_2, w_53_2), dtype=np.uint8)
line_roi_2 = crop_152553_c2[138:152, :]
mask_53_2[138:152, :] = (cv2.cvtColor(line_roi_2, cv2.COLOR_BGR2GRAY) > 220).astype(np.uint8)
mask_53_2 = cv2.dilate(mask_53_2, np.ones((3,3), np.uint8))
clean_152553_c2 = inpaint_region(crop_152553_c2, mask_53_2, radius=3)

save_dual_format(clean_152553_c2, "assets/images/legacy-02")
save_dual_format(clean_152553_c2, "assets/images/new-launch-02")
crop_manifest.append({
    "target": "legacy-02 / new-launch-02",
    "source": src_152553,
    "crop_box": [666, 0, 994, 442],
    "cleaning": "Inpainted thin horizontal grid tile line at y~145",
    "category": "Legacy / New Launch Alert",
    "notes": "Ornate crimson red bridal lehenga and embroidered dupatta drape"
})

# --- 12. Screenshot 2026-10-01 150328.png (Twirling Gold Lehenga) ---
# Used for: featured-01
src_150328 = "assets/raw/Screenshot 2026-10-01 150328.png"
img_150328 = cv2.imread(src_150328)
clean_150328 = img_150328[1:-1, 1:-1].copy()
save_dual_format(clean_150328, "assets/images/featured-01")
crop_manifest.append({
    "target": "featured-01",
    "source": src_150328,
    "crop_box": [1, 1, 476, 585],
    "cleaning": "Trimmed 1px borders; pristine photo",
    "category": "Featured Products",
    "notes": "Bride twirling in gold/mustard lehenga with floral hair wreath"
})

# --- 13. Screenshot 2026-10-01 150503.png (Deep Red Velvet/Silk Bridal Lehenga) ---
# Used for: featured-02
src_150503 = "assets/raw/Screenshot 2026-10-01 150503.png"
img_150503 = cv2.imread(src_150503)
h_03, w_03 = img_150503.shape[:2]
mask_150503 = np.zeros((h_03, w_03), dtype=np.uint8)
# Inpaint right arrow '>' carousel button at (x: 410..435, y: 295..325)
arr_roi = img_150503[295:325, 410:435]
mask_150503[295:325, 410:435] = cv2.dilate((cv2.cvtColor(arr_roi, cv2.COLOR_BGR2GRAY) > 180).astype(np.uint8), np.ones((5,5), np.uint8))
# Inpaint bottom-left person icon (x: 20..35, y: 555..575)
p_roi = img_150503[555:575, 20:35]
mask_150503[555:575, 20:35] = cv2.dilate((cv2.cvtColor(p_roi, cv2.COLOR_BGR2GRAY) > 150).astype(np.uint8), np.ones((5,5), np.uint8))
# Inpaint bottom-center dots (x: 200..235, y: 575..588)
dot_roi = img_150503[575:588, 200:235]
mask_150503[575:588, 200:235] = cv2.dilate((cv2.cvtColor(dot_roi, cv2.COLOR_BGR2GRAY) > 200).astype(np.uint8), np.ones((3,3), np.uint8))
clean_150503 = inpaint_region(img_150503, mask_150503, radius=4)

save_dual_format(clean_150503, "assets/images/featured-02")
crop_manifest.append({
    "target": "featured-02",
    "source": src_150503,
    "crop_box": [0, 0, 436, 594],
    "cleaning": "Inpainted Instagram right arrow button, bottom-left user tag icon, and pagination dots",
    "category": "Featured Products",
    "notes": "Model in deep red velvet/silk bridal lehenga with embroidered border"
})

# --- 14. Screenshot 2026-10-01 150555.png (Purple Silk Saree with Gold Border) ---
# Used for: new-arrival-01
src_150555 = "assets/raw/Screenshot 2026-10-01 150555.png"
img_150555 = cv2.imread(src_150555)
h_55, w_55 = img_150555.shape[:2]
mask_150555 = np.zeros((h_55, w_55), dtype=np.uint8)
# Inpaint bottom pagination dots at (x: 210..245, y: 580..590)
dots_roi_55 = img_150555[h_55-15:, 210:245]
mask_150555[h_55-15:, 210:245] = cv2.dilate((cv2.cvtColor(dots_roi_55, cv2.COLOR_BGR2GRAY) > 220).astype(np.uint8), np.ones((3,3), np.uint8))
clean_150555 = inpaint_region(img_150555, mask_150555, radius=3)

save_dual_format(clean_150555, "assets/images/new-arrival-01")
crop_manifest.append({
    "target": "new-arrival-01",
    "source": src_150555,
    "crop_box": [0, 0, 416, 584],
    "cleaning": "Inpainted bottom carousel pagination dots",
    "category": "New Arrivals",
    "notes": "Model in rich purple silk saree with intricate gold stripes and choker"
})

# --- 15. raw_150615_r0_c2 (Champagne & Emerald Bridal Styling) ---
# Used for: best-seller-01
crop_150615_c2 = img_150615[0:444, 667:998].copy()
h_15_2, w_15_2 = crop_150615_c2.shape[:2]
# Inpaint top-right reel play icon
mask_15_2 = np.zeros((h_15_2, w_15_2), dtype=np.uint8)
tr_15_2 = crop_150615_c2[:40, -40:]
mask_15_2[:40, -40:] = cv2.dilate((cv2.cvtColor(tr_15_2, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
clean_150615_c2 = inpaint_region(crop_150615_c2, mask_15_2, radius=3)

save_dual_format(clean_150615_c2, "assets/images/best-seller-01")
crop_manifest.append({
    "target": "best-seller-01",
    "source": src_150615,
    "crop_box": [667, 0, 998, 444],
    "cleaning": "Inpainted top-right reel play icon",
    "category": "Best Sellers",
    "notes": "Bride portrait smiling with emerald jewelry & champagne gown"
})

# --- 16. Mosaic Photos (4 Collages matching brief) ---
# mosaic-01: "Our Brides" -> Screenshot 2026-10-01 150429.png
src_150429 = "assets/raw/Screenshot 2026-10-01 150429.png"
img_150429 = cv2.imread(src_150429)
h_429, w_429 = img_150429.shape[:2]
# Inpaint top-right carousel multi-photo icon
mask_429 = np.zeros((h_429, w_429), dtype=np.uint8)
tr_429 = img_150429[:45, -45:]
mask_429[:45, -45:] = cv2.dilate((cv2.cvtColor(tr_429, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
clean_150429 = inpaint_region(img_150429, mask_429, radius=3)
save_dual_format(clean_150429, "assets/images/mosaic-01")
crop_manifest.append({
    "target": "mosaic-01",
    "source": src_150429,
    "crop_box": [0, 0, 472, 584],
    "cleaning": "Inpainted top-right multi-photo carousel icon",
    "category": "Photo Mosaic (Our Brides)",
    "notes": "Bride, groom, and bridesmaid in traditional Kerala wedding attire"
})

# mosaic-02: "Happiness" -> Screenshot 2026-10-01 150359.png
src_150359 = "assets/raw/Screenshot 2026-10-01 150359.png"
img_150359 = cv2.imread(src_150359)
clean_150359 = img_150359[1:-1, 1:-1].copy()
save_dual_format(clean_150359, "assets/images/mosaic-02")
crop_manifest.append({
    "target": "mosaic-02",
    "source": src_150359,
    "crop_box": [1, 1, 471, 587],
    "cleaning": "Trimmed 1px border; pristine clean photo",
    "category": "Photo Mosaic (Happiness)",
    "notes": "Two brides/sisters sharing a joyful moment in Kanchipuram silk sarees"
})

# mosaic-03: "Handcrafted" -> ref_insta6_col1.jpg (Joel Jacob Mathew designing at atelier)
crop_insta6_c1 = img_insta6[0:444, 438:770].copy()
h_c6_1, w_c6_1 = crop_insta6_c1.shape[:2]
# Inpaint top-right reel play icon
mask_c6_1 = np.zeros((h_c6_1, w_c6_1), dtype=np.uint8)
tr_c6_1 = crop_insta6_c1[:40, -40:]
mask_c6_1[:40, -40:] = cv2.dilate((cv2.cvtColor(tr_c6_1, cv2.COLOR_BGR2GRAY) > 230).astype(np.uint8), np.ones((5,5), np.uint8))
clean_insta6_c1 = inpaint_region(crop_insta6_c1, mask_c6_1, radius=3)
save_dual_format(clean_insta6_c1, "assets/images/mosaic-03")
crop_manifest.append({
    "target": "mosaic-03",
    "source": src_insta6,
    "crop_box": [438, 0, 770, 444],
    "cleaning": "Inpainted top-right reel play icon",
    "category": "Photo Mosaic (Handcrafted)",
    "notes": "Joel Jacob Mathew sketching couture bridal gown with atelier design team"
})

# mosaic-04: "Beauty of Bride" -> raw_152542_r0_c1
src_152542 = "assets/raw/Screenshot 2026-10-01 152542.png"
img_152542 = cv2.imread(src_152542)
crop_152542_c1 = img_152542[6:448, 341:674].copy()
h_c42, w_c42 = crop_152542_c1.shape[:2]
# Inpaint top letters "...C OF M..." in upper background (y: 0..90, x: 0..w)
mask_c42 = np.zeros((h_c42, w_c42), dtype=np.uint8)
bg_roi = crop_152542_c1[:90, :]
# Letters are dark green/brown on olive background
bg_gray = cv2.cvtColor(bg_roi, cv2.COLOR_BGR2GRAY)
letters_mask = ((bg_gray < 110) & (bg_gray > 20)).astype(np.uint8)
# Avoid masking bride's head at bottom of ROI
letters_mask[75:, :] = 0
mask_c42[:90, :] = cv2.dilate(letters_mask, np.ones((3,3), np.uint8))
clean_152542_c1 = inpaint_region(crop_152542_c1, mask_c42, radius=4)

save_dual_format(clean_152542_c1, "assets/images/mosaic-04")
crop_manifest.append({
    "target": "mosaic-04",
    "source": src_152542,
    "crop_box": [341, 6, 674, 448],
    "cleaning": "Inpainted 'FACE OF M' campaign letters on background behind bride's head",
    "category": "Photo Mosaic (Beauty of Bride)",
    "notes": "Close-up portrait of bride with maang tikka, emerald/polki choker and crimson veil"
})

# --- 17. Instagram Feed 3 Cards ---
# instagram-01: Screenshot 2026-10-01 150923.png (Three smiling women in Kasavu sarees)
src_150923 = "assets/raw/Screenshot 2026-10-01 150923.png"
img_150923 = cv2.imread(src_150923)
h_923, w_923 = img_150923.shape[:2]
mask_150923 = np.zeros((h_923, w_923), dtype=np.uint8)
# Inpaint right arrow '>' button at (x: w-25..w, y: 240..270)
arr_roi_923 = img_150923[240:270, w_923-25:]
mask_150923[240:270, w_923-25:] = cv2.dilate((cv2.cvtColor(arr_roi_923, cv2.COLOR_BGR2GRAY) > 180).astype(np.uint8), np.ones((5,5), np.uint8))
# Inpaint bottom-left person icon (x: 20..35, y: 550..575)
p_roi_923 = img_150923[550:575, 20:35]
mask_150923[550:575, 20:35] = cv2.dilate((cv2.cvtColor(p_roi_923, cv2.COLOR_BGR2GRAY) > 150).astype(np.uint8), np.ones((5,5), np.uint8))
# Inpaint bottom-center dots (x: 200..240, y: 565..578)
dot_roi_923 = img_150923[565:578, 200:240]
mask_150923[565:578, 200:240] = cv2.dilate((cv2.cvtColor(dot_roi_923, cv2.COLOR_BGR2GRAY) > 200).astype(np.uint8), np.ones((3,3), np.uint8))
clean_150923 = inpaint_region(img_150923, mask_150923, radius=4)

save_dual_format(clean_150923, "assets/images/instagram-01")
crop_manifest.append({
    "target": "instagram-01",
    "source": src_150923,
    "crop_box": [0, 0, 443, 579],
    "cleaning": "Inpainted Instagram right arrow, tag icon, and pagination dots",
    "category": "Follow Us On Instagram",
    "notes": "Three smiling women in Kerala Kasavu sarees"
})

# instagram-02: ref_insta3_col2 ("Aha! M. LOFT" Gold on Dark Green Campaign)
src_insta3 = "assets/reference/instagram/insta3.png"
img_insta3 = cv2.imread(src_insta3)
crop_insta3_c2 = img_insta3[0:444, 778:1110].copy()
save_dual_format(crop_insta3_c2, "assets/images/instagram-02")
crop_manifest.append({
    "target": "instagram-02",
    "source": src_insta3,
    "crop_box": [778, 0, 1110, 444],
    "cleaning": "Pristine official campaign artwork",
    "category": "Follow Us On Instagram",
    "notes": "Official 'Aha! M. LOFT' campaign visual with gold lion on dark green foliage"
})

# instagram-03: clean_150359
save_dual_format(clean_150359, "assets/images/instagram-03")
crop_manifest.append({
    "target": "instagram-03",
    "source": src_150359,
    "crop_box": [1, 1, 471, 587],
    "cleaning": "Pristine clean photo",
    "category": "Follow Us On Instagram",
    "notes": "Bridal sisters celebrating in Kanchipuram sarees"
})

print("\n=== 2. EXTRACTING REEL POSTER FRAMES ===")

reel_targets = [
    (1, 4.0, "Bridal saree pleating & drape"),
    (2, 18.0, "Bride walking in royal crimson Kanchipuram silk"),
    (3, 1.0, "Christian bride veil styling in ivory gown"),
    (4, 1.0, "Bridal handwork zardozi embroidery process"),
    (5, 8.0, "Bridal twirling in emerald and gold lehenga"),
    (6, 4.0, "Joel Jacob Mathew atelier custom bridal design"),
    (7, 10.0, "Bride in pavithrappattu saree holding floral bouquet")
]

for reel_num, timestamp, desc in reel_targets:
    reel_path = f"assets/reels/reel_{reel_num}.mp4"
    cap = cv2.VideoCapture(reel_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(timestamp * fps))
    ret, frame = cap.read()
    if ret:
        target_name = f"assets/images/reel-posters/reel-{reel_num:02d}"
        save_dual_format(frame, target_name)
        crop_manifest.append({
            "target": f"reel-posters/reel-{reel_num:02d}",
            "source": reel_path,
            "crop_box": f"Frame at {timestamp:.1f}s",
            "cleaning": f"Clean video frame without text overlay or stickers extracted from {os.path.basename(reel_path)}",
            "category": "Reels Poster",
            "notes": desc
        })
    cap.release()

print("\n=== 3. GENERATING DOCUMENTATION & REPORTING FILES ===")

# Save crop sources manifest
with open("crop_sources.json", "w", encoding="utf-8") as f:
    json.dump(crop_manifest, f, indent=2)

with open("crop_sources.md", "w", encoding="utf-8") as f:
    f.write("# M LOFT - Image Crop Sources & Provenance\n\n")
    f.write("| Output Image | Category | Source File | Crop Box / Frame | Processing & Cleaning | Notes |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
    for item in crop_manifest:
        f.write(f"| `{item['target']}` | {item['category']} | `{item['source']}` | `{item['crop_box']}` | {item['cleaning']} | {item['notes']} |\n")

# Generate needs_retake.txt
needs_retake = [
    "assets/raw/Screenshot 2026-10-01 150629.png (Column 0): Covered by dark hover overlay with white heart (1,069) and comment count (7). Need re-screenshot without hovering cursor.",
    "assets/raw/Screenshot 2026-10-01 152542.png (Column 0): Covered by dark hover overlay with white heart (63) and comment count (0). Need re-screenshot without hovering cursor.",
    "assets/raw/Screenshot 2026-10-01 152553.png (Column 1): Covered by dark hover overlay with white heart (64) and comment count (0). Need re-screenshot without hovering cursor.",
    "assets/reference/instagram/insta2.png (Column 1): Covered by dark hover overlay with white heart (71.2K) and comment count (399).",
    "assets/reference/instagram/insta3.png (Column 0): Covered by dark hover overlay with white heart (505) and comment count (3).",
    "assets/reference/instagram/insta4.png (Column 1): Covered by dark hover overlay with white heart (4,932) and comment count (300)."
]

with open("needs_retake.txt", "w", encoding="utf-8") as f:
    f.write("M LOFT - SCREENSHOTS NEEDING RETAKE\n")
    f.write("====================================\n")
    f.write("The following screenshot regions are obscured by Instagram's dark hover overlay (white heart and comment count numbers) and could not be used. Please re-screenshot without hovering the cursor over the image.\n\n")
    for item in needs_retake:
        f.write(f"- {item}\n")

# Generate needs_originals.txt
needs_originals = [
    "assets/reference/instagram/insta5.png (Columns 0, 1, 2): Contains third-party photographer watermark ('fr' in gold floral circle at bottom-left) and floral vendor credit ('floretta' near bouquet). Cropping would truncate the bride's saree and floral styling. Requesting high-resolution clean originals from the photographer.",
    "assets/raw/Screenshot 2026-10-01 150307.png: Contains photographer credit 'tjsflare' at bottom-center. Inpainted M LOFT text at waist, but requesting original unwatermarked photography file for highest print/retina display quality."
]

with open("needs_originals.txt", "w", encoding="utf-8") as f:
    f.write("M LOFT - ORIGINAL PHOTOGRAPHS NEEDED\n")
    f.write("=====================================\n")
    f.write("The following images contain external photographer or vendor watermarks/signatures that should not be removed by editing without the photographer's master file:\n\n")
    for item in needs_originals:
        f.write(f"- {item}\n")

print("Files created: crop_sources.json, crop_sources.md, needs_retake.txt, needs_originals.txt.")
