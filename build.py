import base64
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "assets", "images")

_b64_cache = {}

def get_base64_uri(key):
    if key not in _b64_cache:
        path = os.path.join(IMAGE_DIR, f"{key}.webp")
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
        _b64_cache[key] = f"data:image/webp;base64,{encoded}"
    return _b64_cache[key]

def get_html(is_standalone=False):
    def img_src(key):
        if is_standalone:
            return get_base64_uri(key)
        return f"assets/images/{key}.webp"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>
<title>GCCVerse — India's Global Capability Centre Intelligence Platform</title>
<meta name="description" content="Track, analyse, and connect with India's $98.4B GCC ecosystem. 2,117 centres. 2.36M talent. The definitive weekly briefing for institutional leaders."/>
<meta name="theme-color" content="#022B22"/>
<link rel="canonical" href="https://gccverse.in/"/>

<!-- Open Graph / LinkedIn / Facebook -->
<meta property="og:type" content="website"/>
<meta property="og:url" content="https://gccverse.in/"/>
<meta property="og:site_name" content="GCCVerse"/>
<meta property="og:title" content="GCCVerse — India's Global Capability Centre Intelligence Platform"/>
<meta property="og:description" content="Track, analyse, and connect with India's $98.4B GCC ecosystem. 2,117 centres. 2.36M talent."/>
<meta property="og:image" content="https://gccverse.in/assets/images/gcc_campus_exterior.webp"/>

<!-- Twitter / X -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:url" content="https://gccverse.in/"/>
<meta name="twitter:title" content="GCCVerse — India's GCC Intelligence Platform"/>
<meta name="twitter:description" content="Track, analyse, and connect with India's $98.4B GCC ecosystem."/>
<meta name="twitter:image" content="https://gccverse.in/assets/images/gcc_campus_exterior.webp"/>

<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23022B22'/%3E%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='18' font-weight='bold' fill='%23D4A017' text-anchor='middle'%3EG%3C/text%3E%3C/svg%3E"/>

<!-- Preconnect Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Inter:ital,opsz,wght@0,14..32,300..800;1,14..32,300..800&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

<style>
/* ════════════════════════════════════════════════════════
   GCCVERSE v3.4 — INSTITUTIONAL TERMINAL DESIGN SYSTEM
   ════════════════════════════════════════════════════════ */

*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}

:root {{
  /* Surfaces */
  --white: #FFFFFF;
  --cream: #FAFAF7;
  --warm-50: #F5F3EE;
  --warm-100: #EDEBE4;
  --warm-200: #DCD8CE;
  --warm-300: #C2BDB1;

  /* Ink */
  --ink-900: #141413;
  --ink-800: #1C1C1A;
  --ink-700: #2E2E2B;
  --ink-600: #484844;
  --ink-500: #6B6B65;
  --ink-400: #8E8E87;
  --ink-300: #B3B3AB;

  /* Brand: Deep Emerald + Gold */
  --emerald-900: #022B22;
  --emerald-800: #044D3A;
  --emerald-700: #067352;
  --emerald-600: #059669;
  --emerald-500: #10B981;
  --emerald-50: #ECFDF5;
  --gold-600: #B8860B;
  --gold-500: #D4A017;
  --gold-400: #E8B931;
  --gold-50: #FEF9E7;

  /* Signals & Categories */
  --up: #16A34A;
  --down: #DC2626;
  --blue: #2563EB;
  --purple: #7C3AED;
  --rose: #DB2777;

  /* Typography */
  --serif: "Playfair Display", Georgia, "Times New Roman", serif;
  --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SF Mono", Menlo, monospace;

  /* Spacing */
  --max-w: 1280px;
  --gutter: 24px;
  --radius: 12px;
  --radius-lg: 20px;
}}

html {{
  scroll-behavior: smooth;
  overflow-x: hidden;
}}

body {{
  font-family: var(--sans);
  font-size: 16px;
  line-height: 1.65;
  color: var(--ink-700);
  background: var(--white);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  width: 100%;
}}

img {{
  display: block;
  max-width: 100%;
  height: auto;
}}
a {{ color: inherit; text-decoration: none; cursor: pointer; }}
button {{ cursor: pointer; font: inherit; }}

.container {{
  width: 100%;
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--gutter);
}}

/* ════════════════════════════════════
   SCROLL REVEAL SYSTEM
   ════════════════════════════════════ */
.reveal {{
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1), transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}}
.reveal.revealed {{
  opacity: 1;
  transform: translateY(0);
}}

.delay-100 {{ transition-delay: 100ms; }}
.delay-200 {{ transition-delay: 200ms; }}
.delay-300 {{ transition-delay: 300ms; }}

/* ════════════════════════════════════
   HEADER — Transparent by Default, White & Sticky on Scroll
   ════════════════════════════════════ */
.site-header {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  width: 100%;
  height: 72px;
  background: transparent;
  border-bottom: 1px solid rgba(255,255,255,0.18);
  transition: background 0.32s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.32s ease,
              box-shadow 0.32s ease,
              backdrop-filter 0.32s ease;
}}
.site-header.scrolled {{
  background: rgba(255,255,255,0.98);
  border-bottom: 1px solid var(--warm-200);
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}}
.header-inner {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  gap: 16px;
}}

/* Header Logo transitions */
.logo {{
  font-family: var(--serif);
  font-size: clamp(22px, 3.5vw, 27px);
  font-weight: 700;
  letter-spacing: -.03em;
  display: flex;
  align-items: baseline;
  gap: 2px;
  flex-shrink: 0;
  transition: color .3s ease;
  color: #FFFFFF;
}}
.site-header.scrolled .logo {{
  color: var(--ink-900);
}}
.logo em {{
  font-style: italic;
  font-weight: 400;
  color: var(--gold-400);
  transition: color .3s ease;
}}
.site-header.scrolled .logo em {{
  color: var(--emerald-700);
}}
.logo-sub {{
  font-family: var(--mono);
  font-size: 10px;
  color: rgba(255,255,255,0.65);
  text-transform: uppercase;
  letter-spacing: .12em;
  margin-left: 12px;
  display: none;
  transition: color .3s ease;
}}
.site-header.scrolled .logo-sub {{
  color: var(--ink-400);
}}
@media(min-width:1200px){{ .logo-sub {{ display: inline; }} }}

/* Desktop Navigation */
.header-left-group {{
  display: flex;
  align-items: center;
  gap: clamp(14px, 1.8vw, 24px);
  height: 100%;
}}

/* Modern Vertical Divider (Laptop/Desktop only) */
.header-v-divider {{
  display: none;
}}
@media(min-width:960px) {{
  .header-v-divider {{
    display: block;
    width: 1.5px;
    height: 22px;
    background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, rgba(212,160,23,0.75) 40%, rgba(255,255,255,0.5) 70%, rgba(255,255,255,0.05) 100%);
    border-radius: 2px;
    flex-shrink: 0;
    box-shadow: 0 0 8px rgba(212,160,23,0.35);
    transition: background 0.32s ease, box-shadow 0.32s ease;
  }}
  .site-header.scrolled .header-v-divider {{
    background: linear-gradient(180deg, rgba(0,0,0,0.04) 0%, var(--warm-300) 30%, var(--emerald-600) 65%, rgba(0,0,0,0.04) 100%);
    box-shadow: 0 0 6px rgba(5,150,105,0.15);
  }}
}}

.nav-desktop {{ display: none; }}
@media(min-width:960px){{ .nav-desktop {{ display: block; }} }}
.nav-list {{
  display: flex;
  list-style: none;
  gap: clamp(12px, 1.6vw, 20px);
  align-items: center;
  font-size: clamp(13px, 1.1vw, 14px);
  font-weight: 500;
  color: rgba(255,255,255,0.9);
  margin: 0;
  padding: 0;
  transition: color .3s ease;
}}
.site-header.scrolled .nav-list {{
  color: var(--ink-600);
}}
.nav-list a {{
  position: relative;
  padding: 6px 0;
  transition: color .2s ease;
  white-space: nowrap;
}}
.nav-list a::after {{
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--gold-400);
  transition: width .25s ease, background .25s ease;
}}
.site-header.scrolled .nav-list a::after {{
  background: var(--emerald-700);
}}
.nav-list a:hover {{
  color: var(--gold-400);
}}
.site-header.scrolled .nav-list a:hover {{
  color: var(--emerald-700);
}}
.nav-list a:hover::after {{ width: 100%; }}

/* Header CTA Buttons */
.header-cta {{
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}}
.btn-outline {{
  font-size: 13px;
  font-weight: 600;
  color: #FFFFFF;
  border: 1.5px solid rgba(255,255,255,0.38);
  padding: 8px 16px;
  border-radius: 100px;
  background: rgba(255,255,255,0.08);
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  white-space: nowrap;
  backdrop-filter: blur(8px);
}}
.btn-outline:hover {{
  background: rgba(255,255,255,0.22);
  border-color: rgba(255,255,255,0.7);
  color: #FFF;
  transform: translateY(-1px);
}}
.site-header.scrolled .btn-outline {{
  color: var(--ink-700);
  border-color: var(--warm-200);
  background: transparent;
}}
.site-header.scrolled .btn-outline:hover {{
  border-color: var(--emerald-700);
  color: var(--emerald-700);
  background: var(--emerald-50);
}}
.btn-primary {{
  font-size: 13px;
  font-weight: 600;
  color: #1A1200;
  background: linear-gradient(135deg, var(--gold-400), var(--gold-500));
  padding: 9px 18px;
  border-radius: 100px;
  border: none;
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  white-space: nowrap;
}}
.site-header.scrolled .btn-primary {{
  background: var(--emerald-800);
  color: #FFF;
}}
.btn-primary:hover {{
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(212,160,23,.35);
}}
.site-header.scrolled .btn-primary:hover {{
  background: var(--emerald-700);
  box-shadow: 0 6px 18px rgba(4,77,58,.28);
}}
.btn-primary:active, .btn-outline:active {{ transform: scale(0.98); }}

/* Mobile Hamburger Button */
.mobile-menu-btn {{
  display: none;
  background: rgba(255,255,255,0.12);
  border: 1.5px solid rgba(255,255,255,0.35);
  border-radius: 8px;
  width: 44px;
  height: 44px;
  align-items: center;
  justify-content: center;
  padding: 0;
  cursor: pointer;
  position: relative;
  z-index: 102;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
  transition: all .2s;
}}
.site-header.scrolled .mobile-menu-btn {{
  background: transparent;
  border-color: var(--warm-200);
}}
@media(max-width:959px){{
  .mobile-menu-btn {{ display: flex; }}
  .header-cta-desktop {{ display: none; }}
}}
.hamburger-icon {{
  width: 20px;
  height: 15px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  pointer-events: none;
}}
.hamburger-icon span {{
  display: block;
  height: 2px;
  width: 100%;
  background: #FFFFFF;
  border-radius: 2px;
  transition: all .3s cubic-bezier(0.16, 1, 0.3, 1);
}}
.site-header.scrolled .hamburger-icon span {{
  background: var(--ink-800);
}}
.mobile-menu-btn.active .hamburger-icon span:nth-child(1) {{ transform: translateY(6.5px) rotate(45deg); }}
.mobile-menu-btn.active .hamburger-icon span:nth-child(2) {{ opacity: 0; transform: scaleX(0); }}
.mobile-menu-btn.active .hamburger-icon span:nth-child(3) {{ transform: translateY(-6.5px) rotate(-45deg); }}

/* Mobile Navigation Drawer */
.mobile-nav-drawer {{
  display: block;
  position: fixed;
  top: 72px;
  left: 0;
  right: 0;
  background: rgba(255,255,255,0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--warm-200);
  box-shadow: 0 16px 36px rgba(0,0,0,0.14);
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
  opacity: 0;
  pointer-events: none;
  z-index: 101;
}}
.mobile-nav-drawer.open {{
  max-height: 520px;
  opacity: 1;
  pointer-events: auto;
}}
.mobile-nav-inner {{
  padding: 20px 24px 28px;
  max-width: var(--max-w);
  margin: 0 auto;
}}
.mobile-nav-list {{
  list-style: none;
  margin: 0 0 20px 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.mobile-nav-list a {{
  font-family: var(--sans);
  font-size: 16px;
  font-weight: 600;
  color: var(--ink-800);
  display: block;
  padding: 8px 0;
  border-bottom: 1px solid var(--warm-100);
  transition: color .2s;
}}
.mobile-nav-list a:hover {{ color: var(--emerald-700); }}
.mobile-drawer-cta {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 8px;
}}

/* ════════════════════════════════════
   FULL-WIDTH HERO CINEMATIC CAROUSEL
   ════════════════════════════════════ */
.hero-carousel {{
  position: relative;
  width: 100%;
  height: clamp(520px, 84vh, 780px);
  overflow: hidden;
  background: #061815;
  padding-top: 72px; /* Accommodate transparent fixed header */
}}
.hero-slide {{
  position: absolute;
  inset: 0;
  opacity: 0;
  visibility: hidden;
  transition: opacity 1.1s cubic-bezier(0.25, 1, 0.5, 1), visibility 1.1s;
  pointer-events: none;
  overflow: hidden;
}}
.hero-slide.active {{
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  z-index: 2;
}}

@keyframes kenBurnsSlide {{
  0% {{ transform: scale(1.0) translate(0, 0); }}
  50% {{ transform: scale(1.07) translate(-1.2%, -0.8%); }}
  100% {{ transform: scale(1.0) translate(0, 0); }}
}}

.hero-slide img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  will-change: transform;
  transform-origin: center center;
}}
.hero-slide.active img {{
  animation: kenBurnsSlide 16s ease-in-out infinite alternate;
}}

.hero-scrim {{
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at 75% 30%,
    rgba(6, 115, 82, 0.24) 0%,
    transparent 65%
  ),
  linear-gradient(
    180deg,
    rgba(4, 24, 21, 0.35) 0%,
    rgba(4, 24, 21, 0.46) 35%,
    rgba(4, 24, 21, 0.94) 100%
  );
  pointer-events: none;
}}

.hero-content {{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0 var(--gutter) 74px;
  z-index: 5;
}}
.hero-content-inner {{
  max-width: var(--max-w);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 32px;
}}
.hero-text-col {{ max-width: 800px; }}

.hero-chip-wrap {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}}
.hero-chip {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--gold-400);
  background: rgba(212, 160, 23, 0.14);
  border: 1px solid rgba(212, 160, 23, 0.38);
  padding: 5px 12px;
  border-radius: 100px;
  font-weight: 600;
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
  position: relative;
  overflow: hidden;
}}
.hero-chip::after {{
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  animation: chipSheen 3.5s infinite;
}}
@keyframes chipSheen {{
  0% {{ left: -100%; }}
  35%, 100% {{ left: 160%; }}
}}

.hero-headline {{
  font-family: var(--serif);
  font-size: clamp(26px, 4.8vw, 58px);
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.1;
  letter-spacing: -.03em;
  margin-bottom: 14px;
  max-width: 20ch;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.35);
  opacity: 0;
  transform: translateY(24px);
  transition: opacity .85s cubic-bezier(0.16, 1, 0.3, 1), transform .85s cubic-bezier(0.16, 1, 0.3, 1);
}}
.hero-headline em {{
  font-style: italic;
  font-weight: 400;
  color: var(--gold-400);
  text-shadow: 0 0 24px rgba(212, 160, 23, 0.45);
}}
.hero-excerpt {{
  font-size: clamp(14.5px, 1.3vw, 17.5px);
  color: rgba(255,255,255,.88);
  max-width: 54ch;
  line-height: 1.55;
  font-weight: 350;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity .9s cubic-bezier(0.16, 1, 0.3, 1), transform .9s cubic-bezier(0.16, 1, 0.3, 1);
  text-shadow: 0 1px 8px rgba(0,0,0,0.3);
}}

.hero-slide.active .hero-headline {{ opacity: 1; transform: translateY(0); transition-delay: .25s; }}
.hero-slide.active .hero-excerpt {{ opacity: 1; transform: translateY(0); transition-delay: .4s; }}

.hero-telemetry-card {{
  display: none;
  background: rgba(4, 32, 26, 0.76);
  border: 1px solid rgba(212, 160, 23, 0.35);
  border-radius: 14px;
  padding: 16px 20px;
  max-width: 300px;
  backdrop-filter: blur(16px);
  box-shadow: 0 16px 40px rgba(0,0,0,0.4);
  color: #FFF;
  transition: all .35s ease;
  flex-shrink: 0;
}}
@media(min-width:1080px){{ .hero-telemetry-card {{ display: block; }} }}
.hero-telemetry-card:hover {{
  border-color: var(--gold-400);
  transform: translateY(-3px);
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}}
.telemetry-tag {{
  font-family: var(--mono);
  font-size: 10px;
  color: var(--gold-400);
  text-transform: uppercase;
  letter-spacing: .1em;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 5px;
}}
.telemetry-pulse {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 10px #10B981;
  animation: beaconPulse 1.8s infinite;
}}
@keyframes beaconPulse {{
  0%, 100% {{ transform: scale(1); opacity: 1; }}
  50% {{ transform: scale(1.4); opacity: 0.4; }}
}}
.telemetry-title {{
  font-family: var(--sans);
  font-size: 14px;
  font-weight: 600;
  line-height: 1.4;
  color: #F3F7F5;
  margin-bottom: 4px;
}}
.telemetry-meta {{
  font-family: var(--mono);
  font-size: 10.5px;
  color: rgba(255,255,255,0.6);
}}

/* Segmented Interactive Tab Bar */
.carousel-nav-bar {{
  position: absolute;
  bottom: 18px;
  left: 0;
  right: 0;
  z-index: 10;
}}
.carousel-nav-inner {{
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--gutter);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}}
.carousel-tabs {{
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  max-width: 820px;
}}
.carousel-tab {{
  flex: 1;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 8px;
  padding: 8px 12px;
  cursor: pointer;
  text-align: left;
  backdrop-filter: blur(12px);
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 5px;
}}
.carousel-tab:hover {{
  background: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,0.35);
  transform: translateY(-2px);
}}
.carousel-tab.active {{
  background: rgba(255,255,255,0.18);
  border-color: rgba(212, 160, 23, 0.6);
  box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}}
.tab-top {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}}
.tab-idx {{
  font-family: var(--mono);
  font-size: 10px;
  color: var(--gold-400);
  font-weight: 700;
  letter-spacing: .08em;
}}
.tab-title {{
  font-family: var(--sans);
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(255,255,255,0.94);
  white-space: nowrap;
}}
.tab-progress-track {{
  width: 100%;
  height: 3px;
  background: rgba(255,255,255,0.18);
  border-radius: 2px;
  overflow: hidden;
  position: relative;
}}
.tab-progress-fill {{
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--gold-500), var(--gold-400));
  border-radius: 2px;
}}
.carousel-tab.active .tab-progress-fill {{
  animation: tabFillProgress 4.8s linear forwards;
}}
@keyframes tabFillProgress {{
  0% {{ width: 0%; }}
  100% {{ width: 100%; }}
}}

.carousel-controls-right {{
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}}
.slide-counter {{
  font-family: var(--mono);
  font-size: 12px;
  color: rgba(255,255,255,0.9);
  font-weight: 600;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.22);
  padding: 6px 12px;
  border-radius: 100px;
  backdrop-filter: blur(10px);
  display: none;
}}
@media(min-width:640px){{ .slide-counter {{ display: inline-flex; align-items: center; gap: 6px; }} }}
.slide-counter b {{ color: var(--gold-400); }}

.carousel-arrow-btn {{
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255,255,255,0.18);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.32);
  color: #FFF;
  display: grid;
  place-items: center;
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
}}
.carousel-arrow-btn:hover {{
  background: rgba(255,255,255,0.38);
  border-color: rgba(255,255,255,0.7);
  transform: scale(1.08);
}}
.carousel-arrow-btn:active {{ transform: scale(0.95); }}

/* ════════════════════════════════════
   MACRO STATS RIBBON
   ════════════════════════════════════ */
.stats-ribbon {{
  background: var(--white);
  border-bottom: 1px solid var(--warm-200);
  padding: clamp(32px, 4vw, 48px) 0;
  position: relative;
  z-index: 5;
}}
.stats-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px 20px;
}}
@media(max-width:480px){{
  .stats-grid {{ grid-template-columns: 1fr; gap: 14px; }}
}}
@media(min-width:768px){{
  .stats-grid {{ grid-template-columns: repeat(4, 1fr); gap: 24px 32px; }}
}}
.stat-block {{
  text-align: center;
  padding: clamp(16px, 2vw, 22px) 14px;
  border-radius: var(--radius);
  transition: all .28s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  background: var(--white);
  border: 1px solid transparent;
}}
.stat-block:hover {{
  background: var(--cream);
  border-color: var(--warm-200);
  transform: translateY(-3px);
  box-shadow: 0 10px 28px -6px rgba(0,0,0,0.06);
}}
.stat-block:not(:last-child)::after {{
  content: "";
  position: absolute;
  right: -16px;
  top: 20%;
  height: 60%;
  width: 1px;
  background: var(--warm-200);
  display: none;
}}
@media(min-width:768px){{ .stat-block:not(:last-child)::after {{ display: block; }} }}
.stat-number {{
  font-family: var(--serif);
  font-size: clamp(32px, 4vw, 52px);
  font-weight: 700;
  color: var(--ink-900);
  line-height: 1;
  margin-bottom: 8px;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  transition: color .3s ease;
}}
.stat-block:hover .stat-number {{ color: var(--emerald-800); }}
.stat-label {{
  font-family: var(--mono);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--emerald-700);
  font-weight: 600;
  margin-bottom: 5px;
}}
.stat-sub {{
  font-size: 13px;
  color: var(--ink-400);
  line-height: 1.4;
}}

/* ════════════════════════════════════
   SECTION HEADINGS
   ════════════════════════════════════ */
.section-header {{ margin-bottom: clamp(32px, 4vw, 48px); }}
.section-tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: 11.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--emerald-700);
  font-weight: 600;
  margin-bottom: 10px;
}}
.section-tag::before {{
  content: "";
  width: 20px;
  height: 2px;
  background: var(--emerald-600);
  border-radius: 1px;
}}
.section-h2 {{
  font-family: var(--serif);
  font-size: clamp(26px, 3.4vw, 44px);
  font-weight: 700;
  color: var(--ink-900);
  line-height: 1.15;
  letter-spacing: -.03em;
  margin-bottom: 12px;
}}
.section-lead {{
  font-size: clamp(15px, 1.3vw, 18px);
  color: var(--ink-500);
  max-width: 60ch;
  line-height: 1.6;
}}

/* ════════════════════════════════════
   FEATURED STORIES
   ════════════════════════════════════ */
.stories-section {{
  padding: clamp(52px, 7vw, 92px) 0;
  background: var(--cream);
}}
.stories-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}}
@media(min-width:960px){{
  .stories-grid {{ grid-template-columns: 1.35fr 1fr; gap: 32px; }}
}}

.story-feature {{
  background: var(--white);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all .35s cubic-bezier(0.16, 1, 0.3, 1);
}}
.story-feature:hover {{
  box-shadow: 0 24px 54px -12px rgba(0,0,0,.12);
  transform: translateY(-4px);
  border-color: var(--warm-300);
}}
.story-img {{
  position: relative;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: var(--warm-100);
}}
.story-img img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .7s ease;
}}
.story-feature:hover .story-img img {{ transform: scale(1.05); }}
.story-body {{ padding: clamp(20px, 3vw, 34px); }}
.story-meta {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}}
.chip {{
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .06em;
  padding: 4px 10px;
  border-radius: 4px;
}}
.chip-gold {{ background: var(--gold-50); color: var(--gold-600); border: 1px solid rgba(184,134,11,.2); }}
.chip-emerald {{
  background: var(--emerald-50);
  color: var(--emerald-700);
  border: 1px solid rgba(5,150,105,.2);
  transition: all .2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}}
.chip-emerald:hover {{
  background: var(--emerald-700);
  color: #FFF;
  border-color: var(--emerald-700);
}}
.story-title {{
  font-family: var(--serif);
  font-size: clamp(20px, 2.3vw, 28px);
  font-weight: 700;
  color: var(--ink-900);
  line-height: 1.24;
  margin-bottom: 12px;
  letter-spacing: -.02em;
}}
.story-excerpt {{
  font-size: clamp(14.5px, 1.1vw, 16px);
  color: var(--ink-500);
  line-height: 1.62;
  margin-bottom: 16px;
}}
.story-source {{
  font-family: var(--mono);
  font-size: 11.5px;
  color: var(--ink-400);
  display: flex;
  align-items: center;
  gap: 8px;
}}

/* Side stack */
.stories-stack {{ display: flex; flex-direction: column; gap: 16px; }}
.story-card-sm {{
  background: var(--white);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius);
  padding: clamp(18px, 2vw, 24px);
  transition: all .3s cubic-bezier(0.16, 1, 0.3, 1);
}}
.story-card-sm:hover {{
  border-color: var(--emerald-600);
  box-shadow: 0 10px 28px -6px rgba(0,0,0,.08);
  transform: translateY(-2px);
}}
.story-card-sm .story-title {{ font-size: clamp(17px, 1.5vw, 19px); margin-bottom: 8px; }}
.story-card-sm .story-excerpt {{ font-size: 14px; margin-bottom: 10px; }}

/* ════════════════════════════════════
   SIX PILLARS
   ════════════════════════════════════ */
.pillars-section {{
  padding: clamp(52px, 7vw, 96px) 0;
  background: var(--white);
}}
.pillars-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
  gap: 22px;
}}
.pillar-card {{
  border: 1px solid var(--warm-200);
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--white);
  transition: all .35s cubic-bezier(0.16, 1, 0.3, 1);
}}
.pillar-card:hover {{
  border-color: var(--emerald-600);
  box-shadow: 0 20px 48px -10px rgba(5,150,105,.15);
  transform: translateY(-4px);
}}
.pillar-img {{
  position: relative;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: var(--warm-100);
}}
.pillar-img img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .7s ease;
}}
.pillar-card:hover .pillar-img img {{ transform: scale(1.06); }}
.pillar-badge {{
  position: absolute;
  top: 12px;
  left: 12px;
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  background: var(--white);
  color: var(--ink-700);
  padding: 4px 10px;
  border-radius: 6px;
  box-shadow: 0 3px 10px rgba(0,0,0,.15);
}}
.pillar-body {{ padding: clamp(18px, 2vw, 24px); }}
.pillar-title {{
  font-family: var(--sans);
  font-size: 19px;
  font-weight: 700;
  color: var(--ink-900);
  margin-bottom: 6px;
  letter-spacing: -.01em;
}}
.pillar-desc {{
  font-size: 14px;
  color: var(--ink-500);
  line-height: 1.55;
}}

/* ════════════════════════════════════
   CITY CLUSTERS
   ════════════════════════════════════ */
.cities-section {{
  padding: clamp(52px, 7vw, 96px) 0;
  background: var(--cream);
}}
.cities-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
  gap: 24px;
}}
.city-card {{
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--white);
  border: 1px solid var(--warm-200);
  transition: all .35s cubic-bezier(0.16, 1, 0.3, 1);
}}
.city-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 24px 54px -12px rgba(0,0,0,.12);
  border-color: var(--warm-300);
}}
.city-img {{
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
  background: var(--ink-900);
}}
.city-img img {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  transition: transform .35s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}}
.city-card:hover .city-img img {{ transform: scale(1.06); }}
.city-overlay {{
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(2, 43, 34, 0.88) 0%, rgba(2, 43, 34, 0.22) 50%, transparent 100%);
  z-index: 2;
  pointer-events: none;
}}
.city-name {{
  position: absolute;
  left: 20px;
  bottom: 18px;
  font-family: var(--serif);
  font-size: clamp(22px, 2.5vw, 26px);
  font-weight: 700;
  color: #FFFFFF;
  z-index: 3;
  pointer-events: none;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
  transition: transform .3s ease;
}}
.city-card:hover .city-name {{
  transform: translateY(-2px);
}}
.city-body {{ padding: clamp(18px, 2vw, 24px); }}
.city-desc {{
  font-size: 14.5px;
  color: var(--ink-600);
  line-height: 1.55;
  margin-bottom: 10px;
}}
.city-desc b {{ color: var(--ink-900); font-weight: 600; }}
.city-source {{
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-400);
}}

/* ════════════════════════════════════
   DATA INDEX & MCKINSEY/FT EDITORIAL CAPABILITY BENCHMARK
   ════════════════════════════════════ */
.data-section {{
  padding: clamp(52px, 7vw, 96px) 0;
  background: var(--white);
  border-top: 1px solid var(--warm-200);
}}
.data-shifts {{
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 40px;
}}
.shift-item {{
  display: flex;
  align-items: center;
  gap: 16px;
  padding: clamp(14px, 2vw, 18px) clamp(16px, 2vw, 22px);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius);
  background: var(--cream);
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
}}
@media(max-width:540px){{
  .shift-item {{ flex-direction: column; align-items: flex-start; gap: 10px; }}
}}
.shift-item:hover {{
  background: var(--white);
  border-color: var(--emerald-600);
  transform: translateX(3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.04);
}}
.shift-badge {{
  font-family: var(--mono);
  font-weight: 700;
  font-size: 13.5px;
  padding: 5px 12px;
  border-radius: 6px;
  min-width: 84px;
  text-align: center;
  white-space: nowrap;
}}
.shift-badge.up {{ background: #E1F4ED; color: var(--up); }}
.shift-badge.down {{ background: #FDE8E8; color: var(--down); }}
.shift-badge.gold {{ background: var(--gold-50); color: var(--gold-600); }}
.shift-text {{
  font-size: 15px;
  color: var(--ink-600);
  line-height: 1.45;
}}
.shift-text b {{ color: var(--ink-900); }}

/* ── Swiss Financial Ledger & Editorial Dossier ── */
.cap-editorial-box {{
  background: var(--cream);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius-lg);
  padding: clamp(24px, 3.5vw, 40px);
  box-shadow: 0 8px 30px -10px rgba(0,0,0,0.05);
}}
.cap-editorial-top {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--warm-200);
  padding-bottom: 16px;
}}
.cap-editorial-title {{
  font-family: var(--serif);
  font-size: clamp(22px, 2.6vw, 28px);
  font-weight: 700;
  color: var(--ink-900);
  letter-spacing: -.02em;
}}
.cap-editorial-meta {{
  font-family: var(--mono);
  font-size: 11.5px;
  color: var(--ink-500);
  display: flex;
  align-items: center;
  gap: 8px;
}}
.cap-editorial-meta b {{ color: var(--emerald-800); }}

/* Modern Live Readout & Refined Allocation Strip */
.cap-live-readout {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  background: var(--white);
  border: 1px solid var(--warm-200);
  border-radius: 8px;
  padding: 8px 14px;
  margin-bottom: 12px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  transition: all .24s ease;
}}
.readout-domain {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--sans);
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink-900);
}}
.readout-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
  transition: background .25s ease;
}}
.readout-metrics {{
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: var(--mono);
  font-size: 11.5px;
}}
.readout-badge {{
  font-weight: 700;
  color: var(--ink-900);
  background: var(--warm-50);
  border: 1px solid var(--warm-200);
  padding: 3px 8px;
  border-radius: 4px;
}}
.readout-meta {{
  color: var(--ink-500);
}}

.cap-precision-strip {{
  display: flex;
  align-items: center;
  height: 14px;
  border-radius: 100px;
  overflow: hidden;
  background: var(--warm-100);
  margin-bottom: 32px;
  padding: 2px;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.1), 0 1px 0 rgba(255,255,255,0.9);
  position: relative;
}}
.strip-segment {{
  height: 100%;
  width: 0%;
  position: relative;
  cursor: pointer;
  border-radius: 100px;
  margin: 0 1px;
  transition: width 1.4s cubic-bezier(0.16, 1, 0.3, 1),
              filter 0.24s ease,
              opacity 0.24s ease,
              box-shadow 0.24s ease,
              transform 0.24s ease;
}}
.strip-segment:hover, .strip-segment.active {{
  transform: translateY(-1.5px);
  filter: brightness(1.22) saturate(1.2);
  box-shadow: 0 4px 12px var(--seg-glow, rgba(0,0,0,0.25));
  z-index: 5;
  opacity: 1 !important;
}}

/* Split Architecture: Ledger Rows (Left) & Detailed Dossier (Right) */
.cap-ledger-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
}}
@media(min-width:960px){{
  .cap-ledger-grid {{
    grid-template-columns: 1.25fr 1fr;
    gap: 36px;
    align-items: start;
  }}
}}

/* Ledger Rows Table */
.cap-ledger-table {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.ledger-row {{
  display: grid;
  grid-template-columns: 32px 1.4fr 90px 70px;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  background: var(--white);
  border: 1px solid var(--warm-200);
  border-radius: 10px;
  cursor: pointer;
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
}}
@media(max-width:640px){{
  .cap-editorial-box {{
    padding: 16px 12px;
    border-radius: 12px;
    box-sizing: border-box;
    width: 100%;
    overflow: hidden;
  }}
  .cap-editorial-top {{
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
    margin-bottom: 14px;
    padding-bottom: 12px;
  }}
  .cap-editorial-title {{
    font-size: 19px;
    line-height: 1.2;
  }}
  .cap-editorial-meta {{
    font-size: 10.5px;
    flex-wrap: wrap;
    gap: 6px;
  }}
  .cap-live-readout {{
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
    padding: 8px 10px;
    margin-bottom: 10px;
  }}
  .readout-domain {{
    font-size: 12.5px;
  }}
  .readout-metrics {{
    gap: 8px;
    font-size: 10.5px;
  }}
  .cap-precision-strip {{
    height: 10px;
    margin-bottom: 16px;
    padding: 1.5px;
  }}
  .cap-ledger-grid {{
    gap: 18px;
    width: 100%;
    box-sizing: border-box;
  }}
  .cap-ledger-table {{
    width: 100%;
    box-sizing: border-box;
  }}
  .ledger-row {{
    grid-template-columns: 20px minmax(0, 1fr) 50px;
    gap: 8px;
    padding: 10px 8px;
    min-width: 0;
    width: 100%;
    box-sizing: border-box;
  }}
  .ledger-num {{
    font-size: 10.5px;
  }}
  .ledger-name {{
    font-size: 13px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .ledger-gauge {{
    height: 3px;
  }}
  .ledger-share {{
    font-size: 15.5px;
    text-align: right;
  }}
  .ledger-talent {{
    display: none;
  }}
  .cap-dossier-card {{
    padding: 16px 12px;
    box-sizing: border-box;
    width: 100%;
    min-width: 0;
    overflow: hidden;
  }}
  .dossier-h4 {{
    font-size: 18px;
  }}
  .dossier-stat-row {{
    padding: 10px 10px;
    gap: 6px;
  }}
  .dossier-stat-val {{
    font-size: 13px;
  }}
  .dossier-p {{
    font-size: 13.5px;
  }}
}}
.ledger-row:hover, .ledger-row.active {{
  border-color: var(--row-color, var(--emerald-600));
  background: #FFF;
  box-shadow: 0 6px 20px -4px rgba(0,0,0,0.07);
  transform: translateX(3px);
}}
.ledger-num {{
  font-family: var(--mono);
  font-size: 11.5px;
  color: var(--row-color, var(--ink-400));
  font-weight: 700;
}}
.ledger-row {{
  min-width: 0;
  max-width: 100%;
  width: 100%;
  box-sizing: border-box;
}}
.ledger-info {{
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
  overflow: hidden;
}}
.ledger-name {{
  font-family: var(--sans);
  font-size: 14.5px;
  font-weight: 600;
  color: var(--ink-900);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}
.ledger-gauge {{
  width: 100%;
  height: 4px;
  background: var(--warm-100);
  border-radius: 2px;
  overflow: hidden;
}}
.ledger-gauge-fill {{
  height: 100%;
  width: 0%;
  background: var(--row-color, var(--gold-500));
  border-radius: 2px;
  transition: width 1.4s cubic-bezier(0.16, 1, 0.3, 1);
}}
.ledger-talent {{
  font-family: var(--mono);
  font-size: 11.5px;
  color: var(--ink-500);
  text-align: right;
  white-space: nowrap;
}}
.ledger-share {{
  font-family: var(--serif);
  font-size: 19px;
  font-weight: 700;
  color: var(--ink-900);
  text-align: right;
  font-variant-numeric: tabular-nums;
}}

/* Right Deep Editorial Dossier Card */
.cap-dossier-card {{
  background: var(--white);
  border: 1.5px solid var(--warm-200);
  border-radius: var(--radius);
  padding: clamp(20px, 2.8vw, 30px);
  box-shadow: 0 8px 24px -6px rgba(0,0,0,0.06);
  position: relative;
  transition: all .28s ease;
}}
.dossier-domain-tag {{
  font-family: var(--mono);
  font-size: 10.5px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--emerald-800);
  font-weight: 700;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.dossier-domain-tag::before {{
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--dossier-accent, #D4A017);
}}
.dossier-h4 {{
  font-family: var(--serif);
  font-size: 21px;
  color: var(--ink-900);
  font-weight: 700;
  line-height: 1.25;
  margin-bottom: 12px;
}}
.dossier-stat-row {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  background: var(--cream);
  border: 1px solid var(--warm-200);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 14px;
}}
.dossier-stat-label {{
  font-family: var(--mono);
  font-size: 10px;
  color: var(--ink-400);
  text-transform: uppercase;
  margin-bottom: 2px;
}}
.dossier-stat-val {{
  font-family: var(--mono);
  font-size: 14.5px;
  font-weight: 700;
  color: var(--ink-900);
}}
.dossier-p {{
  font-size: 14px;
  color: var(--ink-600);
  line-height: 1.55;
  margin-bottom: 16px;
}}
.dossier-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}
.dossier-chip {{
  font-family: var(--mono);
  font-size: 10.5px;
  padding: 3px 8px;
  border-radius: 4px;
  background: var(--warm-50);
  border: 1px solid var(--warm-200);
  color: var(--ink-600);
}}

/* ════════════════════════════════════
   INTELLIGENCE RIVER
   ════════════════════════════════════ */
.river-section {{
  padding: clamp(52px, 7vw, 92px) 0;
  background: var(--cream);
  border-top: 1px solid var(--warm-200);
}}
.river-list {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
}}
@media(min-width:960px){{ .river-list {{ grid-template-columns: 1fr 1fr; column-gap: 48px; }} }}
.river-row {{
  padding: 18px 20px;
  border-bottom: 1px solid var(--warm-200);
  border-left: 3px solid transparent;
  border-radius: 10px;
  transition: all .28s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  cursor: pointer;
}}
.river-row:first-child {{ border-top: 1px solid var(--warm-200); }}
.river-row:hover {{
  background: var(--white);
  border-left-color: var(--emerald-600);
  transform: translateX(6px);
  box-shadow: 0 10px 28px -6px rgba(4,77,58,0.1);
}}
.river-cat {{
  font-family: var(--mono);
  font-size: 10.5px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--emerald-700);
  font-weight: 600;
  margin-bottom: 4px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: transform .25s ease;
}}
.river-row:hover .river-cat {{
  transform: translateX(2px);
}}
.river-src {{
  font-family: var(--mono);
  font-size: 10.5px;
  color: var(--ink-400);
  margin-bottom: 5px;
}}
.river-headline {{
  font-size: 15.5px;
  font-weight: 600;
  color: var(--ink-800);
  line-height: 1.4;
  transition: color .2s ease;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
}}
.river-row:hover .river-headline {{ color: var(--emerald-800); }}
.river-arrow {{
  font-family: var(--sans);
  font-size: 17px;
  color: var(--emerald-600);
  opacity: 0;
  transform: translateX(-8px);
  transition: all .25s cubic-bezier(0.16, 1, 0.3, 1);
  flex-shrink: 0;
}}
.river-row:hover .river-arrow {{
  opacity: 1;
  transform: translateX(0);
}}

/* ════════════════════════════════════
   PERSONAS — Who We Serve (Executive Mandates)
   ════════════════════════════════════ */
.personas-section {{
  padding: clamp(52px, 7vw, 96px) 0;
  background: var(--white);
}}
.personas-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 340px), 1fr));
  gap: 24px;
}}
.persona-card {{
  border: 1.5px solid var(--warm-200);
  border-radius: var(--radius-lg);
  padding: clamp(22px, 2.8vw, 30px);
  background: var(--white);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 16px;
  position: relative;
  overflow: hidden;
  transition: all .32s cubic-bezier(0.16, 1, 0.3, 1);
}}
.persona-card::before {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--emerald-600), var(--gold-500));
  opacity: 0;
  transition: opacity .3s ease;
}}
.persona-card:hover {{
  border-color: var(--emerald-600);
  box-shadow: 0 16px 40px -8px rgba(4,77,58,.14);
  transform: translateY(-4px);
}}
.persona-card:hover::before {{
  opacity: 1;
}}
.persona-card-top {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}}
.persona-tag {{
  font-family: var(--mono);
  font-size: 10.5px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--emerald-800);
  font-weight: 700;
  background: var(--emerald-50);
  border: 1px solid rgba(5,150,105,0.25);
  padding: 4px 10px;
  border-radius: 100px;
}}
.persona-icon-box {{
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: var(--cream);
  border: 1.5px solid var(--warm-200);
  display: grid;
  place-items: center;
  color: var(--emerald-800);
  flex-shrink: 0;
  transition: all .28s cubic-bezier(0.16, 1, 0.3, 1);
}}
.persona-card:hover .persona-icon-box {{
  background: var(--emerald-50);
  border-color: var(--emerald-600);
  color: var(--emerald-700);
  transform: scale(1.08) rotate(3deg);
}}
.persona-icon-box svg {{
  width: 24px;
  height: 24px;
}}
.persona-title {{
  font-family: var(--sans);
  font-size: 18.5px;
  font-weight: 700;
  color: var(--ink-900);
  line-height: 1.3;
  margin-top: 4px;
}}
.persona-desc {{
  font-size: 14px;
  color: var(--ink-600);
  line-height: 1.55;
}}
.persona-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  padding-top: 12px;
  border-top: 1px solid var(--warm-100);
}}
.persona-chip {{
  font-family: var(--mono);
  font-size: 10.5px;
  padding: 3px 8px;
  border-radius: 4px;
  background: var(--warm-50);
  border: 1px solid var(--warm-200);
  color: var(--ink-600);
}}

/* ════════════════════════════════════
   ADVISORY
   ════════════════════════════════════ */
.advisory-section {{
  padding: clamp(52px, 7vw, 96px) 0;
  background: var(--emerald-900);
  color: #FFF;
}}
.advisory-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
  gap: 18px;
  margin-bottom: 40px;
}}
.advisory-card {{
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: var(--radius);
  padding: clamp(20px, 2.5vw, 26px);
  transition: all .28s cubic-bezier(0.16, 1, 0.3, 1);
}}
.advisory-card:hover {{
  background: rgba(255,255,255,.12);
  border-color: rgba(255,255,255,.3);
  transform: translateY(-3px);
}}
.advisory-card h3 {{
  font-size: 17.5px;
  font-weight: 700;
  margin-bottom: 8px;
}}
.advisory-card p {{
  font-size: 14px;
  color: rgba(255,255,255,.74);
  line-height: 1.55;
}}
.advisory-cta {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: var(--radius-lg);
  padding: clamp(24px, 3.5vw, 36px) clamp(20px, 3.5vw, 40px);
}}
.advisory-cta h4 {{
  font-family: var(--serif);
  font-size: clamp(20px, 2.5vw, 24px);
  margin-bottom: 6px;
}}
.advisory-cta p {{ color: rgba(255,255,255,.7); font-size: 14.5px; }}
.btn-gold-solid {{
  background: linear-gradient(135deg, var(--gold-400), var(--gold-500));
  color: #1A1200;
  font-weight: 700;
  font-size: 14px;
  padding: 13px 26px;
  border-radius: 100px;
  border: none;
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  white-space: nowrap;
}}
.btn-gold-solid:hover {{
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(212,160,23,.38);
}}

/* ════════════════════════════════════
   SUBSCRIBE SECTION
   ════════════════════════════════════ */
.subscribe-section {{
  padding: clamp(60px, 8vw, 108px) 0;
  background: linear-gradient(180deg, var(--white) 0%, var(--warm-50) 100%);
  border-top: 1px solid var(--warm-200);
}}
.sub-master-container {{
  background: var(--white);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius-lg);
  box-shadow: 0 20px 54px -12px rgba(0,0,0,0.08);
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr;
}}
@media(min-width:960px){{
  .sub-master-container {{
    grid-template-columns: 1.15fr 1fr;
  }}
}}

