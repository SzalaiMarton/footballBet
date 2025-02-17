import getDataFromSite as data
import processCSVFile
from tkinter import *

window = Tk()
window.title("Bet")
window.geometry("500x500")

getDataLabel = Label(window, text = "To get data from: https://www.football-data.co.uk/englandm.php")
getDataLabel.grid()

getDataSuccessful = Label(window, text = "Data successfully extracted from site")
getDataSuccessful.grid_forget()

getDataFailed = Label(window, text = "Faild to extract data from site")
getDataFailed.grid_forget()

def main():
    window.mainloop()

def getDataPressed():
    if data.getData():
        showSuccess()
    else:
        showError()

def showError():
    getDataFailed.grid()

def showSuccess():
    getDataSuccessful.grid()

getDataButton = Button(window, text = "Press this", command=getDataPressed)
getDataButton.grid()

if __name__ == "__main__":
    main()