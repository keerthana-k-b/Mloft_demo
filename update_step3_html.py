import os

# Define the 24 cards
tabs_data = {
    "new-arrivals": {
        "title": "New Arrivals",
        "id_prefix": "na",
        "panel_id": "panel-new-arrivals",
        "tab_btn_id": "tab-new-arrivals-btn",
        "is_active": True,
        "items": [
            {
                "id": "na-01",
                "name": "Bridal Silk Saree 01",
                "category": "Kanchipuram Silk",
                "price": "from Rs 24,999",
                "img": "assets/images/new-arrival-01.webp"
            },
            {
                "id": "na-02",
                "name": "Temple Heritage Saree 02",
                "category": "Temple Weave",
                "price": "from Rs 28,500",
                "img": "assets/images/hindu-bride-01.webp"
            },
            {
                "id": "na-03",
                "name": "Pastel Floral Lehenga 03",
                "category": "Engagement Couture",
                "price": "from Rs 36,000",
                "img": "assets/images/engagement-01.webp"
            },
            {
                "id": "na-04",
                "name": "Cathedral Lace Gown 04",
                "category": "Christian Bridal",
                "price": "from Rs 42,000",
                "img": "assets/images/christian-bride-01.webp"
            },
            {
                "id": "na-05",
                "name": "Pavithrappattu Silk 05",
                "category": "Heritage Silk",
                "price": "from Rs 22,500",
                "img": "assets/images/pavithrappattu-01.webp"
            },
            {
                "id": "na-06",
                "name": "Roja Crimson Saree 06",
                "category": "Roja Collection",
                "price": "from Rs 26,999",
                "img": "assets/images/roja-01.webp"
            },
            {
                "id": "na-07",
                "name": "Zardozi Bridal Ensemble 07",
                "category": "Handwork Couture",
                "price": "from Rs 48,000",
                "img": "assets/images/handwork-02.webp"
            },
            {
                "id": "na-08",
                "name": "Bespoke Illusion Gown 08",
                "category": "White Gowns",
                "price": "from Rs 39,500",
                "img": "assets/images/white-gown-01.webp"
            }
        ]
    },
    "bestsellers": {
        "title": "Best Sellers",
        "id_prefix": "bs",
        "panel_id": "panel-bestsellers",
        "tab_btn_id": "tab-bestsellers-btn",
        "is_active": False,
        "items": [
            {
                "id": "bs-01",
                "name": "Royal Emerald Gown 01",
                "category": "Boutique Signature",
                "price": "from Rs 34,999",
                "img": "assets/images/best-seller-01.webp"
            },
            {
                "id": "bs-02",
                "name": "Aura Twirl Lehenga 02",
                "category": "Bridal Lehenga",
                "price": "from Rs 45,000",
                "img": "assets/images/featured-01.webp"
            },
            {
                "id": "bs-03",
                "name": "Artisanal Zardozi Saree 03",
                "category": "Intricate Handwork",
                "price": "from Rs 32,500",
                "img": "assets/images/handwork-01.webp"
            },
            {
                "id": "bs-04",
                "name": "Crimson Velvet Lehenga 04",
                "category": "M. Loft Legacy",
                "price": "from Rs 52,000",
                "img": "assets/images/legacy-02.webp"
            },
            {
                "id": "bs-05",
                "name": "Ivory Satin Bridal Gown 05",
                "category": "Christian Couture",
                "price": "from Rs 44,000",
                "img": "assets/images/christian-bride-02.webp"
            },
            {
                "id": "bs-06",
                "name": "Traditional Kerala Kasavu 06",
                "category": "Kerala Traditional",
                "price": "from Rs 18,999",
                "img": "assets/images/mosaic-01.webp"
            },
            {
                "id": "bs-07",
                "name": "Golden Brocade Silk 07",
                "category": "Heritage Weave",
                "price": "from Rs 29,500",
                "img": "assets/images/mosaic-02.webp"
            },
            {
                "id": "bs-08",
                "name": "Champagne Reception Ensemble 08",
                "category": "Occasion Wear",
                "price": "from Rs 38,000",
                "img": "assets/images/featured-03.webp"
            }
        ]
    },
    "featured": {
        "title": "Featured",
        "id_prefix": "ft",
        "panel_id": "panel-featured",
        "tab_btn_id": "tab-featured-btn",
        "is_active": False,
        "items": [
            {
                "id": "ft-01",
                "name": "Scarlet Heritage Lehenga 01",
                "category": "Bridal Velvet",
                "price": "from Rs 49,999",
                "img": "assets/images/featured-02.webp"
            },
            {
                "id": "ft-02",
                "name": "M. Loft Signature Weave 02",
                "category": "Atelier Campaign",
                "price": "from Rs 35,000",
                "img": "assets/images/legacy-01.webp"
            },
            {
                "id": "ft-03",
                "name": "Royal Polki Bridal Drape 03",
                "category": "Bridal Portrait",
                "price": "from Rs 31,500",
                "img": "assets/images/mosaic-04.webp"
            },
            {
                "id": "ft-04",
                "name": "Festive Kasavu Set 04",
                "category": "Festive Occasion",
                "price": "from Rs 21,000",
                "img": "assets/images/instagram-01.webp"
            },
            {
                "id": "ft-05",
                "name": "Ornate Maroon Damask Saree 05",
                "category": "New Launch Alert",
                "price": "from Rs 33,500",
                "img": "assets/images/new-launch-01.webp"
            },
            {
                "id": "ft-06",
                "name": "Embroidered Dupatta Lehenga 06",
                "category": "Bridal Couture",
                "price": "from Rs 47,500",
                "img": "assets/images/new-launch-02.webp"
            },
            {
                "id": "ft-07",
                "name": "Celebration Silk Ensemble 07",
                "category": "Sister of the Bride",
                "price": "from Rs 27,999",
                "img": "assets/images/instagram-03.webp"
            },
            {
                "id": "ft-08",
                "name": "Grand Muhurtham Silk 08",
                "category": "Kanchipuram Silk",
                "price": "from Rs 39,000",
                "img": "assets/images/hero-03.webp"
            }
        ]
    }
}

