import tkinter as tk
#Use arial font for all.

def openGuideMenu(Parent):
#TODO: Parent.Destroy, Parent.Open, guide.Destroy when press press back
    Parent.destroy()

    guideWindow = tk.Tk()
    guideWindow.title("H.A.B.S Guide")

    guideTitle = tk.Label(guideWindow, text = "H.A.B.S Guide", font = ("Arial", 64, "bold"))
    guideTitle.place(relx = 0.5, rely = 0.05)

def openMainMenu():
    #Pass parent variable into the functions which are linked to buttons.
    mainWindow = tk.Tk()
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