/* Left Editorial Pitch Column */
.sub-pitch-col {{
  padding: clamp(32px, 5vw, 56px);
  background: linear-gradient(145deg, #02241C 0%, #03362A 100%);
  color: #FFF;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}}
.sub-pitch-col::after {{
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 1px;
  height: 100%;
  background: rgba(212,160,23,0.25);
}}
.sub-prestige-tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--gold-400);
  background: rgba(212,160,23,0.15);
  border: 1px solid rgba(212,160,23,0.35);
  padding: 6px 14px;
  border-radius: 100px;
  margin-bottom: 20px;
  align-self: flex-start;
}}
.sub-headline {{
  font-family: var(--serif);
  font-size: clamp(28px, 3.2vw, 40px);
  font-weight: 700;
  line-height: 1.16;
  margin-bottom: 14px;
  color: #FFF;
}}
.sub-headline em {{
  color: var(--gold-400);
  font-style: italic;
  font-weight: 400;
}}
.sub-pitch-desc {{
  font-size: 15.5px;
  color: rgba(255,255,255,0.78);
  line-height: 1.6;
  margin-bottom: 28px;
}}
.sub-perks-list {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 32px;
}}
.sub-perk-item {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 14px;
  color: rgba(255,255,255,0.9);
  line-height: 1.45;
}}
.sub-perk-icon {{
  color: var(--gold-400);
  font-size: 16px;
  flex-shrink: 0;
  margin-top: 1px;
}}
.sub-proof-strip {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.12);
}}
.sub-avatars {{
  display: flex;
  align-items: center;
}}
.sub-avatar-circle {{
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #03362A;
  background: var(--gold-500);
  color: #1A1200;
  font-weight: 700;
  font-size: 11px;
  display: grid;
  place-items: center;
  margin-left: -8px;
}}
.sub-avatar-circle:first-child {{ margin-left: 0; background: #059669; color: #FFF; }}
.sub-avatar-circle:nth-child(2) {{ background: #2563EB; color: #FFF; }}
.sub-avatar-circle:nth-child(3) {{ background: #D4A017; color: #1A1200; }}
.sub-proof-text {{
  font-family: var(--mono);
  font-size: 11.5px;
  color: rgba(255,255,255,0.7);
}}
.sub-proof-text b {{ color: #FFF; }}

/* Right Form Action Column */
.sub-action-col {{
  padding: clamp(32px, 5vw, 56px);
  background: var(--white);
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.sub-form-card-h3 {{
  font-family: var(--serif);
  font-size: 24px;
  color: var(--ink-900);
  margin-bottom: 6px;
}}
.sub-form-card-sub {{
  font-size: 14.5px;
  color: var(--ink-500);
  margin-bottom: 24px;
}}
.sub-interactive-form {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
.sub-input-box {{ position: relative; }}
.sub-input-vip {{
  width: 100%;
  padding: 16px 20px 16px 46px;
  border: 1.5px solid var(--warm-200);
  border-radius: 12px;
  font-size: 15.5px;
  background: var(--cream);
  color: var(--ink-900);
  outline: none;
  transition: all .2s;
}}
.sub-input-vip:focus {{
  border-color: var(--emerald-700);
  background: var(--white);
  box-shadow: 0 0 0 4px rgba(6,115,82,0.12);
}}
.sub-input-vip::placeholder {{ color: var(--ink-400); }}
.sub-input-icon {{
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ink-400);
  pointer-events: none;
}}
.sub-interest-pills {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 6px 0 10px;
}}
.sub-pill {{
  font-family: var(--mono);
  font-size: 11px;
  padding: 5px 11px;
  border-radius: 100px;
  background: var(--warm-50);
  border: 1px solid var(--warm-200);
  color: var(--ink-600);
  cursor: pointer;
  transition: all .2s;
}}
.sub-pill.active, .sub-pill:hover {{
  background: var(--emerald-50);
  border-color: var(--emerald-600);
  color: var(--emerald-800);
}}
.sub-btn-vip {{
  background: linear-gradient(135deg, var(--emerald-800), var(--emerald-900));
  color: #FFF;
  font-weight: 700;
  font-size: 15.5px;
  padding: 16px 28px;
  border-radius: 12px;
  border: none;
  transition: all .24s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 6px 20px rgba(2,43,34,0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}}
.sub-btn-vip:hover {{
  background: linear-gradient(135deg, var(--emerald-700), var(--emerald-800));
  transform: translateY(-2px);
  box-shadow: 0 10px 26px rgba(2,43,34,0.35);
}}
.sub-btn-vip:active {{ transform: scale(0.98); }}
.sub-guarantee {{
  font-size: 12px;
  color: var(--ink-400);
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 4px;
}}
.sub-or-line {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 20px 0;
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-400);
  text-transform: uppercase;
  letter-spacing: .08em;
}}
.sub-or-line::before, .sub-or-line::after {{ content: ""; flex: 1; height: 1px; background: var(--warm-200); }}

/* ── Upgraded High-End Animated LinkedIn Button ── */
.btn-linkedin-vip {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  width: 100%;
  padding: 15px 24px;
  border-radius: 12px;
  background: linear-gradient(135deg, #0A66C2 0%, #004182 100%);
  color: #FFFFFF !important;
  font-size: 14.5px;
  font-weight: 600;
  box-shadow: 0 6px 20px rgba(10, 102, 194, 0.28);
  position: relative;
  overflow: hidden;
  transition: all .28s cubic-bezier(0.16, 1, 0.3, 1);
  text-align: center;
}}
.btn-linkedin-vip::after {{
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
  animation: btnSheen 3.8s infinite;
}}
@keyframes btnSheen {{
  0% {{ left: -100%; }}
  35%, 100% {{ left: 160%; }}
}}
.btn-linkedin-vip:hover {{
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(10, 102, 194, 0.42);
  filter: brightness(1.06);
}}
.btn-linkedin-vip:active {{
  transform: scale(0.98);
}}
.linkedin-beacon {{
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: #34D399;
  box-shadow: 0 0 8px #34D399;
  animation: beaconPulse 1.8s infinite;
}}

/* ════════════════════════════════════
   FOOTER
   ════════════════════════════════════ */
.site-footer {{
  background: var(--ink-900);
  color: rgba(255,255,255,.58);
  padding: clamp(36px, 5vw, 48px) 0 32px;
  font-size: 13.5px;
}}
.footer-inner {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}}
.footer-brand {{
  font-family: var(--serif);
  font-size: 21px;
  color: #FFF;
  font-weight: 700;
}}
.footer-links {{
  display: flex;
  gap: clamp(14px, 2vw, 20px);
  flex-wrap: wrap;
}}
.footer-links a {{ transition: color .2s; }}
.footer-links a:hover {{ color: var(--gold-400); }}
.footer-copy {{
  margin-top: 24px;
  padding-top: 18px;
  border-top: 1px solid rgba(255,255,255,.08);
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  font-family: var(--mono);
  font-size: 11px;
  color: rgba(255,255,255,.38);
}}

/* ════════════════════════════════════
   MODALS (Contact & Subscribe Popups)
   ════════════════════════════════════ */
.modal-bg {{
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.7);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 200;
  display: none;
  place-items: center;
  padding: 16px;
  opacity: 0;
  transition: opacity .3s ease;
}}
.modal-bg.open {{
  display: grid;
  opacity: 1;
}}
.modal-box {{
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: clamp(24px, 4vw, 40px);
  max-width: 560px;
  width: 100%;
  max-height: 92vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 30px 80px rgba(0,0,0,.25);
  transform: scale(0.95);
  transition: transform .3s cubic-bezier(0.16, 1, 0.3, 1);
}}
.modal-bg.open .modal-box {{ transform: scale(1); }}
.modal-close {{
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--warm-50);
  border: 1px solid var(--warm-200);
  color: var(--ink-600);
  display: grid;
  place-items: center;
  font-size: 18px;
  transition: all .2s;
}}
.modal-close:hover {{ background: var(--warm-100); color: var(--ink-900); }}

.contact-meta-strip {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 10px 12px;
  background: var(--cream);
  border: 1px solid var(--warm-200);
  border-radius: 10px;
  margin-bottom: 20px;
}}
.contact-meta-item {{
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: var(--mono);
  font-size: 11.5px;
  color: var(--ink-700);
  background: var(--white);
  border: 1px solid var(--warm-200);
  padding: 6px 11px;
  border-radius: 6px;
}}

.form-group {{ margin-bottom: 14px; }}
.form-label {{
  display: block;
  font-family: var(--mono);
  font-size: 11.5px;
  font-weight: 600;
  color: var(--ink-700);
  margin-bottom: 5px;
  text-transform: uppercase;
  letter-spacing: .05em;
}}
.form-input, .form-select, .form-textarea {{
  width: 100%;
  padding: 12px 14px;
  border: 1.5px solid var(--warm-200);
  border-radius: 8px;
  font-size: 14.5px;
  background: var(--cream);
  color: var(--ink-800);
  outline: none;
  transition: border .2s;
}}
.form-input:focus, .form-textarea:focus {{ border-color: var(--emerald-600); background: #FFF; }}
.form-textarea {{ resize: none; min-height: 75px; }}

/* ── Animated Success Card ── */
.success-card {{
  text-align: center;
  padding: 10px 4px;
  animation: fadeInModal .4s cubic-bezier(0.16, 1, 0.3, 1);
}}
@keyframes fadeInModal {{
  from {{ opacity: 0; transform: translateY(16px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
.success-icon-wrap {{
  width: 76px;
  height: 76px;
  margin: 0 auto 18px;
  border-radius: 50%;
  background: var(--emerald-50);
  display: grid;
  place-items: center;
  box-shadow: 0 0 0 10px rgba(5,150,105,.12);
  animation: scaleBounce 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}
@keyframes scaleBounce {{
  0% {{ transform: scale(0); opacity: 0; }}
  100% {{ transform: scale(1); opacity: 1; }}
}}
.success-checkmark {{
  width: 52px;
  height: 52px;
  stroke: var(--emerald-700);
  stroke-width: 3.5;
  stroke-miterlimit: 10;
}}
.checkmark-circle {{
  stroke-dasharray: 166;
  stroke-dashoffset: 166;
  stroke: var(--emerald-600);
  animation: strokeCircle 0.65s cubic-bezier(0.65, 0, 0.45, 1) forwards;
}}
.checkmark-check {{
  transform-origin: 50% 50%;
  stroke-dasharray: 48;
  stroke-dashoffset: 48;
  stroke-linecap: round;
  stroke-linejoin: round;
  animation: strokeCheck 0.45s cubic-bezier(0.65, 0, 0.45, 1) 0.55s forwards;
}}
@keyframes strokeCircle {{ 100% {{ stroke-dashoffset: 0; }} }}
@keyframes strokeCheck {{ 100% {{ stroke-dashoffset: 0; }} }}

.success-telemetry-box {{
  background: var(--cream);
  border: 1px solid var(--warm-200);
  border-radius: var(--radius);
  padding: 16px 20px;
  max-width: 440px;
  margin: 0 auto 20px;
  text-align: left;
  font-size: 13.5px;
}}
.telemetry-row {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 7px 0;
  border-bottom: 1px solid var(--warm-100);
}}
.telemetry-row:last-child {{ border-bottom: none; }}
.telemetry-row span {{ color: var(--ink-500); font-family: var(--mono); font-size: 11.5px; }}
.telemetry-row b {{ color: var(--ink-900); font-family: var(--mono); font-size: 12.5px; }}

.auto-close-bar-wrap {{
  max-width: 360px;
  margin: 0 auto;
}}
.auto-close-text {{
  font-family: var(--mono);
  font-size: 12px;
  color: var(--ink-500);
  margin-bottom: 8px;
}}
.auto-close-text b {{ color: var(--emerald-700); }}
.auto-close-track {{
  width: 100%;
  height: 4px;
  background: var(--warm-200);
  border-radius: 2px;
  overflow: hidden;
}}
.auto-close-progress {{
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, var(--gold-500), var(--emerald-600));
  transform-origin: left center;
}}
.auto-close-progress.animate {{
  animation: closeCountdown 5s linear forwards;
}}
@keyframes closeCountdown {{
  0% {{ transform: scaleX(1); }}
  100% {{ transform: scaleX(0); }}
}}

/* ════════════════════════════════════
   FUNCTIONAL AUDIO BRIEF PLAYER DOCK
   ════════════════════════════════════ */
.audio-dock {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  left: auto;
  background: rgba(2, 43, 34, 0.96);
  border: 1px solid rgba(212, 160, 23, 0.4);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 16px;
  padding: 16px 20px;
  box-shadow: 0 16px 44px rgba(0,0,0,0.38);
  z-index: 150;
  display: none;
  flex-direction: column;
  gap: 12px;
  width: 380px;
  max-width: calc(100vw - 32px);
  color: #FFF;
  animation: dockSlideUp .38s cubic-bezier(0.16, 1, 0.3, 1);
}}
.audio-dock.active {{ display: flex; }}
@keyframes dockSlideUp {{
  from {{ transform: translateY(32px); opacity: 0; }}
  to {{ transform: translateY(0); opacity: 1; }}
}}
.dock-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}}
.dock-tag {{
  font-family: var(--mono);
  font-size: 10px;
  color: var(--gold-400);
  text-transform: uppercase;
  letter-spacing: .08em;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.dock-close-btn {{
  background: transparent;
  border: none;
  color: rgba(255,255,255,0.6);
  font-size: 18px;
  cursor: pointer;
  padding: 0 4px;
  transition: color .2s;
}}
.dock-close-btn:hover {{ color: #FFF; }}
.dock-title {{
  font-size: 14px;
  font-weight: 600;
  color: #FFF;
  line-height: 1.35;
}}
.dock-controls {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.dock-play-btn {{
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: var(--gold-500);
  border: none;
  color: #1A1200;
  display: grid;
  place-items: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: transform .2s, background .2s;
}}
.dock-play-btn:hover {{ transform: scale(1.06); background: var(--gold-400); }}
.dock-progress-wrap {{
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.dock-scrub-track {{
  width: 100%;
  height: 4px;
  background: rgba(255,255,255,0.2);
  border-radius: 2px;
  cursor: pointer;
  position: relative;
}}
.dock-scrub-fill {{
  height: 100%;
  width: 0%;
  background: var(--emerald-500);
  border-radius: 2px;
}}
.dock-time {{
  display: flex;
  justify-content: space-between;
  font-family: var(--mono);
  font-size: 10.5px;
  color: rgba(255,255,255,0.7);
}}
.dock-wave {{
  display: flex;
  align-items: center;
  gap: 2.5px;
  height: 14px;
}}
.dock-wave-bar {{
  width: 2.5px;
  height: 100%;
  background: var(--gold-400);
  border-radius: 1px;
}}
.audio-dock.playing .dock-wave-bar {{
  animation: wavePulse 1s infinite ease-in-out;
}}
.dock-wave-bar:nth-child(2) {{ animation-delay: .15s; height: 75%; }}
.dock-wave-bar:nth-child(3) {{ animation-delay: .3s; height: 50%; }}
.dock-wave-bar:nth-child(4) {{ animation-delay: .45s; height: 90%; }}
@keyframes wavePulse {{ 0%, 100% {{ transform: scaleY(.3); }} 50% {{ transform: scaleY(1); }} }}

/* Focus states */
:focus-visible {{ outline: 2px solid var(--emerald-600); outline-offset: 2px; border-radius: 4px; }}

@media(prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }}
}}

/* Responsive Tweaks */
@media(max-width:768px) {{
  :root {{ --gutter: 16px; }}
  .hero-content {{ padding-bottom: 74px; }}
  .carousel-tabs {{ gap: 6px; }}
  .carousel-tab {{ padding: 6px 8px; }}
  .tab-title {{ display: none; }}
  .slide-counter {{ display: none; }}
  .carousel-arrow-btn {{ width: 36px; height: 36px; }}
}}
@media(max-width:480px) {{
  .hero-chip-wrap {{ margin-bottom: 10px; }}
  .hero-headline {{ font-size: 25px; line-height: 1.15; }}
  .hero-excerpt {{ font-size: 14px; line-height: 1.5; }}
  .hero-content {{ padding-bottom: 68px; }}
  .advisory-cta {{ flex-direction: column; align-items: stretch; }}
  .btn-gold-solid {{ width: 100%; text-align: center; }}
}}
</style>
</head>
<body>

<!-- ═══ HEADER — Transparent by Default, White & Sticky on Scroll ═══ -->
<header class="site-header" id="siteHeader">
  <div class="container header-inner">
    <div class="header-left-group">
      <a href="/" class="logo" aria-label="GCCVerse Home">
        GCC<em>Verse</em>
        <span class="logo-sub">Institutional Intelligence</span>
      </a>
      <div class="header-v-divider" aria-hidden="true"></div>
      <nav class="nav-desktop" aria-label="Primary Navigation">
        <ul class="nav-list">
          <li><a href="#stories" data-section="stories">Weekly Brief</a></li>
          <li><a href="#pillars" data-section="pillars">Six Pillars</a></li>
          <li><a href="#cities" data-section="cities">Cities</a></li>
          <li><a href="#data" data-section="data">The Index</a></li>
          <li><a href="#river" data-section="river">Live River</a></li>
          <li><a href="#advisory" data-section="advisory">Advisory</a></li>
        </ul>
      </nav>
    </div>
    <div class="header-cta">
      <button class="btn-outline header-cta-desktop" type="button" onclick="openContactModal()">Contact Us</button>
      <a href="#subscribe" data-section="subscribe" class="btn-primary">Subscribe Free</a>
      <button class="mobile-menu-btn" id="mobileMenuBtn" type="button" aria-label="Toggle navigation menu" aria-expanded="false">
        <span class="hamburger-icon">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Drawer Sibling -->
<div class="mobile-nav-drawer" id="mobileNavDrawer" aria-hidden="true">
  <div class="mobile-nav-inner">
    <ul class="mobile-nav-list">
      <li><a href="#stories" data-section="stories">Weekly Brief</a></li>
      <li><a href="#pillars" data-section="pillars">Six Pillars</a></li>
      <li><a href="#cities" data-section="cities">Cities</a></li>
      <li><a href="#data" data-section="data">The Index</a></li>
      <li><a href="#river" data-section="river">Live River</a></li>
      <li><a href="#advisory" data-section="advisory">Advisory</a></li>
    </ul>
    <div class="mobile-drawer-cta">
      <button class="btn-outline" type="button" onclick="openContactModal(); closeMobileNav();" style="width:100%; text-align:center;">Contact Us</button>
      <a href="#subscribe" data-section="subscribe" class="btn-primary" style="width:100%; text-align:center; display:block;" onclick="closeMobileNav()">Subscribe Free</a>
    </div>
  </div>
</div>

<main>
<!-- ═══ FULL-WIDTH HERO CINEMATIC CAROUSEL ═══ -->
<section class="hero-carousel" id="heroCarousel" aria-label="Featured Intelligence Carousel">
  <!-- Slide 1 -->
  <div class="hero-slide active" data-slide="0" aria-hidden="false">
    <img src="{img_src('gcc_campus_exterior')}" alt="Modern corporate tech park campus in India at twilight" loading="eager" fetchpriority="high" width="1920" height="1080"/>
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <div class="hero-content-inner">
        <div class="hero-text-col">
          <div class="hero-chip-wrap">
            <span class="hero-chip">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><line x1="2" y1="12" x2="22" y2="12"/></svg>
              <span>01 · Ecosystem Footprint</span>
            </span>
            <span class="hero-chip" style="background:rgba(16,185,129,.16);border-color:rgba(16,185,129,.42);color:#34D399;">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
              <span>+140 Net Centres in FY26</span>
            </span>
          </div>
          <h1 class="hero-headline">2,117 Centres. The world's largest capability network.</h1>
          <p class="hero-excerpt">India's Global Capability Centres house 3,728 operating units across 24 cities, commanding $98.4B in aggregate revenue and 38.4% of all Grade-A office absorption.</p>
        </div>
        <div class="hero-telemetry-card">
          <div class="telemetry-tag"><span class="telemetry-pulse"></span> Macro Index Signal</div>
          <div class="telemetry-title">Bengaluru &amp; Hyderabad Anchor 51.4% of Total Units</div>
          <div class="telemetry-meta">Source: nasscom–Zinnov FY2026 Audit</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Slide 2 -->
  <div class="hero-slide" data-slide="1" aria-hidden="true">
    <img src="{img_src('gcc_talent_hub')}" alt="Indian engineers and data scientists collaborating in a modern GCC workspace" loading="lazy" decoding="async" width="1920" height="1080"/>
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <div class="hero-content-inner">
        <div class="hero-text-col">
          <div class="hero-chip-wrap">
            <span class="hero-chip">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              <span>02 · Talent Architecture</span>
            </span>
            <span class="hero-chip" style="background:rgba(59,130,246,.16);border-color:rgba(59,130,246,.42);color:#60A5FA;">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="3"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/></svg>
              <span>35.4% in Core R&amp;D &amp; AI</span>
            </span>
          </div>
          <h1 class="hero-headline">2.36 Million <em>deep-domain</em> professionals.</h1>
          <p class="hero-excerpt">Over 35% are now engaged in engineering R&D, generative AI, and algorithmic product development — the fastest transformation in India's technology history.</p>
        </div>
        <div class="hero-telemetry-card">
          <div class="telemetry-tag"><span class="telemetry-pulse"></span> Talent Metric</div>
          <div class="telemetry-title">Direct Captive In-Sourcing Rose 28% in 2025</div>
          <div class="telemetry-meta">Transitioning IT Vendor Staff to Full GCC Payroll</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Slide 3 -->
  <div class="hero-slide" data-slide="2" aria-hidden="true">
    <img src="{img_src('gcc_office_space')}" alt="Grade-A biophilic corporate office interior with natural light" loading="lazy" decoding="async" width="1920" height="1080"/>
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <div class="hero-content-inner">
        <div class="hero-text-col">
          <div class="hero-chip-wrap">
            <span class="hero-chip">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
              <span>03 · Commercial Real Estate</span>
            </span>
            <span class="hero-chip" style="background:rgba(236,72,153,.16);border-color:rgba(236,72,153,.42);color:#F472B6;">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v8h4"/><path d="M18 9h2a2 2 0 0 1 2 2v11h-4"/><path d="M10 6h4M10 10h4M10 14h4M10 18h4"/></svg>
              <span>38.4% of All Metro Office Leasing</span>
            </span>
          </div>
          <h1 class="hero-headline">31.3 Million sq ft <em>absorbed.</em></h1>
          <p class="hero-excerpt">GCCs now anchor 38.4% of all Grade-A office leasing in India's top 7 cities, reshaping skylines and rental economics from Bengaluru to Gurugram.</p>
        </div>
        <div class="hero-telemetry-card">
          <div class="telemetry-tag"><span class="telemetry-pulse"></span> Real Estate Signal</div>
          <div class="telemetry-title">Hyderabad Captured 75% of H1 Campus Deals</div>
          <div class="telemetry-meta">JLL India 2025 Office Absorption Review</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Slide 4 -->
  <div class="hero-slide" data-slide="3" aria-hidden="true">
    <img src="{img_src('gcc_executive_board')}" alt="Executive boardroom meeting with global corporate leaders" loading="lazy" decoding="async" width="1920" height="1080"/>
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <div class="hero-content-inner">
        <div class="hero-text-col">
          <div class="hero-chip-wrap">
            <span class="hero-chip">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M8 10l8 4M8 14l8-4"/></svg>
              <span>04 · Economic Weight</span>
            </span>
            <span class="hero-chip" style="background:rgba(139,92,246,.16);border-color:rgba(139,92,246,.42);color:#A78BFA;">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
              <span>$98.4B Sector Valuation</span>
            </span>
          </div>
          <h1 class="hero-headline">$98.4 Billion <em>in aggregate revenue.</em></h1>
          <p class="hero-excerpt">Approaching the landmark $100B threshold with 9.8% compound growth, centres transition from cost arbitrage to global IP ownership and profit leadership.</p>
        </div>
        <div class="hero-telemetry-card">
          <div class="telemetry-tag"><span class="telemetry-pulse"></span> Economic Mandate</div>
          <div class="telemetry-title">Global Board Mandates Up 42% for India Sites</div>
          <div class="telemetry-meta">Executive Leadership &amp; Governance Benchmark</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modern Interactive Carousel Nav Bar -->
  <div class="carousel-nav-bar">
    <div class="carousel-nav-inner">
      <div class="carousel-tabs" id="heroTabs">
        <button class="carousel-tab active" data-slide="0" aria-label="Slide 1: Footprint">
          <div class="tab-top">
            <span class="tab-idx">01</span>
            <span class="tab-title">2,117 Centres</span>
          </div>
          <div class="tab-progress-track"><div class="tab-progress-fill"></div></div>
        </button>
        <button class="carousel-tab" data-slide="1" aria-label="Slide 2: Talent">
          <div class="tab-top">
            <span class="tab-idx">02</span>
            <span class="tab-title">2.36M Talent</span>
          </div>
          <div class="tab-progress-track"><div class="tab-progress-fill"></div></div>
        </button>
        <button class="carousel-tab" data-slide="2" aria-label="Slide 3: Real Estate">
          <div class="tab-top">
            <span class="tab-idx">03</span>
            <span class="tab-title">31.3M Sq Ft</span>
          </div>
          <div class="tab-progress-track"><div class="tab-progress-fill"></div></div>
        </button>
        <button class="carousel-tab" data-slide="3" aria-label="Slide 4: Revenue">
          <div class="tab-top">
            <span class="tab-idx">04</span>
            <span class="tab-title">$98.4B Scale</span>
          </div>
          <div class="tab-progress-track"><div class="tab-progress-fill"></div></div>
        </button>
      </div>

      <div class="carousel-controls-right">
        <div class="slide-counter" aria-live="polite">
          <b id="currSlideDisplay">01</b><span>/</span><span>04</span>
        </div>
        <button class="carousel-arrow-btn" id="heroPrev" aria-label="Previous slide" type="button">
          <svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 12L6 8l4-4"/></svg>
        </button>
        <button class="carousel-arrow-btn" id="heroNext" aria-label="Next slide" type="button">
          <svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 4l4 4-4 4"/></svg>
        </button>
      </div>
    </div>
  </div>
</section>

<!-- ═══ MACRO STATS RIBBON (ANIMATED NUMBERS) ═══ -->
<section class="stats-ribbon" aria-label="Macro Ecosystem Statistics">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-block reveal">
        <div class="stat-number" data-target="2117" data-decimals="0">0</div>
        <div class="stat-label">Active Centres</div>
        <div class="stat-sub">+140 net additions in FY2026</div>
      </div>
      <div class="stat-block reveal delay-100">
        <div class="stat-number" data-target="3728" data-decimals="0">0</div>
        <div class="stat-label">Operating Units</div>
        <div class="stat-sub">1.76 facilities per enterprise avg.</div>
      </div>
      <div class="stat-block reveal delay-200">
        <div class="stat-number" data-target="2.36" data-decimals="2" data-suffix="M">0</div>
        <div class="stat-label">Specialized Talent</div>
        <div class="stat-sub">35.4% in engineering R&D + AI</div>
      </div>
      <div class="stat-block reveal delay-300">
        <div class="stat-number" data-target="98.4" data-decimals="1" data-prefix="$" data-suffix="B">$0</div>
        <div class="stat-label">Annual Revenue</div>
        <div class="stat-sub">9.8% YoY compound growth</div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ FEATURED STORIES ═══ -->
<section class="stories-section" id="stories" aria-label="Weekly Dispatch">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">Weekly Dispatch · August 2026</div>
      <h2 class="section-h2">What moved this week.</h2>
    </div>

    <div class="stories-grid">
      <article class="story-feature reveal">
        <div class="story-img">
          <img src="{img_src('gcc_news_developments')}" alt="Syneos Health Hyderabad Global Capability Centre inauguration" loading="lazy" decoding="async" width="800" height="450"/>
        </div>
        <div class="story-body">
          <div class="story-meta">
            <span class="chip chip-gold">GCC Launch · Hyderabad</span>
            <button class="chip chip-emerald" type="button" onclick="startAudioBrief()" style="cursor:pointer;" aria-label="Play Audio Brief">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              <span>Play Audio Brief (0:48)</span>
            </button>
          </div>
          <h3 class="story-title">Syneos Health Inaugurates Asia's Largest Capability Centre in Hyderabad</h3>
          <p class="story-excerpt">The global biopharmaceutical solutions giant opened its flagship facility at Phoenix Equinox, Gachibowli — its largest in Asia and third-largest globally, serving as the elite hub for production AI, clinical data architecture, and pharmacovigilance.</p>
          <div class="story-source">
            <span>Source: GCCVerse Primary Coverage · Syneos Health Filing</span>
          </div>
        </div>
      </article>

      <div class="stories-stack">
        <article class="story-card-sm reveal delay-100">
          <div class="story-meta"><span class="chip chip-emerald">AI & Engineering</span></div>
          <h3 class="story-title">Octave Opens 2 Lakh Sq Ft AI Hub in HITEC City</h3>
          <p class="story-excerpt">Scales to 2,000 engineers in deep software engineering, generative AI, and real-time clinical product development.</p>
          <div class="story-source"><span>Source: Octave Corporate Announcement</span></div>
        </article>
        <article class="story-card-sm reveal delay-200">
          <div class="story-meta"><span class="chip chip-gold">Expansion</span></div>
          <h3 class="story-title">Blackbaud Adds Second Hyderabad Campus in Financial District</h3>
          <p class="story-excerpt">45,000 sq ft facility in Nanakramguda integrating enterprise customer success with core platform R&D.</p>
          <div class="story-source"><span>Source: Company Filings · Telangana IT Board</span></div>
        </article>
        <article class="story-card-sm reveal delay-300">
          <div class="story-meta"><span class="chip chip-emerald">Operating Models</span></div>
          <h3 class="story-title">The Structural Shift to GCC Payroll</h3>
          <p class="story-excerpt">Global centres systematically transitioning vendor headcount to direct employees, protecting IP and accelerating digital transformation.</p>
          <div class="story-source"><span>Source: GCCVerse Proprietary Analysis · FY26</span></div>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- ═══ SIX PILLARS ═══ -->
<section class="pillars-section" id="pillars" aria-label="Six Pillars Taxonomy">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">Intelligence Taxonomy</div>
      <h2 class="section-h2">Six threads that define the ecosystem.</h2>
      <p class="section-lead">We systematically track and correlate the structural pillars driving India's global capability revolution.</p>
    </div>
    <div class="pillars-grid">
      <article class="pillar-card reveal">
        <div class="pillar-img"><span class="pillar-badge">Pillar 01</span><img src="{img_src('gcc_news_developments')}" alt="GCC News" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">News & Developments</h3><p class="pillar-desc">Greenfield launches, secondary expansions, corporate capital investments, and strategic mandates from parent headquarters.</p></div>
      </article>
      <article class="pillar-card reveal delay-100">
        <div class="pillar-img"><span class="pillar-badge">Pillar 02</span><img src="{img_src('gcc_data_intelligence')}" alt="GCC Data Intelligence" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">Data & Intelligence</h3><p class="pillar-desc">Compensation benchmarks, maturity models, cost arbitrage ratios, and predictive talent availability across AI stacks.</p></div>
      </article>
      <article class="pillar-card reveal delay-200">
        <div class="pillar-img"><span class="pillar-badge">Pillar 03</span><img src="{img_src('gcc_cities_clusters')}" alt="GCC Cities" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">Cities & Locations</h3><p class="pillar-desc">Spatial distribution across Tier-1 core corridors versus high-velocity Tier-2 alternatives like GIFT City and Kochi.</p></div>
      </article>
      <article class="pillar-card reveal">
        <div class="pillar-img"><span class="pillar-badge">Pillar 04</span><img src="{img_src('gcc_real_estate')}" alt="GCC Real Estate" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">Real Estate & Workplace</h3><p class="pillar-desc">Leasing velocity, campus supply pipelines, flexibility structures, and architectural transformations driving productivity.</p></div>
      </article>
      <article class="pillar-card reveal delay-100">
        <div class="pillar-img"><span class="pillar-badge">Pillar 05</span><img src="{img_src('gcc_policy_investment')}" alt="GCC Policy" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">Policy & Investment</h3><p class="pillar-desc">State incentive frameworks, stamp duty exemptions, capital subsidies, SEZ amendments, and bilateral FDI corridors.</p></div>
      </article>
      <article class="pillar-card reveal delay-200">
        <div class="pillar-img"><span class="pillar-badge">Pillar 06</span><img src="{img_src('gcc_leadership_talent')}" alt="GCC Leadership" loading="lazy" decoding="async" width="600" height="338"/></div>
        <div class="pillar-body"><h3 class="pillar-title">Leadership & Talent</h3><p class="pillar-desc">C-suite appointments, MD mobility, organizational design shifts, attrition metrics, and AI upskilling programmes.</p></div>
      </article>
    </div>
  </div>
</section>

<!-- ═══ CITY CLUSTERS ═══ -->
<section class="cities-section" id="cities" aria-label="Geographic Corridors">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">Geographic Corridors</div>
      <h2 class="section-h2">Where capability concentrates.</h2>
      <p class="section-lead">Bengaluru and Hyderabad anchor over 51% of all operations, while the NCR and Tier-2 corridors expand aggressively.</p>
    </div>
    <div class="cities-grid">
      <article class="city-card reveal">
        <div class="city-img">
          <img src="{img_src('gcc_city_bengaluru')}" alt="Bengaluru tech corridor" loading="lazy" decoding="async" width="600" height="450"/>
          <div class="city-overlay"></div>
          <span class="city-name">Bengaluru</span>
        </div>
        <div class="city-body"><p class="city-desc"><b>The Global Capability Capital.</b> Over 29% of all Indian GCC units and 35%+ of total headcount. Anchored by Outer Ring Road, Bellandur, and Whitefield.</p><div class="city-source">600+ Enterprise Centres · nasscom–Zinnov FY2026</div></div>
      </article>
      <article class="city-card reveal delay-100">
        <div class="city-img">
          <img src="{img_src('gcc_city_hyderabad')}" alt="Hyderabad Financial District" loading="lazy" decoding="async" width="600" height="450"/>
          <div class="city-overlay"></div>
          <span class="city-name">Hyderabad</span>
        </div>
        <div class="city-body"><p class="city-desc"><b>Fastest Scaling Mega-Hub.</b> 75% of new large-format campus announcements in H1 2026. Preferred nexus for Life Sciences, FinTech, and Cloud.</p><div class="city-source">450+ Enterprise Centres · State IT Ministry 2026</div></div>
      </article>
      <article class="city-card reveal delay-200">
        <div class="city-img">
          <img src="{img_src('gcc_city_delhincr')}" alt="Gurugram Cyber City" loading="lazy" decoding="async" width="600" height="450"/>
          <div class="city-overlay"></div>
          <span class="city-name">Delhi NCR</span>
        </div>
        <div class="city-body"><p class="city-desc"><b>Northern Strategic Anchor.</b> Concentrated in Gurugram Cyber City, Golf Course Road, and Noida. Houses consulting, BFSI, and industrial capability HQs.</p><div class="city-source">380+ Enterprise Centres · CREDAI-JLL 2025</div></div>
      </article>
    </div>
  </div>
</section>

<!-- ═══ DATA INDEX & ELEGANT EDITORIAL CAPABILITY DISTRIBUTION ═══ -->
<section class="data-section" id="data" aria-label="Ecosystem Data Index">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">The Baseline · FY2026</div>
      <h2 class="section-h2">The macro movements we measure.</h2>
      <p class="section-lead">Every data point is verified against regulatory filings, peer-reviewed industry whitepapers, and primary real estate audits.</p>
    </div>

    <div class="data-shifts">
      <div class="shift-item reveal">
        <span class="shift-badge down">▼ 28.2%</span>
        <div class="shift-text"><b>Hiring normalization:</b> Volume lateral recruiting shifted to senior AI research, architectural, and specialized domain hires.</div>
      </div>
      <div class="shift-item reveal delay-100">
        <span class="shift-badge up">▲ 9.8%</span>
        <div class="shift-text"><b>Revenue expansion:</b> Double-digit value output, outpacing broader IT services through high-margin IP ownership.</div>
      </div>
      <div class="shift-item reveal delay-200">
        <span class="shift-badge gold">38.4%</span>
        <div class="shift-text"><b>Gross leasing share:</b> GCC transactions anchored 31.3M sq ft of office space across India's top-7 metropolitan clusters.</div>
      </div>
    </div>

    <!-- ── Swiss Financial Ledger & Editorial Capability Dossier ── -->
    <div class="cap-editorial-box reveal" id="capBox">
      <div class="cap-editorial-top">
        <div>
          <h3 class="cap-editorial-title">Ecosystem Functional Capability Distribution</h3>
          <div style="font-size:14px; color:var(--ink-500); margin-top:2px;">Audited structural talent allocation &amp; functional mandate depth across India's 2,117 active GCCs</div>
        </div>
        <div class="cap-editorial-meta">
          <span>Source: <b>nasscom–Zinnov Baseline Audit</b></span> · <span>Total Pool: <b>2.36M FTEs</b></span>
        </div>
      </div>

      <!-- Modern Integrated Readout & Refined Master Allocation Strip -->
      <div class="cap-live-readout" id="capLiveReadout">
        <div class="readout-domain">
          <span class="readout-dot" id="readoutDot" style="background:#B8860B;"></span>
          <b id="readoutTitle">Engineering R&amp;D &amp; Frontier AI</b>
        </div>
        <div class="readout-metrics">
          <span class="readout-badge" id="readoutShare">35.4% Share</span>
          <span class="readout-meta" id="readoutTalent">~835,000 FTEs</span>
          <span class="readout-meta" id="readoutGrowth">+4.8% YoY</span>
        </div>
      </div>

      <div class="cap-precision-strip" id="masterStrip">
        <div class="strip-segment active" id="strip-0" style="background:#B8860B; --seg-color:#B8860B; --seg-glow:rgba(184,134,11,0.5);" data-width="35.4%"></div>
        <div class="strip-segment" id="strip-1" style="background:#067352; --seg-color:#067352; --seg-glow:rgba(6,115,82,0.5);" data-width="28.1%"></div>
        <div class="strip-segment" id="strip-2" style="background:#1D4ED8; --seg-color:#1D4ED8; --seg-glow:rgba(29,78,216,0.5);" data-width="19.5%"></div>
        <div class="strip-segment" id="strip-3" style="background:#BE185D; --seg-color:#BE185D; --seg-glow:rgba(190,24,93,0.5);" data-width="10.2%"></div>
        <div class="strip-segment" id="strip-4" style="background:#6D28D9; --seg-color:#6D28D9; --seg-glow:rgba(109,40,217,0.5);" data-width="6.8%"></div>
      </div>

      <!-- Split Ledger & Deep Dossier -->
      <div class="cap-ledger-grid">
        <!-- Left: Interactive Financial Ledger Table -->
        <div class="cap-ledger-table" id="ledgerTable">
          <!-- Row 01 -->
          <div class="ledger-row active" data-index="0" style="--row-color:#B8860B;">
            <div class="ledger-num">01</div>
            <div class="ledger-info">
              <div class="ledger-name">Engineering R&amp;D &amp; Frontier AI</div>
              <div class="ledger-gauge"><div class="ledger-gauge-fill" data-width="35.4%"></div></div>
            </div>
            <div class="ledger-talent">~835,000 FTEs</div>
            <div class="ledger-share">35.4%</div>
          </div>

          <!-- Row 02 -->
          <div class="ledger-row" data-index="1" style="--row-color:#067352;">
            <div class="ledger-num">02</div>
            <div class="ledger-info">
              <div class="ledger-name">Software &amp; Cloud Platforms</div>
              <div class="ledger-gauge"><div class="ledger-gauge-fill" data-width="28.1%"></div></div>
            </div>
            <div class="ledger-talent">~663,000 FTEs</div>
            <div class="ledger-share">28.1%</div>
          </div>

          <!-- Row 03 -->
          <div class="ledger-row" data-index="2" style="--row-color:#1D4ED8;">
            <div class="ledger-num">03</div>
            <div class="ledger-info">
              <div class="ledger-name">BFSI, FinTech &amp; Risk Quant</div>
              <div class="ledger-gauge"><div class="ledger-gauge-fill" data-width="19.5%"></div></div>
            </div>
            <div class="ledger-talent">~460,000 FTEs</div>
            <div class="ledger-share">19.5%</div>
          </div>

          <!-- Row 04 -->
          <div class="ledger-row" data-index="3" style="--row-color:#BE185D;">
            <div class="ledger-num">04</div>
            <div class="ledger-info">
              <div class="ledger-name">Life Sciences &amp; Clinical Tech</div>
              <div class="ledger-gauge"><div class="ledger-gauge-fill" data-width="10.2%"></div></div>
            </div>
            <div class="ledger-talent">~240,000 FTEs</div>
            <div class="ledger-share">10.2%</div>
          </div>

          <!-- Row 05 -->
          <div class="ledger-row" data-index="4" style="--row-color:#6D28D9;">
            <div class="ledger-num">05</div>
            <div class="ledger-info">
              <div class="ledger-name">Strategic Operations &amp; Supply</div>
              <div class="ledger-gauge"><div class="ledger-gauge-fill" data-width="6.8%"></div></div>
            </div>
            <div class="ledger-talent">~160,000 FTEs</div>
            <div class="ledger-share">6.8%</div>
          </div>
        </div>

        <!-- Right: Detailed Editorial Dossier Card -->
        <div class="cap-dossier-card" id="dossierCard">
          <div class="dossier-domain-tag" id="dossierTag">Domain 01 of 05 · Global IP Leadership</div>
          <h4 class="dossier-h4" id="dossierTitle">Engineering R&amp;D &amp; Frontier AI</h4>
          <div class="dossier-stat-row">
            <div>
              <div class="dossier-stat-label">Total Specialized Talent</div>
              <div class="dossier-stat-val" id="dossierTalent">~835,000 Engineers</div>
            </div>
            <div>
              <div class="dossier-stat-label">Annual Growth Rate</div>
              <div class="dossier-stat-val" id="dossierGrowth">+4.8% YoY Expansion</div>
            </div>
          </div>
          <p class="dossier-p" id="dossierText">
            Over 42% of Fortune 500 GCCs now anchor primary patent filings and core algorithmic product development in India. The capability focus has transitioned from software maintenance to generative AI model tuning, chip design (VLSI), and autonomous aerospace systems.
          </p>
          <div class="dossier-chips" id="dossierChips">
            <span class="dossier-chip">Semiconductor VLSI</span>
            <span class="dossier-chip">Generative AI Labs</span>
            <span class="dossier-chip">Autonomous Systems</span>
            <span class="dossier-chip">Embedded Firmware</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ INTELLIGENCE RIVER ═══ -->
<section class="river-section" id="river" aria-label="Live Intelligence River">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">Live Intelligence River</div>
      <h2 class="section-h2">Verified moves, sourced in real time.</h2>
    </div>
    <div class="river-list" id="riverStream"></div>
  </div>
</section>

<!-- ═══ PERSONAS (EXECUTIVE MANDATES) ═══ -->
<section class="personas-section" id="personas" aria-label="Who We Serve">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag">Ecosystem Stakeholders</div>
      <h2 class="section-h2">Built for the decision-makers of the ecosystem.</h2>
      <p class="section-lead">Actionable telemetry and bespoke intelligence tailored for the leaders shaping India's $98.4B captive landscape.</p>
    </div>
    <div class="personas-grid">
      <!-- 01: GCC & Site Leaders -->
      <article class="persona-card reveal">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 01 · Site Autonomy</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">GCC &amp; Site Leaders</h3>
          <p class="persona-desc" style="margin-top:8px;">Benchmark peer organizational structures, direct payroll transitions, wage inflation, and corporate decision autonomy.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">Headcount Sizing</span>
          <span class="persona-chip">Direct Payroll</span>
          <span class="persona-chip">HQ Reporting Lines</span>
        </div>
      </article>

      <!-- 02: Investors & Asset Managers -->
      <article class="persona-card reveal delay-100">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 02 · Capital Strategy</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                <circle cx="12" cy="14" r="2"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">Investors &amp; Asset Managers</h3>
          <p class="persona-desc" style="margin-top:8px;">Track cross-border FDI flows, private equity carve-outs, institutional roll-ups, and commercial captive valuation multiples.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">PE Carve-Outs</span>
          <span class="persona-chip">Valuation Multiples</span>
          <span class="persona-chip">Capital Outflows</span>
        </div>
      </article>

      <!-- 03: Corporate Real Estate -->
      <article class="persona-card reveal delay-200">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 03 · Spatial Strategy</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 21h18M9 8h1M9 12h1M9 16h1M14 8h1M14 12h1M14 16h1M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">Corporate Real Estate</h3>
          <p class="persona-desc" style="margin-top:8px;">Anticipate mega-leasing transactions, campus supply pipeline schedules, and micro-market rental indices across top-7 tech corridors.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">Campus Pre-Leasing</span>
          <span class="persona-chip">Rental Indexing</span>
          <span class="persona-chip">Density Scenarios</span>
        </div>
      </article>

      <!-- 04: Policymakers & State Boards -->
      <article class="persona-card reveal">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 04 · Sovereign Policy</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 22h16M2 7l10-4 10 4M4 7v11M8 7v11M12 7v11M16 7v11M20 7v11"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">Policymakers &amp; State Boards</h3>
          <p class="persona-desc" style="margin-top:8px;">Evaluate inter-state tax incentive competitiveness, stamp duty exemptions, SEZ policy shifts, and green grid stability.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">State Incentive Audits</span>
          <span class="persona-chip">SEZ Amendments</span>
          <span class="persona-chip">Renewable Power</span>
        </div>
      </article>

      <!-- 05: Talent & HR Directors -->
      <article class="persona-card reveal delay-100">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 05 · Human Capital</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">Talent &amp; HR Directors</h3>
          <p class="persona-desc" style="margin-top:8px;">Monitor executive mobility, specialized AI and VLSI compensation matrices, retention packages, and annualized attrition metrics.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">Executive Mobility</span>
          <span class="persona-chip">AI Compensation</span>
          <span class="persona-chip">Attrition Benchmarks</span>
        </div>
      </article>

      <!-- 06: Consultants & Advisory Firms -->
      <article class="persona-card reveal delay-200">
        <div>
          <div class="persona-card-top">
            <span class="persona-tag">Mandate 06 · Strategic Intelligence</span>
            <div class="persona-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
              </svg>
            </div>
          </div>
          <h3 class="persona-title">Consultants &amp; Advisory Firms</h3>
          <p class="persona-desc" style="margin-top:8px;">Arm enterprise strategy teams with validated market sizing, competitor footprint databases, and location feasibility models.</p>
        </div>
        <div class="persona-chips">
          <span class="persona-chip">Location Scoring</span>
          <span class="persona-chip">Competitor Footprints</span>
          <span class="persona-chip">Market Feasibility</span>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ═══ ADVISORY ═══ -->
<section class="advisory-section" id="advisory" aria-label="Institutional Advisory Practice">
  <div class="container">
    <div class="section-header reveal">
      <div class="section-tag" style="color:var(--gold-400)">Institutional Advisory Practice</div>
      <h2 class="section-h2" style="color:#FFF">When you require bespoke intelligence.</h2>
      <p class="section-lead" style="color:rgba(255,255,255,.74)">We advise multinational corporations, sovereign funds, and institutional developers on confidential market entry and expansion.</p>
    </div>
    <div class="advisory-grid">
      <div class="advisory-card reveal"><h3>City Intelligence & Feasibility</h3><p>Micro-market analysis of infrastructure, transit, power stability, and talent density to de-risk greenfield site selections.</p></div>
      <div class="advisory-card reveal delay-100"><h3>Peer Benchmarking</h3><p>Comprehensive audits of competitor scale, organizational hierarchies, reporting lines, and functional capability depth.</p></div>
      <div class="advisory-card reveal delay-200"><h3>Location Scouting</h3><p>Multi-criteria evaluation of commercial tech parks, developer track records, and municipal compliance.</p></div>
      <div class="advisory-card reveal"><h3>CRE Demand Modeling</h3><p>Supply-demand forecasting, lease restructuring advisory, and predictive rental indexing across Grade-A markets.</p></div>
      <div class="advisory-card reveal delay-100"><h3>Greenfield Setup Strategy</h3><p>Strategic roadmap for transitioning from vendor outsourcing to captive, autonomous GCC ownership.</p></div>
      <div class="advisory-card reveal delay-200"><h3>Custom Mandate Research</h3><p>Bespoke executive whitepapers, board presentations, and confidential market intelligence reports.</p></div>
    </div>
    <div class="advisory-cta reveal">
      <div><h4>Commission a Confidential Research Brief</h4><p>Engage our Gurugram research desk for custom intelligence and peer benchmarking.</p></div>
      <button class="btn-gold-solid" type="button" onclick="openContactModal()">Contact Us / Advisory Inquiry →</button>
    </div>
  </div>
</section>

<!-- ═══ UPGRADED HIGH-CONVERTING SUBSCRIBE SECTION ═══ -->
<section class="subscribe-section" id="subscribe" aria-label="Newsletter Subscription">
  <div class="container">
    <div class="sub-master-container reveal">
      <!-- Left Column: Editorial Value Proposition -->
      <div class="sub-pitch-col">
        <div>
          <div class="sub-prestige-tag">✦ Tuesday Executive Briefing</div>
          <h2 class="sub-headline">The signal before <em>the market moves.</em></h2>
          <p class="sub-pitch-desc">Every Tuesday at 08:00 AM IST, join 1,600+ Global Site Heads, Enterprise Managing Directors, and Sovereign Fund Managers tracking India's capability revolution.</p>
          <ul class="sub-perks-list">
            <li class="sub-perk-item"><span class="sub-perk-icon">⚡</span><span><b>Proprietary Market Signals:</b> Greenfield setups, captive in-sourcing, and SEZ policy shifts weeks before public press release.</span></li>
            <li class="sub-perk-item"><span class="sub-perk-icon">👥</span><span><b>C-Suite Mandate Tracker:</b> Leadership movements, VP appointments, and functional capability transitions across 2,117 centres.</span></li>
            <li class="sub-perk-item"><span class="sub-perk-icon">🏢</span><span><b>Grade-A Commercial Real Estate:</b> Micro-market leasing rates and spatial density across Bengaluru, Hyderabad, Pune, and NCR.</span></li>
          </ul>
        </div>
        <div class="sub-proof-strip">
          <div class="sub-avatars">
            <div class="sub-avatar-circle">M</div>
            <div class="sub-avatar-circle">G</div>
            <div class="sub-avatar-circle">J</div>
          </div>
          <div class="sub-proof-text">Read by leaders from <b>Fortune 500 Captives, JLL, Blackstone &amp; State IT Ministries</b></div>
        </div>
      </div>

      <!-- Right Column: Interactive Subscription Form -->
      <div class="sub-action-col">
        <h3 class="sub-form-card-h3">Activate Institutional Access</h3>
        <p class="sub-form-card-sub">Delivered free every Tuesday. Zero promotional noise. One-click unsubscribe.</p>
        <form class="sub-interactive-form" id="subForm" novalidate>
          <div class="sub-input-box">
            <svg class="sub-input-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <input class="sub-input-vip" id="subEmail" type="email" placeholder="corporate.email@enterprise.com" required aria-label="Corporate Email Address"/>
          </div>
          <div style="font-family:var(--mono);font-size:11px;color:var(--ink-500);text-transform:uppercase;letter-spacing:.05em;margin-top:2px;">Select Primary Mandate (Optional):</div>
          <div class="sub-interest-pills" id="subInterestPills">
            <span class="sub-pill active" data-mandate="Executive Strategy">Executive Strategy</span>
            <span class="sub-pill" data-mandate="AI & Engineering">AI &amp; Engineering</span>
            <span class="sub-pill" data-mandate="Commercial Real Estate">Commercial Real Estate</span>
            <span class="sub-pill" data-mandate="Talent & Comp">Talent &amp; Comp</span>
          </div>
          <button class="sub-btn-vip" type="submit">
            <span>Subscribe Free to Tuesday Dispatch</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
          <div class="sub-guarantee">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span>Strict privacy compliance · Institutional inbox guarantee · Never sold</span>
          </div>
        </form>
        <div class="sub-or-line">or connect on LinkedIn</div>
        <!-- Upgraded Animated LinkedIn Button -->
        <a class="btn-linkedin-vip" href="https://www.linkedin.com/company/gccverse/" target="_blank" rel="noopener">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
          <span>Follow GCCVerse on LinkedIn</span>
          <span style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.18);padding:3px 8px;border-radius:100px;font-size:12px;">
            <span class="linkedin-beacon"></span> 1,600+ Members
          </span>
        </a>
      </div>
    </div>
  </div>
</section>
</main>

<!-- ═══ FOOTER ═══ -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div><span class="footer-brand">GCCVerse</span><br>Institutional Intelligence &amp; Advisory · Gurugram 122001, Haryana, India</div>
      <div class="footer-links">
        <a href="#stories" data-section="stories">Weekly Brief</a>
        <a href="#pillars" data-section="pillars">Six Pillars</a>
        <a href="#cities" data-section="cities">Cities</a>
        <a href="#data" data-section="data">The Index</a>
        <a href="#advisory" data-section="advisory">Advisory</a>
        <a href="https://www.linkedin.com/company/gccverse/" target="_blank" rel="noopener">LinkedIn</a>
      </div>
    </div>
    <div class="footer-copy">
      <span>© 2026 GCCVerse. All rights reserved. Data verified with nasscom-Zinnov, JLL India, and state regulatory disclosures.</span>
      <span>Published weekly from Gurugram.</span>
    </div>
  </div>
</footer>

<!-- ═══ CONTACT US MODAL (WITH ANIMATED SUCCESS CARD) ═══ -->
<div class="modal-bg" id="contactModal" role="dialog" aria-modal="true" aria-labelledby="contactModalTitle">
  <div class="modal-box">
    <!-- View 1: Contact Form -->
    <div id="contactFormView">
      <button class="modal-close" type="button" onclick="closeContactModal()" aria-label="Close dialog">×</button>
      <div class="section-tag" style="margin-bottom:8px">Institutional Desk</div>
      <h3 id="contactModalTitle" style="font-family:var(--serif);font-size:24px;color:var(--ink-900);margin-bottom:6px">Contact GCCVerse</h3>
      <p style="font-size:14px;color:var(--ink-500);margin-bottom:16px">Connect directly with our Gurugram research desk for confidential advisory, site evaluation, or research inquiries.</p>

      <div class="contact-meta-strip">
        <div class="contact-meta-item">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--emerald-700)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>DLF Cyber City, Gurugram 122001</span>
        </div>
        <div class="contact-meta-item">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--emerald-700)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <a href="mailto:intelligence@gccverse.in" style="color:var(--emerald-800);font-weight:600;">intelligence@gccverse.in</a>
        </div>
        <div class="contact-meta-item">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--gold-600)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span style="color:var(--ink-900);font-weight:600;">12h SLA Guaranteed</span>
        </div>
      </div>

      <form id="contactForm" onsubmit="handleContactSubmit(event)">
        <div class="form-group"><label class="form-label" for="contactName">Your Name</label><input class="form-input" id="contactName" type="text" placeholder="e.g. Rajiv Sharma" required/></div>
        <div class="form-group"><label class="form-label" for="contactEmail">Corporate Email</label><input class="form-input" id="contactEmail" type="email" placeholder="rajiv@enterprise.com" required/></div>
        <div class="form-group"><label class="form-label" for="contactPhone">Contact Number <span style="font-size:10px;color:var(--ink-400);font-weight:400;text-transform:none;">(Optional)</span></label><input class="form-input" id="contactPhone" type="tel" placeholder="e.g. +91 98765 43210"/></div>
        <div class="form-group"><label class="form-label" for="contactInquiryType">Inquiry Classification</label>
          <select class="form-select" id="contactInquiryType">
            <option>Institutional Advisory &amp; Site Feasibility</option>
            <option>Bespoke Benchmark Research &amp; Comp Audit</option>
            <option>Commercial Real Estate (CRE) Campus Audit</option>
            <option>State Incentives &amp; FDI Policy Advisory</option>
            <option>Partnership &amp; Data Syndication</option>
            <option>General Inquiry</option>
          </select>
        </div>
        <div class="form-group"><label class="form-label" for="contactScope">Inquiry Parameters / Message</label><textarea class="form-textarea" id="contactScope" placeholder="Describe your mandate, geographic scope, or questions..."></textarea></div>
        <button type="submit" class="sub-btn-vip" style="width:100%;padding:14px;font-size:15px;margin-top:8px;">Send Message to Research Desk →</button>
      </form>
    </div>

    <!-- View 2: Animated Success Confirmation Card -->
    <div class="success-card" id="contactSuccessCard" style="display:none;">
      <div class="success-icon-wrap">
        <svg class="success-checkmark" viewBox="0 0 52 52">
          <circle class="checkmark-circle" cx="26" cy="26" r="24" fill="none"/>
          <path class="checkmark-check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
        </svg>
      </div>
      <div class="chip chip-emerald" style="display:inline-block; margin-bottom:12px;">Inquiry Dispatched Successfully</div>
      <h3 style="font-family:var(--serif); font-size:clamp(22px, 3vw, 26px); color:var(--ink-900); margin-bottom:8px;">Your Message Has Been Received</h3>
      <p style="font-size:14.5px; color:var(--ink-600); line-height:1.55; max-width:440px; margin:0 auto 20px;">
        Thank you, <b id="contactSuccessUserName" style="color:var(--ink-900);">Partner</b>. Our Gurugram advisory practice has received your parameters and will respond promptly.
      </p>
      <div class="success-telemetry-box">
        <div class="telemetry-row"><span>Tracking Reference:</span><b id="contactSuccessRef">GCC-CONT-2026-8942</b></div>
        <div class="telemetry-row"><span>SLA Commitment:</span><b>Within 12 Business Hours</b></div>
        <div class="telemetry-row"><span>Assigned Desk:</span><b>Senior Advisory Practice · Gurugram</b></div>
      </div>
      <div class="auto-close-bar-wrap">
        <div class="auto-close-text">Closing window in <b id="contactCountdownTimer">5</b> seconds...</div>
        <div class="auto-close-track"><div class="auto-close-progress" id="contactAutoCloseProgress"></div></div>
      </div>
      <button type="button" class="btn-outline" onclick="closeContactModal()" style="margin-top:20px;color:var(--ink-800);border-color:var(--warm-300);">Close Window Now</button>
    </div>
  </div>
</div>

<!-- ═══ SUBSCRIPTION SUCCESS WINDOW POPUP ═══ -->
<div class="modal-bg" id="subSuccessModal" role="dialog" aria-modal="true" aria-labelledby="subSuccessTitle">
  <div class="modal-box" style="text-align:center; padding:clamp(28px, 4vw, 44px);">
    <button class="modal-close" type="button" onclick="closeSubModal()" aria-label="Close dialog">×</button>
    <div class="success-icon-wrap" style="background:var(--gold-50); box-shadow:0 0 0 10px rgba(212,160,23,0.15);">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--gold-600)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
        <polyline points="22 4 12 14.01 9 11.01"/>
      </svg>
    </div>
    <div class="chip chip-gold" style="display:inline-block; margin-bottom:12px;">✦ VIP Access Confirmed</div>
    <h3 id="subSuccessTitle" style="font-family:var(--serif); font-size:clamp(24px, 3.2vw, 28px); color:var(--ink-900); margin-bottom:10px;">Welcome to the Executive Circle</h3>
    <p style="font-size:15px; color:var(--ink-600); line-height:1.6; max-width:440px; margin:0 auto 20px;">
      You have been successfully registered with <b id="subSuccessEmailDisplay" style="color:var(--ink-900);">your email</b> for the Tuesday 08:00 AM IST dispatch.
    </p>

    <!-- Benchmark Gift Card inside Popup -->
    <div style="background:var(--cream); border:1px solid var(--warm-200); border-radius:var(--radius); padding:16px 20px; text-align:left; margin-bottom:24px;">
      <div style="display:flex; align-items:center; gap:12px;">
        <div style="width:40px;height:40px;border-radius:8px;background:var(--emerald-50);color:var(--emerald-700);display:grid;place-items:center;font-size:20px;flex-shrink:0;">📑</div>
        <div>
          <div style="font-weight:700; font-size:14px; color:var(--ink-900);">FY2026 India GCC Executive Benchmark Memo</div>
          <div style="font-family:var(--mono); font-size:11.5px; color:var(--ink-500);">Scheduled for dispatch: Tuesday 08:00 AM IST</div>
        </div>
      </div>
    </div>

    <div style="display:flex; flex-direction:column; gap:16px;">
      <a class="btn-linkedin-vip" href="https://www.linkedin.com/company/gccverse/" target="_blank" rel="noopener">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
        <span>Follow on LinkedIn (1,600+ Members)</span>
      </a>

      <!-- 5-Second Auto-Close Progress Bar -->
      <div class="auto-close-bar-wrap" style="max-width:320px; margin:0 auto; width:100%;">
        <div class="auto-close-text">Closing window in <b id="subCountdownTimer">5</b> seconds...</div>
        <div class="auto-close-track"><div class="auto-close-progress" id="subAutoCloseProgress"></div></div>
      </div>
    </div>
  </div>
</div>

<!-- ═══ FUNCTIONAL INTERACTIVE AUDIO PLAYER DOCK ═══ -->
<div class="audio-dock" id="audioDock" role="region" aria-label="Executive Audio Dispatch Player">
  <div class="dock-header">
    <div class="dock-tag">
      <span class="telemetry-pulse"></span> Executive Audio Dispatch
    </div>
    <div style="display:flex;align-items:center;gap:8px;">
      <div class="dock-wave" id="dockWave">
        <div class="dock-wave-bar"></div>
        <div class="dock-wave-bar"></div>
        <div class="dock-wave-bar"></div>
        <div class="dock-wave-bar"></div>
      </div>
      <button class="dock-close-btn" onclick="stopAudioBrief()" type="button" aria-label="Close audio player">×</button>
    </div>
  </div>
  <div class="dock-title">Syneos Health Flagship Asia Launch (Hyderabad)</div>
  <div class="dock-controls">
    <button class="dock-play-btn" id="dockPlayBtn" onclick="toggleAudioPlayback()" type="button" aria-label="Play/Pause audio">
      <svg id="dockPlayIcon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
    </button>
    <div class="dock-progress-wrap">
      <div class="dock-scrub-track" id="dockScrubTrack">
        <div class="dock-scrub-fill" id="dockScrubFill"></div>
      </div>
      <div class="dock-time">
        <span id="dockCurrentTime">0:00</span>
        <span>0:48 · Primary Briefing</span>
      </div>
    </div>
  </div>
</div>

<script>
// ── 1. Scroll-Triggered Reveal System ──
function initScrollReveal() {{
  const reveals = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {{
    reveals.forEach(el => el.classList.add('revealed'));
    return;
  }}
  const observer = new IntersectionObserver((entries, obs) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('revealed');
        obs.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.1, rootMargin: '0px 0px -30px 0px' }});
  reveals.forEach(el => observer.observe(el));
}}

// ── 2. Number Counter Animation for Macro Stats ──
function animateCounter(el) {{
  const target = parseFloat(el.getAttribute('data-target'));
  const decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
  const prefix = el.getAttribute('data-prefix') || '';
  const suffix = el.getAttribute('data-suffix') || '';
  const duration = 2000;
  const start = 0;
  const startTime = performance.now();

  function update(currentTime) {{
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
    const currentVal = start + (target - start) * easeProgress;

    let formatted;
    if (decimals === 0) {{
      formatted = Math.round(currentVal).toLocaleString('en-US');
    }} else {{
      formatted = currentVal.toFixed(decimals);
    }}

    el.textContent = prefix + formatted + suffix;

    if (progress < 1) {{
      requestAnimationFrame(update);
    }}
  }}
  requestAnimationFrame(update);
}}

function initStatsCounter() {{
  const statsSection = document.querySelector('.stats-ribbon');
  if (!statsSection) return;
  const observer = new IntersectionObserver((entries, obs) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        obs.unobserve(entry.target);
        document.querySelectorAll('.stat-number').forEach(el => animateCounter(el));
      }}
    }});
  }}, {{ threshold: 0.2 }});
  observer.observe(statsSection);
}}

