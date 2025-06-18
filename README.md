# Python-URL-Shortner
---

### ✅ Suggested Tweaks:

1. **Improve the Screenshot Section** (replace placeholder with actual image once ready).
2. **Add GUI Preview GIF** for more engagement (if available).
3. **Add Requirements Section** before installation.
4. **Link to `.py` file** directly if it's in the repo root.



# 🔗 Python URL Shortener (GUI)

A fun and beginner-friendly desktop app to shorten long URLs using Python!
This app uses the **TinyURL API** and provides a colorful **Tkinter GUI** to make URL shortening smooth and interactive.

![Python URL Shortener](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tkinter GUI](https://img.shields.io/badge/GUI-Tkinter-purple)
![URL Shortening](https://img.shields.io/badge/API-TinyURL-orange)

---

## 💡 Features

* ✂️ Convert long URLs into short links using TinyURL
* 🖥️ Simple graphical interface—no coding required
* ⚡ Real-time results with one click
* 🎨 User-friendly color scheme (purple and red themed)

---

## 🧰 Built With

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI framework
* [pyshorteners](https://pypi.org/project/pyshorteners/) – URL shortening library

---

## 🔧 Requirements

* Python 3.6 or higher
* Internet connection (TinyURL is an online service)
* `pyshorteners` library

Install it using:

```bash
pip install pyshorteners
```

---

## 📸 App Preview

> **Enter a long URL → Click “SHORTEN” → Get a short link instantly!**

---

## 📦 Installation & Usage

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/url-shortener-python.git
   cd url-shortener-python
   ```

2. **Install dependencies:**

   ```bash
   pip install pyshorteners
   ```

3. **Run the app:**

   ```bash
   python url_shortener.py
   ```

---

## 🧠 How It Works

```python
shortner = pyshorteners.Shortener()
short_url = shortner.tinyurl.short(longurl_entry.get())
```

* The user enters a URL into the input field.
* On clicking the **SHORTEN** button, the app uses `pyshorteners` to fetch a TinyURL.
* The result is displayed instantly in the output field.

---

## 🛠️ Future Enhancements

* 📋 "Copy to Clipboard" button
* 🧪 Better error handling for invalid URLs
* 🌐 Support for other services like Bitly, is.gd, etc.

---
