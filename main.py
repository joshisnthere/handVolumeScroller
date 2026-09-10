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


class GestureVolumeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hand Gesture Volume Control")
        self.geometry("740x640")
        self.configure(fg_color=BG)

        self.video_label = ctk.CTkLabel(self, text="", fg_color=PANEL, corner_radius=12)
        self.video_label.pack(padx=20, pady=(20, 10))

        bar_frame = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=12)
        bar_frame.pack(padx=20, pady=(0, 20), fill="x")
        ctk.CTkLabel(bar_frame, text="Volume", text_color=ACCENT).pack(side="left", padx=16, pady=14)
        self.volume_bar = ctk.CTkProgressBar(bar_frame, progress_color=ACCENT)
        self.volume_bar.pack(side="left", fill="x", expand=True, padx=16)
        self.volume_bar.set(vc.get_volume())