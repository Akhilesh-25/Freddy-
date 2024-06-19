from tkinter import*
root = Tk()
root.title("AI Assistent")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

#frame

frame = LabelFrame(root , padx = 100 , pady=7 , borderwidth= 3 , relief="raised")
frame.grid(row = 0 , column = 1 , padx = 55 , pady = 10)

#textlabel

text_label = Label(frame, text="AI ASSISTANT" , font=("comic Sans ms", 14 , "bold") , bg="#")
text_label.grid(row = 0 , column = 0 , padx = 20 , pday = 10)







root.mainloop()