from json import JSONDecodeError

from flask import Flask, render_template, request, redirect, session
import json
import secrets
import os

app = Flask(__name__)
print(secrets.token_hex(16))
app.secret_key = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

EVENT_FILE = "events.json"

def load_events():
    if os.path.exists(EVENT_FILE):
        with open(EVENT_FILE, "r") as file:
            try:
                return json.load(file)
            except JSONDecodeError as ex:
                print(f"Cannot find file please try again. {ex}")
                return {}
    return {}

def save_events(events):
    with open(EVENT_FILE, "w") as file:
        json.dump(events, file, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    role = request.form.get('role')
    username = request.form.get('username')

    if not username or not role:
        return redirect('/')

    session['username'] = username
    session['role'] = role

    if role == 'organizer':
        return redirect('/organizer')
    else:
        return redirect('/attendee')

@app.route('/organizer')
def organizer_dashboard():
    if session.get('role') != 'organizer':
        return redirect('/')

    events = load_events()
    return render_template('organizer_dashboard.html', events=events, organizer=session.get('username'))

@app.route('/attendee')
def attendee_dashboard():
    if session.get('role') != 'attendee':
        return redirect('/')

    events = load_events()
    username = session.get('username')

    my_events = []

    for event_name, event_data in events.items():
        if username in event_data.get('attendees', []):
            my_events.append(event_name)

    return render_template('attendee_dashboard.html', events=events, my_events=my_events, username=username)

@app.route('/create_event', methods=['POST'])
def create_event():
    if session.get('role') != 'organizer':
        return redirect('/')

    event_name = request.form.get('event_name').strip()
    max_attendees = int(request.form.get('max_attendees'))

    if not event_name or max_attendees < 1:
        return redirect('/organizer')

    events = load_events()

    if event_name in events:
        return redirect('/organizer')

    events[event_name] = {
        "max_attendees": max_attendees,
        "attendees": []
    }

    save_events(events)

    return redirect('/organizer')


@app.route('/rsvp_event', methods=['POST'])
def rsvp_event():
    if session.get('role') != 'attendee':
        return redirect('/')

    event_name = request.form.get('event_name')
    username = session.get('username')

    events = load_events()

    if event_name not in events:
        return redirect('/attendee')

    event = events[event_name]


    if username in event['attendees']:
        return redirect('/attendee')

    # Check if event is full
    if len(event['attendees']) >= event['max_attendees']:
        return redirect('/attendee')

    event['attendees'].append(username)
    save_events(events)

    return redirect('/attendee')


@app.route('/cancel_rsvp', methods=['POST'])
def cancel_rsvp():
    if session.get('role') != 'attendee':
        return redirect('/')

    event_name = request.form.get('event_name')
    username = session.get('username')

    events = load_events()

    if event_name in events and username in events[event_name]['attendees']:
        events[event_name]['attendees'].remove(username)
        save_events(events)

    return redirect('/attendee')


@app.route('/delete_event', methods=['POST'])
def delete_event():
    if session.get('role') != 'organizer':
        return redirect('/')

    event_name = request.form.get('event_name')
    events = load_events()

    print(f"Trying to delete: {event_name}")
    print(f"Events: {events}")
    print(f"Attendees for event: {len(events[event_name]['attendees']) if event_name in events else 'N/A'}")

    if event_name in events:
        # Only delete if no RSVPs
        if len(events[event_name]['attendees']) == 0:
            del events[event_name]
            save_events(events)
            print(f"Successfully deleted {event_name}")
        else:
            print(f"Cannot delete - has {len(events[event_name]['attendees'])} attendees")

    return redirect('/organizer')

if __name__ == "__main__":
    app.run(debug=True)