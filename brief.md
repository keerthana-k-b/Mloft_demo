# M LOFT by Joel Jacob Mathew: Website Brief

## Brand
- Name: M LOFT by Joel Jacob Mathew
- Instagram: @mloft_by_joeljacobmathew (755K followers)
- Business: Bridal and occasion wear boutique in Changanassery,
  Kerala. Hindu bridal, Christian bridal and white gowns,
  engagement wear, sarees, lehengas, pavithrappattu, roja,
  handwork, and custom designs.
- Phone/WhatsApp: 8075909720
- Logo: assets/reference/logo.jpg (gold lion on deep teal-green)
- Campaigns: "M. Loft Legacy" (maroon ornate pattern) and
  "Aha!" (gold on dark green)
- Tagline (placeholder): "Crafted for your story."

## Goal
A premium demo website that replaces their old site. It
follows the page structure and interactions of
panchalivastra.com, restyled in M LOFT's own luxury look.
The main action is enquiry and booking via WhatsApp, with a
cart-style flow as a secondary option.

## Reference
- assets/reference/panchali/: structure, spacing and
  interactions to follow (do not copy their text, logo,
  images or code)
- assets/reference/instagram/: brand mood and content source
- Do NOT use the old mloftbyjoeljacobmathew.com site.

## Design system
- Colors:
  - Primary deep teal #0F3B3A
  - Accent antique gold #C9A24B
  - Secondary deep maroon #5A0F1F
  - Background ivory #FAF6EE and white #FFFFFF
  - Text charcoal #222222
  (Panchali's red is replaced by gold and maroon.)
- Fonts (Google Fonts): headings Cormorant Garamond, body and
  nav Montserrat. Section headings are light weight with a
  short gold underline, like Panchali's.
- Cards: rounded corners (14px), soft shadows
- Buttons: gold or teal, slightly rounded, small uppercase
- Motion: gentle fade-up on scroll, slow image zoom on hover,
  smooth carousels

## Page structure (home), in order
1. Header: white, sticky, logo left, centered nav (HOME,
   COLLECTIONS dropdown, REELS, CONTACT), right icons
   (search, Instagram, wishlist, WhatsApp)
2. Hero: slideshow of slanted parallelogram photo panels
   (5 bridal images) with the headline "Timeless Bridal
   Elegance" and a subtitle; buttons "Explore Collections"
   and "Book a Consultation"
3. Announcement strip below hero (gold or maroon): "Custom
   designs and handwork | Enquire on WhatsApp 8075909720"
4. Collections: tall portrait cards (4 per row) with a bottom
   gradient and label: Hindu Bride, Christian Bride,
   Engagement, White Gown, Pavithrappattu, Roja, Handwork,
   Legacy
5. Product tabs: New Arrivals / Best Sellers / Featured, a
   carousel with heart icon, "Enquire" button on hover, round
   arrow buttons and a progress bar
6. Photo mosaic: 4-photo collage with captions "Our Brides",
   "Happiness", "Handcrafted", "Beauty of Bride"
7. New Launch Alert: two tilted stacked photos beside text
   about the "M. Loft Legacy" collection and a "Discover
   More" button
8. REELS ("Watch and Shop"): vertical reel cards (9:16) with
   a play button; hover plays a muted preview; click opens a
   fullscreen modal player with a "Enquire on WhatsApp"
   button; each card has a glass overlay with the outfit name
   and a button
9. Follow Us On Instagram: 3-card carousel, the Instagram icon
   on hover, and a "Follow Us" pill button linking to the
   profile
10. Trust strip: Custom Made, 24/7 WhatsApp Support, Handcrafted
    Quality
11. Footer: logo, quick links, customer care, address, phone,
    map link, newsletter ("Stay Updated"), social icons
12. Floating WhatsApp button (bottom right)

## Other pages
Collections (grid with filter), Collection/product detail,
Reels (full grid), About, Contact (form, map link, address).

## Content rules
- Product names and prices are placeholders for now
- Use only the images in assets/images and videos in
  assets/reels
- Never use the Instagram UI overlays (heart/comment counts,
  play icons, pin icons) in any image

## Tech
- Static site: HTML, CSS, vanilla JavaScript (no frameworks)
- Mobile first and fully responsive; test 375px, 768px, 1280px
- Folders: /css, /js, /assets
- Lazy-load images, compress to WebP where possible