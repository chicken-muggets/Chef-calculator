from tkinter import *
from tkinter import ttk
from ctypes import windll
import tkinter.filedialog
#this stops it from being blurry on high dpi screens I found it on https://bit.ly/3Kvnfyw
windll.shcore.SetProcessDpiAwareness(1)
def main():
    #TODO Add quantitys 
    #makes a window
    window = Tk()
    #defines the propertys of the window like size, title, and wether or not it can be resized
    window.title("Chef calculator")
    window.geometry('500x500')
    window.resizable(False,False)
    #adds a canvas and a scrollbar to allow scrolling
    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    canvas = Canvas(window, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff",highlightthickness=0,borderwidth=0)
    vsb = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    #packs the scrollbar and the canvas
    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    #defines the global variables
    global Food_name_Label
    global Ingredients_Label
    global Ingredient_Label
    global StepsLabel
    global Step_Label
    # main
    #the function called when the select file button is pressed
    def SelFile():
        global Food_name
        #creates a file selection menu
        fileSelector = tkinter.filedialog.askopenfilename()
        #opens the file as a var called openFile
        openFile = open(fileSelector, "r")
        line_number = 1
        for line in openFile:
            line_number += 1
            if "<Foodname>:" in line:
                Food_name = line.replace("<Foodname>:", '').strip()
                line_number = 0
                Food_name_Label= Label(frame, text="Here is the recipie for " + Food_name,wraplength=473,bg='#fff')
                Food_name_Label.pack()
                break
        openFile.close()
        openFile = open(fileSelector, "r")
        for timeLine in openFile:
            if "<MinutesToMake>:" in timeLine:
                time_to_make_name = timeLine.replace("<MinutesToMake>:", '').strip()
                timeLineLabel = Label(frame,text="this will take you " + time_to_make_name + " minutes to make",wraplength=473,bg='#fff')
                timeLineLabel.pack()
                break
        Ingredients_Label = Label(frame, text="You will need: ", font=("Helectivia", 9, "bold"),wraplength=473,bg='#fff')
        Ingredients_Label.pack()
        Ingredient_Number = 1
        Step_Number = 1
        openFile.close()
        openFile = open(fileSelector, "r")
        for Ingr_line in openFile:
            has_Quant = False
            if "<Ingr" + str(Ingredient_Number) + ">:" in Ingr_line:
                Ingredient_Number += 1
                Ingredient = Ingr_line.replace("<Ingr" + str(Ingredient_Number-1) + ">:", '').strip()
                Ingredient_Label = Label(frame, text=Ingredient,wraplength=473,bg='#fff')
                for quant_line in openFile:
                    if "<Quant" + Ingredient + ">:" in quant_line:
                        Quant = quant_line.replace("<Quant" + Ingredient + ">:", '').strip()
                        if selectQuant.get() != "":
                            finalAmount = float(Quant)*float(selectQuant.get())
                        else:
                            finalAmount = float(Quant)*1
                        Ingredient_Label = Label(frame, text=str(finalAmount) + " " + Ingredient,wraplength=473,bg='#fff')
                        Ingredient_Label.pack()
                        break
                    break
        openFile.close()
        openFile = open(fileSelector, "r")
        StepsLabel = Label(frame, text="Steps: ", font=("Helectivia", 9, "bold"),wraplength=473,bg='#fff')
        StepsLabel.pack()
        for Step_line in openFile:
            if "<Step" + str(Step_Number) + ">:" in Step_line:
                Step_Number += 1
                Step = Step_line.replace("<Step" + str(Step_Number-1) + ">:", '').strip()
                Step_Label = Label(frame, text="Step " + str(Step_Number-1) + ": " + Step,wraplength=473,bg='#fff')
                Step_Label.pack()
        openFile.close()
        openFile = open(fileSelector, "r")
        for Creds_line in openFile:
            if "<Creds>:" in Creds_line:
                Optinal_Label = Label(frame, text="Other info", font=("Helectivia", 9, "bold"),wraplength=473,bg='#fff')
                Optinal_Label.pack()
                Credits_Label = Label(frame, text="Credits to " + Creds_line.replace("<Creds>:", '').strip() + " for the recipe",wraplength=473,bg='#fff')
                Credits_Label.pack()
                break
        openFile.close()
        selectFile['state'] = DISABLED
        selectQuant['state'] = DISABLED
        newRecipie.pack()
    def RelFile():
        window.destroy()
        main()
    selectFile = ttk.Button(frame, text="Select File", command=SelFile)
    selectQuant = ttk.Entry(frame)
    selectQuantinfo = ttk.Label(frame,text="how many people are you serving?", background="white")
    newRecipie = ttk.Button(frame, text="Reset", command=RelFile)
    #label only exists to space out the input and the button
    spaceLabel = ttk.Label(frame,text="",background="white")
    selectQuantinfo.pack()
    selectQuant.pack()
    spaceLabel.pack()
    selectFile.pack()
    window.mainloop()
if __name__ == '__main__':
    main()