# **Pi-Secure-Cam**

Welcome to **Pi-Secure-Cam** — your friendly Raspberry Pi-powered security system. With motion detection, dual-camera support, and real-time Discord notifications, this tool helps you stay on top of all the *suspicious* activities around your space. Whether you’re using it to guard your room, office, or secret lair, this is the perfect DIY solution for setting up a simple security cam with minimal hassle. 👀🔒

Tested and works great on **Raspberry Pi 4**!

## 1. Introduction

**Pi-Secure-Cam** is a Python-based security system designed to run on a Raspberry Pi (or any Linux machine) and monitor multiple camera feeds. It detects motion using background subtraction and alerts you via Discord when something moves. You can adjust settings like motion sensitivity and color modes to fit your needs, making it a customizable, lightweight, and easy-to-use home security tool. 📹🐱‍💻

Whether you’re watching over your house, your office, or a top-secret laboratory, **Pi-Secure-Cam** will keep you notified of any action you need to know about.

## 2. Features

- **Multi-Camera Monitoring**: Supports two cameras simultaneously (because one camera is never enough for the truly paranoid). 🔍🔍
- **Motion Detection**: Uses background subtraction to detect motion and notify you when something’s amiss. Perfect for catching any unexpected activity.
- **Discord Notifications**: Get real-time notifications directly to your Discord server when motion is detected. Stay connected even when you're away from your Pi.
- **Customizable Settings**: Tune the motion detection sensitivity, switch between color modes (black & white for that classic security cam vibe), and adjust other settings via a simple web interface.
- **Web-Based Live Feed**: Stream live footage directly in your browser. No more awkwardly popping open VLC or some other software just to check on your space.
- **Headless Mode**: Operates in headless mode, meaning you can run it without a GUI — perfect for those who love their terminal and minimal setups.

## 3. How It Works (Because We’re Fancy Like That)

1. **Set Up Your Cameras**: Connect one or two cameras to your Raspberry Pi. One for the entrance, one for the valuables. 🎥🎥
2. **Motion Detection**: The system constantly checks for motion using background subtraction techniques. If movement crosses your configured threshold, the system triggers a notification.
3. **Get Notified**: You’ll receive a notification in your Discord channel whenever motion is detected, so you can act fast.
4. **View the Live Feed**: Need to see what’s going on in real-time? Just load up the live feed in your browser and watch the action as it unfolds.

## 4. Installation and Setup

Here’s how you can set up **Pi-Secure-Cam** on your Raspberry Pi in just a few steps:

### Step 1: Clone the Repository
First, make sure you have Python and Git installed on your Pi. Then clone the repository:

```bash
git clone https://github.com/verpxnter/Pi-Secure-Cam.git
cd Pi-Secure-Cam
