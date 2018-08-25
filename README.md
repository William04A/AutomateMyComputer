# AutomateMyComputer
A super simple way to automate actions on your computer via IFTTT or other services. Application written in Python.

## Intro & Info:
A few months ago I found AssistantComputerControl (https://github.com/AlbertMN/AssistantComputerControl) after trying several ways to automate my computer. I must credit the developer AlbertMN for doing such a wonderful application. However, I wanted something a little bit more open. AssistantComputerControl only supports voice assistants. AutomateMyComputer supports every application you can think of, if you make an integration for it. **AutomateMyComputer has support for all IFTTT apps** if you don´t want to code a custom integration. I also wanted my version to a be a little more well-documented.


## Demo and inspiration:
AutomateMyComputer runs as a background process in your computer. It requires almost no setup for the application itself. However, you need to have the following things installed:
**Required:**

- Python 3 with pip.
- A Dropbox account and the a cloud-connected Dropbox folder (https://www.dropbox.com/help/desktop-web/add-files under "Vista/Win7/Win8/Win10") enabled. This also required the Dropbox desktop application.
- A Windows computer.
- The following **external** Python repositories:
- PyAutoGui

## Preparations:
1. Download the Dropbox desktop client and create a Dropbox account. (https://www.dropbox.com/downloading).
2. Download Python from https://www.python.org.
3. Install the two applications mentioned above - **Make sure to install the Python command line tools as well (you will find an option to enable that in the Python setup**.
4. Create an IFTTT account if you don´t already have one.
5. Download this repository to your computer using the button "Download" or using git (requires extra installation).

## Setup:
Now, it is time to set up the application itself.
Start by using the Windows explorer to locate your Dropbox folder.
Right-click and choose New>Directory. Enter "AutomateMyComputer" **exactly as it is spelled** as the name.
Hold down the shift tangent the same time as you right-click your new folder. Now, select "Copy as path". That´s everything you need to do.

We are now going to use CMD, the Windows terminal to do a few things. Press the Windows key and the letter "S" on your keyboard at the same time to get to the Windows search interface. You can also tap the "Search" button on your taskbar. Search for "cmd" and click on the terminal window icon.

Once the window opens, type "pip install pyautogui" and wait for the installation to complete.
Next, close cmd and hit the Windows and "R" key at the same time. Type "shell:autostart" and press enter.
After that, right-click and choose New>Shortcut. Find the folder where AutomateMyComputer is. Press the file named "AutomateMyComputer x.x.py". Now, you are good to go and you can use AutomateMyComputer. To verify that everything is working correctly, you can try to run the AutomateMyComputer file. After a few seconds, you should see "Action already activated" being printed out in the window that just opened. AutomateMyComputer will continue to check after updates in the background and you can click the "Hide" button to minimize the application. Don´t close it!
**Please note: if AutomateMyComputer runs for a while and the closes or starts and then rapidly closes, something might be wrong. If so, please make sure that you´ve followed all the steps above or submit a new issue.**

## Connecting with IFTTT:
AutomateMyComputer works with IFTTT´s Dropbox integration as it is connected to the cloud-synced Dropbox folder on your computer. If you want to quickly get started, you can check out these pre-made IFTTT recipes for AutomateMyComputer:

https://ifttt.com/hello_world_63dc2ae5f3



**Writing will be continued later.**
