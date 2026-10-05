/**
 * M LOFT by Joel Jacob Mathew — Master Product & Collection Catalog
 * Contains all product and photography data grouped by category slugs:
 * hindu-bride, christian-bride, engagement, white-gown, pavithrappattu, roja, handwork, legacy
 */

const CATEGORIES = [
  { slug: 'all', name: 'All Collections', desc: 'Complete bespoke bridal couture & occasion wear' },
  { slug: 'hindu-bride', name: 'Hindu Bride', desc: 'Kanchipuram & temple Korvai weaves' },
  { slug: 'christian-bride', name: 'Christian Bride', desc: 'Cathedral veils & corset gowns' },
  { slug: 'engagement', name: 'Engagement Wear', desc: 'Pastel lehengas & modern luxury' },
  { slug: 'white-gown', name: 'White Gowns', desc: 'Handcrafted bespoke western couture' },
  { slug: 'pavithrappattu', name: 'Pavithrappattu', desc: 'Heritage silk & metallic Kasavu zari' },
  { slug: 'roja', name: 'Roja Collection', desc: 'Signature crimson silks & hand embroidery' },
  { slug: 'handwork', name: 'Handwork Details', desc: 'Artisanal zardozi, dabka & cutwork' },
  { slug: 'legacy', name: 'M. Loft Legacy', desc: 'Signature royal archives & festive silhouettes' }
];

