# -*- coding: utf-8 -*-
"""
Static-site generator for Mitchell Plumbing & Heating (mphsd.com).
Run:  python build.py
Outputs plain static HTML — host anywhere (Netlify, GitHub Pages, IIS, Apache).
Editing content? Update the PAGES section near the bottom and re-run.
"""
import json, os

# ----------------------------------------------------------------------------
# Business facts (single source of truth — also drives JSON-LD structured data)
# ----------------------------------------------------------------------------
SITE_URL   = "https://mphsd.com"
BIZ_NAME   = "Mitchell Plumbing & Heating Co. Inc."
BIZ_ALT    = "Mitchell Plumbing and Heating"
PHONE_DISP = "(605) 996-7583"
PHONE_TEL  = "+16059967583"
EMAIL      = "cody@mphsd.com"
ADDR_ST    = "801 N. Rowley St."
ADDR_CITY  = "Mitchell"
ADDR_STATE = "SD"
ADDR_ZIP   = "57301"
SLOGAN     = "Fast. Reliable. Clean."
FOUNDED    = "1990"
GEO_LAT    = 43.7094
GEO_LON    = -98.0298

# ----------------------------------------------------------------------------
# "Now Hiring" banner (shows at the top of the homepage).
#   Turn it on/off:  set HIRING_BANNER_ON to True or False
#   Change wording:  edit the TEXT / CTA lines below
#   Then re-run:     python pages.py
# ----------------------------------------------------------------------------
HIRING_BANNER_ON   = True
HIRING_BANNER_TEXT = "We're growing! Join the Mitchell Plumbing & Heating crew."
HIRING_BANNER_CTA  = "See Open Positions"
HIRING_BANNER_LINK = "careers.html"

# Off-site profiles. Paste real URLs here to (1) populate schema.org `sameAs`
# entity links and (2) activate the footer social icons. Leave "" to disable.
GBP_URL      = ""   # Google Business Profile (e.g. https://g.page/r/...) — none yet
FACEBOOK_URL = "https://www.facebook.com/people/Mitchell-Plumbing/100067968330886/"
SAME_AS = [u for u in (GBP_URL, FACEBOOK_URL) if u]

AREAS = ["Mitchell", "Mount Vernon", "Ethan", "Alexandria", "Parkston", "Plankinton",
         "Letcher", "Loomis", "Stickney", "Salem", "Howard", "Woonsocket", "Corsica",
         "Wessington Springs", "Emery", "Canistota"]
COUNTIES = ["Davison County", "Hanson County", "Sanborn County", "Aurora County",
            "Jerusalem", "Douglas County"]

# Real client testimonial (used on-page and in Review schema)
TESTIMONIAL = {
    "author": "Greg Neppl",
    "org": "Dakota Custom Builders, LLC",
    "body": ("Dakota Custom Builders has worked with Mitchell Plumbing & Heating on numerous "
             "residential construction projects, and they continue to be one of our most trusted "
             "trade partners. Their team consistently delivers quality workmanship, excellent "
             "communication, and dependable service from start to finish. Whether it's a custom "
             "home, remodel, or service-related issue, they approach every project with "
             "professionalism and attention to detail. Their scheduling, responsiveness, and "
             "willingness to work collaboratively help keep our projects moving smoothly and our "
             "clients happy. In an industry where reliability matters, Mitchell Plumbing & Heating "
             "stands out. We appreciate their commitment to quality and customer service and would "
             "confidently recommend them to anyone looking for a plumbing contractor they can trust.")
}

