# -*- coding: utf-8 -*-
"""All page content + technical SEO files. Run: python pages.py"""
import os, json
from build import (SITE_URL, BIZ_NAME, PHONE_DISP, PHONE_TEL, EMAIL, ADDR_ST, ADDR_CITY,
                   ADDR_STATE, ADDR_ZIP, SLOGAN, FOUNDED, GEO_LAT, GEO_LON, AREAS, COUNTIES,
                   TESTIMONIAL, TESTIMONIAL2, IC,
                   HIRING_BANNER_ON, HIRING_BANNER_TEXT, HIRING_BANNER_CTA,
                   HIRING_BANNER_LINK)
from make import render, page_hero, service_card

P = PHONE_TEL
PD = PHONE_DISP
TEL = f'<a href="tel:{P}">{PD}</a>'

# ============================================================================
# HOME
# ============================================================================
hiring_banner = f'''
<div class="hiring-banner">
  <div class="container">
    <span class="hb-tag">Now Hiring</span>
    <span class="hb-text">{HIRING_BANNER_TEXT}</span>
    <a class="hb-link" href="{HIRING_BANNER_LINK}">{HIRING_BANNER_CTA} &rarr;</a>
  </div>
</div>''' if HIRING_BANNER_ON else ''

home_body = hiring_banner + f'''
<section class="hero">
  <div class="container">
    <div class="starburst"><span><small>Est.</small><b>1990</b><small>Mitchell SD</small></span></div>
    <div class="hero-grid">
      <div class="reveal in">
        <p class="eyebrow" style="color:#ffd98a">Mitchell, South Dakota &middot; Since 1990</p>
        <h1>Plumbing &amp; Heating Done Right<span class="script">Fast. Reliable. Clean.</span></h1>
        <p class="hero-sub">Your local, family-owned plumbing and heating experts. From a dripping faucet to a full Lochinvar boiler system &mdash; residential, commercial, and government &mdash; no job is too big or too small for Mitch&apos;s crew.</p>
        <div class="hero-cta">
          <a class="btn btn--gold btn--lg" href="tel:{P}">{IC["phone"]} Call {PD}</a>
          <a class="btn btn--ghost btn--lg" href="contact.html" style="--btn-fg:#fff;background:rgba(255,255,255,.08)">Get a Free Estimate</a>
        </div>
        <div class="hero-trust">
          <span>{IC["check"]} 35+ Years Local</span>
          <span>{IC["check"]} Licensed &amp; Insured</span>
          <span>{IC["check"]} Free Estimates</span>
        </div>
      </div>
      <div class="hero-mascot reveal in">
        <img src="assets/img/mitch-hero.png" alt="Mitch, the Mitchell Plumbing &amp; Heating mascot, running with a wrench and toolbox" width="440" height="440" fetchpriority="high">
      </div>
    </div>
  </div>
</section>

<section class="section--tight bg-cream2" style="border-bottom:3px solid var(--navy)">
  <div class="container">
    <div class="pill-row" style="justify-content:center">
      <span class="pill">{IC["drop"]} Residential</span>
      <span class="pill">{IC["building"]} Commercial</span>
      <span class="pill">{IC["shield"]} Government</span>
      <span class="pill">{IC["thermo"]} Hydronic Heat</span>
      <span class="pill">{IC["snow"]} Commercial Chillers</span>
      <span class="pill">{IC["flame"]} Lochinvar Boilers</span>
      <span class="pill">{IC["check"]} Free Estimates</span>
    </div>
  </div>
</section>

<section class="section bg-dots">
  <div class="container">
    <div class="text-center reveal">
      <p class="eyebrow">What We Do</p>
      <h2 class="section-title">One Call Does It All</h2>
      <p class="lead">Whether it&apos;s a burst pipe, no heat on a cold night, or a brand-new radiant heating system, our Mitchell technicians show up on time and get it done clean.</p>
    </div>
    <div class="grid grid-3" style="margin-top:44px">
      {service_card("drop","Plumbing Service & Repair","Leaks, clogs, water heaters, fixtures, repipes, sewer and drain lines. Fast diagnosis and a clean fix &mdash; the first time.","plumbing.html","Explore Plumbing")}
      {service_card("flame","Heating & Hydronics","Radiant in-floor heat and hydronic systems, powered by high-efficiency Lochinvar boilers &mdash; installed, serviced, and repaired to keep South Dakota winters outside.","heating.html","Explore Heating","card--coral")}
      {service_card("thermo","Lochinvar Boilers","We design, install, and service high-efficiency Lochinvar boiler systems built to last through decades of Dakota cold.","boilers.html","See Boiler Systems","card--gold")}
      {service_card("building","Commercial Plumbing","Restaurants, offices, retail, and multi-unit buildings. Code-compliant work that keeps your business running.","commercial.html","Commercial Work","card--blue")}
      {service_card("shield","Government & Municipal","Trusted partner for city, county, and public projects with the documentation and reliability the work demands.","commercial.html","Public Projects")}
      {service_card("tools","New Construction & Remodel","Builders&apos; trusted trade partner for custom homes and remodels &mdash; on schedule and on spec.","plumbing.html","Building or Remodeling?","card--coral")}
    </div>
  </div>
</section>

<section class="section bg-navy">
  <div class="container">
    <div class="split">
      <div class="split-media reveal">
        <div class="story-card">
          <span class="story-tag">Our Story</span>
          <div class="story-inner">
            <img class="story-mitch" src="assets/img/mitch-story.png" alt="Mitch the plumber pointing to the Mitchell Plumbing &amp; Heating company timeline" width="310" height="344" loading="lazy">
            <ul class="story-timeline">
              <li class="tl-gold"><b>1990</b><span><strong>It all begins.</strong> A family opens Mitchell Plumbing &amp; Heating right here on N. Rowley Street.</span></li>
              <li class="tl-teal"><b>Grew</b><span>From small home repairs to major commercial &amp; government jobs &mdash; no job too big or small.</span></li>
              <li class="tl-coral"><b>Today</b><span>Three decades on, your trusted plumbing, radiant heating &amp; Lochinvar boiler experts.</span></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="reveal">
        <p class="eyebrow">Your Hometown Pros</p>
        <h2 class="section-title">Local Since 1990 &mdash; <span class="script">and Proud of It</span></h2>
        <p class="lead">Mitchell Plumbing &amp; Heating Co. Inc. is your local, family-owned and operated plumbing and heating business. Since our inception in {FOUNDED}, we&apos;ve provided Mitchell and Eastern South Dakota with quality installation and service &mdash; from large commercial projects to small residential needs.</p>
        <ul class="checks">
          <li>Real local technicians who answer the phone &mdash; never a call center</li>
          <li>Up-front communication and clean, respectful work in your home or jobsite</li>
          <li>Decades of experience with Dakota&apos;s toughest heating challenges</li>
        </ul>
        <a class="btn btn--gold" href="about.html">Read Our Story</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-checker">
  <div class="container">
    <div class="text-center reveal">
      <p class="eyebrow">Why Neighbors Choose Mitch</p>
      <h2 class="section-title">Built On Trust</h2>
    </div>
    <div class="grid grid-4" style="margin-top:40px">
      <div class="card text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["clock"]}</div><h3>On Time, Every Time</h3><p>We respect your schedule and show up when we say we will.</p></div>
      <div class="card card--coral text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["drop"]}</div><h3>Sparkling Clean</h3><p>We treat your home like our own and leave it spotless.</p></div>
      <div class="card card--gold text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["shield"]}</div><h3>Quality Guaranteed</h3><p>Expert technicians and workmanship that stands the test of time.</p></div>
      <div class="card card--blue text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["heart"]}</div><h3>Customer First</h3><p>Friendly, honest service focused on what&apos;s right for you.</p></div>
    </div>
  </div>
</section>

<section class="section bg-navy">
  <div class="container">
    <div class="grid grid-4">
      <div class="stat reveal"><b>35+</b><span>Years in Business</span></div>
      <div class="stat reveal"><b>3</b><span>Generations Served</span></div>
      <div class="stat reveal"><b>Free</b><span>Estimates</span></div>
      <div class="stat reveal"><b>1</b><span>Trusted Local Team</span></div>
    </div>
  </div>
</section>

<section class="section bg-cream2">
  <div class="container">
    <div class="text-center reveal">
      <p class="eyebrow">In Their Words</p>
      <h2 class="section-title">Don&apos;t Just Take <span class="script">our word for it</span></h2>
    </div>
    <div class="grid grid-2" style="align-items:start;margin-top:40px">
      <div class="quote-card reveal">
        <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
        <p>&ldquo;In an industry where reliability matters, Mitchell Plumbing &amp; Heating stands out. They consistently deliver quality workmanship, excellent communication, and dependable service from start to finish. We would confidently recommend them to anyone looking for a plumbing contractor they can trust.&rdquo;</p>
        <p class="quote-author">{TESTIMONIAL["author"]}<span>{TESTIMONIAL["org"]}</span></p>
      </div>
      <div class="quote-card reveal">
        <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
        <p>&ldquo;{TESTIMONIAL2["highlight"]}&rdquo;</p>
        <p class="quote-author">{TESTIMONIAL2["author"]}<span>{TESTIMONIAL2["org"]}</span></p>
      </div>
    </div>
    <div class="text-center" style="margin-top:30px"><a class="btn btn--ghost" href="reviews.html">Read More Reviews</a></div>
  </div>
</section>
'''

