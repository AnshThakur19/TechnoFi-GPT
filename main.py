import tkinter as tk
import tkinter.ttk as ttk
from customtkinter import CTkScrollableFrame
from textwrap import wrap
from chatbot import askBot


class ResumeTab(tk.Frame):

    def __init__(self, parent):
        super().__init__(master=parent)

        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 14), padx=20, pady=10)

        tk.Label(self, text="Resume Generator", font=("Arial", 20, "bold")).pack(pady=10)

        frame1 = tk.Frame(self, padx=25)
        frame1.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=1)
        frame1.columnconfigure(1, weight=1)
        frame1.columnconfigure(2, weight=10)

        tk.Label(frame1, text="Name: ", font=("Arial", 14)).grid(row=1, column=1, pady=10, sticky="ew")

        self.name = ttk.Entry(frame1, font=("Arial", 14))
        self.name.grid(row=1, column=2, sticky="ew")

        tk.Label(frame1, text="E-Mail: ", font=("Arial", 14)).grid(row=2, column=1, pady=10, sticky="ew")

        self.email = ttk.Entry(frame1, font=("Arial", 14))
        self.email.grid(row=2, column=2, sticky="ew")

        tk.Label(frame1, text="Phone: ", font=("Arial", 14)).grid(row=3, column=1, pady=10, sticky="ew")

        self.phone = ttk.Entry(frame1, font=("Arial", 14))
        self.phone.grid(row=3, column=2, sticky="ew")

        tk.Label(frame1, text="Address: ", font=("Arial", 14)).grid(row=4, column=1, pady=10, sticky="ew")

        self.address = ttk.Entry(frame1, font=("Arial", 14))
        self.address.grid(row=4, column=2, sticky="ew")

        tk.Label(frame1, text="Job: ", font=("Arial", 14)).grid(row=5, column=1, pady=10, sticky="ew")

        self.job = ttk.Entry(frame1, font=("Arial", 14))
        self.job.grid(row=5, column=2, sticky="ew")

        tk.Label(frame1, text="Work Experience: ", font=("Arial", 14)).grid(row=6, column=1, pady=10, sticky="ew")

        self.work_exp = ttk.Entry(frame1, font=("Arial", 14))
        self.work_exp.grid(row=6, column=2, sticky="ew")

        tk.Label(frame1, text="Skills:", font=("Arial", 14)).grid(row=7, column=1, pady=10, sticky="ew")

        self.skills = ttk.Entry(frame1, font=("Arial", 14))
        self.skills.grid(row=7, column=2, sticky="ew")

        frame1.pack(fill="both", expand=True)

        text_button = ttk.Button(self, text="Save As Text File", command=self.getResponse)
        text_button.pack(pady=20)

    def getResponse(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        address = self.address.get()
        job = self.job.get()
        work_exp = self.work_exp.get()
        skills = self.skills.get()

        resume = askBot(f"Generate a professional Resume on the job: {job}. Here are some info, name: {name}, email: {email}, address: {address}, work experience: {work_exp}, skils: {skills}")
        with open(f"{job} Resume.txt", "w") as file:
            file.write(resume)


class ChatbotTab(tk.Frame):

    def __init__(self, parent):
        super().__init__(master=parent)

        tk.Label(self, text="ChatBot", font=("Arial", 20, "bold")).pack(pady=5)

        self.chatarea = CTkScrollableFrame(self, fg_color=self.cget("background"))
        self.chatarea.pack(fill="both", expand=True)

        frame1 = tk.Frame(self, padx=20, pady=10)
        frame1.rowconfigure(1, weight=1)
        frame1.columnconfigure(1, weight=10)
        frame1.columnconfigure(2, weight=1)

        self.userinput = ttk.Entry(frame1, font=("Consolas", 16))
        self.userinput.grid(row=1, column=1, sticky="nsew", padx=(0, 10))

        self.send_button = ttk.Button(frame1, text="Send", command=self.sendMessage)
        self.send_button.grid(row=1, column=2, sticky="nsew")

        frame1.pack(fill="x", side="bottom")

    def sendMessage(self):
        user_message = self.userinput.get()
        if user_message == "": return
        tk.Label(self.chatarea, text=user_message, font=("Consolas", 18), background="#a0a0a0", justify="left", padx=10, pady=5).pack(anchor="e", pady=10)

        self.userinput.delete(0, "end")
        self.after(100, lambda: self.receiveMessage(user_message))

    def receiveMessage(self, user_message):
        response = askBot(user_message)
        tk.Label(self.chatarea, text=self.format(response), font=("Consolas", 18), background="#a0a0a0", justify="left", padx=10, pady=5).pack(anchor="w", pady=10)

    def format(self, text):
        formatted_text = []
        for line in text.split("\n"):
            words = line.split("**")
            if words[0].startswith("# "): words = words[2:]
            elif words[0].startswith("## "): words = words[3:]
            elif words[0].startswith("### "): words = words[4:]
            elif words[0] == "* ": words[0] = "•"

            words = " ".join(words)
            words = "\n".join(wrap(words, 80))

            formatted_text.append(words)

        return "\n".join(formatted_text)[:-1]

        
root = tk.Tk()
root.geometry("500x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

resume_tab = ResumeTab(notebook)
resume_tab.pack(fill="both", expand=True)

chatbot_tab = ChatbotTab(notebook)
chatbot_tab.pack(fill="both", expand=True)

notebook.add(resume_tab, text="Resume Generator")
notebook.add(chatbot_tab, text="Chat Bot")

root.mainloop()
