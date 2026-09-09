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

import volume_control as vc

ctk.set_appearance_mode("dark")

BG = "#0e0f12"
PANEL = "#1a1c20"
ACCENT = "#5ec8f8"