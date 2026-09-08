"""
Hand Gesture Volume Control

Pinch your thumb and index finger together or apart in front of the webcam
to lower or raise your system volume. Hand tracking works anywhere;
the actual volume control uses pycaw, which is Windows only.
"""

import customtkinter as ctk
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk