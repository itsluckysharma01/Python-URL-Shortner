import tkinter as tk
from tkinter import ttk, messagebox
import pyshorteners

def shorten():
    url = longurl_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL to shorten.")
        return
    try:
        shortner = pyshorteners.Shortener()
        short_url = shortner.tinyurl.short(url)
        shorturl_entry.config(state='normal')
        shorturl_entry.delete(0, tk.END)
        shorturl_entry.insert(0, short_url)
        shorturl_entry.config(state='readonly')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL:\n{e}")

def copy_to_clipboard():
    short_url = shorturl_entry.get()
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")

root = tk.Tk()
root.title("URL SHORTENER")
root.geometry("700x400")
root.configure(bg='#6C3483')

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#6C3483')
style.configure('TLabel', background='#6C3483', foreground='white', font=('Segoe UI', 12))
style.configure('Header.TLabel', background='#BB8FCE', foreground='#4A235A', font=('Segoe UI', 22, 'bold'))
style.configure('TButton', background='#BB8FCE', foreground='#4A235A', font=('Segoe UI', 11, 'bold'))
style.map('TButton', background=[('active', '#F7DC6F')])

main_frame = ttk.Frame(root, padding=20, style='TFrame', borderwidth=3, relief='ridge')
main_frame.pack(expand=True, fill='both', padx=15, pady=15)

header = ttk.Label(main_frame, text="URL SHORTENER", style='Header.TLabel', anchor='center')
header.pack(pady=(0, 15))

longurl_label = ttk.Label(main_frame, text="Enter Long URL:")
longurl_label.pack(anchor='w')
longurl_entry = ttk.Entry(main_frame, width=45, font=('Segoe UI', 11))
longurl_entry.pack(pady=(0, 10))

shorturl_label = ttk.Label(main_frame, text="Shortened URL:")
shorturl_label.pack(anchor='w')
shorturl_entry = ttk.Entry(main_frame, width=45, font=('Segoe UI', 11), state='readonly')
shorturl_entry.pack(pady=(0, 10))

shorten_button = ttk.Button(main_frame, text="SHORTEN", command=shorten)
shorten_button.pack(pady=8)

copy_button = ttk.Button(main_frame, text="COPY", command=copy_to_clipboard)
copy_button.pack(pady=8)    

root.mainloop() 