# Mitchell Plumbing & Heating — Website

Retro 1950s look, modern build. Static HTML/CSS/JS — fast, accessible, and built to climb
search rankings (SEO) and answer-engine results (AEO/GEO/AIO). Host it anywhere: Netlify,
GitHub Pages, Cloudflare Pages, IIS, or Apache. No database, no server code required.

**Brand:** *Fast. Reliable. Clean.* · Est. 1990 · Mitchell, SD · Mascot: "Mitch"

---

## What's here

```
site/
├── index.html              Home
├── about.html              Our story + Meet Mitch
├── services.html           Services hub
├── plumbing.html           Plumbing services
├── heating.html            Heating & hydronics
├── boilers.html            Lochinvar boilers + vendor catalog links
├── commercial.html         Commercial & government
├── service-area.html       Service-area / local SEO (GEO)
├── reviews.html            Testimonials
├── faq.html                FAQ (with FAQ rich-result schema)
├── contact.html            Contact + free-estimate form
├── thank-you.html          Form success page
├── 404.html                Not-found page
├── blog/                   Blog hub + first article (for scheduled content)
├── robots.txt              Crawler rules (welcomes AI crawlers)
├── sitemap.xml             XML sitemap
├── site.webmanifest        PWA manifest
├── css/style.css           The whole retro design system
├── js/main.js              Nav, accordion, scroll reveal, form, etc.
├── assets/img/             Logo, Mitch mascot art, building photo, favicon
└── build.py / make.py / pages.py   Page generator (see below)
```

## Editing content

Pages are generated from Python so the header, footer, nav, and structured data stay
identical across every page. To change content:

1. Edit **`pages.py`** (page text) — or `make.py` (header/footer/layout) / `build.py`
   (business facts + schema, e.g. phone, address, service area).
2. Re-generate:
   ```
   cd site
   python pages.py
   ```
   This rewrites all the `.html` files. Commit/upload the results.

> You can also edit the `.html` files directly if you prefer — just know a future
> `python pages.py` run will overwrite them.

**Single source of truth** for phone, address, hours, service-area towns, and the
testimonial lives at the top of `build.py`. Change it once, re-run, done.

## Before you go live

1. **Wire up the form.** `js/main.js` currently simulates submission. Point the
   `<form data-quote-form>` in `contact.html` at a real endpoint — e.g.
   [Formspree](https://formspree.io), Netlify Forms, or your CRM — and have it redirect to
   `thank-you.html` on success.
2. **Confirm the domain** in `build.py` (`SITE_URL`) is `https://mphsd.com`, then re-run
   `python pages.py` so canonicals/Open Graph/schema all use the live URL.
3. **Add real profiles.** In `build.py`, fill the `"sameAs"` list with the company's Google
   Business Profile, Facebook, etc. — this strengthens SEO/AEO. Update the footer Facebook link.
4. **Verify business hours** in `build.py` (`openingHoursSpecification`) — currently Mon–Fri
   8–5 with 24/7 emergency noted in copy.
5. **Submit `sitemap.xml`** to Google Search Console and Bing Webmaster Tools.
6. (Optional) Generate PNG favicons / a 512×512 maskable icon if you want richer PWA install
   art; `favicon.svg` and the logo already cover modern browsers.

## SEO / AEO / GEO / AIO built in

- Unique `<title>` + meta description, canonical, Open Graph & Twitter cards on every page
- **JSON-LD structured data**: `Plumber` + `HVACBusiness` LocalBusiness graph (NAP, geo,
  hours, area served, services, a real review), plus per-page `Service`, `FAQPage`,
  `BreadcrumbList`, and `BlogPosting` schema
- Geo meta tags + a dedicated **Service Area** page naming the towns and counties you serve
- `robots.txt` explicitly welcomes AI/answer-engine crawlers (GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, etc.) for AIO/AEO visibility
- Semantic HTML, descriptive alt text, fast (no heavy frameworks), mobile-first, accessible

## Vendor catalogs

The Boilers page links to Lochinvar's official product catalog. To add more vendor catalogs,
edit the "Vendor Catalogs" section in `pages.py` (`boilers_body`).

## Hosting on GitHub Pages

This repository **is** the website — the HTML lives at the repo root, so GitHub Pages can serve
it directly with no build step.

1. Push this repo to GitHub (see below).
2. On GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch"**,
   Branch: **`main`**, Folder: **`/ (root)`**, then **Save**.
3. Your site goes live at `https://<username>.github.io/<repo>/` within a minute or two.

**Custom domain (mphsd.com):** the site's canonical URLs, Open Graph tags, and structured data
all use `https://mphsd.com` (set as `SITE_URL` in `build.py`). To serve it there, add your domain
under **Settings → Pages → Custom domain**, create a `CNAME` file in this folder containing
`mphsd.com`, and point your DNS at GitHub Pages. Until then the pages still work on the
`github.io` URL — only the absolute canonical/OG links point at the production domain.

`.nojekyll` is included so GitHub Pages serves every file as-is (no Jekyll processing).

### Hosting elsewhere

Because it's plain static files, you can also drop this folder onto Netlify, Cloudflare Pages,
IIS, Apache, or any static host. No server or database required.