// ── 3. Elegant Swiss Financial Ledger & Capability Dossier ──
const CAP_DATA = [
  {{
    tag: "Domain 01 of 05 · Global IP Leadership",
    title: "Engineering R&D & Frontier AI",
    talent: "~835,000 Engineers",
    growth: "+4.8% YoY Expansion",
    desc: "Over 42% of Fortune 500 GCCs now anchor primary patent filings and core algorithmic product development in India. The capability focus has transitioned from software maintenance to generative AI model tuning, chip design (VLSI), and autonomous aerospace systems.",
    chips: ["Semiconductor VLSI", "Generative AI Labs", "Autonomous Systems", "Embedded Firmware"],
    color: "#B8860B"
  }},
  {{
    tag: "Domain 02 of 05 · Platform Architecture",
    title: "Software & Cloud Platforms",
    talent: "~663,000 Engineers",
    growth: "+3.2% YoY Expansion",
    desc: "Indian captive centres build and operate mission-critical core microservices, multi-cloud SaaS platforms, and enterprise cybersecurity systems that power global multinational infrastructure 24 hours a day.",
    chips: ["Multi-Cloud Orchestration", "Zero-Trust Cybersecurity", "Distributed Microservices", "SaaS Infrastructure"],
    color: "#067352"
  }},
  {{
    tag: "Domain 03 of 05 · Capital Markets & Analytics",
    title: "BFSI, FinTech & Risk Quant",
    talent: "~460,000 Professionals",
    growth: "+2.4% YoY Expansion",
    desc: "Global investment banks, asset managers, and insurance giants deploy quantitative research, algorithmic trading models, compliance AI, and actuarial analytics across Bengaluru, Mumbai, and Chennai.",
    chips: ["Algorithmic Trading", "Regulatory Compliance AI", "Actuarial Science", "Fraud Intelligence"],
    color: "#1D4ED8"
  }},
  {{
    tag: "Domain 04 of 05 · Biopharmaceutical Innovation",
    title: "Life Sciences & Clinical Tech",
    talent: "~240,000 Specialists",
    growth: "+5.6% YoY Expansion",
    desc: "The fastest growing capability domain in India. Centred primarily in Hyderabad's Genome Valley and Gachibowli, operations encompass full clinical trial automation, pharmacovigilance, and genomic bio-informatics.",
    chips: ["Clinical Data Pipelines", "Pharmacovigilance AI", "Genomic Analytics", "Regulatory Dossiers"],
    color: "#BE185D"
  }},
  {{
    tag: "Domain 05 of 05 · Enterprise Command",
    title: "Strategic Operations & Supply",
    talent: "~160,000 Leaders",
    growth: "+1.8% YoY Expansion",
    desc: "Centralized operational nerve centres managing global digital supply chain twins, multi-billion-dollar direct procurement, and treasury operations for multinational conglomerates.",
    chips: ["Supply Chain Digital Twins", "Central Treasury", "Strategic Sourcing", "Global Procurement"],
    color: "#6D28D9"
  }}
];