home_schema = []  # business + website already global

# ============================================================================
# ABOUT
# ============================================================================
about_body = f'''
{page_hero("About Mitchell Plumbing &amp; Heating", "Family-owned, locally trusted, and proudly serving Mitchell, South Dakota and Eastern South Dakota since 1990.", "Meet the team behind the wrench")}
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Our Story</p>
        <h2 class="section-title">A Hometown Name <span class="script">Since 1990</span></h2>
        <p>Mitchell Plumbing &amp; Heating Co. Inc. is your local, family-owned and operated plumbing and heating business. Since its inception in {FOUNDED}, Mitchell Plumbing &amp; Heating has provided Mitchell and Eastern South Dakota with quality plumbing, heating, and radiant heating installation and service.</p>
        <p>From large commercial projects to small residential needs, we&apos;ve always believed in doing the job right, treating people fairly, and standing behind our work. We want to thank Mitchell and the surrounding communities for trusting us with all their plumbing and heating needs &mdash; we appreciate your business and look forward to serving you for years to come.</p>
        <div class="pill-row" style="margin-top:18px">
          <span class="pill">{IC["pin"]} {ADDR_ST}</span>
          <span class="pill">{IC["phone"]} {PD}</span>
        </div>
      </div>
      <div class="split-media reveal">
        <img src="assets/img/mph-building.jpg" alt="The Mitchell Plumbing &amp; Heating shop in Mitchell, SD" width="760" height="470" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section bg-teal">
  <div class="container">
    <div class="split split--rev">
      <div class="split-media reveal">
        <img src="assets/img/mitch-mascot-sheet.png" alt="Mitch the plumber mascot in friendly poses &mdash; waving hello, thumbs up, on his way, your comfort is my priority" width="700" height="700" loading="lazy" style="box-shadow:5px 5px 0 var(--navy);background:#fff">
      </div>
      <div class="reveal">
        <p class="eyebrow" style="color:#ffe9b0">Say Hello To</p>
        <h2 class="section-title">Meet &ldquo;Mitch&rdquo;</h2>
        <p class="lead" style="color:#eafffb">Mitch is the friendly face of our crew &mdash; and the spirit behind how we work. He&apos;s on time, he&apos;s tidy, and he treats every home and jobsite like it&apos;s his own. When you see Mitch, you know the job&apos;s going to get done right.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-dots">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">What We Stand For</p><h2 class="section-title">Our Values</h2></div>
    <div class="grid grid-4" style="margin-top:40px">
      <div class="card text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["heart"]}</div><h3>Family-Owned</h3><p>Local roots and local accountability &mdash; you&apos;re a neighbor, not a ticket number.</p></div>
      <div class="card card--coral text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["check"]}</div><h3>Do It Right</h3><p>Quality workmanship and attention to detail on every single job.</p></div>
      <div class="card card--gold text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["users"]}</div><h3>Honest Communication</h3><p>Clear answers, fair pricing, and no surprises.</p></div>
      <div class="card card--blue text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["clock"]}</div><h3>Dependable</h3><p>We show up, we follow through, and we&apos;re here when you need us.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:840px">
    <div class="quote-card reveal">
      <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
      <p>&ldquo;{TESTIMONIAL["body"]}&rdquo;</p>
      <p class="quote-author">{TESTIMONIAL["author"]}<span>{TESTIMONIAL["org"]}</span></p>
    </div>
  </div>
</section>
'''

# ============================================================================
# SERVICES (hub)
# ============================================================================
services_body = f'''
{page_hero("Our Services", "Complete plumbing and heating solutions for homes, businesses, and public projects across the Mitchell, SD area.", "Anything plumbing &amp; heating")}
<section class="section bg-dots">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">Full-Service Contractor</p><h2 class="section-title">How Can Mitch Help?</h2><p class="lead">No job is too big or too small. Here&apos;s a look at what we do &mdash; click any service to learn more.</p></div>
    <div class="grid grid-3" style="margin-top:44px">
      {service_card("heart","Residential Services","Plumbing, heating, remodels &mdash; and name-brand fixtures you pick from our vendor catalogs.","residential.html","Residential &amp; Product Lines")}
      {service_card("drop","Plumbing Service &amp; Repair","Faucets, toilets, water heaters, repipes, drain &amp; sewer cleaning, gas lines, and more.","plumbing.html","Plumbing Details","card--blue")}
      {service_card("flame","Heating &amp; Hydronics","Radiant in-floor heat and hydronic heating systems engineered for efficient, even South Dakota comfort.","heating.html","Heating &amp; Hydronics","card--coral")}
      {service_card("thermo","Lochinvar Boiler Systems","High-efficiency boiler design, installation, and service from a name built for cold climates.","boilers.html","Boiler Systems","card--gold")}
      {service_card("building","Commercial Plumbing","Reliable, code-compliant plumbing for restaurants, offices, retail, and multi-unit properties.","commercial.html","Commercial","card--blue")}
      {service_card("shield","Government &amp; Municipal","A documented, dependable partner for city, county, and public-sector work.","commercial.html","Public Projects")}
      {service_card("snow","Commercial Chillers","Chiller systems for cooling large facilities &mdash; designed, installed, serviced &amp; maintained.","commercial.html","Chiller Service","card--blue")}
      {service_card("tools","New Construction &amp; Remodel","Builders&apos; trusted trade partner for custom homes, additions, and renovations.","plumbing.html","New Builds","card--coral")}
    </div>
  </div>
</section>
<section class="section bg-cream2">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">The Mitch Difference</p>
        <h2 class="section-title">What You Can Expect</h2>
        <ul class="checks">
          <li><strong>A real person on the phone.</strong> Local technicians, local answers.</li>
          <li><strong>On-time arrival.</strong> We respect your time and your schedule.</li>
          <li><strong>A clean worksite.</strong> We tidy up like we were never there.</li>
          <li><strong>Honest, up-front pricing.</strong> You approve the plan before we start.</li>
        </ul>
        <a class="btn" href="contact.html">Request Service</a>
      </div>
      <div class="split-media reveal">
        <div class="guarantee">
          <svg class="g-seal" viewBox="0 0 400 400" role="img" aria-label="One hundred percent satisfaction guaranteed — the Mitch Promise, family-owned since 1990">
            <defs><path id="gArcTop" d="M 60,200 A 140,140 0 0 1 340,200"/></defs>
            <path d="M 200.0,7.0 L 224.3,30.7 L 254.4,14.8 L 271.0,44.5 L 304.3,37.6 L 312.0,70.8 L 345.9,73.6 L 343.9,107.6 L 375.6,119.8 L 364.1,151.8 L 391.0,172.5 L 371.0,200.0 L 391.0,227.5 L 364.1,248.2 L 375.6,280.2 L 343.9,292.4 L 345.9,326.4 L 312.0,329.2 L 304.3,362.4 L 271.0,355.5 L 254.4,385.2 L 224.3,369.3 L 200.0,393.0 L 175.7,369.3 L 145.6,385.2 L 129.0,355.5 L 95.7,362.4 L 88.0,329.2 L 54.1,326.4 L 56.1,292.4 L 24.4,280.2 L 35.9,248.2 L 9.0,227.5 L 29.0,200.0 L 9.0,172.5 L 35.9,151.8 L 24.4,119.8 L 56.1,107.6 L 54.1,73.6 L 88.0,70.8 L 95.7,37.6 L 129.0,44.5 L 145.6,14.8 L 175.7,30.7 Z" fill="#f4b63e" stroke="#15294c" stroke-width="5" stroke-linejoin="round"/>
            <circle cx="200" cy="200" r="159" fill="#15294c"/>
            <circle cx="200" cy="200" r="127" fill="#fffdf6" stroke="#15294c" stroke-width="3"/>
            <circle cx="60" cy="200" r="6" fill="#f4b63e"/>
            <circle cx="340" cy="200" r="6" fill="#f4b63e"/>
            <text class="g-arc"><textPath href="#gArcTop" startOffset="50%" text-anchor="middle">100% SATISFACTION GUARANTEED</textPath></text>
            <path d="M170,151 l18,20 l40,-46" fill="none" stroke="#e8503a" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            <text class="g-title" x="200" y="214" text-anchor="middle" font-size="37">OUR PROMISE</text>
            <text class="g-title" x="200" y="249" text-anchor="middle" font-size="37">TO YOU</text>
            <text class="g-est" x="200" y="281" text-anchor="middle" font-size="17">★ SINCE 1990 ★</text>
          </svg>
          <img class="g-mitch" src="assets/img/mitch-thumb.png" alt="Mitch the plumber giving a thumbs up" width="300" height="360" loading="lazy">
        </div>
      </div>
    </div>
  </div>
</section>
'''

