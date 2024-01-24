# Duck timer!
## Some of the features you might like
- You can put any song you like inside the assets/sound/music folder and it will be randomly selected, also the ducks move at the speed of the song's BPM (sort of since it is using a library to aproximate it)

- You can also implement your own ducks with the create_from_gif.py file inside the src folder since it strips any .gif file into a framesheet and creates a .json file into the ducks folder, you should change the options in the .json file so it suits better your duck needs. The file uses an input and an optional output file name argument.
  
- Note that the way you declare new ducks is by placing a new file in the ducks folder, please use the .json format so you don't have problems.
  
```bash
#From the main directory
python ./assets/create_from_gif.py -i duck.gif -o my_duck
#This will output my_duck.png file in the assets/sprites directory and my_duck.json into the ducks folder
```

# How to start the duck timer
- If you want to start the program, you first need to install the dependencies in the requierements.txt file, preferably use a virtual enviroment. Then you will have to run the main.py file parsing the arguments as an specific hour and optionally minutes and even seconds.
```bash
pip install -r requirements.txt
#From the main directory
python main.py 14 -m 15
#This will set up a counter from the time it is started to the time of the day you want the timer to count
```
# You want to build it so you can run it at any time? Use pyinstaller!

To bundle the application with its assets and ducks 🦆, use the following command:

```bash
pyinstaller --name dtimer main.py --add-data './assets/:assets/' --add-data './ducks/:ducks/'
```
This command tells PyInstaller to bundle the main.py script into an executable and to include the assets and the ducks in the bundled application.

### Windows
If you're using Windows, you might want to add the directory containing the bundled application to your PATH environment variable, or move the bundled application to a directory that's already in your PATH. Here's how you can add a directory to your PATH:

```cmd
Replace /path/to/dtimer with the actual path to the dtimer directory
set PATH=/path/to/dtimer;%PATH%
```

### Linux

*TODO, haven't tryed yet to run this in linux, most likelly scenario is that it works*

### Have some ideas? Please let me know!
klatort@gmail.com
## Disclaimer

Please note that I do not own any of the assets used in this project, including images and music. These assets are the property of their respective owners and are used for educational purposes only. If you are the owner of any of these assets and would like them to be removed, please contact me.
