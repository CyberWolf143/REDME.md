# 🔐 Password Strength Checker & Generator (Python)

A Python-based password security tool that checks password strength,
provides feedback, and generates strong passwords and secure passphrases.

---

## ✨ Features

- Password strength scoring (0–5)
- Advanced checking using zxcvbn (if available)
- Automatic fallback strength checker
- Strong random password generator
- Secure passphrase generator
- Bulk password checking from file
- Save generated passwords to file
- Colorful terminal output

---

## 📦 Requirements

- Python 3.7 or higher
- Optional (recommended):
  pip install zxcvbn

---
## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/CyberWolf143/REDME.md.git
```

2. Navigate to the project folder:
```bash
cd REDME.md
```

3. (Optional) Install zxcvbn:
```bash
pip install zxcvbn
```
---

## ▶️ Usage

### Interactive Mode
python password_tool_advanced.py

- Enter a password to check strength
- Get feedback and suggestions
- Type exit to quit

---

### Bulk Mode
python password_tool_advanced.py passwords.txt

Example passwords.txt:
password123
Admin@123
MySecurePass!9

---

## 💾 Output

Saved passwords location:
output/suggested_passwords.txt

---

## 🧠 Strength Levels

0 - Very Weak  
1 - Weak  
2 - Fair  
3 - Good  
4 - Strong  

---

## 🔑 Example Strong Password

X9@qL!2Fv^sA

---

## 🔤 Example Passphrase

matrix-galaxy-cyber-delta

---

## ⚠️ Notes

- Do not reuse passwords
- Store passwords securely
- For educational use only

---

## 👤 Author

CyberWolf143