# ============================================================================
# Helper: build a service detail page
# ============================================================================
def detail_intro(eyebrow, title, script, lead, bullets, img, alt, img_bg="", img_w=700, img_h=700):
    items = "".join(f"<li>{b}</li>" for b in bullets)
    return f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">{eyebrow}</p>
        <h2 class="section-title">{title} <span class="script">{script}</span></h2>
        <p class="lead">{lead}</p>
        <ul class="checks">{items}</ul>
        <a class="btn" href="contact.html">Get a Free Estimate</a>
      </div>
      <div class="split-media reveal"><img src="{img}" alt="{alt}" width="{img_w}" height="{img_h}" loading="lazy" style="{img_bg}"></div>
    </div>
  </div>
</section>'''

def services_grid(title, eyebrow, cards, bg="bg-dots"):
    c = ""
    for icon, h, b, mod in cards:
        c += f'<article class="card {mod} reveal"><div class="card-icon">{IC[icon]}</div><h3>{h}</h3><p>{b}</p></article>'
    return f'''
<section class="section {bg}">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">{eyebrow}</p><h2 class="section-title">{title}</h2></div>
    <div class="grid grid-3" style="margin-top:42px">{c}</div>
  </div>
</section>'''

# PLUMBING
plumbing_body = (
  page_hero("Plumbing Services in Mitchell, SD", "From a leaky faucet to a full repipe &mdash; residential and commercial plumbing done fast, reliable, and clean.", "Leaks, clogs, water heaters &amp; more")
  + detail_intro("Residential &amp; Commercial Plumbing", "Plumbing You Can Count On", "done right the first time",
      "When something&apos;s leaking, clogged, or just not working, you want a plumber who shows up fast and fixes it for good. Our Mitchell technicians handle everything from quick repairs to whole-home repipes &mdash; with clean, respectful work every time.",
      ["Fast, responsive local service",
       "Up-front pricing approved before we start",
       "Workmanship that lasts &mdash; backed by 35+ years"],
      "assets/img/mitch-trusted-plumber.png", "Mitch the plumber mascot flexing &mdash; Expert Technicians", "background:#fff", 410, 405)
  + services_grid("Plumbing Services We Offer", "What We Fix &amp; Install", [
      ("drop","Leak Detection &amp; Repair","Hidden leaks, dripping faucets, running toilets, and pipe repairs &mdash; found fast and fixed clean.","" ),
      ("flame","Water Heaters","Repair and installation of tank and tankless water heaters sized right for your home or business.","card--coral"),
      ("tools","Drain &amp; Sewer Cleaning","Clogged drains and sewer lines cleared with professional equipment, plus camera inspections.","card--gold"),
      ("building","Repipes &amp; New Lines","Whole-home repiping, new water and gas lines, and fixture upgrades.","card--blue"),
      ("check","Fixtures &amp; Faucets","Sinks, tubs, showers, toilets, garbage disposals, and that perfect new faucet installed right.",""),
      ("shield","Gas Lines","New gas piping and safe, code-compliant connections for ranges, dryers, and appliances.","card--coral"),
    ])
  + services_grid("Common Reasons Neighbors Call", "How Can We Help?", [
      ("drop","No Hot Water","We diagnose and repair or replace your water heater fast.",""),
      ("tools","Clogged or Slow Drains","Kitchen, bath, and main-line clogs cleared and inspected.","card--gold"),
      ("flame","Frozen or Burst Pipes","Dakota winters are tough &mdash; we thaw, repair, and prevent.","card--coral"),
    ], bg="bg-checker")
)

# RESIDENTIAL SERVICES + VENDOR PRODUCT LINES
VENDORS = [
    ("The Onyx Collection", "https://www.onyxcollection.com/",
     "Custom shower bases, wall panels, and vanity tops built to order for your bathroom."),
    ("Moen", "https://www.moen.com/",
     "Faucets, showerheads, garbage disposals, and kitchen &amp; bath fixtures."),
    ("Delta Faucet Outlet", "https://www.deltafaucet.com/outlet",
     "Recertified and discounted Delta kitchen and bathroom products."),
    ("Kohler", "https://www.kohler.com/",
     "Kitchen and bathroom fixtures &mdash; sinks, faucets, toilets, tubs &amp; more."),
    ("Gerber", "https://www.gerber-us.com/",
     "Toilets, showers, sinks, and faucets for every home."),
    ("Salo Manufacturing", "https://salomfg.com/",
     "Fiberglass showers and tubs, manufactured since 1986."),
    ("Sterling", "https://www.sterlingplumbing.com/",
     "Durable showers, tubs, toilets and more from a Kohler company."),
    ("American Standard", "https://www.americanstandard-us.com/",
     "Bathroom and kitchen fixtures, faucets, sinks, toilets and accessories."),
]
vendor_cards = "".join(f'''<article class="card reveal">
      <h3 style="color:var(--blue)">{name}</h3>
      <p>{blurb}</p>
      <a class="card-link" href="{url}" target="_blank" rel="nofollow noopener">Browse Catalog</a>
    </article>''' for name, url, blurb in VENDORS)

residential_body = f'''
{page_hero("Residential Services", "Everything your home needs from one local crew &mdash; plumbing, heating, remodels, and name-brand fixtures you pick out yourself.", "Your home, done right")}
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">For Your Home</p>
        <h2 class="section-title">One Crew For <span class="script">the whole house</span></h2>
        <p class="lead">From a dripping faucet to a full bathroom remodel or a new radiant heating system, Mitchell Plumbing &amp; Heating handles it all &mdash; installed by the same local, family-owned crew your neighbors have trusted since 1990.</p>
        <ul class="checks">
          <li><strong>Plumbing service &amp; repair</strong> &mdash; leaks, drains, water heaters, repipes</li>
          <li><strong>Radiant &amp; hydronic heating</strong> &mdash; powered by Lochinvar boilers</li>
          <li><strong>Fixtures &amp; remodels</strong> &mdash; sinks, tubs, showers, toilets &amp; faucets you choose</li>
        </ul>
        <div class="pill-row">
          <a class="btn" href="contact.html">Get a Free Estimate</a>
          <a class="btn btn--ghost" href="#product-lines">Browse Product Lines</a>
        </div>
      </div>
      <div class="split-media reveal" style="display:flex;justify-content:center">
        <img src="assets/img/mitch-thumb.png" alt="Mitch the plumber mascot giving a thumbs up for residential services" width="300" height="360" loading="lazy" style="background:var(--cream);padding:26px 22px;max-width:320px;width:100%;height:auto">
      </div>
    </div>
  </div>
