import tkinter as tk
from response_logic import get_response
from tts_speaker import speak

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")
        master.geometry("750x700")

        # === Themes ===
        self.light_theme = {
            "bg": "#ffffff",
            "fg": "#000000",
            "input_bg": "#f0f0f0",
            "chat_bg": "#eeeeee",
            "bot_bg": "#4CAF50",
            "copy_bg": "#2196F3",
            "voice_bg": "#ff9800"
        }

        self.dark_theme = {
            "bg": "#2e2e2e",
            "fg": "#ffffff",
            "input_bg": "#3e3e3e",
            "chat_bg": "#444444",
            "bot_bg": "#6aaf6a",
            "copy_bg": "#5fa8f0",
            "voice_bg": "#f57c00"
        }

        self.current_theme = self.dark_theme

        # === Chat Display ===
        self.chat_log = tk.Text(master, bg=self.current_theme["chat_bg"], fg=self.current_theme["fg"],
                                font=("Arial", 12), wrap=tk.WORD)
        self.chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        self.chat_log.config(state=tk.DISABLED)

        # === Button Frame ===
        self.button_frame = tk.Frame(master, bg=self.current_theme["bg"])
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(5, 10))

        # === Input Field (ABOVE buttons) ===
        self.user_input = tk.Entry(master, font=("Arial", 13),
                                   bg=self.current_theme["input_bg"], fg=self.current_theme["fg"])
        self.user_input.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0, 0))
        self.user_input.bind("<Return>", lambda e: self.send_message())

        # === Voice Menu Button ===
        self.tts_enabled = False
        self.voice_gender = "female"

        self.voice_button = tk.Button(self.button_frame, text="🔇 Voice", font=("Arial", 12),
                                      bg=self.current_theme["voice_bg"], fg="white")
        self.voice_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.voice_menu = tk.Menu(self.master, tearoff=0)
        self.voice_menu.add_command(label="Enable Voice (♀ Female)", command=lambda: self.set_voice(True, "female"))
        self.voice_menu.add_command(label="Enable Voice (♂ Male)", command=lambda: self.set_voice(True, "male"))
        self.voice_menu.add_separator()
        self.voice_menu.add_command(label="Disable Voice", command=lambda: self.set_voice(False))

        self.voice_button.bind("<Enter>", self.show_voice_menu)

        # === Theme Button ===
        self.theme_button = tk.Button(self.button_frame, text="☀️", command=self.toggle_theme,
                                      font=("Arial", 12), bg="#888", fg="white")
        self.theme_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # === Send Button ===
        self.send_button = tk.Button(self.button_frame, text="Send", command=self.send_message,
                                     font=("Arial", 12), bg=self.current_theme["bot_bg"], fg="white")
        self.send_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # === Copy Button ===
        self.copy_button = tk.Button(self.button_frame, text="Copy Selected", command=self.copy_selected_text,
                                     font=("Arial", 12), bg=self.current_theme["copy_bg"], fg="white")
        self.copy_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # === Initial Greeting ===
        self.update_chat("Bot", "Hello! I'm your chatbot. \nHow can I assist you today?")

        # === Apply Theme Initially ===
        self.apply_theme()

    def send_message(self):
        user_msg = self.user_input.get().strip()
        if user_msg == "":
            return
        self.user_input.delete(0, tk.END)
        self.update_chat("You", user_msg)
        bot_response = get_response(user_msg)
        self.update_chat("Bot", bot_response)
        if self.tts_enabled:
            self.master.after(100, lambda: speak(bot_response, gender=self.voice_gender))

    def update_chat(self, sender, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, f"{sender}:\n{message}\n\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.see(tk.END)

    def copy_selected_text(self):
        try:
            selected_text = self.chat_log.selection_get()
            self.master.clipboard_clear()
            self.master.clipboard_append(selected_text)
            self.master.update()
            self.update_chat("Bot", "Text copied to clipboard.")
        except tk.TclError:
            self.update_chat("Bot", "Nothing selected to copy.")

    def show_voice_menu(self, event):
        try:
            self.voice_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.voice_menu.grab_release()

    def set_voice(self, enabled, gender=None):
        self.tts_enabled = enabled
        if gender:
            self.voice_gender = gender
        icon = "🔊" if self.tts_enabled else "🔇"
        self.voice_button.config(text=f"{icon} Voice")

    def toggle_theme(self):
        if self.current_theme == self.light_theme:
            self.current_theme = self.dark_theme
            self.theme_button.config(text="☀️")
        else:
            self.current_theme = self.light_theme
            self.theme_button.config(text="🌙")
        self.apply_theme()

    def apply_theme(self):
        t = self.current_theme
        self.master.configure(bg=t["bg"])
        self.chat_log.configure(bg=t["chat_bg"], fg=t["fg"])
        self.user_input.configure(bg=t["input_bg"], fg=t["fg"], insertbackground=t["fg"])
        self.button_frame.configure(bg=t["bg"])
        self.send_button.configure(bg=t["bot_bg"])
        self.copy_button.configure(bg=t["copy_bg"])
        self.voice_button.configure(bg=t["voice_bg"])
        self.theme_button.configure(bg="#888")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
