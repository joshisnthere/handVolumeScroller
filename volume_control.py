"""
Thin wrapper around pycaw so the rest of the app doesn't touch COM
interfaces directly. get_volume()/set_volume() work on a 0.0-1.0 scale.
Falls back to a no-op if pycaw isn't available (non-Windows systems).
"""

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume