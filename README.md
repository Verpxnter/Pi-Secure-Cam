# **Pi-Secure-Cam**

Welcome to **Pi-Secure-Cam** — a simple, Raspberry Pi-powered security camera system. With multi-camera support, motion detection, and real-time Discord notifications, it's the perfect DIY solution for setting up a home or office security system. 📹🔒

## 1. Introduction

**Pi-Secure-Cam** is a Python script that allows you to connect multiple USB cameras to your Raspberry Pi and view their live feeds on a customizable web dashboard. It also features motion detection to keep you updated when something unusual happens and sends notifications directly to your Discord channel.

Whether you're setting this up to monitor your home, office, or just want to try out some fun surveillance tech, **Pi-Secure-Cam** is easy to set up and works great on **Raspberry Pi 4**.

## 2. Features

- **Multi-Camera Support**: Connect and monitor multiple USB cameras. You can manually add cameras by editing the `app.py` and HTML files. 📷📷
- **Motion Detection**: Uses background subtraction to detect motion and trigger alerts. Customizable motion sensitivity.
- **Discord Notifications**: Sends real-time notifications to your Discord server whenever motion is detected. *(Note: The Discord webhook is functional but will receive updates in future versions.)*
- **Customizable Camera Index**: If you're having issues with the camera not displaying, you may need to adjust the camera index by editing `cv2.VideoCapture(index)` in `app.py` (lines 10-11). Changing the index can resolve conflicts with how the system assigns cameras.
- **Web-Based Dashboard**: Stream live footage directly in your browser. Includes real-time video feed from each connected camera.
- **Headless Mode**: Run the application in the background without needing a monitor or GUI.

## 3. How It Works

1. **Camera Setup**: Plug in your USB cameras to your Raspberry Pi. You can add additional cameras manually by modifying the `app.py` and HTML files.
2. **Motion Detection**: The system checks for motion using background subtraction. If motion exceeds the sensitivity threshold, a notification is sent to your Discord server.
3. **View the Dashboard**: Access the live camera feed on your browser through the web-based dashboard.

## 4. Installation and Setup

Here’s how to get **Pi-Secure-Cam** up and running:

### Step 1: Clone the Repository
Clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/YourUsername/Pi-Secure-Cam.git
cd Pi-Secure-Cam
```

### Step 2: Install Dependencies
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```
### Step 3: Run the Application
To start monitoring your cameras, run:

```bash
python app.py
```

### Step 4: Access the Dashboard
Once the application is running, you can view the live feed in your browser:

```bash
http://<your-pi-ip>:5000/
```
Here, you'll see the live feeds from your connected cameras.

## 5. Adding Additional Cameras

To add more cameras to your **Pi-Secure-Cam** setup, follow these steps:

### Step 1: Edit `app.py`

Find the following lines in `app.py` (lines 10-11):

```python
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
```
To add more cameras, increase the index number and add additional `VideoCapture` instances:
```python
cap3 = cv2.VideoCapture(2)  # For a third camera
cap4 = cv2.VideoCapture(3)  # For a fourth camera
```

### Step 2: Update index.html
In the `index.html` file, add new `<img>` tags for each additional camera feed. For example, to add a third camera:

```html
<img src="{{ url_for('video_feed_3') }}" />
```
Repeat this for as many camera feeds as you want to display.

### Step 3: Add New Routes in app.py
For each additional camera, create a new route in `app.py` to serve the camera feed. For example, for the third camera:

```python
@app.route('/video_feed_3')
def video_feed_3():
    return Response(gen3(), mimetype='multipart/x-mixed-replace; boundary=frame')
```
You’ll also need to create a new `gen3()` function that handles the third camera feed, just like the existing `gen()` and `gen2()` functions:
```python
def gen3():
    while True:
        ret, frame = cap3.read()
        if not ret:
            break
        if settings['color_mode'] == 'black_white':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, img_encoded = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')
```
Repeat this process for each additional camera.

### Step 4: Handle Camera Index Issues
If one of your camera feeds isn’t working or if the wrong camera is showing up, you might need to adjust the camera index number in `app.py`. Camera indexes are assigned by your system and can vary, so try changing the index values:

```python
cap = cv2.VideoCapture(0)  # Change the 0 to a different index if needed
cap2 = cv2.VideoCapture(1)  # Likewise, change this to another number if necessary
```

## 6. Discord Webhook Setup
To enable Discord notifications for motion detection, replace the placeholder webhook URL in `app.py` with your own Discord webhook:

```python
webhook_url = "https://discord.com/api/webhooks/your-webhook-url"
```
Whenever motion is detected, the system will send an alert message to your Discord channel. While this feature is fully functional, future updates will improve notification customization and performance.

## 7. Conclusion
That’s it! You've now set up a versatile, multi-camera security system powered by your Raspberry Pi. You can customize it to add more cameras, tweak motion detection settings, and receive real-time Discord alerts. Enjoy your newfound security with Pi-Secure-Cam! 🔒📷

```css
This section explains how to add additional cameras, troubleshoot camera index issues, and configure the Discord webhook for notifications.
```
