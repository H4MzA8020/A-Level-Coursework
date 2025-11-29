import tkinter as tk
#Use arial font for all.

def mainMenu():
    #Parent window.
    mainWindow = tk.Tk()
    mainWindow.title("Historically Accurate Battle Simulator!")

    title = tk.Label(mainWindow, text = "H.A.B.S", font = ("Arial", 64, "bold"))
     #Max paramter is 1.0 (Far right of parent on x-axis, botom edge of parent on y-axis)
    title.place(relx = 0.5, rely = 0.05)

    battleButton = tk.Button(mainWindow, text = "Battle", width = 20)
    battleButton.place(relx = 0.5, rely = 0.6)

    guideButton = tk.Button(mainWindow, text = "Guide", width = 20)
    guideButton.place(relx = 0.5, rely = 0.7)

    settingsButton = tk.Button(mainWindow, text = "Settings", width = 20)
    settingsButton.place(relx = 0.5, rely = 0.8)

    mainWindow.mainloop()


mainMenu()