</section>
<section class="section bg-dots" id="product-lines">
  <div class="container">
    <div class="text-center reveal">
      <p class="eyebrow">Pick What You Love</p>
      <h2 class="section-title">Our Product Lines</h2>
      <p class="lead center-block">We install trusted name brands &mdash; and you get to choose. Browse each vendor&apos;s catalog, jot down the products and model numbers you like, and we&apos;ll take it from there with a quote, ordering, and professional installation.</p>
    </div>
    <div class="grid grid-4" style="margin-top:42px">{vendor_cards}</div>
  </div>
</section>
<section class="section bg-cream2">
  <div class="container" style="max-width:900px">
    <div class="text-center reveal"><p class="eyebrow">How It Works</p><h2 class="section-title">Three Easy Steps</h2></div>
    <div class="grid grid-3" style="margin-top:38px">
      <div class="card text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["doc"]}</div><h3>1. Browse</h3><p>Explore the catalogs above and find the fixtures and finishes you love.</p></div>
      <div class="card card--coral text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["phone"]}</div><h3>2. Tell Mitch</h3><p>Call {PD} or <a href="contact.html">send us the list</a> &mdash; product names or model numbers work great.</p></div>
      <div class="card card--gold text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["wrench"]}</div><h3>3. We Handle It</h3><p>We quote it, order it, and install it right &mdash; fast, reliable, and clean.</p></div>
    </div>
  </div>
</section>
'''
residential_schema = [{
  "@type": "Service", "name": "Residential Plumbing, Heating & Fixture Installation",
  "serviceType": "Residential plumbing and heating",
  "provider": {"@id": SITE_URL + "/#business"},
  "areaServed": {"@type": "City", "name": "Mitchell, SD"},
  "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Residential Product Lines",
    "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Product",
      "name": n, "brand": {"@type": "Brand", "name": n}}} for n, _, _ in VENDORS]}
}]

# HEATING / COOLING / HVAC
heating_body = (
  page_hero("Heating &amp; Hydronic Systems", "Radiant in-floor heat, hydronic systems, and high-efficiency Lochinvar boilers &mdash; cozy, efficient warmth for Mitchell-area homes and businesses all winter long.", "Warm floors, warm homes")
  + detail_intro("Radiant &amp; Hydronic Heating", "Comfort From The Ground Up", "no more cold floors",
      "Hydronic heating moves warm water through your home to deliver gentle, even heat with no drafts and no noise &mdash; and it&apos;s our specialty. Powered by high-efficiency Lochinvar boilers, it&apos;s one of the most comfortable, efficient ways to heat a South Dakota home or business.",
      ["Radiant in-floor &amp; hydronic heating powered by Lochinvar boilers",
       "Even, draft-free warmth &mdash; quiet, clean, and energy-efficient",
       "Residential &amp; commercial &mdash; new construction &amp; replacement"],
      "assets/img/mitch-quality-guaranteed.png", "Mitch the plumber mascot giving a thumbs up &mdash; Quality Work Guaranteed", "background:#fff", 450, 430)
  + services_grid("Heating Services", "What We Do", [
      ("flame","Radiant In-Floor Heat","Design and installation of cozy in-floor radiant systems for new builds and remodels.","card--coral"),
      ("thermo","Boilers &amp; Hydronics","Boiler-driven hot-water heating engineered and balanced for your space.","card--gold"),
      ("leaf","High-Efficiency Upgrades","Replace aging equipment with modern, high-efficiency systems that lower your energy bills.","card--blue"),
      ("building","Snow-Melt Systems","Hydronic snow-melt for driveways, walks, and entrances &mdash; safer, ice-free winters.",""),
      ("tools","Maintenance &amp; Tune-Ups","Keep your boiler and heating system running efficiently with seasonal service and repairs.",""),
      ("shield","Shops &amp; Garages","Radiant heat for shops, garages, and additions &mdash; comfortable workspaces all winter.","card--coral"),
    ])
  + f'''
<section class="section bg-navy">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">Comfort You Can Count On</p><h2 class="section-title">The Comfortable Choice</h2></div>
    <div class="grid grid-3" style="margin-top:40px">
      <div class="card text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["flame"]}</div><h3>Even, Cozy Heat</h3><p>Warmth starts at the floor &mdash; no hot-and-cold spots, just steady comfort throughout.</p></div>
      <div class="card card--coral text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["drop"]}</div><h3>Quiet &amp; Clean</h3><p>No blowing dust or noisy fans &mdash; just silent, healthy comfort in every room.</p></div>
      <div class="card card--gold text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["leaf"]}</div><h3>Efficient &amp; Reliable</h3><p>High-efficiency systems and seasonal tune-ups that lower bills and prevent breakdowns.</p></div>
    </div>
  </div>
</section>'''
)

# BOILERS
boilers_body = (
  page_hero("Lochinvar Boiler Systems", "We feature high-efficiency Lochinvar boilers &mdash; designed, installed, and serviced to outlast the Dakota cold.", "Built for serious winters")
  + f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Featured Manufacturer</p>
        <h2 class="section-title">Powered By <span class="script">Lochinvar</span></h2>
        <p class="lead">Mitchell Plumbing &amp; Heating proudly features Lochinvar boiler systems &mdash; a leader in high-efficiency, reliable hot-water and hydronic heating. We help you choose the right unit, install it to spec, and keep it running for the long haul.</p>
        <ul class="checks">
          <li>High-efficiency condensing boilers that cut energy costs</li>
          <li>Properly sized and engineered for your home or building</li>
          <li>Expert installation plus ongoing maintenance and repair</li>
        </ul>
        <div class="pill-row">
          <a class="btn btn--blue" href="contact.html">Ask About a Boiler</a>
          <a class="btn btn--ghost" href="https://www.lochinvar.com/products/" rel="nofollow noopener" target="_blank">{IC["doc"]} Browse Lochinvar Catalog</a>
        </div>
      </div>
      <div class="split-media reveal" style="display:grid;place-items:center;background:var(--navy);border:4px solid var(--navy);border-radius:26px;box-shadow:5px 5px 0 var(--coral-deep);padding:60px 44px">
        <img src="assets/img/lochinvar-logo.png" alt="Lochinvar boiler systems logo" width="360" height="66" loading="lazy" style="border:none;box-shadow:none;border-radius:0;width:100%;max-width:360px;height:auto">
        <p class="tag-area" style="margin:20px 0 0;text-align:center;color:#c5d2ee">High-Efficiency Boilers &amp; Water Heaters</p>
      </div>
    </div>
  </div>
</section>'''
  + services_grid("Boiler &amp; Hydronic Services", "Design, Install, Maintain", [
      ("thermo","Boiler Installation","Professional sizing and installation of new high-efficiency Lochinvar systems.",""),
      ("tools","Boiler Repair","Fast diagnosis and repair to restore heat and efficiency.","card--coral"),
      ("clock","Seasonal Maintenance","Annual tune-ups that extend equipment life and prevent breakdowns.","card--gold"),
      ("flame","System Replacement","Upgrade aging or oversized boilers to modern, money-saving units.","card--blue"),
      ("drop","Domestic Hot Water","Boiler-integrated hot water and indirect tanks for endless supply.",""),
      ("building","Commercial Boilers","Right-sized commercial boiler solutions for businesses and facilities.","card--coral"),
    ])
  + f'''
<section class="section bg-cream2">
  <div class="container" style="max-width:820px;text-align:center">
    <div class="reveal">
      <p class="eyebrow">Vendor Catalogs</p>
      <h2 class="section-title">Browse Product Catalogs</h2>
      <p class="lead center-block">Want to see the equipment we install? Explore our featured vendor&apos;s official product catalog, then call us and we&apos;ll help you pick the perfect fit.</p>
      <div class="grid grid-2" style="margin-top:34px;text-align:left">
        <article class="card reveal"><div class="card-icon">{IC["download"]}</div><h3>Lochinvar Boilers &amp; Water Heaters</h3><p>Residential and commercial condensing boilers, water heaters, and hydronic equipment.</p><a class="card-link" href="https://www.lochinvar.com/products/" rel="nofollow noopener" target="_blank">View Catalog</a></article>
        <article class="card card--gold reveal"><div class="card-icon">{IC["phone"]}</div><h3>Not Sure What You Need?</h3><p>Tell us about your space and budget &mdash; we&apos;ll recommend the right system and give you a free estimate.</p><a class="card-link" href="contact.html">Ask Mitch</a></article>
      </div>
    </div>
  </div>
</section>'''
)

