# BreadFast — Cafeteria Pre-Order Website (Sprint 1)

A Flask + SQLite full-stack prototype with a student ordering page and a kitchen dashboard.

## Features mapped to Jira

| Jira story | Feature | Implementation |
|---|---|---|
| SCRUM-6 | View menu and availability | `/` and `GET /api/menu` |
| SCRUM-11 | Add items to cart | Browser cart in `static/js/student.js` |
| SCRUM-12 | Select pickup time/place and place order | Checkout form and `POST /api/orders` |
| SCRUM-16 | Kitchen incoming orders queue | `/kitchen`, `GET /api/orders`, status update API |

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended):

   Windows:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the website:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` for the student site.
7. Open `http://127.0.0.1:5000/kitchen` for the kitchen dashboard.

The SQLite database is created automatically on first run.

## Run tests

```bash
python -m pytest -q
```

## Four-person split

- Person 1 — SCRUM-6: menu display and availability (`/api/menu`, menu UI).
- Person 2 — SCRUM-11: cart interactions (`static/js/student.js`).
- Person 3 — SCRUM-12: checkout and order creation (`POST /api/orders`).
- Person 4 — SCRUM-16: kitchen dashboard and status updates (`templates/kitchen.html`, `static/js/kitchen.js`, kitchen APIs).

Shared integration files: `app.py`, `templates/base.html`, `static/css/style.css`, and `tests/test_app.py`.

## Prototype limitations to confirm against the course brief

This is a local demonstration app, not deployed online. It does not yet include student/staff login, payment, real-time push updates, admin authentication, or strict validation against configured cafeteria pickup slots. The kitchen dashboard is not access-controlled. Add those only if they are part of your actual acceptance criteria.


## Latest checkout fix
The checkout handler now saves the form reference before awaiting the API response, avoiding the `Cannot read properties of null (reading 'reset')` browser error. It also disables the submit button during submission and shows clearer API/network errors. After replacing an older copy, restart Flask and refresh the browser with Ctrl+F5.
