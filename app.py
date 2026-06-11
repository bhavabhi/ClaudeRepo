from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from models import db, Event, Task, Reminder
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def dashboard():
    selected_date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
    except ValueError:
        date_obj = datetime.now().date()

    events = Event.query.filter_by(date=date_obj).all()
    tasks = Task.query.filter_by(date=date_obj).all()
    reminders = Reminder.query.filter_by(date=date_obj).all()

    items = {
        'events': [e.to_dict() for e in events],
        'tasks': [t.to_dict() for t in tasks],
        'reminders': [r.to_dict() for r in reminders],
    }

    return render_template('dashboard.html', selected_date=selected_date, items=items)


@app.route('/api/items', methods=['GET'])
def get_items():
    date_str = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    events = Event.query.filter_by(date=date_obj).all()
    tasks = Task.query.filter_by(date=date_obj).all()
    reminders = Reminder.query.filter_by(date=date_obj).all()

    return jsonify({
        'events': [e.to_dict() for e in events],
        'tasks': [t.to_dict() for t in tasks],
        'reminders': [r.to_dict() for r in reminders],
    })


if __name__ == '__main__':
    app.run(debug=True)