# COMMERCIAL
commercial_body = (
  page_hero("Commercial &amp; Government Plumbing &amp; Heating", "A documented, dependable plumbing, heating &amp; mechanical partner for businesses, builders, and public projects &mdash; any size, any sector.", "Big jobs, handled")
  + detail_intro("Commercial &amp; Public Sector", "No Job Too Big", "or too small",
      "From restaurants and retail to offices, multi-unit housing, and municipal facilities, we deliver code-compliant plumbing, heating, and commercial chiller service that keeps operations running. Builders and general contractors count on us as a trusted trade partner &mdash; on schedule, on spec, and on budget.",
      ["Commercial, government, and new-construction experience",
       "Reliable scheduling and clear communication",
       "Documentation and professionalism public work demands"],
      "assets/img/mitch-on-time.png", "Mitch the plumber mascot with a wrench and calendar &mdash; On Time, Every Time", "background:#fff", 430, 425)
  + services_grid("Sectors We Serve", "Who We Work With", [
      ("building","Restaurants &amp; Retail","Grease lines, fixtures, water heaters, and fast service that protects your hours.",""),
      ("users","Offices &amp; Multi-Unit","Reliable plumbing and heating for office buildings, apartments, and condos.","card--coral"),
      ("shield","Government &amp; Municipal","Dependable, documented work for city, county, and public-sector projects.","card--gold"),
      ("tools","General Contractors","A trusted trade partner for custom homes, commercial builds, and remodels.","card--blue"),
      ("snow","Commercial Chillers","Commercial chiller systems for cooling large facilities, plus boiler &amp; hydronic heating &mdash; designed, installed, serviced &amp; maintained.",""),
      ("clock","Service Contracts","Scheduled maintenance to keep your building&apos;s systems running year-round.","card--coral"),
    ])
  + f'''
<section class="section bg-cream2">
  <div class="container" style="max-width:860px">
    <div class="quote-card reveal">
      <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
      <p>&ldquo;{TESTIMONIAL["body"]}&rdquo;</p>
      <p class="quote-author">{TESTIMONIAL["author"]}<span>{TESTIMONIAL["org"]}</span></p>
    </div>
  </div>
</section>'''
)

# ============================================================================
# SERVICE AREA (GEO)
# ============================================================================
area_chips = "".join(f'<span class="pill">{IC["pin"]} {a}, SD</span>' for a in AREAS)
county_chips = "".join(f'<span class="pill">{IC["shield"]} {c}</span>' for c in COUNTIES if "Jerusalem" not in c)
service_area_body = f'''
{page_hero("Service Area", "Proudly serving Mitchell and Eastern South Dakota &mdash; if you&apos;re in our neck of the prairie, we&apos;ve got you covered.", "Your neighborhood plumber")}
<section class="section bg-dots">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Where We Work</p>
        <h2 class="section-title">Based In Mitchell, <span class="script">serving the region</span></h2>
        <p class="lead">Our shop is right here at {ADDR_ST} in {ADDR_CITY}, {ADDR_STATE}. From there, our trucks reach homes, businesses, and jobsites across Davison County and Eastern South Dakota. Don&apos;t see your town? Give us a call &mdash; chances are we&apos;re already nearby.</p>
        <p class="pill-row"><a class="btn" href="tel:{P}">{IC["phone"]} Call {PD}</a></p>
      </div>
      <div class="reveal">
        <div class="card" style="padding:0;overflow:hidden">
          <iframe title="Map of Mitchell, South Dakota service area" width="100%" height="340" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
            src="https://www.openstreetmap.org/export/embed.html?bbox=-98.30%2C43.62%2C-97.76%2C43.80&amp;layer=mapnik&amp;marker=43.7094%2C-98.0298"></iframe>
          <div style="padding:16px 18px"><strong>{BIZ_NAME}</strong><br>{ADDR_ST}, {ADDR_CITY}, {ADDR_STATE} {ADDR_ZIP}<br><a href="https://www.google.com/maps?q={GEO_LAT},{GEO_LON}" target="_blank" rel="noopener">Open in Google Maps &rarr;</a></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section bg-cream2">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">Cities &amp; Towns</p><h2 class="section-title">Communities We Serve</h2></div>
    <div class="pill-row reveal" style="justify-content:center;margin-top:30px;max-width:900px;margin-inline:auto">{area_chips}</div>
    <div class="text-center reveal" style="margin-top:36px"><p class="eyebrow">Counties</p></div>
    <div class="pill-row reveal" style="justify-content:center;margin-top:12px">{county_chips}</div>
    <p class="text-center tag-area reveal" style="margin-top:30px">&hellip; and communities across Eastern South Dakota. Not listed? <a href="contact.html">Just ask</a> &mdash; we travel.</p>
  </div>
</section>
'''

# ============================================================================
# REVIEWS
# ============================================================================
extra_reviews = [
    ("A custom home, a remodel, or a service call &mdash; they approach every project with professionalism and attention to detail. Their scheduling and responsiveness keep our projects moving smoothly.", "Greg Neppl", "Dakota Custom Builders, LLC"),
    ("Family-owned and operated since 1990, providing Mitchell and the surrounding communities with quality plumbing and radiant heating installation and service.", "Our Promise To You", "Mitchell Plumbing &amp; Heating"),
]
reviews_cards = f'''
<div class="quote-card reveal" style="grid-column:1/-1">
  <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
  <p>&ldquo;{TESTIMONIAL["body"]}&rdquo;</p>
  <p class="quote-author">{TESTIMONIAL["author"]}<span>{TESTIMONIAL["org"]}</span></p>
</div>
<div class="quote-card reveal" style="grid-column:1/-1">
  <div class="stars" aria-label="5 out of 5 stars">{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}{IC["star"]}</div>
  <p>&ldquo;{TESTIMONIAL2["body"]}&rdquo;</p>
  <p class="quote-author">{TESTIMONIAL2["author"]}<span>{TESTIMONIAL2["org"]}</span></p>
</div>'''
reviews_body = f'''
{page_hero("Reviews &amp; Testimonials", "Don&apos;t just take our word for it &mdash; hear from the builders and neighbors who trust Mitchell Plumbing &amp; Heating.", "Rated by the people who matter")}
<section class="section bg-dots">
  <div class="container">
    <div class="grid grid-2" style="align-items:start">{reviews_cards}</div>
    <div class="text-center" style="margin-top:40px">
      <p class="lead center-block">Worked with us recently? We&apos;d love to hear about it &mdash; and so would your neighbors.</p>
      <a class="btn btn--gold" href="https://www.google.com/search?q=Mitchell+Plumbing+and+Heating+Mitchell+SD" target="_blank" rel="noopener">{IC["google"]} Leave a Google Review</a>
    </div>
  </div>
</section>
<section class="section bg-navy">
  <div class="container">
    <div class="grid grid-4">
      <div class="stat reveal"><b>5.0</b><span>Customer Rating</span></div>
      <div class="stat reveal"><b>35+</b><span>Years Trusted</span></div>
      <div class="stat reveal"><b>100%</b><span>Local &amp; Family-Owned</span></div>
      <div class="stat reveal"><b>Free</b><span>Estimates</span></div>
    </div>
  </div>
</section>
'''

