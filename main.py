"""
Guardian Landing Pages — FastAPI app serving PPC landing pages
for Guardian Impact Windows & Roofing.

Deployed on Railway at soothing-patience-production-dfe2.up.railway.app
Custom domain: quote.guardwhatmatters.com
"""
import os

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Guardian Landing Pages", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

GA4_MEASUREMENT_ID = os.environ.get("GA4_MEASUREMENT_ID", "G-5V08YKMFED")
CALLRAIL_SWAP_SCRIPT = os.environ.get(
    "CALLRAIL_SWAP_SCRIPT",
    "//cdn.callrail.com/companies/374823998/4072c504e3dfbc6e3563/12/swap.js",
)
PHONE_NUMBER = os.environ.get("PHONE_NUMBER", "(954) 245-0497")
PHONE_HREF = os.environ.get("PHONE_HREF", "tel:+19542450497")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Root redirect or generic page."""
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "page_title": "Guardian Impact Windows & Roofing | Free Quote",
        "h1": "Protect Your Home with Impact Windows & Roofing",
        "subhead": "South Florida's Trusted Contractor — Free Estimates, Financing Available",
        "product": "Impact Windows & Roofing",
        "geo": "South Florida",
        "ga4_id": GA4_MEASUREMENT_ID,
        "callrail_script": CALLRAIL_SWAP_SCRIPT,
        "phone": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.get("/impact-windows-broward", response_class=HTMLResponse)
async def impact_windows_broward(request: Request):
    """Impact Windows Broward County — premium landing page."""
    return templates.TemplateResponse("impact-windows-broward.html", {
        "request": request,
        "ga4_measurement_id": GA4_MEASUREMENT_ID,
        "callrail_swap_script": CALLRAIL_SWAP_SCRIPT,
        "phone_number": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.post("/submit-lead")
async def submit_lead(request: Request, response: Response):
    """Accept lead form submissions and forward to GuardianQA."""
    import json, httpx
    body = await request.json()
    # Forward to GuardianQA
    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                "https://web-production-adfe7.up.railway.app/api/landing-page/lead",
                json=body,
                timeout=5.0,
            )
    except Exception:
        pass
    return {"status": "ok"}


@app.get("/impact-windows-palm-beach", response_class=HTMLResponse)
async def impact_windows_palm_beach(request: Request):
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "page_title": "Impact Windows Palm Beach | Guardian Impact Windows",
        "h1": "Impact Windows for Palm Beach County",
        "subhead": "Code-Compliant Installation — Free Estimate, Licensed & Insured",
        "product": "Impact Windows",
        "geo": "Palm Beach County",
        "ga4_id": GA4_MEASUREMENT_ID,
        "callrail_script": CALLRAIL_SWAP_SCRIPT,
        "phone": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.get("/impact-windows-miami-dade", response_class=HTMLResponse)
async def impact_windows_miami_dade(request: Request):
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "page_title": "Impact Windows Miami-Dade | Guardian Impact Windows",
        "h1": "Impact Windows for Miami-Dade County",
        "subhead": "Hurricane Protection Experts — Financing Available, Se Habla Español",
        "product": "Impact Windows",
        "geo": "Miami-Dade County",
        "ga4_id": GA4_MEASUREMENT_ID,
        "callrail_script": CALLRAIL_SWAP_SCRIPT,
        "phone": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.get("/roofing-broward", response_class=HTMLResponse)
async def roofing_broward(request: Request):
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "page_title": "Roofing Broward County | Guardian Roofing",
        "h1": "Roof Replacement & Repair in Broward County",
        "subhead": "Licensed FL Roofer — Insurance Claim Help, Free Inspection",
        "product": "Roofing",
        "geo": "Broward County",
        "ga4_id": GA4_MEASUREMENT_ID,
        "callrail_script": CALLRAIL_SWAP_SCRIPT,
        "phone": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.get("/roofing-palm-beach", response_class=HTMLResponse)
async def roofing_palm_beach(request: Request):
    return templates.TemplateResponse("landing.html", {
        "request": request,
        "page_title": "Roofing Palm Beach County | Guardian Roofing",
        "h1": "Roof Replacement & Repair in Palm Beach County",
        "subhead": "Storm Damage Experts — Free Roof Inspection, Financing Available",
        "product": "Roofing",
        "geo": "Palm Beach County",
        "ga4_id": GA4_MEASUREMENT_ID,
        "callrail_script": CALLRAIL_SWAP_SCRIPT,
        "phone": PHONE_NUMBER,
        "phone_href": PHONE_HREF,
    })


@app.get("/health", response_class=HTMLResponse)
async def health():
    return "ok"