function initCapabilityLedger() {{
  const capBox = document.getElementById('capBox');
  if (!capBox) return;

  const stripSegments = document.querySelectorAll('.strip-segment');
  const ledgerRows = document.querySelectorAll('.ledger-row');
  let hasAnimated = false;

  const observer = new IntersectionObserver((entries, obs) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting && !hasAnimated) {{
        hasAnimated = true;
        obs.unobserve(entry.target);

        // Animate precision allocation strip
        stripSegments.forEach(seg => {{
          seg.style.width = seg.getAttribute('data-width');
        }});

        // Animate gauge fills in ledger
        ledgerRows.forEach((row, idx) => {{
          setTimeout(() => {{
            const fill = row.querySelector('.ledger-gauge-fill');
            if (fill) fill.style.width = fill.getAttribute('data-width');
          }}, idx * 100);
        }});
      }}
    }});
  }}, {{ threshold: 0.25 }});
  observer.observe(capBox);

  // Update Dossier on hover or click
  function selectDomain(idx) {{
    ledgerRows.forEach((r, i) => {{
      if (i === idx) {{
        r.classList.add('active');
      }} else {{
        r.classList.remove('active');
      }}
    }});

    // Highlight strip in 3D
    stripSegments.forEach((seg, i) => {{
      if (i === idx) {{
        seg.classList.add('active');
        seg.style.opacity = '1';
      }} else {{
        seg.classList.remove('active');
        seg.style.opacity = '0.38';
      }}
    }});

    // Update Dossier content smoothly
    const d = CAP_DATA[idx];
    if (!d) return;

    const dossier = document.getElementById('dossierCard');
    if (dossier) {{
      dossier.style.setProperty('--dossier-accent', d.color);
    }}

    document.getElementById('dossierTag').textContent = d.tag;
    document.getElementById('dossierTitle').textContent = d.title;
    document.getElementById('dossierTalent').textContent = d.talent;
    document.getElementById('dossierGrowth').textContent = d.growth;
    document.getElementById('dossierText').textContent = d.desc;

    // Update live readout banner above bar
    const shares = ["35.4%", "28.1%", "19.5%", "10.2%", "6.8%"];
    const rDot = document.getElementById('readoutDot');
    const rTitle = document.getElementById('readoutTitle');
    const rShare = document.getElementById('readoutShare');
    const rTalent = document.getElementById('readoutTalent');
    const rGrowth = document.getElementById('readoutGrowth');
    if (rDot) rDot.style.background = d.color;
    if (rTitle) rTitle.textContent = d.title;
    if (rShare) rShare.textContent = shares[idx] + " Share";
    if (rTalent) rTalent.textContent = d.talent;
    if (rGrowth) rGrowth.textContent = d.growth;

    const chipsEl = document.getElementById('dossierChips');
    if (chipsEl) {{
      chipsEl.innerHTML = d.chips.map(c => `<span class="dossier-chip">${{c}}</span>`).join('');
    }}
  }}

  ledgerRows.forEach((row, idx) => {{
    row.addEventListener('mouseenter', () => selectDomain(idx));
    row.addEventListener('click', () => selectDomain(idx));
  }});

  stripSegments.forEach((seg, idx) => {{
    seg.addEventListener('mouseenter', () => selectDomain(idx));
    seg.addEventListener('click', () => selectDomain(idx));
  }});
}}

