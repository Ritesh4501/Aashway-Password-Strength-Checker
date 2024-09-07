
# Password Strength Checker Tool

## Overview
The **Password Strength Checker Tool** is a Python-based desktop application built using `Tkinter`. It helps users evaluate the strength of their passwords in real-time and provides feedback based on several password criteria such as length, use of uppercase/lowercase characters, numbers, and special characters.

### Features:
- **Real-time Password Evaluation**: As you type, the strength of your password is assessed.
- **Dynamic Progress Bar**: A color-changing progress bar (red -> orange -> green) visually indicates password strength.
- **Strength Feedback**: Text feedback is displayed based on the strength of the password (Weak, Medium, or Strong).
- **Strong Password Suggestions**: A button generates a strong, random password.
- **Cross-platform**: Works on Windows, macOS, and Linux.

## Screenshot
![Password Strength Checker Tool](./screenshots/password_strength_checker.png)

## Requirements
- **Python 3.x** 
- `Tkinter` (Python's standard GUI library)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ritesh4501/Aashway-Password-Strength-Checker.git
   cd password-strength-checker
   ```

2. **Install Tkinter (if not already installed):**

   - **Ubuntu/Debian:**
     ```bash
     sudo apt-get install python3-tk
     ```
   - **macOS:**
     ```bash
     brew install python-tk
     ```
   - **Windows:**
     Tkinter comes pre-installed with Python.

3. **Run the Application:**

   ```bash
   python3 password_checker.py
   ```

## Usage

1. **Enter your password**: Type your password into the input field.
2. **Real-time feedback**: The tool will evaluate the strength of your password in real time.
3. **View strength**: The progress bar changes color from red (weak) to orange (medium) to green (strong) based on the strength of your password.
4. **Generate a strong password**: Click on the `Generate Strong Password` button to get a secure password suggestion.

## Customization

- **Change Password Strength Criteria**: 
   You can customize the password strength criteria by modifying the `calculate_strength()` function in `password_checker.py`.
   
- **Change Password Length**:
   Modify the password length for generated passwords in the `suggestStrongPassword()` function in `password_checker.py`.

## Example

Here’s how the tool works:

```python
import tkinter as tk
from tkinter import ttk

# Functionality of Password Checker Tool...
```

## Contributing
Feel free to open a pull request or issue if you want to contribute to this project.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Open a pull request when your feature is ready.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.