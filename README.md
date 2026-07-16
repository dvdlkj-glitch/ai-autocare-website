# AI AutoCare — Customer Flow Website

**Smart Service. Better Rides.** — A webpage + Telegram driven auto-service workflow site.

Live demo: https://dvdlkj-glitch.github.io/ai-autocare-website/

## What's on the page

Built from the AI AutoCare customer-flow infographic:

- **Entry Channels** — webpage intake + Telegram bot
- **10-Step Customer Flow** — intake → vehicle info → AI recommendation → booking → technician photos & checklist → AI report + 3 quotes → customer decision → service → record update → AI follow-up
- **AI Recommendation services** — suitable tires, maintenance package, initial inspection focus
- **Quotation tiers** — Essential / Recommended / Complete
- **Core System Modules** — Webpage, Telegram Bot, AI Recommendation Engine, Inspection Report, Quotation Generator, Customer Database, Reminder Automation
- **Booking form** — demo vehicle-info form (not yet connected to a backend)

## Stack

Single-file static site: `index.html` (vanilla HTML/CSS/JS, no build step), plus a Streamlit wrapper for Streamlit Cloud.

## Deployments

- **GitHub Pages** (auto-deploys from `main`): https://dvdlkj-glitch.github.io/ai-autocare-website/
- **Streamlit Cloud**: point a new app at this repo with main file `streamlit_app.py` (serves the same site full-screen via `st.iframe`).

Run locally with Streamlit:

```
streamlit run streamlit_app.py
```

## Status

Draft demo version — pending tuning (copy, branding assets, Telegram bot link, backend hookup).
