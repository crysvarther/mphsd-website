# Analytics & KPIs — mphsd.com

Everything Wix Analytics gives you, built from free Google tools. The tracking code is
already wired into the site generator — it just needs two IDs pasted into `build.py`
(a one-time, ~10-minute job that requires signing in to Google, so it has to be done by
a person with the company Google account).

---

## What's already built in

Once `GA4_ID` is set in `build.py`, every page automatically reports:

| Event | Fires when a visitor… | Why it matters |
|---|---|---|
| `page_view` | views any page | traffic, top pages, where visitors come from |
| `phone_call` | taps/clicks any phone number | **your #1 conversion** — includes which page they were on |
| `generate_lead` | successfully submits the contact form | quote requests, with the request type (estimate/service/account) |
| `sms_click` | taps the "text us photos" number | photo-quote leads |
| `email_click` | clicks the email address | email leads |
| `outbound_click` | clicks to Facebook, Google, Lochinvar, etc. | which off-site profiles get traffic |

If `GA4_ID` is left `""`, zero tracking code is emitted — the site stays tracker-free.

## One-time setup (do these in order)

### 1. Google Analytics 4 (~5 min)
1. Go to https://analytics.google.com and sign in with the company Google account.
2. Admin (gear icon) → **Create Property** → name it "Mitchell Plumbing & Heating".
3. Add a **Web** data stream for `https://mphsd.com`.
4. Copy the **Measurement ID** (looks like `G-ABC123XYZ`).
5. Paste it into `GA4_ID` in `build.py`, then:
   ```
   cd site
   python pages.py
   ```
   Commit & push. Data starts appearing within a day.
6. After a phone click and a form submit have happened at least once: in GA4 go to
   **Admin → Events**, and flip the **"Mark as key event"** toggle on `phone_call` and
   `generate_lead`. That makes them show up as conversions everywhere in GA4.

### 2. Google Search Console (~3 min) — do this the day the site goes live
1. Go to https://search.google.com/search-console → **Add property** → **URL prefix**
   → `https://mphsd.com`.
2. Choose the **HTML tag** verification method. It shows a line like
   `<meta name="google-site-verification" content="TOKEN">`.
3. Paste just the TOKEN into `GSC_VERIFICATION` in `build.py`, re-run `python pages.py`,
   commit & push, then click **Verify** back in Search Console.
4. In Search Console: **Sitemaps** → submit `https://mphsd.com/sitemap.xml`.

Search data takes a few weeks to accumulate — which is why this should happen at launch,
not later.

### 3. Google Business Profile (biggest local-SEO lever)
Claim/verify the profile at https://business.google.com. Its built-in insights show
calls, direction requests, and profile views from Google Maps — for a local trade
business this often drives more calls than the website itself. Once claimed, paste the
profile URL into `GBP_URL` in `build.py` (it feeds the schema.org `sameAs` links and the
footer Google icon) and re-run `python pages.py`.

### 4. Optional: one dashboard to rule them all (~20 min, free)
[Looker Studio](https://lookerstudio.google.com) connects to both GA4 and Search Console
and gives you a single bookmarkable "how's the website doing" page: visits, top pages,
search queries, phone clicks, form leads, month-over-month trends. Create a blank report
→ Add data → pick the GA4 property and the Search Console property → drop in scorecards
for the events above.

## The KPIs worth watching monthly

1. **Phone calls + form leads** (GA4 key events) — the only numbers that pay the bills
2. **Calls / directions from Google Business Profile** — the Maps side of the funnel
3. **Search impressions, clicks, and average position** (Search Console) — is SEO working
4. **Top queries** (Search Console) — what people actually search; feeds blog topics
5. **Top pages + traffic sources** (GA4) — which services and towns pull visitors

Ignore raw pageviews and "sessions" as goals — they're inputs, not results.

## Later, if the business wants more

- **Uptime monitoring** — free at https://uptimerobot.com (alerts if the site goes down)
- **Call tracking** (CallRail, ~$45+/mo) — swap-in tracking phone number that attributes
  calls to ads vs. website vs. truck wrap. Only worth it once there's ad spend.
- **Rank tracking** — a monthly manual check of "plumber mitchell sd" etc. is free;
  paid trackers only matter if competing for many keywords.