TESTIMONIAL2 = {
    "author": "Jordan Beukelman",
    "org": "Beukelman & Associates, Mitchell SD",
    "highlight": ("Their pricing was very competitive, and they kept me informed throughout the "
                  "entire process start to finish. The work itself was high quality, too. I'd "
                  "absolutely recommend Mitchell Plumbing for both great customer service and "
                  "solid workmanship."),
    "body": ("I recently had the pleasure of working with Derek and Cody at Mitchell Plumbing to "
             "get a bid for a sewer replacement at my home. What stood out right away was their "
             "professionalism and customer service. When I called for a quote, they asked if they "
             "could meet me in person—both to shake my hand and to take precise measurements so the "
             "estimate would be accurate. We scheduled a visit for later that week, and they arrived "
             "right on time. Derek and Cody greeted me with a friendly smile and handshake, then took "
             "the time to carefully measure the project. He mentioned that quotes typically go out "
             "within about 48 hours to your email, but I was impressed to receive mine the very same "
             "day—especially since other local companies were taking much longer (2–3 weeks). Their "
             "pricing was very competitive, and once I got on their schedule, they kept me informed "
             "throughout the entire process start to finish. The work itself was high quality, too. "
             "I'd absolutely recommend Mitchell Plumbing for both great customer service and solid "
             "workmanship.")
}

# ----------------------------------------------------------------------------
# Inline SVG icons (stroke style)
# ----------------------------------------------------------------------------
def svg(d, fill=False):
    f = 'fill="currentColor" stroke="none"' if fill else 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg viewBox="0 0 24 24" {f} aria-hidden="true">{d}</svg>'