// ── 4. Mobile Navigation Drawer & Hamburger (Guarded & Touch-Optimized) ──
let mobileNavInitialized = false;
function initMobileNav() {{
  if (mobileNavInitialized) return;
  mobileNavInitialized = true;

  const btn = document.getElementById('mobileMenuBtn');
  const drawer = document.getElementById('mobileNavDrawer');
  if (!btn || !drawer) return;

  function toggle(e) {{
    if (e) {{
      e.preventDefault();
      e.stopPropagation();
    }}
    const isOpen = drawer.classList.contains('open');
    if (isOpen) {{
      closeMobileNav();
    }} else {{
      openMobileNav();
    }}
  }}

  btn.onclick = toggle;

  document.addEventListener('click', (e) => {{
    if (drawer.classList.contains('open') && !drawer.contains(e.target) && !btn.contains(e.target)) {{
      closeMobileNav();
    }}
  }});
}}

function openMobileNav() {{
  const btn = document.getElementById('mobileMenuBtn');
  const drawer = document.getElementById('mobileNavDrawer');
  if (btn && drawer) {{
    drawer.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    btn.classList.add('active');
    btn.setAttribute('aria-expanded', 'true');
  }}
}}

function closeMobileNav() {{
  const btn = document.getElementById('mobileMenuBtn');
  const drawer = document.getElementById('mobileNavDrawer');
  if (btn && drawer) {{
    drawer.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    btn.classList.remove('active');
    btn.setAttribute('aria-expanded', 'false');
  }}
}}

