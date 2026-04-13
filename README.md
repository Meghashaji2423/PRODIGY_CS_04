# ⌨️ Educational Keylogger Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-red.svg)
![Educational](https://img.shields.io/badge/purpose-educational-green.svg)

> **⚠️ IMPORTANT DISCLAIMER**: This tool is created for **EDUCATIONAL PURPOSES ONLY**. 
> Only use on your own computer or with explicit written permission. 
> Unauthorized keylogging is ILLEGAL and violates privacy laws.


## 🎯 Overview

This is a **simple educational keylogger** developed for **Prodigy Infotech Task-04**. It demonstrates how keyboard input can be captured and logged, helping understand:
- How malicious software can track keystrokes
- Security vulnerabilities in systems
- Methods to protect against keyloggers

## ❓ What is a Keylogger?

A **keylogger** (keystroke logger) is a type of surveillance software that records every key pressed on a keyboard. 

### Types of Keyloggers:

| Type | Description | Example |
|------|-------------|---------|
| **Software-based** | Runs as a program in background | This project |
| **Hardware-based** | Physical device between keyboard and computer | USB keylogger |
| **Kernel-level** | Runs at operating system level | Rootkit keyloggers |
| **Browser-based** | JavaScript keyloggers in web pages | Form jacking |

## ✨ Features

- ✅ **Real-time key capture** - Records keys as they're pressed
- ✅ **Timestamp logging** - Each keystroke has exact time
- ✅ **Special key handling** - Captures Space, Enter, Backspace, etc.
- ✅ **Clean log files** - Organized output for easy reading
- ✅ **Live display** - Shows keystrokes in terminal
- ✅ **Easy stop mechanism** - Press ESC or Ctrl+C to stop
- ✅ **Cross-platform** - Works on Windows, Mac, Linux

## 🔧 How It Works

### Simple Explanation:
## 🔧 How It Works
### Simple Explanation:
1. Uses **pynput library** to listen to keyboard events
2. Every key press triggers a callback function
3. Keystrokes are saved to a log file with timestamps
4. Special keys (Space, Enter, Backspace) are handled separately
5. Press **ESC** to stop the logger

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/Meghashaji2423/PRODIGY_CS_04.git
cd PRODIGY_CS_04

# Install required library
pip3 install pynput

# Run the program
python3 keylogger.py
```

## 📋 Usage Guide
```bash
# Start the keylogger
python3 keylogger.py

# Type anything to log keystrokes
# Press ESC or Ctrl+C to stop
```

## 📄 Example Output
=== Keylogger Started ===
[2026-04-12 15:30:01] Key: H
[2026-04-12 15:30:01] Key: e
[2026-04-12 15:30:01] Key: l
[2026-04-12 15:30:01] Key: [Space]
[2026-04-12 15:30:02] Key: [Enter]
=== Keylogger Stopped ===

## ⚖️ Ethical Guidelines
- 🔴 **NEVER** use on someone else's computer without permission
- 🔴 **NEVER** use to steal passwords or personal information
- 🟢 **ONLY** use for educational purposes
- 🟢 **ONLY** use on your own computer
- 🟢 **ALWAYS** delete log files after testing

## 🛡️ Protection Against Keyloggers
- Use a **Virtual Keyboard** for sensitive input
- Install a good **Antivirus** software
- Keep your **OS updated**
- Use **Two-Factor Authentication**
- Monitor running processes regularly

## 📁 Project Structure
PRODIGY_CS_04/
│
├── keylogger.py        # Main Python script
└── README.md           # Project documentation

## 📚 What I Learned
- How keyloggers work internally
- The pynput library for keyboard monitoring
- Importance of ethical hacking and user consent
- Why endpoint security matters
- Real-world cybersecurity vulnerabilities

## ⚠️ Legal Disclaimer
This project is strictly for **educational purposes** as part of a Cyber Security internship at Prodigy InfoTech. The author is not responsible for any misuse of this tool.

## 🏢 Internship Details
**Company:** Prodigy InfoTech  
**Track:** Cyber Security  
**Task:** PRODIGY_CS_04  
**Duration:** March 2026 – April 2026

## 👤 Author
**Megha Shaji**  
🔗 [LinkedIn](https://www.linkedin.com/in/megha-shaji/)  
🐙 [GitHub](https://github.com/Meghashaji2423)
