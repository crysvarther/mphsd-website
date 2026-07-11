# -*- coding: utf-8 -*-
"""Page partials + content + generator. Run: python make.py"""
import os
from build import (SITE_URL, BIZ_NAME, BIZ_ALT, PHONE_DISP, PHONE_TEL, EMAIL, ADDR_ST,
                   ADDR_CITY, ADDR_STATE, ADDR_ZIP, SLOGAN, FOUNDED, GEO_LAT, GEO_LON,
                   AREAS, COUNTIES, TESTIMONIAL, IC, jsonld, breadcrumb_node,
                   GBP_URL, FACEBOOK_URL)

# ----------------------------------------------------------------------------
# Navigation
# ----------------------------------------------------------------------------
NAV = [
    ("Home", "index.html", None),
    ("About", "about.html", None),
    ("Services", "services.html", [
        ("Residential Services", "residential.html"),
        ("Plumbing", "plumbing.html"),
        ("Heating & Hydronics", "heating.html"),
        ("Lochinvar Boilers", "boilers.html"),
        ("Commercial & Government", "commercial.html"),
    ]),
    ("Service Area", "service-area.html", None),
    ("Reviews", "reviews.html", None),
    ("FAQ", "faq.html", None),
    ("Blog", "blog/index.html", None),
]

def head(title, desc, canonical, prefix, extra_schema=None, og_image="assets/img/mitch-hero.png",
         robots="index, follow, max-image-preview:large", og_type="website"):
    full_canon = SITE_URL + "/" + canonical
    schema = jsonld(extra_schema)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{full_canon}">
<meta name="robots" content="{robots}">
<meta name="author" content="{BIZ_NAME}">
<meta name="geo.region" content="US-SD">
<meta name="geo.placename" content="Mitchell, South Dakota">
<meta name="geo.position" content="{GEO_LAT};{GEO_LON}">
<meta name="ICBM" content="{GEO_LAT}, {GEO_LON}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BIZ_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{full_canon}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/{og_image}">
<link rel="icon" href="{prefix}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefix}assets/img/mph-logo.png">
<link rel="manifest" href="{prefix}site.webmanifest">
<meta name="theme-color" content="#15294c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@500;600;700&family=Pacifico&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
{schema}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>'''

def header(prefix):
    items = []
    for label, href, sub in NAV:
        h = prefix + href
        if sub:
            subs = "".join(f'<li><a href="{prefix}{s_href}">{s_label}</a></li>' for s_label, s_href in sub)
            items.append(f'<li class="has-sub"><a href="{h}">{label}</a><ul class="submenu">{subs}</ul></li>')
        else:
            items.append(f'<li><a href="{h}">{label}</a></li>')
    nav_items = "".join(items)
    return f'''
<header class="site-header">
  <div class="topbar"><div class="container">
    <span>{IC["pin"]} {ADDR_ST}, {ADDR_CITY}, {ADDR_STATE}</span>
    <span class="sep">|</span>
    <span>{IC["clock"]} Mon&ndash;Fri 8&ndash;5</span>
    <span class="sep">|</span>
    <span>{IC["phone"]} <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></span>
  </div></div>
  <div class="container">
    <nav class="nav" aria-label="Primary">
      <a class="brand" href="{prefix}index.html" aria-label="{BIZ_NAME} home">
        <img src="{prefix}assets/img/mph-logo-header.png" alt="Mitchell Plumbing &amp; Heating logo with Mitch the plumber mascot" width="60" height="60">
        <span class="brand-name">
          <span class="bn-name">Mitchell</span>
          <span class="bn-sub">Plumbing <span class="bn-amp">&amp;</span> Heating</span>
          <span class="bn-tag">Est. 1990 &middot; Mitchell, SD</span>
        </span>
      </a>
      <ul class="nav-links" id="primary-menu">
        {nav_items}
        <li class="nav-cta"><a class="btn" href="{prefix}contact.html">Free Estimate</a></li>
      </ul>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="primary-menu"><span></span></button>
    </nav>
  </div>
  <div class="zigzag" aria-hidden="true"></div>
</header>
<div class="nav-backdrop" aria-hidden="true"></div>'''

def cta_band(prefix):
    return f'''
<section class="cta-band">
  <div class="container">
    <p class="eyebrow" style="color:#ffe9b0">Ready When You Are</p>
    <h2>Need a Plumbing or Heating Pro in Mitchell?</h2>
    <p style="font-size:1.15rem;max-width:60ch;margin:0 auto 1.2em">Talk to a real local technician &mdash; not a call center. Fast, friendly service from right here in Mitchell.</p>
    <a class="cta-phone" href="tel:{PHONE_TEL}">{IC["phone"]} {PHONE_DISP}</a>
    <div style="margin-top:22px"><a class="btn btn--gold btn--lg" href="{prefix}contact.html">Request a Free Estimate</a></div>
  </div>
