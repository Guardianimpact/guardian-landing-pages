# Guardian Landing Pages

PPC landing pages for Google Ads campaigns — Guardian Impact Windows & Roofing.

## Tech Stack
- **Framework**: FastAPI + Jinja2 (lightweight, no database)
- **Deploy**: Railway auto-deploy from GitHub on push
- **Repo**: `Guardianimpact/guardian-landing-pages`

## URLs
- **Railway**: `https://soothing-patience-production-dfe2.up.railway.app`
- **Custom domain**: `https://quote.guardwhatmatters.com`

## DNS — IMPORTANT
- **Nameservers are SiteGround** (`ns1.siteground.net`, `ns2.siteground.net`)
- **GoDaddy DNS records do NOTHING** — the domain is registered at GoDaddy but nameservers point to SiteGround
- To change DNS: log into SiteGround > Site Tools > Domain > DNS Zone Editor
- CNAME for `quote`: `9ow9q41k.up.railway.app`
- TXT for `_railway-verify.quote`: `railway-verify=923e9d55bd253b7bb624763184e3d26a42895c1941d9f8df80454db3c6d75001`

## Deployment
- `git push origin main` → Railway auto-deploys
- Railway CLI: `/c/Users/Ethan/railway-cli/railway.exe` (must run from this repo dir)
- No CI configured — do NOT enable "Wait for CI" in Railway
- Procfile: `web: uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}`

## Routes (main.py)
| Route | Template | Description |
|-------|----------|-------------|
| `GET /` | `landing.html` | Generic landing page |
| `GET /impact-windows-broward` | `impact-windows-broward.html` | Premium Broward page (Ares campaign target) |
| `GET /impact-windows-palm-beach` | `landing.html` | Palm Beach impact windows |
| `GET /impact-windows-miami-dade` | `landing.html` | Miami-Dade impact windows |
| `GET /roofing-broward` | `landing.html` | Broward roofing |
| `GET /roofing-palm-beach` | `landing.html` | Palm Beach roofing |
| `POST /submit-lead` | — | Forwards lead JSON to GuardianQA |
| `GET /health` | — | Returns "ok" |

## Lead Flow
1. User fills form on landing page
2. JavaScript captures GCLID + UTM params from cookies (90-day persistence)
3. `POST /submit-lead` receives JSON payload
4. Server forwards to GuardianQA: `https://web-production-adfe7.up.railway.app/api/landing-page/lead`
5. Returns `{"status": "ok"}` regardless (silent failure — user sees success)

## Templates
- `landing.html` — Generic reusable template. Accepts: page_title, h1, subhead, product, geo, ga4_id, callrail_script, phone, phone_href
- `impact-windows-broward.html` — Premium standalone page with inline CSS. Uses: ga4_measurement_id, callrail_swap_script, phone_number, phone_href

## Static Assets (static/img/landing/)
- Real Guardian project photos ONLY — no stock photos
- Drone shots: Jones, Ioannou, Sikandar projects
- Videos: drone-ioannou.mp4, drone-jones.mp4, employee-testimonial.mp4, owner-process.mp4
- Logos: guardian-logo.png, guardian-logo-hires.png
- Source: `G:\Shared drives\Marketing\Content\In-House Media\Customers\Complete\`

## Environment Variables (all have defaults)
| Variable | Default | Purpose |
|----------|---------|---------|
| `GA4_MEASUREMENT_ID` | `G-5V08YKMFED` | Google Analytics 4 |
| `CALLRAIL_SWAP_SCRIPT` | `//cdn.callrail.com/companies/374823998/...` | Dynamic number swap |
| `PHONE_NUMBER` | `(954) 245-0497` | Display phone |
| `PHONE_HREF` | `tel:+19542450497` | Click-to-call link |

## Ares Campaign Integration
The `/impact-windows-broward` page is the landing page for the Google Ads campaign "Guardian - Impact Windows Broward - ARES-TEST" (campaign ID: 23633445288). Copy is optimized for these exact-match keywords:
- impact windows installation
- impact window installation cost
- impact windows near me
- impact window companies near me
- hurricane windows
- hurricane impact windows
- impact resistant windows

## Business Details
- **Company**: Guardian Impact Windows & Roofing
- **Phone**: (954) 245-0497
- **Contractor licenses**: CGC-1524314 (General), CCC-1334906 (Roofing)
- **Service area**: Broward, Palm Beach & Miami-Dade Counties
- **Manufacturers**: CGI Windows & Doors, ES Windows

## Gotchas
- The premium Broward template has ALL CSS inline (no external stylesheet)
- The generic `landing.html` uses different Jinja variable names than the Broward template (ga4_id vs ga4_measurement_id, phone vs phone_number)
- CallRail swap.js dynamically replaces phone numbers based on traffic source
- GCLID capture uses 90-day cookies for Google Ads attribution
- `meta robots noindex` is set — page is not indexed by search engines (PPC only)
