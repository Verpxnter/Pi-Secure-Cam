from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import requests
import time
import threading
import json

app = Flask(__name__)

cap = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(2)

backSub = cv2.createBackgroundSubtractorMOG2()
# backSub2 = cv2.createBackgroundSubtractorMOG2()

SETTINGS_FILE = 'settings.json'

default_settings = {
    "color_mode": "black_white",      
    "motion_threshold": 1000
}

def load_settings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        settings = default_settings
    return settings

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

last_notification_time = 0

def detect_motion():
    global last_notification_time
    motion_detected = False
    settings = load_settings()
    motion_threshold = settings['motion_threshold']

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        fgMask = backSub.apply(frame)
        count = cv2.countNonZero(fgMask)
        if count > motion_threshold and not motion_detected:
            motion_detected = True
            current_time = time.time()
            send_discord_notification("```Motion in cam 1```")
        elif count < motion_threshold and motion_detected:
            motion_detected = False

# def detect_motion2():
#     global last_notification_time
#     motion_detected = False
#     settings = load_settings()  
#     motion_threshold = settings['motion_threshold']

#     while True:
#         ret, frame = cap2.read()
#         if not ret:
#             break
#         fgMask = backSub2.apply(frame)
#         count = cv2.countNonZero(fgMask)
#         if count > motion_threshold and not motion_detected:
#             motion_detected = True
#             current_time = time.time()
#             send_discord_notification("```Motion in cam 2```")
#         elif count < motion_threshold and motion_detected:
#             motion_detected = False

def send_discord_notification(message):
    webhook_url = "https://discord.com/api/webhooks/<UR_WEBHOOK_URL>"
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print("Error sending notification:", response.text)

@app.route('/')
def index():
    settings = load_settings()
    return render_template('index.html', settings=settings)

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed_2')
# def video_feed_2():
#     return Response(gen2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/save_settings', methods=['POST'])
def save_settings_route():
    color_mode = request.form.get('color_mode')
    motion_threshold = request.form.get('motion_threshold', type=int)

    settings = {
        "color_mode": color_mode,
        "motion_threshold": motion_threshold
    }

    save_settings(settings)

    return redirect(url_for('index'))

def gen():
    settings = load_settings()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if settings['color_mode'] == 'black_white':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        _, img_encoded = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')

# def gen2():
#     settings = load_settings()

#     while True:
#         ret, frame = cap2.read()
#         if not ret:
#             break

#         if settings['color_mode'] == 'black_white':
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

#         _, img_encoded = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')

if __name__ == '__main__':
    t1 = threading.Thread(target=detect_motion)
    # t2 = threading.Thread(target=detect_motion2)
    t1.start()
    # t2.start()
    app.run(host='0.0.0.0', port=5000)
