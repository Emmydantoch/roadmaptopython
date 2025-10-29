import customtkinter as ctk

app = ctk.CTk()
app.geometry("1000x800")
app.title("Eating Healthy")

lable = ctk.CTkLabel(app, text="hello world", bg_color="blue")

lable.grid(row=0, column=0, padx=20, pady=20)


app.mainloop()
