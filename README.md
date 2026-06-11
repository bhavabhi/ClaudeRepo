# Calendar Application

A Python Flask web application dashboard with calendar integration for managing events, tasks, and reminders.

## Features

- **Daily View Calendar**: Default view showing all events, tasks, and reminders for the selected date
- **Date Picker**: Select any date to view corresponding items
- **Event Management**: View scheduled events with time details
- **Task Tracking**: Manage tasks with priority levels and completion status
- **Reminders**: Track reminders with scheduled times
- **Modern UI**: Built with clean, responsive design using shadcn UI standards

## Project Structure

```
.
├── app.py                 # Flask application and routes
├── models.py             # Database models (Event, Task, Reminder)
├── requirements.txt      # Python dependencies
├── templates/
│   └── dashboard.html    # Main dashboard template
├── docs/
│   └── ui.md            # UI standards and guidelines
└── calendar.db          # SQLite database (generated on first run)
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhavabhi/ClaudeRepo.git
cd ClaudeRepo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Viewing the Dashboard
- The dashboard defaults to the current date
- Use the date picker to select different dates
- View all events, tasks, and reminders for the selected date

### Database
The application uses SQLite for data persistence. The database is automatically created on first run.

To seed sample data (optional):
```bash
python seed_data.py
```

## UI Standards

See [docs/ui.md](docs/ui.md) for comprehensive UI guidelines including:
- Component standards (shadcn UI only)
- Date formatting rules (ordinal format)
- Color palette
- Typography guidelines
- Responsive design requirements
- Accessibility standards

## API Endpoints

### Dashboard
- `GET /` - Main dashboard page with optional `date` parameter
  - Query params: `date` (YYYY-MM-DD format, defaults to today)

### API
- `GET /api/items` - Get events, tasks, and reminders for a specific date
  - Query params: `date` (YYYY-MM-DD format)
  - Returns: JSON with events, tasks, and reminders arrays

## Technologies Used

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Date Formatting**: date-fns library (via CDN)
- **UI Framework**: shadcn UI (via CDN)

## Development

To run in development mode with auto-reload:
```bash
FLASK_ENV=development python app.py
```

The application will reload automatically when you make changes to Python files.

## Date Formatting

Dates are displayed in ordinal format (e.g., "1st Sept 2026", "15th June 2026") using the date-fns library.

## License

This project is open source and available under the MIT License.