def render_card(item):
    wa_msg = f"Hi M LOFT, I am interested in {item['name']}"
    import urllib.parse
    wa_url = "https://wa.me/918075909720?text=" + urllib.parse.quote(wa_msg)
    
    return f"""                <!-- Card: {item['name']} -->
                <div class="product-card" data-product-id="{item['id']}">
                  <div class="product-img-wrap">
                    <img src="{item['img']}" alt="{item['name']}" class="product-img" width="320" height="400" loading="lazy">
                    <button class="product-heart-btn" aria-label="Add {item['name']} to Wishlist" data-id="{item['id']}" type="button">
                      <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    </button>
                    <div class="product-wa-overlay">
                      <a href="{wa_url}" target="_blank" rel="noopener" class="btn-product-wa" aria-label="Enquire on WhatsApp about {item['name']}">
                        <svg viewBox="0 0 32 32"><path d="M16 2a13.9 13.9 0 0 0-11.9 21.1L2 30l7.1-1.9A13.9 13.9 0 1 0 16 2zm0 25.5a11.5 11.5 0 0 1-5.9-1.6l-.4-.3-4.4 1.2 1.2-4.3-.3-.4A11.6 11.6 0 1 1 16 27.5zm6.4-8.6c-.3-.2-2-.1-2.3-1.1s-.8-1-1.1-1-.7 0-1 .4-1.3 1.6-1.6 1.9-.6.4-1 .2a12.8 12.8 0 0 1-3.8-2.3 14.1 14.1 0 0 1-2.6-3.3c-.2-.4 0-.6.2-.8s.4-.5.6-.7.2-.4.4-.6a1.5 1.5 0 0 0 0-.8c-.1-.2-.9-2.2-1.2-3s-.6-.7-.9-.7h-.7a1.4 1.4 0 0 0-1 .5 4.3 4.3 0 0 0-1.3 3.2 7.5 7.5 0 0 0 1.6 4 17.2 17.2 0 0 0 6.6 5.8c2.8 1.2 3.4 1 4 1a3.4 3.4 0 0 0 2.3-1.6 2.8 2.8 0 0 0 .2-1.6c-.1-.2-.4-.3-.7-.5z"/></svg>
                        <span>Enquire on WhatsApp</span>
                      </a>
                    </div>
                  </div>
                  <div class="product-info">
                    <span class="product-cat-label">{item['category']}</span>
                    <h3 class="product-title">{item['name']}</h3>
                    <span class="product-price">{item['price']}</span>
                  </div>
                </div>"""

