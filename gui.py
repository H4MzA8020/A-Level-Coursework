import tkinter as tk
#TODO: Use arial font for all text.

global mainWindow
mainWindow = tk.Tk()
# Hides mainwindow until main function is called.
mainWindow.withdraw()

def returnToMain(currentWindow, mainWindow):
    currentWindow.withdraw()
    mainWindow.deiconify()

def openGuideMenu(Parent):
    #TODO: Parent.Destroy;  Parent.Open -->  guide.Destroy when press press back
    #Hides window, does not destroy it so window can be opened again.
    Parent.withdraw()

    guideWindow = tk.Tk()
    guideWindow.title("H.A.B.S Guide")

    guideTitle = tk.Label(guideWindow, text = "H.A.B.S Guide", font = ("Arial", 64, "bold"))
    guideTitle.place(relx = 0.5, rely = 0.025)

    unitGuideHeading = tk.Label(guideWindow, text = "Unit Types", font = ("Arial", 32, "underline"))
    unitGuideHeading.place(relx = 0.01, rely = 0.095)

    unitStatsHeading = tk.Label(guideWindow, text = "Unit Statistics", font = ("Arial", 32, "underline"))
    unitStatsHeading.place(relx = 0.01, rely = 0.45)

    with open("unitguide.txt", "r") as unitTextFile:
        unitText = unitTextFile.read()
    with open("unitstats.txt", "r") as unitStatsFile:
        unitStats = unitStatsFile.read()

    unitGuide = tk.Message(guideWindow, width = 960, bg = guideWindow["bg"], relief = "flat", text = unitText )
    unitGuide.place(relx = 0.01, rely = 0.15)

    unitStatGuide = tk.Message(guideWindow, width = 960, bg = guideWindow["bg"], relief = "flat", text = unitStats)
    unitStatGuide.place(relx = 0.01, rely = 0.5)
    # Returns user to main menu.
    returnButton = tk.Button(guideWindow, text = "Return to menu", command = lambda: returnToMain(guideWindow, mainWindow))
    returnButton.place(relx = 0.01, rely = 0.01)


def openMainMenu():
    mainWindow.deiconify()
    mainWindow.title("Historically Accurate Battle Simulator!")

    title = tk.Label(mainWindow, text = "H.A.B.S", font = ("Arial", 64, "bold"))
     #Max paramter is 1.0 (Far right of parent on x-axis, botom edge of parent on y-axis)
    title.place(relx = 0.5, rely = 0.05)

    battleButton = tk.Button(mainWindow, text = "Battle", width = 20)
    battleButton.place(relx = 0.5, rely = 0.6)

    guideButton = tk.Button(mainWindow, text = "Guide", width = 20, command = lambda: openGuideMenu(mainWindow) )
    guideButton.place(relx = 0.5, rely = 0.7)

    settingsButton = tk.Button(mainWindow, text = "Settings", width = 20)
    settingsButton.place(relx = 0.5, rely = 0.8)

    mainWindow.mainloop()


openMainMenu()
