# H.A.I.S.O – Desktop Assistant

**H.A.I.S.O** is a multilingual, lightweight, and user-friendly Kivy-based desktop assistant. It provides a simple yet powerful interface with functionalities such as breathing exercises, weather forecast, system cleaner, shutdown scheduler, reminders, and more.

---

## Features

- Breathing Exercise (with countdowns and calm messages)
- Clock and Date display
- Temporary file cleaner (Windows)
- Live weather forecast via OpenWeatherMap API
- Reminder popup (with sound and message)
- On-screen calculator
- Schedule PC shutdown
- Time-based greeting
- Packaged as a `.exe` (with PyInstaller support)

---

## Tech Stack

- Language: Python 3
- GUI Framework: Kivy
- API: OpenWeatherMap
- Packaging: PyInstaller (supports `sys._MEIPASS` for resource loading)

---

## How It Works

### `main.py`

- Initializes the app.
- Sets fixed screen resolution (900x600).
- Loads the `.kv` layout file.
- Launches `AsistanApp`, which returns the `AsistanEkrani`.

---

### `ui.kv`

- Declares UI layout using Kivy language.
- Left panel: command buttons
- Right panel: displays the current user command and assistant's response.
- Custom button style (`HoverButton`) defined for uniform look.

---

### `ui.py` – `AsistanEkrani` class

- Central screen logic.
- Initializes greeting message based on time.
- Handles button clicks and input text.
- Dynamically calls the correct command function based on the user's input.
- Uses callbacks and `Clock.schedule_once()` to update UI from threads.

---

### `breath.py`

- Runs a guided 4-7-8 breathing exercise in a background thread.
- Uses countdowns and calming messages via callback.
- Example steps:
- "Take a deep breath" (4 seconds)
- "Hold your breath" (7 seconds)
- "Exhale slowly" (8 seconds)

---

### `cleaner.py`

- Deletes Windows temporary files:
  - `%TEMP%`
  - `C:\Windows\Temp`
  - `C:\Windows\Prefetch`
- Silent execution with error handling.

---

### `weather.py`

- Uses OpenWeatherMap API (`appid` required).
- Accepts city names from input.
- Returns current temperature and weather description.

---

### `clock.py`

- Returns formatted current time and date.

---

### `calculator.py`

- Opens a basic calculator popup with:
  - Digits, operators, clear, equals.
- Secure `eval()` use (no builtins).

---

### `reminder.py`

- Opens a popup where users enter:
- Duration (in minutes)
- Reminder message
- After countdown, plays `ding.mp3` and shows message popup.

---

### `shutdown.py`

- Opens popup to schedule a Windows shutdown.