IC = {
 "phone": svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>'),
 "wrench": svg('<path d="M14.7 6.3a4 4 0 0 0 5 5l-9 9a2.83 2.83 0 0 1-4-4l9-9-1 1"/><path d="M14.7 6.3 18 3l3 3-3.3 3.3"/>'),
 "flame": svg('<path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 .5-2 .5-2S6 11 6 14a6 6 0 0 0 12 0c0-5-6-12-6-12Z"/>'),
 "snow": svg('<path d="M12 2v20M3.5 7l17 10M20.5 7l-17 10M12 2l-2.2 2.2M12 2l2.2 2.2M12 22l-2.2-2.2M12 22l2.2 2.2M3.5 7l.1 3.1M3.5 7l3-1M20.5 17l-.1-3.1M20.5 17l-3 1M20.5 7l-3-1M20.5 7l-.1 3.1M3.5 17l3 1M3.5 17l.1-3.1"/>'),
 "wind": svg('<path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h9a2.5 2.5 0 1 1-2.5 2.5"/>'),
 "ac": svg('<rect x="2" y="4" width="20" height="9" rx="2"/><path d="M6 17v.5a2 2 0 0 0 4 0M14 17a2 2 0 0 0 4 0v-.5M5 8h2M9 8h2"/>'),
 "drop": svg('<path d="M12 2.5S5 10 5 14.5a7 7 0 0 0 14 0C19 10 12 2.5 12 2.5Z"/>'),
 "clock": svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "shield": svg('<path d="M12 2 4 5v6c0 5 3.5 8.5 8 11 4.5-2.5 8-6 8-11V5Z"/><path d="m9 12 2 2 4-4"/>'),
 "star": svg('<path d="m12 3 2.6 5.3 5.9.9-4.3 4.1 1 5.9L12 16.9 6.8 19.2l1-5.9L3.5 9.2l5.9-.9Z"/>', fill=True),
 "check": svg('<path d="M20 6 9 17l-5-5"/>'),
 "pin": svg('<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/>'),
 "mail": svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
 "calendar": svg('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
 "users": svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13A4 4 0 0 1 16 11"/>'),
 "building": svg('<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>'),
 "thermo": svg('<path d="M14 14.76V5a2 2 0 0 0-4 0v9.76a4 4 0 1 0 4 0Z"/>'),
 "leaf": svg('<path d="M11 20A7 7 0 0 1 4 13c0-6 8-9 16-9 0 8-3 16-9 16Z"/><path d="M4 20c2-4 5-7 9-9"/>'),
 "tools": svg('<path d="M14.7 6.3a4 4 0 0 0 5 5l-9 9a2.83 2.83 0 0 1-4-4l9-9"/><path d="m7 17 3-3"/>'),
 "doc": svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>'),
 "download": svg('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/>'),
 "arrow-up": svg('<path d="M12 19V5M5 12l7-7 7 7"/>'),
 "facebook": svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3Z"/>', fill=True),
 "google": svg('<path d="M12 11v3h5.1c-.7 2.2-2.7 3.7-5.1 3.7A5.7 5.7 0 1 1 16 7.6l2.1-2.1A8.7 8.7 0 1 0 21 12c0-.3 0-.7-.1-1Z"/>', fill=True),
 "spark": svg('<path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l3 3M16 16l3 3M19 5l-3 3M8 16l-3 3"/>'),
 "heart": svg('<path d="M19 14c1.5-1.5 3-3.3 3-5.5A4.5 4.5 0 0 0 12 6 4.5 4.5 0 0 0 2 8.5c0 2.2 1.5 4 3 5.5l7 7Z"/>'),
}

# ----------------------------------------------------------------------------
# Structured data (LocalBusiness graph) — shared across all pages
# ----------------------------------------------------------------------------
def business_node():
    return {
        "@type": ["Plumber", "HVACBusiness", "LocalBusiness"],
        "@id": SITE_URL + "/#business",
        "name": BIZ_NAME,
        "alternateName": BIZ_ALT,
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/mph-logo.png",
        "image": [SITE_URL + "/assets/img/mph-building.jpg", SITE_URL + "/assets/img/mph-logo.png"],
        "telephone": PHONE_TEL,
        "email": EMAIL,
        "priceRange": "$$",
        "currenciesAccepted": "USD",
        "paymentAccepted": "Cash, Check, Credit Card",
        "foundingDate": FOUNDED,
        "slogan": SLOGAN,
        "description": ("Family-owned plumbing and heating contractor serving "
                        "Mitchell and Eastern South Dakota since 1990. "
                        "Residential, commercial, and government work — high-efficiency Lochinvar "
                        "boiler & hydronic heating systems, plus commercial chiller service."),
        "address": {"@type": "PostalAddress", "streetAddress": ADDR_ST, "addressLocality": ADDR_CITY,
                    "addressRegion": ADDR_STATE, "postalCode": ADDR_ZIP, "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
        "hasMap": "https://www.google.com/maps?q=%s,%s" % (GEO_LAT, GEO_LON),
        "areaServed": [{"@type": "AdministrativeArea", "name": "Eastern South Dakota"}] +
                      [{"@type": "City", "name": c + ", SD"} for c in AREAS] +
                      [{"@type": "AdministrativeArea", "name": c + ", SD"} for c in COUNTIES],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
             "opens": "08:00", "closes": "17:00"}],
        "knowsAbout": ["Hydronic heating", "Radiant floor heating", "Lochinvar boilers",
                       "Boiler installation & repair", "Water heaters", "Tankless water heaters",
                       "Drain cleaning", "Sewer line service", "Fixture installation",
                       "Commercial plumbing", "Commercial chillers", "Chiller installation & repair",
                       "New construction plumbing", "Remodel plumbing",
                       "Moen fixtures", "Delta fixtures", "Kohler fixtures", "Gerber fixtures",
                       "Sterling fixtures", "American Standard fixtures",
                       "Onyx Collection showers", "Salo fiberglass tubs & showers"],
        "sameAs": SAME_AS,
        # NOTE: self-serving aggregateRating/review markup on your own LocalBusiness
        # is disregarded (and can be flagged) by Google. Testimonials remain visible
        # on-page; rich-result stars should come from your Google Business Profile.
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
            ["Residential Plumbing", "Commercial Plumbing", "Government & Municipal Plumbing",
             "Hydronic & Radiant Heating", "Lochinvar Boiler Systems",
             "Commercial Chiller Service", "Water Heater Installation",
             "Drain & Sewer Service", "New Construction & Remodel Plumbing"]],
    }

def website_node():
    return {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/",
            "name": BIZ_NAME, "publisher": {"@id": SITE_URL + "/#business"},
            "inLanguage": "en-US"}

def jsonld(extra_nodes=None):
    graph = [business_node(), website_node()]
    if extra_nodes:
        graph.extend(extra_nodes)
    data = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)

def breadcrumb_node(crumbs, prefix):
    # crumbs: list of (name, href-or-None)
    items = []
    for i, (name, href) in enumerate(crumbs, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if href:
            el["item"] = SITE_URL + "/" + href
        items.append(el)
    return {"@type": "BreadcrumbList", "itemListElement": items}
