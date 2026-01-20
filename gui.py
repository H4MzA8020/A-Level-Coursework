import tkinter as tk
volume = 0
# Initializes main window.
mainWindow = tk.Tk()
# Hides main window until main function is called.
mainWindow.withdraw()

def returnToMain(currentWindow, mainWindow):
    currentWindow.withdraw()
    mainWindow.deiconify()

def openGuideMenu(Parent):
    #Hides window, does not destroy it so window can be opened again.
    Parent.withdraw()

    guideWindow = tk.Tk()
    guideWindow.title("H.A.B.S Guide")

    guideTitle = tk.Label(guideWindow, text = "H.A.B.S Guide", font = ("Arial", 64, "bold"))
    guideTitle.place(relx = 0.4, rely = 0.025)

    unitGuideHeading = tk.Label(guideWindow, text = "Unit Types", font = ("Arial", 32, "underline"))
    unitGuideHeading.place(relx = 0.01, rely = 0.095)

    unitStatsHeading = tk.Label(guideWindow, text = "Unit Statistics", font = ("Arial", 32, "underline"))
    unitStatsHeading.place(relx = 0.01, rely = 0.45)

    #Guides are stored in a text file outside GUI program for cleaner code.
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


def setVolume(volumeSlider):
    global volume
    volume = volumeSlider.get()
    # Printing for testing purposes. Delete later.
    print(volume)

def openSettingsMenu(Parent):
    global volume
    Parent.withdraw()

    settingsWindow = tk.Tk()

    settingsTitle = tk.Label(settingsWindow, text = "Settings", font = ("Arial", 64, "bold"))
    settingsTitle.place(relx = 0.43, rely = 0.025)

    returnButton = tk.Button(settingsWindow, text = "Return to menu", command = lambda: returnToMain(settingsWindow, mainWindow))
    returnButton.place(relx = 0.01, rely = 0.01)

    volumeHeading = tk.Label(settingsWindow, text = "Volume", font = ("Arial", 32, "underline"))
    volumeHeading.place(relx = 0.01, rely = 0.2)

    volumeBar = tk.Scale(settingsWindow, from_=0, to=100, length = 600, tickinterval = 5, orient = tk.HORIZONTAL)
    volumeBar.place(relx = 0.3, rely = 0.3)

    setVolumeButton = tk.Button(settingsWindow, text = "Set Volume", width = 20, command = lambda: setVolume(volumeBar))
    setVolumeButton.place(relx = 0.3, rely = 0.4)

    changeLanguageHeading = tk.Label(settingsWindow, text = "Change Language", font = ("Arial", 32, "underline"))
    changeLanguageHeading.place(relx = 0.01, rely = 0.5)
    #TODO: Add Functionality which changes language.
    changeToEnglishButton = tk.Button(settingsWindow, text = "English", width = 40, height = 5)
    changeToEnglishButton.place(relx = 0.35, rely = 0.6)

    changeToFrenchButton = tk.Button(settingsWindow, text = "French", width = 40, height = 5)
    changeToFrenchButton.place(relx = 0.35, rely = 0.75)

    changeToSpanishButton = tk.Button(settingsWindow, text = "Spanish", width = 40, height = 5)
    changeToSpanishButton.place(relx = 0.35, rely = 0.9)

def openBattleMenu(Parent):
    Parent.withdraw()

    mapSelectionWindow = tk.Tk()

    mapSelectionHeading = tk.Label(mapSelectionWindow, text = "Choose a battlefield...", font = ("Arial", 64, "bold"))
    mapSelectionHeading.place(relx = 0.3, rely = 0.025)

    returnButton = tk.Button(mapSelectionWindow, text = "Return to menu", command = lambda: returnToMain(mapSelectionWindow, mainWindow))
    returnButton.place(relx = 0.01, rely = 0.01)


def openMainMenu():
    mainWindow.deiconify()
    mainWindow.title("Historically Accurate Battle Simulator!")

    title = tk.Label(mainWindow, text = "H.A.B.S", font = ("Arial", 64, "bold"))
    #Max paramter is 1.0 (Far right of parent on x-axis, botom edge of parent on y-axis)
    title.place(relx = 0.45, rely = 0.05)

    battleButton = tk.Button(mainWindow, text = "Battle", width = 30, height = 3, command = lambda: openBattleMenu(mainWindow))
    battleButton.place(relx = 0.45, rely = 0.6)

    guideButton = tk.Button(mainWindow, text = "Guide", width = 30, height = 3, command = lambda: openGuideMenu(mainWindow) )
    guideButton.place(relx = 0.45, rely = 0.7)

    settingsButton = tk.Button(mainWindow, text = "Settings", width = 30, height = 3,  command = lambda: openSettingsMenu(mainWindow))
    settingsButton.place(relx = 0.45, rely = 0.8)

    mainWindow.mainloop()


openMainMenu()
