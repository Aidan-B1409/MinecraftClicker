# MinecraftClicker
An auto-clicking script using PyAutoGUI
For automating mining on a Minecraft Skyblock server. 
Automatically rotates between pickaxes in the Minecraft toolbar

# To Use
1) Download the release, or clone the source code and download the required packages by running `pip install -r requirements.txt`
  Note: To run the source code natively, you will need to download Python 3.8 or newer. 
2) Ensure your hotbar (slots 1-9) are filled with stone pickaxes. The script is configured to hold down the left mouse button for 190 seconds, which is the theoretical mine time for a stone pickaxe. 
4) Approach a source of cobblestone
5) Execute script.exe
6) A 10 second timer will begin. Tab back to your game during this time period
7) The script will run until all pickaxes are disposed of, or until the user terminates the program. 
NOTE: The program can be terminateed by swiftly moving the cursor to any of the 4 corners of the screen, or by pressing CTRL+C in terminal. 

Program is compiled to run in Windows, but can be built on Linux or MacOS. A package requirements file is included for those who would like to compile the script themselves. 
