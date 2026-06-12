# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Calendar Application** is a Flask-based web dashboard for managing events, tasks, and reminders with a daily view (default). The application provides a clean, responsive UI with date selection and a JSON API.

### Key Architecture

**Backend Stack**:
- **Flask 3.0.0**: Lightweight web framework
- **SQLAlchemy ORM**: Database abstraction layer
- **SQLite**: Persistent data storage (auto-created at `calendar.db`)

**Frontend Stack**:
- **HTML5/CSS3/JavaScript**: Vanilla frontend (no framework)
- **date-fns**: Date formatting library (via CDN)
- **shadcn UI**: Component framework (via CDN, referenced but not heavily integrated yet)

**Data Model**: Three entities (Event, Task, Reminder) each with date-based filtering. All models include `to_dict()` methods for JSON serialization.

### Core Flows

1. **Dashboard Route (`GET /`)**: Accepts optional `date` query param, fetches all calendar items for that date, renders dashboard.html
2. **API Route (`GET /api/items`)**: Same date filtering, returns JSON response (used for programmatic access)
3. **Date Fallback**: Invalid dates default to today's date (dashboard) or return 400 error (API)

## Getting Started

### Installation & Setup
```bash
pip install -r requirements.txt
python seed_data.py        # Load sample data
python app.py              # Start dev server at http://localhost:5000
```

### Development Mode
```bash
FLASK_ENV=development python app.py
```
Flask auto-reloads on Python file changes.

### Database
- Auto-created on first run from models in `models.py`
- `seed_data.py` populates with 10 sample items across multiple dates
- Delete `calendar.db` to reset

## Key Files & Responsibilities

| File | Purpose |
|------|---------|
| `app.py` | Flask app initialization, two routes (dashboard, API), date parsing |
| `models.py` | SQLAlchemy models: Event, Task, Reminder with `to_dict()` serialization |
| `templates/dashboard.html` | Responsive UI: date picker, three-section layout (events/tasks/reminders), inline JavaScript for date formatting |
| `seed_data.py` | Standalone script to populate database with sample data |
| `docs/ui.md` | UI standards enforcing shadcn UI components and ordinal date formatting |

## Design Patterns & Constraints

**UI Standards** (from `docs/ui.md`):
- Use **shadcn UI components only** (no custom UI components)
- Date formatting: **ordinal format** (e.g., "12th Jun 2026") via date-fns
- Color palette: Primary #007bff, Success #28a745, Warning #ffc107, Danger #dc3545
- Responsive: Must work desktop, tablet, mobile

**Date Handling**:
- Backend: Expects YYYY-MM-DD format, silently falls back to today on invalid input
- Frontend: Uses native HTML `<input type="date">` and date-fns for ordinal formatting
- All queries filter by `date` column (currently no indexes—performance consideration for large datasets)

**Database Design**:
- No migrations framework (direct `db.create_all()`)
- All timestamps in UTC (`datetime.utcnow`)
- Serialization via `to_dict()` adds `'type'` field (event/task/reminder) for frontend filtering

## Common Tasks

### Add a New Calendar Item Type
1. Create model in `models.py` (inherit from db.Model, add `to_dict()`)
2. Query it in both routes in `app.py` (dashboard + get_items)
3. Add a new section to `templates/dashboard.html` with appropriate styling
4. Update `seed_data.py` for test data
5. Update `docs/ui.md` if UI standards change

### Modify the Dashboard Layout
Edit `templates/dashboard.html`. Key sections:
- `.header`: Title and date picker
- `.daily-view`: Grid container for three sections
- `.section`: Each category (events/tasks/reminders)
- Inline CSS in `<style>` tag and JavaScript at bottom

### Query Calendar Items
Use Flask-SQLAlchemy on any model:
```python
Event.query.filter_by(date=some_date).all()
Task.query.filter_by(date=some_date, completed=False).all()
```

## Code Review Findings & Known Issues

- ⚠️ **Unused import**: `import os` in app.py (line 4)
- ⚠️ **No database indexes**: `date` column should have `index=True` for performance
- ⚠️ **Debug mode hardcoded**: `app.run(debug=True)` should use `FLASK_DEBUG` env var
- ⚠️ **Inline JavaScript**: dashboard.html has inline script block; extract to `static/js/` for maintainability
- ⚠️ **CDN dependencies**: date-fns and shadcn/ui via CDN lack Subresource Integrity (SRI) checks
- ⚠️ **No test coverage**: No unit tests for models or routes
- ⚠️ **Duplicate logic**: Date filtering repeated in both routes (refactor candidate)

**Post-merge improvements** (low priority):
- Add database indexes on `date` columns
- Extract inline JS to separate file
- Add unit tests (models, API responses, date validation)
- Add accessibility attributes (`aria-label`, `role="region"`)

## Future Features & Architecture Considerations

Currently read-only (GET only). Future enhancements:
- **CRUD Operations**: POST/PUT/DELETE routes and database operations
- **User Authentication**: User-scoped calendars, login flow
- **Timezone Support**: Store/display in user's timezone
- **Calendar Views**: Week/month view alongside current daily view
- **Notifications**: Real-time reminders or scheduled alerts

No breaking changes anticipated for the current daily-view architecture.

## UI/Frontend Notes

- **Responsive Design**: CSS Grid for layout, Flexbox for item lists
- **Date Picker**: Native HTML `<input type="date">` with `onchange="updateDate()"`
- **Date Formatting**: Client-side ordinal suffix calculation (formatDate function)
- **Empty States**: Each section shows "No items" message when empty
- **Styling**: Inline CSS only; consider moving to external stylesheet as complexity grows

## Deployment Considerations

- Production should use a WSGI server (Gunicorn, uWSGI) instead of Flask's debug server
- Database file should live outside the repo root or use a production database (PostgreSQL, MySQL)
- `FLASK_ENV=production` should disable debug mode and auto-reload
- Consider adding CSP (Content Security Policy) headers for CDN dependencies
