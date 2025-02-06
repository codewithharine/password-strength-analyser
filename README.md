# password-strength-analyser
checking the strength  of any password
# Password Strength Checker

This simple Python program evaluates the strength of a password based on various criteria, including length, lowercase and uppercase letters, numbers, and special characters.

## 🚀 Features
- Checks if the password meets these security criteria:
  - At least **8 characters long**
  - Contains at least **one lowercase letter**
  - Contains at least **one uppercase letter**
  - Includes at least **one numeric digit**
  - Has at least **one special character** (`!@#$%^&*(),.?":{}|<>`)
- Provides detailed feedback for weak passwords.

---

## 🛠️ How to Use

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the program:**  
   Make sure you have Python installed and then execute:
   ```bash
   python password_checker.py
   ```

3. **Input Example:**
   ```
   Enter your password: MySecur3Pass!
   Strong Password!
   ```

---

## 📋 Requirements
- Python 3.x
- No external libraries are required (`re` is part of the standard library).

---

## 📝 Example Outputs
### **Weak Password Example**
```
Enter your password: abc123
Weak Password. Please ensure your password:
- Is at least 8 characters long
- Has at least one uppercase letter
- Contains at least one special character (!@#$%^&*)
```
### **Strong Password Example**
```
Enter your password: StrongP@ssw0rd
Strong Password!
```

---

## 🤔 Want Improvements?
Feel free to fork this project and contribute by adding features such as:
- GUI interface for better user interaction
- Saving password evaluation results in a file