# ============================================================================
# FAQ (with FAQPage schema)
# ============================================================================
FAQS = [
  ("Do you handle both residential and commercial work?",
   "Yes. Mitchell Plumbing &amp; Heating serves residential, commercial, and government customers. From a small home repair to a large commercial boiler system, no job is too big or too small."),
  ("What areas do you serve?",
   f"We&apos;re based in Mitchell, SD and serve communities across Eastern South Dakota, including {', '.join(AREAS[:8])} and the rest of Davison County and nearby areas. If you&apos;re not sure, just call {PD}."),
  ("What kind of heating systems do you install?",
   "We install, service, and repair radiant in-floor and hydronic heating and high-efficiency Lochinvar boiler systems for homes and businesses."),
  ("Do you do air conditioning or cooling?",
   "We focus on plumbing and heating, so we don&apos;t install or service residential air conditioning. For commercial customers, we do install and service commercial chiller systems &mdash; give us a call to talk through your building&apos;s needs."),
  ("Why choose hydronic or radiant heating?",
   "Hydronic systems deliver even, draft-free warmth that&apos;s quiet, clean, and energy-efficient &mdash; ideal for South Dakota winters. They&apos;re great for whole homes, additions, shops, and garages."),
  ("Are you licensed and insured?",
   "Yes. We&apos;re a licensed, insured, family-owned business that&apos;s served the Mitchell area since 1990."),
  ("Do you give free estimates?",
   "Yes. Tell us about your project and we&apos;ll provide a free estimate with honest, up-front pricing before any work begins."),
  ("How long have you been in business?",
   "Since 1990 &mdash; over 35 years serving Mitchell and Eastern South Dakota."),
]
faq_items = "".join(
  f'<div class="faq-item reveal"><button class="faq-q" id="faq{i}">{q}</button><div class="faq-a"><div class="faq-a-inner">{a}</div></div></div>'
  for i,(q,a) in enumerate(FAQS))
faq_body = f'''
{page_hero("Frequently Asked Questions", "Quick answers about our plumbing and heating services, service area, and what to expect.", "Good questions, straight answers")}
<section class="section bg-dots">
  <div class="container" style="max-width:840px">
    {faq_items}
    <div class="text-center" style="margin-top:34px">
      <p class="lead center-block">Still have a question? Mitch is happy to help.</p>
      <a class="btn" href="tel:{P}">{IC["phone"]} Call {PD}</a>
    </div>
  </div>
</section>
'''
faq_schema = [{
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": q.replace("&apos;","'").replace("&amp;","&"),
     "acceptedAnswer": {"@type": "Answer", "text": a.replace("&apos;","'").replace("&amp;","&").replace("&mdash;","—")}}
    for q,a in FAQS]
}]

# ============================================================================
# CONTACT
# ============================================================================
contact_body = f'''
{page_hero("Contact Us", "Ready to get started? Reach out for fast, friendly service and a free estimate.", "Let&apos;s get it fixed")}
<section class="section bg-dots">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Get In Touch</p>
        <h2 class="section-title">Talk To A Real Local Pro</h2>
        <div class="grid" style="gap:22px;margin-top:10px">
          <div class="info-tile"><div class="ico">{IC["phone"]}</div><div><h3>Call or Text</h3><a href="tel:{P}"><strong>{PD}</strong></a></div></div>
          <div class="info-tile"><div class="ico">{IC["mail"]}</div><div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
          <div class="info-tile"><div class="ico">{IC["pin"]}</div><div><h3>Visit Us</h3>{ADDR_ST}<br>{ADDR_CITY}, {ADDR_STATE} {ADDR_ZIP}</div></div>
          <div class="info-tile"><div class="ico">{IC["clock"]}</div><div><h3>Hours</h3>Mon&ndash;Fri 8:00am&ndash;5:00pm</div></div>
        </div>
        <div class="card" style="padding:0;overflow:hidden;margin-top:26px">
          <iframe title="Map to Mitchell Plumbing &amp; Heating" width="100%" height="260" style="border:0;display:block" loading="lazy"
            src="https://www.openstreetmap.org/export/embed.html?bbox=-98.10%2C43.68%2C-97.95%2C43.74&amp;layer=mapnik&amp;marker=43.7094%2C-98.0298"></iframe>
        </div>
      </div>
      <div class="reveal">
        <form class="form-card" data-quote-form action="#" method="post" novalidate>
          <h2 style="font-family:var(--font-head);text-transform:uppercase;margin-bottom:4px">Request a Free Estimate</h2>
          <p class="form-note" style="margin-bottom:18px">Fill this out and Mitch will get right back to you. <span class="req">*</span> required.</p>
          <div class="grid grid-2" style="gap:0 18px">
            <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="phone">Phone <span class="req">*</span></label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
          </div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"></div>
          <div class="field"><label for="service">How can we help?</label>
            <select id="service" name="service">
              <option value="">Choose a service&hellip;</option>
              <option>Plumbing repair or install</option>
              <option>Water heater</option>
              <option>Drain or sewer</option>
              <option>Commercial chiller / cooling</option>
              <option>Hydronic / radiant heating</option>
              <option>Lochinvar boiler</option>
              <option>Commercial or government project</option>
              <option>New construction / remodel</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field"><label for="message">Project details</label><textarea id="message" name="message" placeholder="Tell us what&apos;s going on, your address or town, and the best time to reach you."></textarea></div>
          <button class="btn btn--lg" type="submit" style="width:100%">Send My Request</button>
          <p class="form-status" role="status" aria-live="polite"></p>
          <p class="form-note" style="margin-top:10px">Prefer to talk? Call <a href="tel:{P}"><strong>{PD}</strong></a> &mdash; a real local technician will answer.</p>
        </form>
      </div>
    </div>
  </div>
</section>
'''
contact_schema = [{
  "@type": "ContactPage", "@id": SITE_URL + "/contact.html",
  "name": "Contact " + BIZ_NAME, "url": SITE_URL + "/contact.html"
}]

# ============================================================================
# CAREERS
# ============================================================================
careers_body = f'''
{page_hero("Careers", "Build a career in the trades with a family-owned crew that&apos;s been part of Mitchell since 1990.", "Come work with Mitch")}
<section class="section bg-dots">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Join Mitch&apos;s Crew</p>
        <h2 class="section-title">Good Work. <span class="script">Good people.</span></h2>
        <p class="lead">Plumbing and heating is honest, skilled work that every community needs &mdash; and at Mitchell Plumbing &amp; Heating, it comes with a team that treats you like family. We&apos;ve served Mitchell and Eastern South Dakota since 1990, and we&apos;re proud of the crew that makes it happen.</p>
        <ul class="checks">
          <li><strong>Learn a real trade.</strong> Work alongside experienced plumbing &amp; heating pros.</li>
          <li><strong>Serve your neighbors.</strong> Local work in Mitchell and the surrounding communities.</li>
          <li><strong>Family-owned values.</strong> Do the job right, treat people fairly, stand behind your work.</li>
        </ul>
        <div class="pill-row">
          <span class="pill">{IC["wrench"]} Plumbing</span>
          <span class="pill">{IC["flame"]} Heating &amp; Hydronics</span>
          <span class="pill">{IC["users"]} Apprentice-Friendly</span>
        </div>
      </div>
      <div class="split-media reveal" style="display:flex;justify-content:center">
        <img src="assets/img/mitch-thumb.png" alt="Mitch the plumber mascot giving a thumbs up &mdash; join the Mitchell Plumbing &amp; Heating team" width="300" height="360" loading="lazy" style="background:var(--cream);padding:26px 22px;max-width:320px;width:100%;height:auto">
      </div>
    </div>
  </div>
</section>
<section class="section bg-cream2">
  <div class="container" style="max-width:900px">
    <div class="text-center reveal">
      <p class="eyebrow">Interested?</p>
      <h2 class="section-title">How To Apply</h2>
      <p class="lead center-block">We don&apos;t have any openings posted right now &mdash; but we&apos;re always glad to meet skilled, dependable people. Introduce yourself and we&apos;ll keep you in mind.</p>
    </div>
    <div class="grid grid-3" style="margin-top:38px">
      <div class="card text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["mail"]}</div><h3>Email Us</h3><p>Send a note about yourself and your experience to<br><a href="mailto:{EMAIL}?subject=Careers%20at%20Mitchell%20Plumbing%20%26%20Heating"><strong>{EMAIL}</strong></a></p></div>
      <div class="card card--coral text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["phone"]}</div><h3>Call Us</h3><p>Talk to a real person about working here.<br><a href="tel:{P}"><strong>{PD}</strong></a></p></div>
      <div class="card card--gold text-center reveal"><div class="card-icon" style="margin-inline:auto">{IC["pin"]}</div><h3>Stop By</h3><p>Come say hello at the shop.<br><strong>{ADDR_ST}, {ADDR_CITY}, {ADDR_STATE} {ADDR_ZIP}</strong></p></div>
    </div>
  </div>
</section>
'''
careers_schema = [{
  "@type": "WebPage", "@id": SITE_URL + "/careers.html",
  "name": "Careers at " + BIZ_NAME, "url": SITE_URL + "/careers.html",
  "description": "Career opportunities in plumbing and heating with Mitchell Plumbing & Heating in Mitchell, SD."
}]

