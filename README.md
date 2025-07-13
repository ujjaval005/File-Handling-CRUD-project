# 🗂️ File Manager CLI – CRUD Operations Using Python

## 📌 Project Overview
This is a command-line interface (CLI) tool built in Python that allows users to perform basic **CRUD operations** (Create, Read, Update, Delete) on text files. It provides a simple way to manage file content directly from the terminal, making it ideal for learning file handling and building foundational skills in Python.

---

## 🚀 Features

- ✅ **Create**: Generate new text files and write initial content.
- 📖 **Read**: Display the contents of existing files.
- ✏️ **Update**: Append new data to existing files.
- 🗑️ **Delete**: Remove files from the system safely.
- 🛡️ **Validation**: Checks for file existence and handles exceptions gracefully.
- 🧩 **Modular Design**: Each operation is encapsulated in its own function for clarity and reuse.

---

## 🛠️ Technologies Used

- **Python 3.x**
- `os` and `pathlib` modules for file system interaction
- Exception handling for robust error management

---

## 📁 File Operations

| Operation | Function Name     | Description                              |
|-----------|-------------------|------------------------------------------|
| Create    | `createfile()`     | Creates a new file and writes content    |
| Read      | `readfile()`       | Displays contents of a file              |
| Update    | `updatefile()`     | Appends new content to an existing file  |
| Delete    | `deletefile()`     | Deletes a specified file                 |

---

## 🧠 Learning Outcomes

- Understand Python file I/O operations (`open`, `read`, `write`, `append`, `delete`)
- Practice exception handling and user input validation
- Build CLI tools with modular code structure
- Lay the groundwork for integrating file handling with data analysis or OSINT tools

---

## 📦 How to Run

1. Clone or download the repository.
2. Open the terminal and navigate to the project directory.
3. Run the Python script:
   ```bash
   python main.py