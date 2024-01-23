# Duck timer!
## Some of the features you might like
- You can put any song you like inside the sound/music folder and it will be randomly selected, also the ducks move at the speed of the song's BPM (sort of since it is using a library to aproximate it)

- You can also implement your own ducks with the create_from_gif.py file inside the assets folder since it strips any .gif file into a framesheet and creates a .json file into the ducks folder, you should change the options in the .json file so it suits better your duck needs. The file uses an input and an optional output file name argument.
  
- Note that the way you declare new ducks is by placing a new file in the ducks folder, please use the .json format so you don't have problems.
  
```python
#From the main directory
python ./assets/create_from_gif.py -i duck.gif -o my_duck
#This will output my_duck.png file in the assets/sprites directory and my_duck.json into the ducks folder
```

# How to start the duck timer
- If you want to start the program, you first need to install the dependencies in the requierements.txt file, preferably use a virtual enviroment. Then you will have to run the main.py file parsing the arguments as an specific hour and optionally minutes and even seconds.
```python
pip install -r requirements.txt
#From the main directory
python main.py 14 -m 15
#This will set up a counter from the time it is started to the time of the day you want the timer to count
```

## Have some ideas? Please let me know!

## Disclaimer

Please note that I do not own any of the assets used in this project, including images and music. These assets are the property of their respective owners and are used for educational purposes only. If you are the owner of any of these assets and would like them to be removed, please contact me.