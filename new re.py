import re
import random
import string
import os
import sys

try:
    from zxcvbn import zxcvbn
    ZXCVBN_AVAILABLE = True
except Exception:
    ZXCVBN_AVAILABLE = False


# ---------- COLORS ----------
class C:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


# ---------- GENERATORS ----------
def generate_strong_password(length=14):
    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*()-_=+[]{}<>?/|"
    )

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_=+[]{}<>?/|"),
    ]

    password += [random.choice(chars) for _ in range(length - 4)]
    random.shuffle(password)

    return "".join(password)


def generate_passphrase(words=4):
    wordlist = [
        "matrix","tiger","rocket","shadow","cyber","secure",
        "python","galaxy","signal","ocean","hunter","legend",
        "binary","spartan","fusion","cosmos","metal","delta"
    ]
    return "-".join(random.sample(wordlist, words))


def save_to_file(password):
    os.makedirs("output", exist_ok=True)
    path = "output/suggested_passwords.txt"

    with open(path, "a") as f:
        f.write(password + "\n")

    print(f"{C.CYAN}Saved to:{C.END} {path}")


# ---------- FALLBACK CHECK ----------
def fallback_score(password: str):
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("Include numbers.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\",.<>/?]", password): score += 1
    else: feedback.append("Include special characters.")

    labels = ["Very Weak","Weak","Fair","Good","Strong","Very Strong"]
    score = min(score, 5)

    return score, labels[score], feedback


# ---------- ZXCVBN ----------
def check_password(password: str):
    if ZXCVBN_AVAILABLE:
        result = zxcvbn(password)
        score = result["score"]
        strength = ["Very Weak","Weak","Fair","Good","Strong"][score]
        feedback = result["feedback"]["suggestions"]
        return score, strength, feedback

    return fallback_score(password)


# ---------- BULK MODE ----------
def bulk_check(file_path):
    if not os.path.exists(file_path):
        print(f"{C.RED}File not found:{C.END} {file_path}")
        return

    print(f"\n{C.BOLD}{C.CYAN}Bulk Checking Passwords...{C.END}\n")

    with open(file_path, "r") as f:
        for line in f:
            pwd = line.strip()
            if not pwd:
                continue

            score, strength, _ = check_password(pwd)
            bar = "█" * score + "-" * (5 - score)

            print(f"{pwd:25}  [{bar}]  {strength}")

    print(f"\n{C.GREEN}Done.{C.END}\n")


# ---------- MAIN LOOP ----------
def main():
    # bulk mode via: python password_tool_advanced.py passwords.txt
    if len(sys.argv) == 2:
        bulk_check(sys.argv[1])
        return

    print(f"\n{C.BOLD}{C.CYAN}🔐 Password Strength Checker + Suggestions{C.END}")
    print("Type exit to quit\n")

    while True:
        pwd = input("Enter password: ")

        if pwd.lower() == "exit":
            print("\nGoodbye 👋")
            break

        if not pwd.strip():
            print(f"{C.YELLOW}Password cannot be empty\n{C.END}")
            continue

        score, strength, feedback = check_password(pwd)

        colors = [C.RED, C.RED, C.YELLOW, C.CYAN, C.GREEN, C.GREEN]
        bar = "█" * score + "-" * (5 - score)

        print(f"\n{colors[score]}Score: [{bar}] {score}/5{C.END}")
        print(f"Strength: {C.BOLD}{strength}{C.END}")

        if feedback:
            print(f"\n{C.YELLOW}Improve:{C.END}")
            for f in feedback:
                print(" -", f)

        strong = generate_strong_password()
        phrase = generate_passphrase()

        print(f"\n{C.GREEN}Suggested Strong Password:{C.END}\n > {strong}")
        print(f"\n{C.CYAN}Passphrase:{C.END}\n > {phrase}")

        save = input("\nSave suggestions to file? (y/n): ").lower()
        if save == "y":
            save_to_file(strong)
            save_to_file(phrase)

        print("\n----------------------------------\n")


if __name__ == "__main__":
    main()