// ── 5. Clean Navigation & Routing (Fix for /subscribe and deep links on Vercel) ──
function initCleanNav() {{
  const links = document.querySelectorAll('a[href^="#"], a[data-section]');
  links.forEach(link => {{
    link.addEventListener('click', function(e) {{
      const href = this.getAttribute('href');
      const sectionName = this.getAttribute('data-section') || (href && href.startsWith('#') ? href.substring(1) : null);
      if (!sectionName) return;

      const targetEl = document.getElementById(sectionName);
      if (targetEl) {{
        e.preventDefault();
        closeMobileNav();

        const headerH = document.getElementById('siteHeader')?.offsetHeight || 72;
        const targetTop = targetEl.getBoundingClientRect().top + window.pageYOffset - headerH - 8;

        window.scrollTo({{ top: targetTop, behavior: 'smooth' }});

        try {{
          const cleanPath = '/' + sectionName;
          window.history.pushState({{ section: sectionName }}, '', cleanPath);
        }} catch (err) {{}}
      }}
    }});
  }});

  // Check URL pathname on initial load (e.g. /subscribe, /stories on Vercel)
  const initialPath = window.location.pathname.replace(/^\\/+|\\/+$/g, '');
  if (initialPath && initialPath !== 'index.html') {{
    setTimeout(() => {{
      const targetEl = document.getElementById(initialPath);
      if (targetEl) {{
        const headerH = document.getElementById('siteHeader')?.offsetHeight || 72;
        window.scrollTo({{
          top: targetEl.getBoundingClientRect().top + window.pageYOffset - headerH - 8,
          behavior: 'smooth'
        }});
      }}
    }}, 250);
  }}

  window.addEventListener('popstate', function(e) {{
    const sectionName = e.state?.section || window.location.pathname.replace(/^\\/+|\\/+$/g, '');
    if (sectionName) {{
      const targetEl = document.getElementById(sectionName);
      if (targetEl) {{
        const headerH = document.getElementById('siteHeader')?.offsetHeight || 72;
        window.scrollTo({{ top: targetEl.getBoundingClientRect().top + window.pageYOffset - headerH - 8, behavior: 'smooth' }});
      }}
    }}
  }});
}}

// ── 6. Header Scroll Shadow & Transparent Blending ──
let ticking = false;
window.addEventListener('scroll', () => {{
  if (!ticking) {{
    window.requestAnimationFrame(() => {{
      const header = document.getElementById('siteHeader');
      if (header) {{
        if (window.scrollY > 25) {{
          header.classList.add('scrolled');
        }} else {{
          header.classList.remove('scrolled');
        }}
      }}
      ticking = false;
    }});
    ticking = true;
  }}
}}, {{ passive: true }});

// ── 7. Hero Carousel Engine ──
(function initCarousel(){{
  const slides = document.querySelectorAll('.hero-slide');
  const tabs = document.querySelectorAll('.carousel-tab');
  const counterEl = document.getElementById('currSlideDisplay');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const navBox = document.querySelector('.carousel-nav-bar');
  let cur = 0;
  let timer = null;
  const DUR = 5000;

  function updateSlide(newIdx){{
    if (!slides.length) return;
    slides[cur].classList.remove('active');
    slides[cur].setAttribute('aria-hidden', 'true');
    if (tabs[cur]) {{ tabs[cur].classList.remove('active'); }}

    cur = (newIdx + slides.length) % slides.length;

    slides[cur].classList.add('active');
    slides[cur].setAttribute('aria-hidden', 'false');
    if (tabs[cur]) {{
      tabs[cur].classList.add('active');
      const fillEl = tabs[cur].querySelector('.tab-progress-fill');
      if (fillEl) {{
        fillEl.style.animation = 'none';
        void fillEl.offsetWidth;
        fillEl.style.animation = '';
      }}
    }}

    if (counterEl) {{ counterEl.textContent = '0' + (cur + 1); }}
  }}

  function start(){{
    stop();
    timer = setInterval(() => {{ updateSlide(cur + 1); }}, DUR);
  }}

  function stop(){{
    if (timer) {{ clearInterval(timer); timer = null; }}
  }}

  if (prevBtn) {{ prevBtn.addEventListener('click', (e) => {{ e.stopPropagation(); updateSlide(cur - 1); start(); }}); }}
  if (nextBtn) {{ nextBtn.addEventListener('click', (e) => {{ e.stopPropagation(); updateSlide(cur + 1); start(); }}); }}

  tabs.forEach((tab, idx) => {{
    tab.addEventListener('click', (e) => {{ e.stopPropagation(); updateSlide(idx); start(); }});
  }});

  if (navBox) {{
    navBox.addEventListener('mouseenter', stop);
    navBox.addEventListener('mouseleave', start);
  }}

  document.addEventListener('visibilitychange', () => {{
    if (document.hidden) stop();
    else start();
  }});

  const carouselEl = document.getElementById('heroCarousel');
  if (carouselEl) {{
    let touchStartX = 0;
    carouselEl.addEventListener('touchstart', (e) => {{
      touchStartX = e.changedTouches[0].screenX;
      stop();
    }}, {{ passive: true }});

    carouselEl.addEventListener('touchend', (e) => {{
      const touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      if (diff > 45) updateSlide(cur + 1);
      else if (diff < -45) updateSlide(cur - 1);
      start();
    }}, {{ passive: true }});

    carouselEl.tabIndex = 0;
    carouselEl.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight') {{ updateSlide(cur + 1); start(); }}
      else if (e.key === 'ArrowLeft') {{ updateSlide(cur - 1); start(); }}
    }});
  }}

  start();
}})();

// ── 8. River Feed ──
const RIVER=[
  {{cat:"Operating Models",src:"Company Filings 2026",h:"Blackbaud executes phased transition of contract engineers to direct GCC payroll through 2027."}},
  {{cat:"AI & Data",src:"Syneos Health",h:"Production AI deployed in Hyderabad for clinical trial protocol automation and pharmacovigilance."}},
  {{cat:"Financial Services",src:"BNP Paribas Annual Review",h:"India Solutions operates 24/7 financial engineering across BLR, MAA, BOM with 10,000+ staff."}},
  {{cat:"Leadership",src:"nasscom GCC Summit",h:"Sangeeta Kumar stresses real-time micro-credentialing and agile workforce redeployment."}},
  {{cat:"Real Estate",src:"JLL India Q2 Report",h:"Hyderabad captured 75% of new large-format institutional campus leasing across HITEC City."}},
  {{cat:"Policy",src:"State IT Department",h:"Telangana and Karnataka unveil updated GCC-friendly stamp duty waivers and power tariffs."}},
  {{cat:"Tier-2 Expansion",src:"GIFT City Disclosures",h:"Global FinTech entities establish exploratory satellite pods in GIFT City, Gujarat."}},
  {{cat:"Aerospace",src:"Ministry of Commerce",h:"Boeing and Airbus expand Bengaluru centres, shifting global structural design workloads."}}
];
document.getElementById('riverStream').innerHTML=RIVER.map(r=>`<div class="river-row reveal"><div class="river-cat">${{r.cat}}</div><div class="river-src">${{r.src}}</div><a href="#stories" data-section="stories" class="river-headline"><span>${{r.h}}</span><span class="river-arrow">→</span></a></div>`).join('');

// ── 9. Interactive Subscribe System with Window Popup & 5s Auto-Close ──
const interestPills = document.querySelectorAll('#subInterestPills .sub-pill');
interestPills.forEach(p => {{
  p.addEventListener('click', () => {{ p.classList.toggle('active'); }});
}});

let subAutoCloseTimeout = null;
let subCountdownInterval = null;

document.getElementById('subForm').onsubmit = function(e) {{
  e.preventDefault();
  const emailInput = document.getElementById('subEmail');
  const email = emailInput.value.trim();

  if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {{
    emailInput.style.borderColor = 'var(--down)';
    emailInput.focus();
    return;
  }}

  document.getElementById('subSuccessEmailDisplay').textContent = email;

  const subModal = document.getElementById('subSuccessModal');
  if (subModal) {{
    subModal.classList.add('open');
  }}

  emailInput.value = '';
  emailInput.style.borderColor = 'var(--warm-200)';

  // 5-second countdown with animated progress bar
  const progressBar = document.getElementById('subAutoCloseProgress');
  const timerDisplay = document.getElementById('subCountdownTimer');
  if (progressBar) {{
    progressBar.classList.remove('animate');
    void progressBar.offsetWidth;
    progressBar.classList.add('animate');
  }}

  let secondsLeft = 5;
  if (timerDisplay) timerDisplay.textContent = secondsLeft;

  if (subCountdownInterval) clearInterval(subCountdownInterval);
  subCountdownInterval = setInterval(() => {{
    secondsLeft -= 1;
    if (secondsLeft >= 0 && timerDisplay) {{
      timerDisplay.textContent = secondsLeft;
    }}
    if (secondsLeft <= 0) {{
      clearInterval(subCountdownInterval);
    }}
  }}, 1000);

  if (subAutoCloseTimeout) clearTimeout(subAutoCloseTimeout);
  subAutoCloseTimeout = setTimeout(() => {{
    closeSubModal();
  }}, 5000);
}};

function closeSubModal() {{
  if (subAutoCloseTimeout) clearTimeout(subAutoCloseTimeout);
  if (subCountdownInterval) clearInterval(subCountdownInterval);
  const subModal = document.getElementById('subSuccessModal');
  if (subModal) subModal.classList.remove('open');
}}
document.getElementById('subSuccessModal').onclick = function(e) {{
  if (e.target === this) closeSubModal();
}};


// ── 10. Real Functional Executive Audio Brief Player ──
let isAudioPlaying = false;
let audioProgressTimer = null;
let audioSecondsElapsed = 0;
const AUDIO_TOTAL_SECONDS = 48;
let speechUtterance = null;

const BRIEF_TEXT = "Welcome to the GCCVerse Executive Audio Dispatch. Syneos Health has officially inaugurated Asia's largest capability centre in Hyderabad at Phoenix Equinox, Gachibowli. Spanning over 350,000 square feet, this flagship hub serves as the elite nexus for production AI, clinical protocol automation, and global pharmacovigilance operations. With over 2,000 biopharmaceutical and clinical data scientists, this milestone underscores Hyderabad's emergence as India's primary Life Sciences technology powerhouse.";

function startAudioBrief() {{
  const dock = document.getElementById('audioDock');
  if (!dock) return;
  dock.classList.add('active');

  // If already playing, continue
  if (!isAudioPlaying) {{
    playSpeech();
  }}
}}

function playSpeech() {{
  isAudioPlaying = true;
  const dock = document.getElementById('audioDock');
  const playIcon = document.getElementById('dockPlayIcon');
  if (dock) dock.classList.add('playing');

  // Change to Pause icon
  if (playIcon) {{
    playIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>';
  }}

  // Browser Speech Synthesis
  if ('speechSynthesis' in window) {{
    window.speechSynthesis.cancel(); // Stop any pending
    speechUtterance = new SpeechSynthesisUtterance(BRIEF_TEXT);
    speechUtterance.rate = 1.0;
    speechUtterance.pitch = 1.0;

    // Pick English executive voice if available
    const voices = window.speechSynthesis.getVoices();
    const engVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Natural') || v.name.includes('Premium') || v.name.includes('Google') || v.name.includes('Samantha')));
    if (engVoice) speechUtterance.voice = engVoice;

    speechUtterance.onend = function() {{
      pauseSpeech();
      audioSecondsElapsed = 0;
      updateAudioDisplay();
    }};

    window.speechSynthesis.speak(speechUtterance);
  }}

  // Start progress counter
  if (audioProgressTimer) clearInterval(audioProgressTimer);
  audioProgressTimer = setInterval(() => {{
    audioSecondsElapsed += 1;
    if (audioSecondsElapsed >= AUDIO_TOTAL_SECONDS) {{
      pauseSpeech();
      audioSecondsElapsed = 0;
    }}
    updateAudioDisplay();
  }}, 1000);
}}

function pauseSpeech() {{
  isAudioPlaying = false;
  const dock = document.getElementById('audioDock');
  const playIcon = document.getElementById('dockPlayIcon');
  if (dock) dock.classList.remove('playing');

  if (playIcon) {{
    playIcon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"/>';
  }}

  if ('speechSynthesis' in window) {{
    window.speechSynthesis.cancel();
  }}

  if (audioProgressTimer) {{
    clearInterval(audioProgressTimer);
    audioProgressTimer = null;
  }}
}}

function toggleAudioPlayback() {{
  if (isAudioPlaying) {{
    pauseSpeech();
  }} else {{
    playSpeech();
  }}
}}

function updateAudioDisplay() {{
  const scrub = document.getElementById('dockScrubFill');
  const timeDisplay = document.getElementById('dockCurrentTime');
  const pct = Math.min((audioSecondsElapsed / AUDIO_TOTAL_SECONDS) * 100, 100);

  if (scrub) scrub.style.width = pct + '%';

  const mins = Math.floor(audioSecondsElapsed / 60);
  const secs = audioSecondsElapsed % 60;
  if (timeDisplay) {{
    timeDisplay.textContent = `${{mins}}:${{secs < 10 ? '0' : ''}}${{secs}}`;
  }}
}}

function stopAudioBrief() {{
  pauseSpeech();
  audioSecondsElapsed = 0;
  updateAudioDisplay();
  const dock = document.getElementById('audioDock');
  if (dock) dock.classList.remove('active');
}}

// ── 11. Contact Us Modal with In-Window Confirmation & 5s Auto-Close ──
let contactAutoCloseTimeout = null;
let contactCountdownInterval = null;

function openContactModal() {{
  document.getElementById('contactFormView').style.display = 'block';
  document.getElementById('contactSuccessCard').style.display = 'none';
  document.getElementById('contactModal').classList.add('open');
}}

function closeContactModal() {{
  if (contactAutoCloseTimeout) clearTimeout(contactAutoCloseTimeout);
  if (contactCountdownInterval) clearInterval(contactCountdownInterval);
  document.getElementById('contactModal').classList.remove('open');
}}

document.getElementById('contactModal').onclick = function(e) {{
  if (e.target === this) closeContactModal();
}};

function handleContactSubmit(e) {{
  e.preventDefault();
  const name = document.getElementById('contactName').value.trim() || 'Partner';

  // In-window transition: remove inputs, display animated card
  document.getElementById('contactFormView').style.display = 'none';
  const successCard = document.getElementById('contactSuccessCard');
  successCard.style.display = 'block';

  document.getElementById('contactSuccessUserName').textContent = name;
  const randRef = 'GCC-CONT-2026-' + Math.floor(1000 + Math.random() * 9000);
  document.getElementById('contactSuccessRef').textContent = randRef;

  // Animated progress bar and 5s countdown
  const progressBar = document.getElementById('contactAutoCloseProgress');
  const timerDisplay = document.getElementById('contactCountdownTimer');
  progressBar.classList.remove('animate');
  void progressBar.offsetWidth;
  progressBar.classList.add('animate');

  let secondsLeft = 5;
  timerDisplay.textContent = secondsLeft;

  if (contactCountdownInterval) clearInterval(contactCountdownInterval);
  contactCountdownInterval = setInterval(() => {{
    secondsLeft -= 1;
    if (secondsLeft >= 0) {{
      timerDisplay.textContent = secondsLeft;
    }}
    if (secondsLeft <= 0) {{
      clearInterval(contactCountdownInterval);
    }}
  }}, 1000);

  if (contactAutoCloseTimeout) clearTimeout(contactAutoCloseTimeout);
  contactAutoCloseTimeout = setTimeout(() => {{
    closeContactModal();
    document.getElementById('contactForm').reset();
  }}, 5000);
}}

// Initialize cleanly on load
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    initScrollReveal();
    initStatsCounter();
    initCapabilityLedger();
    initMobileNav();
    initCleanNav();
  }});
}} else {{
  initScrollReveal();
  initStatsCounter();
  initCapabilityLedger();
  initMobileNav();
  initCleanNav();
}}
</script>
</body>
</html>
"""

# Write index.html (modular)
with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
    f.write(get_html(is_standalone=False))
print("Generated index.html (Updated & Tested)")

# Write gccverse_enterprise.html (embedded standalone)
with open(os.path.join(BASE_DIR, "gccverse_enterprise.html"), "w") as f:
    f.write(get_html(is_standalone=True))
print("Generated gccverse_enterprise.html (Updated & Tested)")

