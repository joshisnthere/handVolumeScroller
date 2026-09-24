"""
Thin wrapper around pycaw so the rest of the app doesn't touch COM
interfaces directly. get_volume()/set_volume() work on a 0.0-1.0 scale.
Falls back to a no-op if pycaw isn't available (non-Windows systems).
"""

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    _devices = AudioUtilities.GetSpeakers()
    _interface = _devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    _volume = cast(_interface, POINTER(IAudioEndpointVolume))
    AVAILABLE = True
except Exception:
    AVAILABLE = False
    _volume = None


def get_volume():
    if not AVAILABLE:
        return 0.5
    return _volume.GetMasterVolumeLevelScalar()


def set_volume(level):
    level = max(0.0, min(1.0, level))
    if AVAILABLE:
        _volume.SetMasterVolumeLevelScalar(level, None)