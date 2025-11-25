# Event Planner

A Flask web application for event management with two user roles: organizers can create and manage events, attendees can RSVP and view their schedule.

## Features

- ✅ Two user roles: Event Organizer and Attendee
- ✅ Organizers can create, view, and delete events
- ✅ Attendees can view available events and RSVP
- ✅ Cancel RSVP functionality
- ✅ Event capacity management (max attendees)
- ✅ View attendee roster (organizers only)
- ✅ Session-based authentication
- ✅ Persistent data storage (JSON)

## Tech Stack

- Python 3
- Flask
- HTML/CSS
- JSON (data storage)
- Session management

## Live Demo

[Event Planner Live](https://event-planner-o8lf.onrender.com)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/drewdavis816/EventPlanner.git
cd EventPlanner
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python3 main.py
```

5. Open your browser and go to `http://127.0.0.1:5000`

## How to Use

### As an Organizer:
1. Enter your name and select "Event Organizer"
2. Create events with a name and max attendee count
3. View all your events and their attendance rosters
4. Delete events (only if no RSVPs)

### As an Attendee:
1. Enter your name and select "Attendee"
2. View all available events
3. RSVP to events you're interested in
4. View your schedule in "My Events"
5. Cancel RSVP if needed

## Project Structure
```
EventPlanner/
├── main.py              # Flask app and routes
├── templates/
│   ├── index.html       # Login/role selection
│   ├── organizer_dashboard.html  # Organizer interface
│   └── attendee_dashboard.html   # Attendee interface
├── static/
│   └── style.css        # Styling
├── events.json          # Data storage
└── requirements.txt     # Dependencies
```

## What I Learned

- Flask routing with multiple routes
- Session management for user authentication
- Role-based access control
- Template inheritance concepts
- Form handling and data validation
- JSON data persistence
- Building multi-user applications

## Future Improvements

- User database integration
- Email notifications for RSVPs
- Event date/time tracking
- Event categories
- User profiles