const PRODUCTS = [
  // ==========================================
  // HINDU BRIDE
  // ==========================================
  {
    id: 'hb-1',
    name: 'Aurelia Royal Crimson Kanchipuram Saree',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹48,500',
    badge: 'Best Seller',
    images: [
      'assets/images/hindu-bride-01.webp',
      'assets/images/hero-03.webp',
      'assets/images/mosaic-04.webp'
    ],
    description: '(Sample specification) Pure mulberry silk handwoven using traditional Korvai interlocking techniques. Features intricate temple border motifs and pure gold zari floral buttas designed for ceremonial sacred rituals.',
    fabric: 'Pure Mulberry Kanchipuram Silk & Pure Gold Zari',
    work: 'Authentic Korvai Handloom Weave with Sacred Temple Motifs',
    details: [
      'Handloom silk certified with Silk Mark authentication',
      'Heavily embellished contrast pallu with traditional annapakshi motifs',
      'Includes unstitched matching pure silk blouse piece with zari border',
      'Bespoke blouse design & tailored fitting available at our Changanassery atelier',
      'Estimated crafting & delivery timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'hb-2',
    name: 'Ananya Saffron Sheer Veil Bridal Ensemble',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹56,000',
    badge: 'Editorial Pick',
    images: [
      'assets/images/hindu-bride-02.webp',
      'assets/images/handwork-01.webp'
    ],
    description: '(Sample specification) Luminous saffron bridal drape paired with a scalloped sheer organza veil. Finished with delicate hand-embroidered kiran lace and antique gold micro sequins along the perimeter.',
    fabric: 'Raw Silk & Fine Translucent Silk Organza',
    work: 'Hand Zardozi Kiran Edging with Muted Sequin Clusters',
    details: [
      'Dual-layer bridal veil styling with custom length options',
      'Intricately embellished border with traditional gota and zardozi detailing',
      'Styled for ceremonial muhurtham and morning bridal entries',
      'Bespoke color matching available for custom jewelry coordination',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'hb-3',
    name: 'Mayura Tangerine Korvai Silk Saree',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹51,000',
    badge: 'Heirloom',
    images: [
      'assets/images/hindu-bride-03.webp',
      'assets/images/hindu-bride-01.webp'
    ],
    description: '(Sample specification) Vibrant tangerine pure Kanchipuram silk saree with contrast peacock green border. Handwoven with interlocking zari techniques and auspicious floral vine medallions.',
    fabric: 'Heirloom Heavy-Ply Pure Kanchipuram Silk',
    work: 'Interlocked Korvai Zari Weft with Mayil (Peacock) Motifs',
    details: [
      'Traditional triple-shuttle Korvai hand-weaving',
      'Heavy gold zari pallu with traditional temple gopuram motifs',
      'Coordinating bottle green silk blouse piece included',
      'Preserved with heritage heirloom anti-tarnish tissue wrapping',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'hb-4',
    name: 'Kalyani Temple Gold Silk Drape',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹53,000',
    badge: 'Sacred Weave',
    images: [
      'assets/images/hindu-bride-04.webp',
      'assets/images/handwork-02.webp'
    ],
    description: '(Sample specification) Sacred temple gold bridal ensemble woven with auspicious South Indian border patterns. Designed for brides who revere classical heritage elegance with royal gold tones.',
    fabric: 'Pure Gold Tissue Silk with Mulberry Weft',
    work: 'Solid Gold Zari Brocade & Hand-Tasseled Pallu Ends',
    details: [
      'All-over intricate micro-butta detailing',
      'Handcrafted zari tassels along the pallu finish',
      'Comes with embroidered raw silk blouse piece',
      'Custom blouse stitching with temple jewelry necklines available',
      'Estimated crafting timeframe: 4 weeks'
    ]
  },
  {
    id: 'hb-5',
    name: 'Samriddhi Heirloom Sister Silk Drapes',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹44,000',
    badge: 'Festive Bridal',
    images: [
      'assets/images/mosaic-02.webp',
      'assets/images/instagram-03.webp'
    ],
    description: '(Sample specification) Coordinated Kanchipuram silks created for bridal sisters and family entourages. Crafted in rich dual-tone jewel shades with gold zari border contrast.',
    fabric: '100% Pure Mulberry Silk & Fine Metallic Zari',
    work: 'Contrast Border Korvai Weaving with Floral Belts',
    details: [
      'Available in coordinating bridal party colorways',
      'Lightweight yet luxurious drape for day-long festive comfort',
      'Includes contrast blouse fabric with border work',
      'Custom group consultation and family styling support',
      'Estimated crafting timeframe: 2–3 weeks'
    ]
  },
  {
    id: 'hb-6',
    name: 'Devika Crimson Veil & Polki Bridal Set',
    category: 'hindu-bride',
    categoryName: 'Hindu Bride',
    price: '₹62,000',
    badge: 'New Edition',
    images: [
      'assets/images/mosaic-04.webp',
      'assets/images/hindu-bride-02.webp'
    ],
    description: '(Sample specification) Regal crimson bridal portrait ensemble featuring an ornate zardozi veil and matching pure silk lehenga saree drape tailored for evening muhurtham ceremonies.',
    fabric: 'Deep Crimson Silk Velvet & Pure Silk Dupion',
    work: 'Hand-Cutwork Border, Real Micro Seed Pearls & Dabka',
    details: [
      'Dimensional zardozi wirework with hand-embroidered scalloped borders',
      'Paired with lightweight ceremonial sheer head dupatta',
      'Complete personalized atelier trial and drape assistance in Kerala',
      'Custom family emblem monogramming option available',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },

  // ==========================================
  // CHRISTIAN BRIDE
  // ==========================================
  {
    id: 'cb-1',
    name: 'Seraphina French Lace Cathedral Veil Gown',
    category: 'christian-bride',
    categoryName: 'Christian Bride',
    price: '₹75,000',
    badge: 'Couture Signature',
    images: [
      'assets/images/christian-bride-01.webp',
      'assets/images/hero-05.webp',
      'assets/images/white-gown-02.webp'
    ],
    description: '(Sample specification) Architectural corseted bridal gown featuring hand-placed French Chantilly lace, hand-cut scallop train, and a sweeping raw silk veil custom-tailored to the bride’s height.',
    fabric: 'French Chantilly Lace, Silk Tulle & Duchess Satin',
    work: 'Hand-Appliquéd Lace, Micro Swarovski Crystals & Pearl Boning',
    details: [
      'Bespoke inner corset boning with built-in bust support and hook-and-eye closure',
      'Includes 3.5-meter cathedral-length scalloped lace veil with hair comb',
      'Scalloped hemline hand-cut along the lace motifs',
      'Multiple atelier fittings included at our studio in Changanassery',
      'Estimated crafting timeframe: 5–7 weeks'
    ]
  },
  {
    id: 'cb-2',
    name: 'Valerie Classic Duchess Satin Bridal Gown',
    category: 'christian-bride',
    categoryName: 'Christian Bride',
    price: '₹46,000',
    badge: 'Minimalist Grace',
    images: [
      'assets/images/christian-bride-02.webp',
      'assets/images/white-gown-01.webp'
    ],
    description: '(Sample specification) Heavy bridal duchess satin gown crafted with clean architectural lines, graceful boatneck, covered silk buttons down the illusion spine, and a delicate seed pearl belt.',
    fabric: 'Ultra-Luxe Heavy Duchess Satin & Silk Organza',
    work: 'Architectural Seaming, Hand-Covered Silk Buttons & Pearl Belt',
    details: [
      'Timeless clean silhouette tailored for church ceremony modesty',
      'Concealed deep side pockets seamlessly integrated into pleated skirt',
      'Structured chapel train that easily bustles for the evening reception',
      'Complimentary garment bag and personalized satin hanger',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'cb-3',
    name: 'Celeste Pearl-Work Organza Bridal Saree',
    category: 'christian-bride',
    categoryName: 'Christian Bride',
    price: '₹54,000',
    badge: 'Bespoke Saree',
    images: [
      'assets/images/christian-bride-03.webp',
      'assets/images/handwork-01.webp'
    ],
    description: '(Sample specification) Handcrafted Christian bridal saree in shimmering ivory organza, embellished with scalloped pearl borders, cutwork lace, and fine tone-on-tone floral thread embroidery.',
    fabric: 'Pure Shimmer Silk Organza & French Lace Borders',
    work: 'Hand Cutwork, Natural Seed Pearls & Silk Floss Embroidery',
    details: [
      'Scalloped perimeter hand-worked with lustrous ivory pearls',
      'Translucent drape tailored for church ceremony and reception lighting',
      'Includes custom corseted blouse piece with lace back styling',
      'Custom veil matching available upon consultation',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'cb-4',
    name: 'Evangeline Antique Gold Tissue Bridal Saree',
    category: 'christian-bride',
    categoryName: 'Christian Bride',
    price: '₹49,000',
    badge: 'Church Couture',
    images: [
      'assets/images/christian-bride-04.webp',
      'assets/images/handwork-03.webp'
    ],
    description: '(Sample specification) Luminous antique gold tissue bridal saree styled with intricate hand-embroidered pearl scallops and tailored corset blouse for stately bridal majesty on church steps.',
    fabric: 'Pure Metallic Tissue Silk & Gold Thread Weave',
    work: 'Hand-Embroidered Scallop Pearl Border with Muted Bullion Wire',
    details: [
      'Radiant soft metallic sheen that captures church ambient light',
      'Pre-stitched pleating option available upon request',
      'Includes heavily worked statement designer blouse fabric',
      'Crafted in limited numbers per bridal season',
      'Estimated crafting timeframe: 4 weeks'
    ]
  },

  // ==========================================
  // ENGAGEMENT WEAR
  // ==========================================
  {
    id: 'eng-1',
    name: 'Noor Blush Pink Organza Bridal Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹58,000',
    badge: 'Pastel Dream',
    images: [
      'assets/images/engagement-01.webp',
      'assets/images/hero-01.webp',
      'assets/images/engagement-02.webp'
    ],
    description: '(Sample specification) Ethereal blush pink ensemble adorned with champagne beads, floral threadwork, and sheer dupatta crafted for magical engagement and sangeet evenings.',
    fabric: 'Pure Silk Organza, Soft Net & Butter Silk Lining',
    work: 'Resham Floral Threadwork, Micro Pearls & Champagne Cutdana',
    details: [
      'Voluminous 16-kali kalidar lehenga skirt with canvas can-can flare',
      'Sweetheart neckline blouse with intricate hand-embroidered sleeves',
      'Lightweight dupatta with delicate four-sided scalloped borders',
      'Custom waistbelt (kamarbandh) included upon request',
      'Estimated crafting timeframe: 4–6 weeks'
    ]
  },
  {
    id: 'eng-2',
    name: 'Aurelia Floral Organza Balcony Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹59,000',
    badge: 'Romantic Glamour',
    images: [
      'assets/images/engagement-02.webp',
      'assets/images/engagement-01.webp'
    ],
    description: '(Sample specification) Romantic pastel lehenga handcrafted in sheer silk organza, adorned with hand-painted floral motifs and glistening champagne sequin handwork.',
    fabric: 'Hand-Painted Silk Organza & Shimmer Crepe',
    work: 'Watercolour Botanical Print with Hand Sequin Embellishment',
    details: [
      'Unique bespoke botanical artwork developed at M LOFT studio',
      'Delicate micro-pleated waistband with handcrafted latkan tassels',
      'Tailored blouse with sheer illusion back and pearl button fastening',
      'Ideal for sunset outdoor celebrations and palace venues',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'eng-3',
    name: 'Samira Fuchsia Zari Chevron Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹68,000',
    badge: 'Reception Glow',
    images: [
      'assets/images/engagement-03.webp',
      'assets/images/handwork-02.webp'
    ],
    description: '(Sample specification) Radiant fuchsia raw silk bridal lehenga lavishly woven with antique gold zari chevron patterns, paired with a heavily embroidered zardozi blouse and emerald jewel contrast.',
    fabric: 'Raw Silk & Fine Heritage Metallic Gold Weft',
    work: 'Chevron Zari Geometrics, Zardozi Floral Bodice & Tilla Lace',
    details: [
      'Geometric chevron pattern adds visual height and regal posture',
      'Heavy blouse with padded cups and custom deep-neckline finishes',
      'Two dupattas provided (one styling dupatta, one lightweight veil)',
      'Custom sizing tailored down to exact millimeter measurements',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },
  {
    id: 'eng-4',
    name: 'Althea Royal Emerald Velvet Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹64,000',
    badge: 'Winter Royale',
    images: [
      'assets/images/engagement-04.webp',
      'assets/images/featured-02.webp'
    ],
    description: '(Sample specification) Regal deep emerald velvet lehenga embroidered with antique dabka and tilla threadwork, designed for evening receptions and royal sangeet soirees.',
    fabric: 'Micro-Velvet & Tissue Organza Dupatta',
    work: 'Antique Dabka, Nakshi Wirework & Emerald Crystal Accents',
    details: [
      'Rich jewel tone with deep light absorption and luxurious drape',
      'Blouse features 3D organza floral shoulder appliqués',
      'Skirting lined with reinforced double can-can for grand ball flare',
      'Custom color adaptations available on request',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },
  {
    id: 'eng-5',
    name: 'Sitara Heirloom Ivory Silk Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹62,000',
    badge: 'Heirloom Luxe',
    images: [
      'assets/images/engagement-05.webp',
      'assets/images/white-gown-03.webp'
    ],
    description: '(Sample specification) Ivory heirloom silk lehenga designed with subtle vintage mirror reflection motifs, scalloped borders, and ethereal sheer veil draping.',
    fabric: 'Ivory Dupion Silk & Translucent Net',
    work: 'Fine Mirror Work Borders, Ivory Thread Embroidery & Zardozi',
    details: [
      'Subtle metallic shimmer designed for candlelit evening banquets',
      'Customized sleeve lengths (sleeveless, elbow, or full sleeve)',
      'Includes handcrafted fabric potli bag matching the lehenga embroidery',
      'Private styling consultation with Joel Jacob Mathew included',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'eng-6',
    name: 'Veda Antique Gold Twirling Lehenga',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹49,500',
    badge: 'Festive Twirl',
    images: [
      'assets/images/featured-01.webp',
      'assets/images/hero-02.webp'
    ],
    description: '(Sample specification) Shimmering gold and mustard lehenga silhouette engineered for effortless movement and graceful 360-degree twirling on the dance floor.',
    fabric: 'Tissue Georgette & Pure Gold Brocade Skirt',
    work: 'Sequinned Chevron Flare with Floral Wreath Appliques',
    details: [
      'Lightweight multi-tiered construction for effortless twirls',
      'Contrast maroon and emerald handwork accents along hem',
      'Includes custom-fitted blouse with deep round back and tie-up dori',
      'Dry-clean only with preservation instructions included',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'eng-7',
    name: 'Elysian Champagne Reception Couture Set',
    category: 'engagement',
    categoryName: 'Engagement Wear',
    price: '₹72,000',
    badge: 'Couple Edit',
    images: [
      'assets/images/featured-03.webp',
      'assets/images/hero-04.webp'
    ],
    description: '(Sample specification) Champagne reception gown ensemble tailored with champagne sequins, liquid silk draping, and coordinating groom styling palette.',
    fabric: 'Champagne Shimmer Tulle & Duchess Crepe',
    work: 'Vertical Bugle Bead Encrusting & Micro Crystal Cascade',
    details: [
      'Flattering elongated silhouette that drapes like liquid light',
      'Includes removable sheer train attachment for after-party dancing',
      'Coordinating groom sherwani / pocket square fabric swatches provided',
      'Private fitting room session at our flagship Changanassery atelier',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },

  // ==========================================
  // WHITE GOWNS
  // ==========================================
  {
    id: 'wg-1',
    name: 'Ophelia Beaded Tulle Fit-and-Flare Gown',
    category: 'white-gown',
    categoryName: 'White Gowns',
    price: '₹62,000',
    badge: 'Western Atelier',
    images: [
      'assets/images/white-gown-01.webp',
      'assets/images/christian-bride-02.webp'
    ],
    description: '(Sample specification) Graceful fit-and-flare white bridal gown rendered in micro-pleated tulle with hand-embroidered pearl vines along the neckline and corset back.',
    fabric: 'Micro-Pleated Silk Tulle & Soft Crepe Lining',
    work: 'Hand-Embroidered Pearl Vines & Crystal Bodice Applique',
    details: [
      'Structured internal corset with flexible spiral steel boning',
      'Lace-up back allowing adjustable micro-adjustments for perfect fit',
      'Built-in bra cups and hidden waist stay band for complete support',
      'Includes bridal garment storage box and heirloom veil',
      'Estimated crafting timeframe: 4–6 weeks'
    ]
  },
  {
    id: 'wg-2',
    name: 'Giselle Beaded Cathedral Cape Bridal Gown',
    category: 'white-gown',
    categoryName: 'White Gowns',
    price: '₹78,000',
    badge: 'Couture Cape',
    images: [
      'assets/images/white-gown-02.webp',
      'assets/images/white-gown-01.webp'
    ],
    description: '(Sample specification) Bespoke ivory bridal gown with sheer pearl-embellished cape, handcrafted floral lace corsetry, and majestic sweeping cathedral train.',
    fabric: 'Ivory Silk Organza, Beaded Lace & French Tulle Cape',
    work: 'Dimensional Cape Embroidery, Pearl Droplets & Floral Applique',
    details: [
      'Detachable 3-meter sheer cape with pearl encrusted shoulder epaulets',
      'Column gown silhouette underneath for dual looks during reception',
      'Hemline reinforced with horsehair braid for dramatic architectural flare',
      'Handcrafted under the direct direction of Joel Jacob Mathew',
      'Estimated crafting timeframe: 6–8 weeks'
    ]
  },
  {
    id: 'wg-3',
    name: 'Rosalind Pearl Tassel Champagne Silhouette Gown',
    category: 'white-gown',
    categoryName: 'White Gowns',
    price: '₹58,000',
    badge: 'Modern Runway',
    images: [
      'assets/images/white-gown-03.webp',
      'assets/images/best-seller-01.webp'
    ],
    description: '(Sample specification) Modern champagne silhouette gown crafted with architectural boning, delicate pearl fringe tassels, and a softly cascading fluid skirt.',
    fabric: 'Champagne Fluid Silk Crepe & Fine Netting',
    work: 'Hand-strung Pearl Fringe Tassels & Geometric Cutdana',
    details: [
      'Pearl fringe sways gracefully with every step and movement',
      'Plunging illusion neckline with ultra-fine skin-tone mesh',
      'Low open back with delicate horizontal pearl strap detail',
      'Personalized embroidery of wedding date inside bodice lining',
      'Estimated crafting timeframe: 4–5 weeks'
    ]
  },
  {
    id: 'wg-4',
    name: 'Adeline Emerald Jewel Collar Reception Gown',
    category: 'white-gown',
    categoryName: 'White Gowns',
    price: '₹52,000',
    badge: 'Cocktail Couture',
    images: [
      'assets/images/best-seller-01.webp',
      'assets/images/white-gown-03.webp'
    ],
    description: '(Sample specification) Sophisticated champagne reception gown featuring an architectural high neckline and structured bodice designed for formal evening celebrations.',
    fabric: 'Duchess Satin & Beaded Silk Tulle',
    work: 'Micro-Beaded Choker Collar & Fine Pleated Bodice',
    details: [
      'Designed to pair harmoniously with high-end emerald or diamond jewelry',
      'Flattering mermaid contour with concealed back zipper',
      'Tailored to individual bust, waist, and hip specifications',
      'Delivery with protective hanging suit bag and anti-wrinkle care',
      'Estimated crafting timeframe: 4 weeks'
    ]
  },

  // ==========================================
  // PAVITHRAPPATTU
  // ==========================================
  {
    id: 'pp-1',
    name: 'Avani Metallic Kasavu Pavithrappattu Saree',
    category: 'pavithrappattu',
    categoryName: 'Pavithrappattu',
    price: '₹36,000',
    badge: 'Kerala Heritage',
    images: [
      'assets/images/pavithrappattu-01.webp',
      'assets/images/pavithrappattu-02.webp'
    ],
    description: '(Sample specification) Sacred traditional pavithrappattu woven with pure golden zari yarns, preserving Kerala cultural sanctity while delivering refined contemporary drape aesthetic.',
    fabric: 'Authentic Pavithrappattu Silk & Traditional Kerala Kasavu',
    work: 'Pure Gold Zari Border Weave with Sacred Geometric Borders',
    details: [
      'Woven by master weavers upholding ancient temple weaving traditions',
      'Copper-tinted gold zari giving radiant natural warmth to Kerala skin tones',
      'Includes unstitched Kasavu blouse fabric with matching border strip',
      'Traditional Kerala Kasavu authentication certificate provided',
      'Estimated crafting timeframe: 2–3 weeks'
    ]
  },
  {
    id: 'pp-2',
    name: 'Vrinda Emerald & Maroon Heritage Pavithrappattu',
    category: 'pavithrappattu',
    categoryName: 'Pavithrappattu',
    price: '₹46,500',
    badge: 'Temple Weave',
    images: [
      'assets/images/pavithrappattu-02.webp',
      'assets/images/pavithrappattu-01.webp'
    ],
    description: '(Sample specification) Timeless Pavithrappattu silk featuring an emerald body and contrasting rich maroon pallu, woven with traditional South Indian golden temple motifs.',
    fabric: 'Heavy Weight Pavithrappattu Silk & Pure Metallic Zari',
    work: 'Two-Tone Contrast Weave with Intricate Temple Gopuram Borders',
    details: [
      'Dual-tone body and pallu interplay for magnificent ceremonial presence',
      'Authentic Kerala bridal silhouette favored for temple weddings',
      'Includes contrast rich maroon silk blouse piece with gold border',
      'Custom blouse neck embellishment available at our atelier',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'pp-3',
    name: 'Tharavadu Heritage Kasavu Wedding Ensemble',
    category: 'pavithrappattu',
    categoryName: 'Pavithrappattu',
    price: '₹42,000',
    badge: 'Traditional Weave',
    images: [
      'assets/images/mosaic-01.webp',
      'assets/images/instagram-01.webp'
    ],
    description: '(Sample specification) Traditional Kerala Kasavu wedding attire woven with heritage kasavu borders for couples celebrating classical ancestral rituals.',
    fabric: 'Organic Kerala Kasavu Cotton-Silk & Heritage Gold Zari',
    work: 'Handloom Shuttle Weave with Broad Temple Karas (Borders)',
    details: [
      'Authentic handloom texture with pristine off-white ivory body',
      'Broad golden kara (border) suitable for sacred ritual ceremonies',
      'Matching set available for both bride and groom attire',
      'Hand-washed and pre-conditioned for ultimate ceremonial softness',
      'Estimated crafting timeframe: 2–3 weeks'
    ]
  },
  {
    id: 'pp-4',
    name: 'Souparnika Handwoven Kerala Kasavu Drapes',
    category: 'pavithrappattu',
    categoryName: 'Pavithrappattu',
    price: '₹34,000',
    badge: 'Atelier Favorite',
    images: [
      'assets/images/instagram-01.webp',
      'assets/images/mosaic-01.webp'
    ],
    description: '(Sample specification) Refined handloom Kasavu sarees curated for festive bridesmaid entourages and Kerala temple celebrations with radiant gold borders.',
    fabric: 'Fine Count Handloom Kerala Silk & Kasavu Zari',
    work: 'Featherweight Handloom Drape with Delicate Metallic Weft',
    details: [
      'Breathable weave ideal for tropical Kerala climates',
      'Versatile drape suitable for traditional temple weddings and Onam festivities',
      'Includes matching contrast green or red blouse options upon consultation',
      'Available in set quantities for bridal entourages',
      'Estimated crafting timeframe: 2 weeks'
    ]
  },

  // ==========================================
  // ROJA COLLECTION
  // ==========================================
  {
    id: 'rj-1',
    name: 'Imperial Crimson Roja Scalloped Zardozi Saree',
    category: 'roja',
    categoryName: 'Roja Collection',
    price: '₹42,500',
    badge: 'Roja Signature',
    images: [
      'assets/images/roja-01.webp',
      'assets/images/roja-02.webp'
    ],
    description: '(Sample specification) Deep crimson red bridal silk embellished with intricate scalloped zardozi pallu and cutwork details from the coveted Roja capsule collection.',
    fabric: 'Signature Roja Crimson Silk & Heavy Zari Weft',
    work: 'Hand-Cut Scalloped Zardozi Pallu with Bullion Wire Embellishment',
    details: [
      'Signature shade of deep crimson exclusively dyed for M LOFT',
      'Hand-cut scalloped borders embroidered on wooden adda frames',
      'Includes heavily worked crimson silk blouse piece',
      'Comes packaged in signature velvet keepsake storage trunk',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'rj-2',
    name: 'Charulata Chartreuse & Plum Zari Festive Silk Saree',
    category: 'roja',
    categoryName: 'Roja Collection',
    price: '₹45,000',
    badge: 'Dual Tone Edit',
    images: [
      'assets/images/roja-02.webp',
      'assets/images/roja-01.webp'
    ],
    description: '(Sample specification) Exquisite chartreuse silk drape complemented by a plum purple border and delicate floral zari buttas, reflecting heirloom ceremonial royalty.',
    fabric: 'Dual-Tone Shot Silk (Chartreuse & Royal Plum)',
    work: 'Traditional Korvai Border with Zardozi Vine Motifs',
    details: [
      'Color-shifting shot silk that captures distinct tones in warm light',
      'Plum border finished with delicate antique gold floral wirework',
      'Coordinating deep plum unstitched blouse piece included',
      'Handloom authenticity certified with Silk Mark tag',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'rj-3',
    name: 'Gulzar Deep Red Velvet Embroidered Lehenga',
    category: 'roja',
    categoryName: 'Roja Collection',
    price: '₹65,000',
    badge: 'Roja Royale',
    images: [
      'assets/images/featured-02.webp',
      'assets/images/roja-01.webp'
    ],
    description: '(Sample specification) Model in deep red velvet and silk bridal lehenga with embroidered border and regal dupatta drape from the Roja winter capsule.',
    fabric: 'Plush Silk Velvet & Shimmer Organza Dupatta',
    work: 'Dense Kasab & Tilla Hand Embroidery with Resham Florals',
    details: [
      'Lavish velvet skirt with weighted hemline for regal posture',
      'Matching blouse with sweetheart front and intricate sleeve cuffs',
      'Translucent organza dupatta with scalloped zardozi lace',
      'Customized tailor fitting in Changanassery atelier',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },

  // ==========================================
  // ARTISANAL HANDWORK
  // ==========================================
  {
    id: 'hw-1',
    name: 'Dahlia Intricate Cutwork & Pearl Blouse Set',
    category: 'handwork',
    categoryName: 'Handwork Details',
    price: '₹32,000',
    badge: 'Artisanal Cutwork',
    images: [
      'assets/images/handwork-01.webp',
      'assets/images/handwork-03.webp'
    ],
    description: '(Sample specification) Architectural laser and hand cutwork blouse enriched with Swarovski seed pearls, kasab zardozi, and hand-tasseled back dori.',
    fabric: 'Raw Silk & Fine French Net Base',
    work: 'Laser & Hand Cutwork, Seed Pearls & Fine Kasab Wire',
    details: [
      'Over 80 hours of meticulous hand-needle embroidery per piece',
      'Reinforced cutwork edges that maintain shape across wears',
      'Custom back neckline cutouts tailored to client preference',
      'Pairs seamlessly with plain organza or heritage Kanchipuram sarees',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'hw-2',
    name: 'Marquise Bullion Wire Gold Zardozi Blouse Set',
    category: 'handwork',
    categoryName: 'Handwork Details',
    price: '₹28,500',
    badge: 'Hand Zardozi',
    images: [
      'assets/images/handwork-02.webp',
      'assets/images/hero-02.webp',
      'assets/images/handwork-03.webp'
    ],
    description: '(Sample specification) Intricate bullion wire zardozi embroidery with micro pearl enhancements on raw silk, meticulously handcrafted by our master artisans in Changanassery.',
    fabric: 'Pure Mulberry Raw Silk & Gold Bullion Wires',
    work: 'Authentic Adda Frame Zardozi, French Knots & Seed Pearls',
    details: [
      'Pure metal bullion wires that retain their rich luster over decades',
      'Tailored with premium inner lining and interlining for zero skin itch',
      'Padded bust cups and side zip fastening for a sculpted fit',
      'Color can be customized to match any client saree swatch',
      'Estimated crafting timeframe: 3 weeks'
    ]
  },
  {
    id: 'hw-3',
    name: 'Atelier Adda Handcrafted Zardozi Artistry',
    category: 'handwork',
    categoryName: 'Handwork Details',
    price: '₹34,500',
    badge: 'Master Craft',
    images: [
      'assets/images/handwork-03.webp',
      'assets/images/mosaic-03.webp'
    ],
    description: '(Sample specification) Signature artisan-crafted bridal blouse featuring dimensional zardozi wire embroidery, micro seed pearls, and hand-cut metallic borders.',
    fabric: 'Pure Silk Canvas & Metallic Gilt Threads',
    work: 'Master Adda Embroidery with Raised 3D Threadwork',
    details: [
      'Showcases the apex of traditional South Indian bridal embroidery',
      'Directly worked on heritage wooden adda embroidery frames',
      'Tailored exclusively to individual body measurements',
      'Custom wedding date or monogram embroidery option included',
      'Estimated crafting timeframe: 3–4 weeks'
    ]
  },
  {
    id: 'hw-4',
    name: 'Joel Jacob Mathew Atelier Bespoke Sketch & Drape',
    category: 'handwork',
    categoryName: 'Handwork Details',
    price: 'Price on Request',
    badge: 'Bespoke Atelier',
    images: [
      'assets/images/mosaic-03.webp',
      'assets/images/handwork-03.webp'
    ],
    description: '(Sample specification) Bespoke one-on-one bridal couture service led by designer Joel Jacob Mathew, from custom watercolor sketching to personalized fabric sourcing and fittings.',
    fabric: 'Curated Couture Silks, French Lace & Handloom Weaves',
    work: 'Custom Bespoke Development, Personalized Silhouette & Embroidery',
    details: [
      'Initial 1-on-1 design consultation with Joel Jacob Mathew',
      'Custom conceptual sketches and moodboard development',
      'Personalized fabric swatching and exclusive embroidery sampling',
      'Three progressive fitting sessions before final dispatch',
      'Lead time: 6–10 weeks (express booking available upon request)'
    ]
  },

  // ==========================================
  // M. LOFT LEGACY
  // ==========================================
  {
    id: 'lg-1',
    name: 'M. Loft Royal Heritage Crimson Embroidered Set',
    category: 'legacy',
    categoryName: 'M. Loft Legacy',
    price: '₹72,000',
    badge: 'Legacy Archive',
    images: [
      'assets/images/legacy-02.webp',
      'assets/images/roja-01.webp'
    ],
    description: '(Sample specification) Ornate crimson red bridal lehenga and embroidered dupatta drape embodying timeless aristocratic glamour with dual-tone antique gold zari and dense floral pallu artistry.',
    fabric: 'Heirloom Crimson Silk & Antique Gold Tissue',
    work: 'Royal Archive Zari Brocade & Hand-Appliqued Borders',
    details: [
      'Heritage archive design celebrating the inception of M LOFT couture',
      'Dual-tone antique zari creating deep dimensional shadows and shine',
      'Comes with commemorative engraved brass archival crest tag',
      'Private salon fitting session included at Changanassery flagship',
      'Estimated crafting timeframe: 5–6 weeks'
    ]
  },
  {
    id: 'lg-2',
    name: 'M. Loft Rajkanya Purple Silk & Antique Gold Saree',
    category: 'legacy',
    categoryName: 'M. Loft Legacy',
    price: '₹38,500',
    badge: 'Legacy Edition',
    images: [
      'assets/images/new-arrival-01.webp',
      'assets/images/handwork-02.webp'
    ],
    description: '(Sample specification) Model in rich purple silk saree with intricate gold stripes and choker border. Pure mulberry silk woven with antique gold zari motifs and intricate temple border work.',
    fabric: 'Pure Mulberry Silk & Antique Gold Zari Stripes',
    work: 'Fine Warp-Striped Gold Zari Weave with Temple Karas',
    details: [
      'Striking royal purple body woven with alternating gold pinstripes',
      'Ideal for reception evenings, engagement rituals, and festive galas',
      'Includes unstitched designer blouse piece with gold border accent',
      'Certified Silk Mark India authentication included',
      'Estimated crafting timeframe: 3 weeks'
    ]
  }
];

// Attach to window object for universal script access
if (typeof window !== 'undefined') {
  window.PRODUCTS = PRODUCTS;
  window.CATEGORIES = CATEGORIES;
}

// Support CommonJS if loaded in Node environment
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CATEGORIES, PRODUCTS };
}
