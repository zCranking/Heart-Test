from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x700")
root.config(background="#5158bb")
root.title("Heart Test")

q1_input = StringVar(value = "0")
q1Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="1. Do you experience shortness of breath during routine activites?")
q1radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q1_input, value="yes")
q1radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q1_input, value="no")
q1Label.place(relx=0.5, rely=0.05, anchor=CENTER)
q1radioY.place(relx=0.5, rely=0.1, anchor=CENTER)
q1radioN.place(relx=0.5, rely=0.15, anchor=CENTER)

q2_input = StringVar(value = "0")
q2Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="2. Do you experience shortness of breath while at rest/lying down?")
q2radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q2_input, value="yes")
q2radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q2_input, value="no")
q2Label.place(relx=0.5, rely=0.2, anchor=CENTER)
q2radioY.place(relx=0.5, rely=0.25, anchor=CENTER)
q2radioN.place(relx=0.5, rely=0.3, anchor=CENTER)

q3_input = StringVar(value = "0")
q3Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), wraplength=600, text="3. Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?")
q3radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q3_input, value="yes")
q3radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q3_input, value="no")
q3Label.place(relx=0.5, rely=0.35, anchor=CENTER)
q3radioY.place(relx=0.5, rely=0.4, anchor=CENTER)
q3radioN.place(relx=0.5, rely=0.45, anchor=CENTER)

q4_input = StringVar(value = "0")
q4Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), wraplength=600, text="4. Do you feel tired while doing routien activites such as shopping, climbing stairs, carrying groceries or walking?")
q4radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q4_input, value="yes")
q4radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q4_input, value="no")
q4Label.place(relx=0.5, rely=0.5, anchor=CENTER)
q4radioY.place(relx=0.5, rely=0.55, anchor=CENTER)
q4radioN.place(relx=0.5, rely=0.6, anchor=CENTER)

q5_input = StringVar(value = "0")
q5Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="5. Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
q5radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q5_input, value="yes")
q5radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q5_input, value="no")
q5Label.place(relx=0.5, rely=0.65, anchor=CENTER)
q5radioY.place(relx=0.5, rely=0.7, anchor=CENTER)
q5radioN.place(relx=0.5, rely=0.75, anchor=CENTER)

q6_input = StringVar(value = "0")
q6Label = Label(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="6. Do you often feel that you are having a racing heartbeat and experience palpitations?")
q6radioY = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="yes", variable=q6_input, value="yes")
q6radioN = Radiobutton(root, bg="#5158bb", foreground="#7ABA50", font=("Comic Sans MS", "12", "normal"), text="no", variable=q6_input, value="no")
q6Label.place(relx=0.5, rely=0.8, anchor=CENTER)
q6radioY.place(relx=0.5, rely=0.85, anchor=CENTER)
q6radioN.place(relx=0.5, rely=0.9, anchor=CENTER)

score_label = Label(root, text="Score : 0")
score_label.place(relx=0.05, rely=0.05, anchor=CENTER)

def teachercheck():
    score = 0
    if q1_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q2_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q3_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q4_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q5_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q6_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    
    if score < 2:
        messagebox.showinfo("Summary", "You have a very low chance of having any heart problems.")
    if score >= 2 and score <=4:
        messagebox.showinfo("Score", "You might want to get checked by the doctor if you have a recent history.")
    if score >= 5:
        messagebox.showinfo("Score", "You want to get checked by the doctor.")


btn = Button(root, text="check", command=teachercheck)
btn.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()