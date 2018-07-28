font = ['', '                _                        _       __  __        _____                            _',
        '     /\\        | |                      | |     |  \\/  |      / ____|                          | |',
        '    /  \\  _   _| |_ ___  _ __ ___   __ _| |_ ___| \\  / |_   _| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __',
        "   / /\\ \\| | | | __/ _ \\| '_ ` _ \\ / _` | __/ _ \\ |\\/| | | | | |    / _ \\| '_ ` _ \\| '_ \\| | | | __/ _ \\ '__|",
        '  / ____ \\ |_| | || (_) | | | | | | (_| | ||  __/ |  | | |_| | |___| (_) | | | | | | |_) | |_| | ||  __/ |',
        ' /_/    \\_\\__,_|\\__\\___/|_| |_| |_|\\__,_|\\__\\___|_|  |_|\\__, |\\_____\\___/|_| |_| |_| .__/ \\__,_|\\__\\___|_|',
        '                                                         __/ |                     | |',
        '                                                        |___/                      |_|']



for i in range(len(font)):


    print(font[i])


print("AutomateMyComputer 1.0")
print("\n")
try:
    import os
    import time
    import winsound

    import webbrowser
    import pyautogui
    import subprocess
    import ctypes
except ImportError:

    print("Please make sure to have all the required packages installed. See https://github.com/William04A/AutomateMyComputer for more info.")


try:
    path = os.path.join("C:\\Users\\Albin\\Dropbox\\AutomateMyComputer")

    if os.path.exists(path) == True:
        with open(os.path.join(path + "\\latestaction.txt"), "w") as latestactionfile:

            latestactionfile.truncate()
    else:
        raise Exception

except:
    pathinput = input("Please specify the path of the Dropbox folder on your computer: ")
    path = os.path.join(pathinput)


while True:
    try:
        with open(os.path.join(path + "\\latestaction.txt"), "r+") as latestactionfile:
            filecontents = latestactionfile.read().split()

        try:
            if filecontents[len(filecontents)-2].replace("_", " ") == "Activated.":
                print("Action already activated.")
                time.sleep(3)
                continue

            elif filecontents[len(filecontents)-2].replace("_", " ") == "Not activated.":

                subject = filecontents[1].replace("_", " ")
                with open(os.path.join(path + "\\latestaction.txt"), "w") as latestactionfile:

                    latestactionfile.truncate()

        except Exception as e:

            if len(filecontents) == 0:
                print("Action already activated.")
                print("Time until next search (3 second delay): ")
                loadingtime = 3
                for i in range(3):
                    print(str(loadingtime) + " seconds left.")
                    time.sleep(1)
                    loadingtime -= 1
                print("\n")

                continue
            else:
                print("An unexpected error occured. (" + str(e) + ")")

        if "Mute speakers" in subject:
            pyautogui.press("volumemute")
            print("NOTIFICATION: Muting the speakers.")

        elif "Increase the volume by " in subject:
            volumeup = int(subject.replace("Increase the volume by ", ""))
            print("NOTIFICATION: Increasing the volume by: " + str(volumeup) + ".")
            for i in range(volumeup):
                pyautogui.press("volumeup")

        elif "Decrease the volume by " in subject:
            volumedown = int(subject.replace("Decrease the volume by ", ""))
            print("NOTIFICATION: Decreasing the volume by " + str(volumedown) + ".")
            for i in range(volumedown):
                pyautogui.press("volumedown")

        elif "Play sound" in subject:
            print("NOTIFICATION: Playing sound " + subject.replace("Play sound ", ""))
            winsound.PlaySound(os.path.join(os.getcwd() + "/sounds/" + subject.replace("Play sound ", "") + ".wav"), winsound.SND_FILENAME)


        elif "Google the search term " in subject:
            searchterm = subject.replace("Google the search term ", "").replace(" ", "+")
            print("NOTIFICATION: Searching Google for: " + str(searchterm) + ".")
            webbrowser.open("https://google.com/search?q=" + searchterm)

        elif "Turn off computer (command)" in subject:
            print("NOTIFICATION: Turning off computer...")

            subprocess.Popen("shutdown", shell=True)

        elif "Log out of computer (command)" in subject:
            print("NOTIFICATION: Logging out of user...")

            subprocess.Popen("shutdown -L", shell=True)
        elif "Start the application " in subject:
            applicationname = subject.replace("Start the application ", "")
            try:
                print("NOTIFICATION: Opening program \"" + applicationname + "\".")
                os.startfile(applicationname + ".exe")
                print("NOTIFICATION: The program \"" + applicationname + "\" has been opened successfully.")
            except FileNotFoundError:
                print("ALERT: The program \"" + applicationname + "\" was not found.")
        elif "Open the website " in subject:
            print("NOTIFICATION: Opening website in browser.")
            url = subject.replace("Open the website ", "")
            webbrowser.open(url)

        elif "Calculate " in subject:


            calculation = subject.replace("Calculate ", "")
            print("NOTIFICATION: Calculating " + calculation + ".")
            try:

                answer = eval(calculation)

                ctypes.windll.user32.MessageBoxW(None, "The answer for the calculation \"" + str(calculation) + "\". is " + str(answer) + " (via AutomateMyComputer).", "AutomateMyComputer", 0x40 | 0x0)
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(None, "An error occured while calculating \"" + str(calculation) + "\". Error: \"" + str(e) + "\".", "AutomateMyComputer", 0x10 | 0x0)
        elif "Display the message " in subject:
            message = subject.replace("Display the message ", "")
            ctypes.windll.user32.MessageBoxW(None, "Message from AutomateMyComputer: " + str(message), "AutomateMyComputer", 0x40 | 0x0)
        elif "Send an email to " in subject:
            emailadress = subject.replace("Send an email to ", "")

            link = "mailto://" + emailadress
            webbrowser.open(link)
        elif "Open Windows settings" in subject:
            webbrowser.open("ms-settings://")
        else:
            print("ALERT: The command \"" + subject + "\" is not a command detected by AutomateMyComputer.")
            print("This could potentially be something for you to worry about, if the command listed has something to do with AutomateMyComputer.")


        print("Time until next search (3 second delay): ")
        loadingtime = 3
        for i in range(3):

            print(str(loadingtime) + " seconds left.")
            time.sleep(1)
            loadingtime -= 1
        print("\n")
    except Exception as e:
        print("ALERT: An error occured. (" + str(e) + ").")
        ctypes.windll.user32.MessageBoxW(None, "An error occured while running AutomateMyComputer. " + "Error: \"" + str(e) + "\".", "AutomateMyComputer", 0x10 | 0x0)

