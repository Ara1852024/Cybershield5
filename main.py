# main.py
import threading
import webview
from app import app  # Import the app object from app.py

def start_flask():
    app.run()

if __name__ == '__main__':
    threading.Thread(target=start_flask).start()
    webview.create_window("Cybershield", "http://127.0.0.1:5000")
