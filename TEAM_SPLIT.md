# BreadFast — 5-member file ownership

Each member has a separate folder under `team_members/` containing their assigned files and a README. The complete runnable application remains in the project root. These folders are handoff copies/reference contributions; merge edits into the matching root paths, not by running the files from the member folders.

| Member | Jira story / responsibility | Owned files in the complete app |
|---|---|---|
| 1 | SCRUM-6 — Menu and availability | `templates/index.html`, `static/js/menu.js` |
| 2 | SCRUM-11 — Cart | `static/js/cart.js` |
| 3 | SCRUM-12 — Checkout and place order | `static/js/checkout.js` |
| 4 | SCRUM-16 — Kitchen queue | `templates/kitchen.html`, `static/js/kitchen.js` |
| 5 | Backend, database, integration and tests | `app.py`, `tests/test_app.py`, `requirements.txt`, `templates/base.html`, `static/css/style.css` |

## Shared integration contract
- Menu: `GET /api/menu` returns items with `id`, `name`, `description`, `price`, `emoji`, and `available`.
- Checkout: `POST /api/orders` accepts `student_name`, `pickup_time`, `pickup_place`, and `items` (`id`, `quantity`).
- Kitchen: `GET /api/orders` returns the order queue; `PATCH /api/orders/<id>/status` updates status.
- Student scripts load in this order: `menu.js`, `cart.js`, `checkout.js`. `menu.js` creates `window.BreadFast`; cart and checkout use it.

## Git workflow
Each person should create a branch, commit only their owned files, push it, and open a pull request to `main`. Member 5 reviews integration and runs the tests after merges. Avoid having two people edit the same file at the same time.

## Run the full application
`python -m pip install -r requirements.txt` then `python app.py`; open `http://127.0.0.1:5000`. Kitchen: `http://127.0.0.1:5000/kitchen`. Run tests with `python -m pytest -q`.
