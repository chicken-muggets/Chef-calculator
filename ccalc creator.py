import tkinter.filedialog

def main():
    print("where should we create the file")
    dir = tkinter.filedialog.askdirectory()
    filename = input("what is the name of the file: ")
    finaldir = dir+"\\"+filename+".ccalc"
    file = open(finaldir,'a+')
    recipeName = input("what is the name of the recipie: ")
    file.write("<Foodname>: "+ recipeName +"\n")
    def writeIngr(ingrAmount):
        ingr = input("write an ingredient: ")
        file.write("<Ingr"+str(ingrAmount)+">:"+ingr+"\n")
        ingrServe = input("how much is needed per serving: ")
        file.write("<Quant"+ingr+">:"+ingrServe+"\n")
        more = input("is there another ingredient?: ")
        ingrAmount+=1
        if more=="yes":
            writeIngr(ingrAmount)
        else:
            print("stopping adding recipies")
    writeIngr(1)
    def writeStep(stepAmount):
        Step = input("write a Step: ")
        file.write("<Step"+str(stepAmount)+">:"+Step+"\n")
        more = input("is there another Step?: ")
        stepAmount+=1
        if more=="yes":
            writeStep(stepAmount)
        else:
            print("stopping adding recipies")
    writeStep(1)
    credtest = input("Do you have any website, book, ect to credit [yes] [no]: ")

    if credtest == "yes":
        creds = input("place the website or book here: ")
        file.write("<Creds>: "+ creds + "\n")
    minsToMake = input("how many minutes do you think it would take for the average person to make: ")
    file.write("<MinutesToMake>: " + minsToMake + "\n")
    creator = input("who is the creator (put unknown if you don't know): ")
    if creator != "unknown":
        file.write("<RecipeCreator>: "+ creator + "\n")
    else:
        print("No creator added")
    Difficulty = input("what is the difficulty of this recipe to the average person [beginner, intermediate, advanced]: ")
    file.write("<Difficulty>: " + Difficulty)
    file.close()
    print("finished creating file")
main()