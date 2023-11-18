import tkinter as tk
from predict import do_prediction
from rqst import add_report
from rqst import first_start


root= tk.Tk()
root.title("SPAM CHECKER")
root.geometry("500x600")
root.resizable(width=True, height=True)

def get_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    textBox.delete('1.0', 'end')
    return inputValue

def union():
    msg = get_input()
    result = do_prediction(msg)
    if (result == 1):
        final_opinion = "✅"
    else:
        final_opinion = "❌"
    #final_opinion = ("Spam result is " + str(result))
    label_result.configure(text=final_opinion)
    label_result.pack()
    add_report(str(msg), str(result[0][0]))


image = tk.PhotoImage(file='./Image/logo.png')
smaller_image = image.subsample(5, 5)  
panel = tk.Label(root, image = smaller_image)

textBox= tk.Text(root, 
             height=3, width=80, 
             borderwidth=5,
             font="Arial 18")

panel_text = tk.Label(text="Spam checker",
                   font="Arial 16")
panel_values = tk.Label(text="✅ = spam \n ❌ = NOT spam",
                   font="Arial 16")

buttonCommit= tk.Button(root, 
                    height=1, width=10, 
                    text="Check spam",font='Arial 20', 
                    command=lambda: union(),
                    borderwidth=5)

label_result = tk.Label(text="Loading...", font="Arial 20")
filler = tk.Label(text=' ')

first_start()

panel.pack(side = "top", fill = "both", expand = "yes")

panel_text.pack()
panel_values.pack()
textBox.pack()
buttonCommit.pack()
label_result.pack()
filler.pack()
tk.mainloop()