# Chat App

This project was developed when I was **11 years old**.
It’s a simple chatbot app with a custom GUI using [customtkinter](https://github.com/TomSchimansky/CustomTkinter) and [Ollama](https://ollama.com).

---

## 🚀 How does it work?
- User writes text into the entry box and presses **Enter** or **"Say"** button.
- The bot generates a response using the Ollama model.
- Special commands:
    - `/exit`, `/quit`, `/leave` → exit the program
    - `/clear`, `/cls` → clear the messages
    - `/reset`, `/restart` → clear history + reset chat

---


## 📦 Requirements
- Python 3.x
- `customtkinter` library
- Ollama CLI (with model of your choice)

---

## ⚙️ Setup

### 1. Install customtkinter:
Open **cmd** and run:

`pip install customtkinter`

### 2. Install Ollama model

`ollama pull [model_name]`

Replace [model_name] with the model you want.
In this project I used llama3.1:8b, so I wrote:

`ollama pull llama3.1:8b`

Check installed models with:

`ollama list`

## ▶️ Running
Download this project and place it in a folder.
Open cmd and navigate to the folder:

`cd [path]`

✅ Example:

`cd C:\Users\User\Documents\VS-Projects`

❌ Not like this (because main.py is a file, not a folder):
`cd C:\Users\User\Documents\VS-Projects\main.py`

Run the script:

`py main.py`

A window will appear and you can start using the chatbot 🎉

---

## 🎥 Demo

To see how it works, check out this  [YouTube video](url)

## 📖 License

MIT License

This code is completely open. You can use it however you want, share it, and develop it.  
**Please give credit** by linking back to the original project so people can find the real data.
