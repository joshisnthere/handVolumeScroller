# Hand Gesture Volume Control

Pinch your thumb and index finger closer together or further apart in
front of your webcam to lower or raise your system volume in real time.

## Setup

    pip install -r requirements.txt
    python main.py

## Notes

- Hand tracking (mediapipe) works on any OS.
- The actual volume change uses `pycaw`, which talks to Windows Core
  Audio -- it's Windows only. On other systems the gesture still shows on
  screen, it just won't move your real volume.
