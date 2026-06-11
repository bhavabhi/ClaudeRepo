#!/usr/bin/env python
"""Seed sample data for calendar application."""

from datetime import datetime, timedelta
from app import app
from models import db, Event, Task, Reminder

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Event).delete()
        db.session.query(Task).delete()
        db.session.query(Reminder).delete()
        db.session.commit()

        today = datetime.now().date()

        # Add sample events
        events = [
            Event(
                title='Team Standup',
                description='Daily team sync meeting',
                date=today,
                start_time=datetime.strptime('09:00', '%H:%M').time(),
                end_time=datetime.strptime('09:30', '%H:%M').time(),
            ),
            Event(
                title='Project Review',
                description='Quarterly project status review',
                date=today,
                start_time=datetime.strptime('14:00', '%H:%M').time(),
                end_time=datetime.strptime('15:30', '%H:%M').time(),
            ),
            Event(
                title='Client Meeting',
                description='Discussion on new requirements',
                date=today + timedelta(days=1),
                start_time=datetime.strptime('10:00', '%H:%M').time(),
                end_time=datetime.strptime('11:00', '%H:%M').time(),
            ),
        ]

        # Add sample tasks
        tasks = [
            Task(
                title='Complete Documentation',
                description='Finish API documentation',
                date=today,
                priority='high',
                completed=False,
            ),
            Task(
                title='Code Review',
                description='Review pull requests',
                date=today,
                priority='medium',
                completed=False,
            ),
            Task(
                title='Bug Fixes',
                description='Fix reported issues',
                date=today + timedelta(days=1),
                priority='high',
                completed=False,
            ),
            Task(
                title='Write Tests',
                description='Add unit tests for new features',
                date=today + timedelta(days=2),
                priority='medium',
                completed=False,
            ),
        ]

        # Add sample reminders
        reminders = [
            Reminder(
                title='Pay Invoice',
                description='Monthly invoice payment',
                date=today,
                time=datetime.strptime('16:00', '%H:%M').time(),
                acknowledged=False,
            ),
            Reminder(
                title='Team Lunch',
                description='Lunch with team members',
                date=today + timedelta(days=1),
                time=datetime.strptime('12:00', '%H:%M').time(),
                acknowledged=False,
            ),
            Reminder(
                title='Birthday Reminder',
                description="Friend's birthday",
                date=today + timedelta(days=3),
                acknowledged=False,
            ),
        ]

        db.session.add_all(events)
        db.session.add_all(tasks)
        db.session.add_all(reminders)
        db.session.commit()

        print('✅ Sample data seeded successfully!')
        print(f'   Events: {len(events)}')
        print(f'   Tasks: {len(tasks)}')
        print(f'   Reminders: {len(reminders)}')

if __name__ == '__main__':
    seed_data()
