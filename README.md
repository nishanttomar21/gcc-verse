# GCCVerse — Institutional Intelligence Platform

> **Decoding India's Global Capability Centre (GCC) Ecosystem**  
> *Track · Analyse · Connect · Empower*

[![LinkedIn Follow](https://img.shields.io/badge/LinkedIn-GCCVerse-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/company/gccverse/)
[![Ecosystem Value](https://img.shields.io/badge/GCC_Market_Scale-$98.4B-067352?style=flat-square)](https://gccverse.in)
[![Centres Tracked](https://img.shields.io/badge/Active_Centres-2,117-D4A017?style=flat-square)](https://gccverse.in)
[![Design Standard](https://img.shields.io/badge/Design_System-UI/UX_Pro_Max-black?style=flat-square)](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

## 🏛️ Executive Summary

**GCCVerse** is the premier market intelligence platform tracking capital allocations, commercial real estate absorption, AI mandates, and C-suite leadership across India's **2,117+ Global Capability Centres (GCCs)**.

Published every Tuesday from Gurugram, India, GCCVerse arms multinational executives, sovereign investors, corporate real estate (CRE) leaders, and state policymakers with unvarnished data and verified intelligence.

---

## 📊 The Macro Baseline (FY2026)

- **2,117 Active Centres**: 3,728 individual delivery units across 24 Indian cities.
- **2.36 Million Talent**: Over 35.4% specialized in product engineering, deep tech, and Generative AI.
- **31.3 Million Sq Ft Leased**: GCCs drove **38.4%** of all Grade-A commercial real estate absorption in 2025 (*Source: JLL India*).
- **$98.4 Billion Revenue**: High-margin IP ownership outpacing traditional IT services (*Source: nasscom–Zinnov*).

---

## 🎨 Design System & Interactive Architecture

GCCVerse is built to the **UI/UX Pro Max** design intelligence standard, inspired by **The Financial Times**, **McKinsey Quarterly**, and **Stripe**:

- **Premium Light Editorial Theme**: Warm alabaster/ivory canvas (`#FAFAF7`) with crisp white elevated cards and delicate 1px hairline borders (`#DCD8CE`).
- **Full-Width Hero Image Carousel**: Cinematic 75vh full-viewport slideshow showcasing real Grade-A Indian tech corridors (Bengaluru, Hyderabad, Gurugram).
- **Smooth Number Counter Animations**: `IntersectionObserver`-triggered animated count-up for all macro numbers (`2,117`, `3,728`, `2.36M`, `$98.4B`) with mathematical `easeOutExpo` deceleration curves.
- **Scroll-Triggered Staggered Reveals**: Smooth cubic-bezier entry transitions across all editorial feature cards, pillar tiles, and river dispatches.
- **Interactive Capability Bar**: Dynamic progress fill animation displaying sectoral distributions (AI & Engineering 35.4%, Software 28.1%, BFSI 19.5%, Life Sciences 10.2%, Strategic Ops 6.8%).
- **Clean Hash-Free Navigation**: Clicking navigation items updates the browser address bar cleanly (`/stories`, `/pillars`, `/cities`, `/data`, `/advisory`) without unsightly `#` hash symbols, with smooth scrolling and full browser back/forward history support.
- **Accessibility & Craft**: 100% bespoke inline SVGs (zero emojis), visible `:focus-visible` rings, and full `prefers-reduced-motion` compliance.

---

## 📁 Repository Structure

```
gccverse/
├── index.html                    # Modular production build (references WebP assets)
├── gccverse_enterprise.html      # Standalone single-file edition (all images embedded as base64)
├── README.md                     # Documentation & project architecture
├── .gitignore                    # Git ignore file for macOS/editor/build artifacts
├── build.py                      # Build script to regenerate modular & standalone files
└── assets/
    ├── images/                   # 13 losslessly compressed WebP images (~2.8 MB total)
    │   ├── gcc_campus_exterior.webp
    │   ├── gcc_cities_clusters.webp
    │   ├── gcc_city_bengaluru.webp
    │   ├── gcc_city_delhincr.webp
    │   ├── gcc_city_hyderabad.webp
    │   ├── gcc_data_intelligence.webp
    │   ├── gcc_executive_board.webp
    │   ├── gcc_leadership_talent.webp
    │   ├── gcc_news_developments.webp
    │   ├── gcc_office_space.webp
    │   ├── gcc_policy_investment.webp
    │   ├── gcc_real_estate.webp
    │   └── gcc_talent_hub.webp
    └── images_data.json          # Pre-encoded base64 data URIs dictionary
```

---

## 🚀 Quick Start & Deployment

### Local Development
To preview the website locally:

```bash
# Clone the repository
git clone https://github.com/nishanttomar21/gcc-verse.git
cd gcc-verse

# Run with any local HTTP server
python3 -m http.server 8000
# Open http://localhost:8000 in your browser
```

Or simply double-click `gccverse_enterprise.html` to run offline anywhere with zero dependencies.

### Deploying to GitHub Pages
1. In your GitHub repository settings, navigate to **Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose the `main` branch and `/ (root)` folder.
4. Your site will be live at `https://nishanttomar21.github.io/gcc-verse/`.

---

## 📜 Citations & Sources

- **nasscom–Zinnov**: *India GCC Landscape Benchmark Report, FY2026*
- **JLL India**: *Commercial Real Estate Review & Office Leasing Audit, 2025*
- **GCCVerse Research Desk**: *Primary enterprise disclosures & state IT ministry filings*

---

© 2026 GCCVerse. All rights reserved. Published weekly from Gurugram 122001, Haryana, India.