</section>'''

def footer(prefix):
    serv = "".join(f'<li><a href="{prefix}{h}">{l}</a></li>' for l, h in [
        ("Residential Services","residential.html"),("Residential Plumbing","plumbing.html"),
        ("Heating & Hydronics","heating.html"),("Lochinvar Boilers","boilers.html"),
        ("Fixtures & Product Lines","residential.html"),("Commercial Chillers","commercial.html"),
        ("Commercial & Government","commercial.html"),("Drain & Sewer","plumbing.html")])
    comp = "".join(f'<li><a href="{prefix}{h}">{l}</a></li>' for l, h in [
        ("About Us","about.html"),("Service Area","service-area.html"),("Reviews","reviews.html"),
        ("FAQ","faq.html"),("Blog","blog/index.html"),("Careers","careers.html"),
        ("Contact","contact.html")])
    areas = " &middot; ".join(AREAS[:10])
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="{prefix}assets/img/mph-logo.png" alt="Mitchell Plumbing &amp; Heating" width="64" height="64">
          <span class="brand-name">
            <span class="bn-name">Mitchell</span>
            <span class="bn-sub">Plumbing <span class="bn-amp">&amp;</span> Heating</span>
          </span>
        </div>
        <p style="color:#c5d2ee">Your local, family-owned plumbing &amp; heating team since {FOUNDED}. {SLOGAN}</p>
        <p class="pill" style="margin-top:6px">{IC["shield"]} Licensed &middot; Insured &middot; Trusted</p>
      </div>
      <div><h4>Services</h4><ul class="footer-links">{serv}</ul></div>
      <div><h4>Company</h4><ul class="footer-links">{comp}</ul></div>
      <div>
        <h4>Get In Touch</h4>
        <ul class="footer-links">
          <li>{IC["phone"]} <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISP}</strong></a></li>
          <li>{IC["mail"]} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{IC["pin"]} {ADDR_ST}<br><span style="padding-left:28px">{ADDR_CITY}, {ADDR_STATE} {ADDR_ZIP}</span></li>
          <li>{IC["clock"]} Mon&ndash;Fri 8am&ndash;5pm</li>
        </ul>
        <div class="footer-soc" style="margin-top:8px">
          <a href="{GBP_URL or 'https://www.google.com/search?q=Mitchell+Plumbing+and+Heating+Mitchell+SD'}" aria-label="Find us on Google" title="Google">{IC["google"]}</a>
          {f'<a href="{FACEBOOK_URL}" aria-label="Find us on Facebook" title="Facebook">{IC["facebook"]}</a>' if FACEBOOK_URL else ''}
        </div>
      </div>
    </div>
    <p style="color:#8ea2cc;font-size:.82rem;margin-top:34px">Proudly serving {areas} &amp; communities across Eastern South Dakota.</p>
  </div>
  <div class="footer-bottom"><div class="container">
    <span>&copy; <span data-year>2026</span> {BIZ_NAME} &middot; All rights reserved.</span>
    <span>{SLOGAN} &middot; Est. {FOUNDED} &middot; Mitchell, South Dakota</span>
  </div></div>
</footer>'''

def floating(prefix):
    return f'''
<div class="callbar">
  <a class="cb-call" href="tel:{PHONE_TEL}">{IC["phone"]} Call Now</a>
  <a class="cb-quote" href="{prefix}contact.html">{IC["wrench"]} Free Estimate</a>
</div>
<button class="back-to-top" aria-label="Back to top">{IC["arrow-up"]}</button>
<script src="{prefix}js/main.js" defer></script>
</body>
</html>'''

def breadcrumb_html(crumbs, prefix):
    parts = []
    for name, href in crumbs:
        parts.append(f'<a href="{prefix}{href}">{name}</a>' if href else f'<span>{name}</span>')
    inner = '<span class="sep">/</span>'.join(parts)
    return f'<div class="bg-cream2"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb">{inner}</nav></div></div>'

def render(fname, cfg):
    prefix = cfg.get("prefix", "")
    extra = list(cfg.get("schema", []))
    if cfg.get("crumbs"):
        extra.append(breadcrumb_node(cfg["crumbs"], prefix))
    html = head(cfg["title"], cfg["desc"], cfg["canonical"], prefix, extra,
                cfg.get("og_image", "assets/img/mitch-hero.png"),
                cfg.get("robots", "index, follow, max-image-preview:large"),
                cfg.get("og_type", "website"))
    html += header(prefix)
    if cfg.get("crumbs") and cfg.get("show_crumbs", True):
        html += breadcrumb_html(cfg["crumbs"], prefix)
    html += '<main id="main">' + cfg["body"] + '</main>'
    if cfg.get("cta", True):
        html += cta_band(prefix)
    html += footer(prefix) + floating(prefix)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return fname

# ----------------------------------------------------------------------------
# Reusable content helpers
# ----------------------------------------------------------------------------
def page_hero(title, sub, script_line=None):
    s = f'<span class="script" style="display:block;font-size:.6em;margin-bottom:6px">{script_line}</span>' if script_line else ''
    return f'<section class="page-hero"><div class="container">{s}<h1>{title}</h1><p>{sub}</p></div></section>'

def service_card(icon, title, body, link_href, link_text, mod=""):
    return f'''<article class="card {mod} reveal">
      <div class="card-icon">{IC[icon]}</div>
      <h3>{title}</h3>
      <p>{body}</p>
      <a class="card-link" href="{link_href}">{link_text}</a>
    </article>'''

from build import jsonld as _j  # ensure available

print("partials loaded")
