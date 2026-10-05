# M LOFT by Joel Jacob Mathew — Bridal Atelier Website

A bespoke bridal couture and occasion wear boutique web application designed for **M LOFT by Joel Jacob Mathew**, located in Changanassery, Kerala.

---

## 1. How to Run the Site Locally

Because the application uses modern JavaScript modules and fetch operations, run it via any local HTTP server:

### Option A: Using Python (Built-in)
```bash
# From the project root or the deploy/ folder:
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### Option B: Using Node.js / npx
```bash
# Using serve
npx serve .
# Or to preview the production-ready build:
npx serve deploy
```

### Option C: VS Code / IDE Live Server
Right-click on `index.html` (or `deploy/index.html`) and select **"Open with Live Server"**.

---

## 2. How to Edit Products (`js/products.js`)

All product and gallery data are centrally managed in [`js/products.js`](js/products.js). To add, edit, or remove bridal creations, update the `PRODUCTS_DATA` array.

### Product Object Schema

```javascript
{
  id: 'hindu-bride-01',                  // Unique identifier slug
  name: 'Aurelia Royal Kanchipuram',     // Display title
  category: 'hindu-bride',               // Category slug (see supported categories below)
  images: [                              // Image path array (first is main card image)
    'assets/images/hindu-bride-01.webp',
    'assets/images/hindu-bride-02.webp'
  ],
  price: '₹58,000',                      // Display price or "Price on Request"
  desc: 'Sample specification text describing the ensemble.',
  specs: {
    fabric: 'Pure Mulberry Kanchipuram Silk & Tissue Weave',
    work: 'Zari Brocade, Hand Adda Beading & Cutdana',
    leadTime: '4–6 Weeks (Handcrafted)',
    location: 'Changanassery Atelier & Worldwide Shipping'
  },
  bullets: [
    'Pure handloom silk base with authentic zari borders',
    'Custom tailored neckline and blouse adaptation available'
  ]
}
```

### Supported Category Slugs:
- `hindu-bride` — Hindu Bride
- `christian-bride` — Christian Bride
- `engagement` — Engagement Wear
- `white-gown` — White Gowns
- `pavithrappattu` — Pavithrappattu
- `roja` — Roja Collection
- `handwork` — Handwork Details
- `legacy` — M. Loft Legacy

Updating `js/products.js` will automatically reflect across the Collections catalog (`collections.html`), category filter pills, search bar, and single product detail view (`product-detail.html?id=...`).

---

## 3. Production Deployment (`deploy/`)

The standalone `deploy/` directory contains strictly production essentials:
- HTML Pages: `index.html`, `collections.html`, `product-detail.html`, `reels.html`, `about.html`, `contact.html`, `404.html`
- Stylesheets: `css/style.css`
- Scripts: `js/main.js`, `js/products.js`
- Assets: Referenced images and reel video files (`assets/images/`, `assets/reels/`)