# ============================================================================
# BLOG INDEX + first post
# ============================================================================
POSTS = [
  {"slug":"blog/hydronic-heating-south-dakota-winters.html",
   "title":"Why Hydronic Heating Is the Smart Choice for South Dakota Winters",
   "seo_title":"Hydronic Heating for South Dakota Winters | Mitchell P&H",
   "desc":"Even, efficient, draft-free warmth: how hydronic and radiant in-floor heating keep Mitchell-area homes cozy all winter — and save on energy bills.",
   "date":"2026-05-22","date_disp":"May 22, 2026",
   "excerpt":"If you've ever walked across a cold tile floor on a January morning in Mitchell, you already understand the appeal of radiant heat. Here's how hydronic systems work and why they're worth it."},
]
def blog_card(p, prefix=""):
    return f'''<article class="card reveal">
      <div class="card-icon card--coral" style="background:var(--coral)">{IC["flame"]}</div>
      <p class="tag-area" style="margin-bottom:6px">{p["date_disp"]} &middot; Heating</p>
      <h3>{p["title"]}</h3>
      <p>{p["excerpt"]}</p>
      <a class="card-link" href="{prefix}{p["slug"].split("/")[-1]}">Read Article</a>
    </article>'''

blog_index_body = f'''
{page_hero("The Mitch Blog", "Tips, guides, and straight talk on plumbing, heating, and keeping your South Dakota home comfortable.", "From the shop")}
<section class="section bg-dots">
  <div class="container">
    <div class="text-center reveal"><p class="eyebrow">Latest Articles</p><h2 class="section-title">Helpful Reads</h2></div>
    <div class="grid grid-3" style="margin-top:42px">
      {"".join(blog_card(p) for p in POSTS)}
      <article class="card card--gold reveal"><div class="card-icon">{IC["spark"]}</div><h3>More On The Way</h3><p>We publish seasonal tips and how-tos on a regular schedule. Check back soon &mdash; or call Mitch with your question anytime.</p><a class="card-link" href="../contact.html">Ask a Question</a></article>
    </div>
  </div>
</section>
'''

post0 = POSTS[0]
post_body = f'''
<article>
<section class="page-hero">
  <div class="container" style="max-width:820px">
    <p class="eyebrow" style="color:#ffd98a">Heating &middot; {post0["date_disp"]}</p>
    <h1>{post0["title"]}</h1>
    <p>By the team at {BIZ_NAME}</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:760px">
    <div class="reveal maxw-prose center-block">
      <p class="lead">If you&apos;ve ever stepped onto a cold tile floor on a January morning in Mitchell, you already understand the appeal of radiant heat. Hydronic heating &mdash; warming your home by moving heated water rather than blowing hot air &mdash; is one of the most comfortable and efficient ways to beat a South Dakota winter.</p>
      <h2 class="section-title" style="font-size:1.8rem;margin-top:30px">How Hydronic Heating Works</h2>
      <p>A boiler (we feature high-efficiency <a href="../boilers.html">Lochinvar systems</a>) heats water, which is then circulated through tubing in your floors or through radiators and baseboards. The warmth radiates gently and evenly into the room. There are no blowing fans, no ductwork distributing dust, and no hot-and-cold spots &mdash; just steady, quiet comfort.</p>
      <h2 class="section-title" style="font-size:1.8rem;margin-top:30px">Four Reasons Dakota Homeowners Love It</h2>
      <ul class="checks">
        <li><strong>Even warmth.</strong> Heat starts at the floor &mdash; right where you want it &mdash; instead of collecting at the ceiling.</li>
        <li><strong>Efficiency.</strong> Water carries heat far more effectively than air, so modern hydronic systems can lower your energy bills.</li>
        <li><strong>Quiet &amp; clean.</strong> No noisy blowers and no blown dust circulating through your home.</li>
        <li><strong>Versatile.</strong> Perfect for whole homes, additions, basements, shops, and garages &mdash; and even driveway snow-melt.</li>
      </ul>
      <h2 class="section-title" style="font-size:1.8rem;margin-top:30px">Is It Right for Your Home?</h2>
      <p>Radiant and hydronic systems shine in new construction and remodels, but they can fit many existing homes too. The key is a properly sized boiler and a system engineered for your space &mdash; which is exactly what our crew has done across the Mitchell area since 1990. We&apos;ll walk your home, talk through your goals and budget, and give you an honest, free estimate.</p>
      <div class="hr-fancy"></div>
      <p><strong>Thinking about warmer floors this winter?</strong> Learn more about our <a href="../heating.html">heating &amp; hydronic services</a> and <a href="../boilers.html">Lochinvar boilers</a>, or <a href="../contact.html">request a free estimate</a>. Questions? Call Mitch at <a href="tel:{P}">{PD}</a>.</p>
    </div>
  </div>
</section>
</article>
'''
post_schema = [{
  "@type":"BlogPosting","@id":SITE_URL+"/"+post0["slug"],
  "headline":post0["title"],"description":post0["desc"],
  "datePublished":post0["date"],"dateModified":post0["date"],
  "image":SITE_URL+"/assets/img/mitch-hero.png",
  "author":{"@type":"Organization","name":BIZ_NAME},
  "publisher":{"@id":SITE_URL+"/#business"},
  "mainEntityOfPage":SITE_URL+"/"+post0["slug"],
  "inLanguage":"en-US"
}]

# ============================================================================
# THANK-YOU + 404
# ============================================================================
thankyou_body = f'''
<section class="page-hero"><div class="container"><h1>Thanks &mdash; We&apos;ve Got It!</h1><p>Mitch received your request and a real local technician will be in touch within one business day.</p></div></section>
<section class="section text-center"><div class="container" style="max-width:640px">
  <div class="seal center-block" style="margin-bottom:24px"><span><b>{IC["check"]}</b><small>On Its Way</small></span></div>
  <p class="lead center-block">Need help right now? Give us a call.</p>
  <a class="btn btn--lg" href="tel:{P}">{IC["phone"]} {PD}</a>
  <p style="margin-top:24px"><a href="index.html">&larr; Back to Home</a></p>
</div></section>
'''
notfound_body = f'''
<section class="page-hero"><div class="container"><p class="eyebrow" style="color:#ffd98a">Error 404</p><h1>This Pipe Goes Nowhere</h1><p>We couldn&apos;t find that page &mdash; but Mitch can still help you find what you need.</p></div></section>
<section class="section text-center"><div class="container" style="max-width:680px">
  <p class="lead center-block">Try one of these instead:</p>
  <div class="pill-row" style="justify-content:center;margin:20px 0 30px">
    <a class="pill" href="index.html">{IC["check"]} Home</a>
    <a class="pill" href="services.html">{IC["wrench"]} Services</a>
    <a class="pill" href="boilers.html">{IC["thermo"]} Boilers</a>
    <a class="pill" href="contact.html">{IC["phone"]} Contact</a>
  </div>
  <a class="btn btn--lg" href="tel:{P}">{IC["phone"]} Call {PD}</a>
</div></section>
'''