def render_tab_panel(tab_key, data):
    active_cls = " active" if data["is_active"] else ""
    cards_html = "\n\n".join([render_card(it) for it in data["items"]])
    return f"""          <!-- Tab: {data['title']} -->
          <div class="product-tab-panel{active_cls}" id="{data['panel_id']}" role="tabpanel" aria-labelledby="{data['tab_btn_id']}">
            <div class="product-carousel" data-carousel="{tab_key}" tabindex="0" aria-label="{data['title']} Carousel">
              <div class="product-track">
{cards_html}
              </div>
            </div>
          </div>"""

html_section = f"""        </div>
      </div>
    </section>

    <!-- ====================================================================
         Section D: Product Showcase (Tabs & Carousel) - Step 3
         ==================================================================== -->
    <section class="products-section" id="collection-highlights" aria-label="Our Collection Highlights">
      <div class="container">
        
        <!-- Section Heading: Light weight with short gold underline -->
        <div class="products-header">
          <h2 class="products-heading">Our Collection Highlights</h2>
          
          <!-- Tabs: Three rounded pill buttons -->
          <div class="product-tabs-wrap">
            <div class="product-tabs" role="tablist" aria-label="Our Collection Highlights Tabs">
              <button class="product-tab-btn active" role="tab" id="tab-new-arrivals-btn" aria-selected="true" aria-controls="panel-new-arrivals" tabindex="0" data-tab="new-arrivals">New Arrivals</button>
              <button class="product-tab-btn" role="tab" id="tab-bestsellers-btn" aria-selected="false" aria-controls="panel-bestsellers" tabindex="-1" data-tab="bestsellers">Best Sellers</button>
              <button class="product-tab-btn" role="tab" id="tab-featured-btn" aria-selected="false" aria-controls="panel-featured" tabindex="-1" data-tab="featured">Featured</button>
            </div>
          </div>
        </div>

        <!-- Carousel Container with Navigation Arrows & Indicator -->
        <div class="product-carousel-wrapper">
          
{render_tab_panel("new-arrivals", tabs_data["new-arrivals"])}

{render_tab_panel("bestsellers", tabs_data["bestsellers"])}

{render_tab_panel("featured", tabs_data["featured"])}

          <!-- Carousel Controls: Left / Right Arrows (teal with gold border) & Scroll Progress Bar -->
          <div class="carousel-bottom-bar">
            <div class="carousel-progress-track" role="progressbar" aria-label="Product carousel progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
              <div class="carousel-progress-thumb"></div>
            </div>
            <div class="carousel-arrows">
              <button class="carousel-arrow carousel-arrow-prev" aria-label="Previous products" type="button">
                <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
              </button>
              <button class="carousel-arrow carousel-arrow-next" aria-label="Next products" type="button">
                <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the start: line after the end of collection cards
start_marker = '<a href="collections.html?c=legacy" class="collection-card" aria-label="View M. Loft Legacy Collection">'
end_marker = '</main>'

idx_start_ref = content.find(start_marker)
if idx_start_ref == -1:
    print("Could not find start marker!")
    exit(1)

# Find the next </div> closing collections-grid
grid_close_idx = content.find('</div>', idx_start_ref)
# Find the next </div> closing container or Section D comment
section_d_comment_idx = content.find('<!-- ===', grid_close_idx)
main_close_idx = content.find('</main>', section_d_comment_idx)

# Replace everything from grid_close_idx to main_close_idx
new_content = content[:grid_close_idx] + html_section + "\n\n  " + content[main_close_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully updated index.html!")