# ============================================================================
# Crumb helpers
# ============================================================================
def cr(*pairs): return list(pairs)
HOME = ("Home","index.html")

# ============================================================================
# RENDER ALL
# ============================================================================
PAGES = [
 ("index.html", dict(title="Mitchell Plumbing & Heating | Boilers & Hydronic Heat, SD",
    desc="Family-owned plumbing & heating in Mitchell, SD since 1990 — radiant & hydronic heating, Lochinvar boilers & free estimates. Call (605) 996-7583.",
    canonical="index.html", body=home_body, cta=True)),
 ("about.html", dict(title="About Us | Mitchell Plumbing & Heating — Local Since 1990",
    desc="Meet Mitchell Plumbing & Heating: a family-owned plumbing & heating company serving Mitchell, SD since 1990. Meet Mitch and learn what we stand for.",
    canonical="about.html", body=about_body, crumbs=cr(HOME,("About",None)))),
 ("services.html", dict(title="Plumbing & Heating Services | Mitchell, SD",
    desc="Plumbing & heating in Mitchell, SD — repairs, water heaters, drains, radiant & hydronic heating, Lochinvar boilers & commercial work. Free estimates.",
    canonical="services.html", body=services_body, crumbs=cr(HOME,("Services",None)))),
 ("plumbing.html", dict(title="Plumbing Services in Mitchell, SD | Repairs & Drains",
    desc="Fast, clean plumbing in Mitchell, SD: leak repair, water heaters, drain & sewer cleaning, repipes & free estimates. Call (605) 996-7583.",
    canonical="plumbing.html", body=plumbing_body, crumbs=cr(HOME,("Services","services.html"),("Plumbing",None)),
    schema=[{"@type":"Service","name":"Plumbing Services","serviceType":"Plumbing","provider":{"@id":SITE_URL+"/#business"},"areaServed":{"@type":"City","name":"Mitchell, SD"}}])),
 ("residential.html", dict(title="Residential Services & Product Lines | Mitchell, SD",
    desc="Residential plumbing, heating & fixtures in Mitchell, SD. Browse product lines from Moen, Delta, Kohler, Onyx, Gerber, Salo, Sterling & American Standard — we quote, order & install.",
    canonical="residential.html", body=residential_body, schema=residential_schema,
    crumbs=cr(HOME,("Services","services.html"),("Residential Services",None)))),
 ("heating.html", dict(title="Heating & Hydronic Systems in Mitchell, SD | Boilers",
    desc="Radiant & hydronic heating in Mitchell, SD: in-floor heat, hydronic systems & high-efficiency Lochinvar boilers — install, service & repair. Free estimates.",
    canonical="heating.html", body=heating_body, crumbs=cr(HOME,("Services","services.html"),("Heating & Hydronics",None)),
    schema=[{"@type":"Service","name":"Heating & Hydronic Systems","serviceType":"Heating","provider":{"@id":SITE_URL+"/#business"},"areaServed":{"@type":"City","name":"Mitchell, SD"},
             "hasOfferCatalog":{"@type":"OfferCatalog","name":"Heating Services","itemListElement":[
               {"@type":"Offer","itemOffered":{"@type":"Service","name":"Radiant & Hydronic Heating"}},
               {"@type":"Offer","itemOffered":{"@type":"Service","name":"Lochinvar Boiler Systems"}}]}}])),
 ("boilers.html", dict(title="Lochinvar Boiler Systems | Mitchell, SD",
    desc="High-efficiency Lochinvar boiler systems designed, installed & serviced in Mitchell, SD. Get a free estimate — call (605) 996-7583.",
    canonical="boilers.html", body=boilers_body, crumbs=cr(HOME,("Services","services.html"),("Lochinvar Boilers",None)),
    schema=[{"@type":"Service","name":"Lochinvar Boiler Installation & Service","serviceType":"Boiler installation","provider":{"@id":SITE_URL+"/#business"},"brand":"Lochinvar","areaServed":{"@type":"City","name":"Mitchell, SD"}}])),
 ("commercial.html", dict(title="Commercial & Government Plumbing & Heating | Mitchell, SD",
    desc="Commercial & government plumbing, heating & chiller service in Mitchell, SD — code-compliant, dependable work for builders, businesses & public projects.",
    canonical="commercial.html", body=commercial_body, crumbs=cr(HOME,("Services","services.html"),("Commercial & Government",None)),
    schema=[{"@type":"Service","name":"Commercial & Government Plumbing","serviceType":"Commercial plumbing","provider":{"@id":SITE_URL+"/#business"},"areaServed":{"@type":"City","name":"Mitchell, SD"}}])),
 ("service-area.html", dict(title="Service Area | Mitchell, SD & Surrounding Communities",
    desc="Mitchell Plumbing & Heating serves Mitchell & Eastern South Dakota — Mount Vernon, Ethan, Alexandria, Parkston, Plankinton & more. See the list.",
    canonical="service-area.html", body=service_area_body, crumbs=cr(HOME,("Service Area",None)))),
 ("reviews.html", dict(title="Reviews & Testimonials | Mitchell Plumbing & Heating",
    desc="See why builders and neighbors trust Mitchell Plumbing & Heating. Read testimonials from clients across the Mitchell, SD area and leave your own review.",
    canonical="reviews.html", body=reviews_body, crumbs=cr(HOME,("Reviews",None)))),
 ("faq.html", dict(title="FAQ | Mitchell Plumbing & Heating — Mitchell, SD",
    desc="Answers about Mitchell Plumbing & Heating: services, service area, radiant & hydronic heating, boilers & free estimates in Mitchell, SD.",
    canonical="faq.html", body=faq_body, schema=faq_schema, crumbs=cr(HOME,("FAQ",None)))),
 ("contact.html", dict(title="Contact | Free Estimate | Mitchell Plumbing & Heating",
    desc="Contact Mitchell Plumbing & Heating for fast, friendly service and a free estimate. Call (605) 996-7583 or request service online.",
    canonical="contact.html", body=contact_body, schema=contact_schema, crumbs=cr(HOME,("Contact",None)))),
 ("careers.html", dict(title="Careers | Mitchell Plumbing & Heating — Mitchell, SD",
    desc="Interested in a plumbing or heating career in Mitchell, SD? Meet Mitchell Plumbing & Heating — a family-owned crew serving Eastern South Dakota since 1990.",
    canonical="careers.html", body=careers_body, schema=careers_schema, crumbs=cr(HOME,("Careers",None)))),
 ("thank-you.html", dict(title="Thank You | Mitchell Plumbing & Heating",
    desc="Thanks for contacting Mitchell Plumbing & Heating. We'll be in touch within one business day. Questions? Call (605) 996-7583.",
    canonical="thank-you.html", body=thankyou_body, cta=False, robots="noindex, follow")),
 ("404.html", dict(title="Page Not Found | Mitchell Plumbing & Heating",
    desc="The page you were looking for could not be found. Explore our plumbing and heating services or contact Mitchell Plumbing & Heating in Mitchell, SD.",
    canonical="404.html", body=notfound_body, cta=False, robots="noindex, follow")),
 ("blog/index.html", dict(title="Blog | Plumbing & Heating Tips | Mitchell Plumbing & Heating",
    desc="Plumbing and heating tips, guides, and seasonal advice for South Dakota homeowners from the team at Mitchell Plumbing & Heating.",
    canonical="blog/index.html", body=blog_index_body, prefix="../", crumbs=cr(HOME,("Blog",None)))),
 (post0["slug"], dict(title=post0["seo_title"],
    desc=post0["desc"], canonical=post0["slug"], body=post_body, prefix="../", schema=post_schema,
    og_type="article", og_image="assets/img/mitch-hero.png",
    crumbs=cr(HOME,("Blog","blog/index.html"),("Hydronic Heating",None)))),
]

for fname, cfg in PAGES:
    render(fname, cfg)
    print("  +", fname)

print("Rendered", len(PAGES), "pages.")
