# Some features
- You can put any song you like inside the sound/music folder and it will be randomly selected, also the ducks move at the speed of the song's BPM (sort of since it is using a library to aproximate it)
- You can add also extra ducks by declaring them into an array (Probably will add an external file to easyly include ducks at anytime with any sprite you like without touching any code, see the duck class to have a better idea on the options you have)
- You can also implement your own ducks with the divide_gif.py file inside the assets folder since it strips any .gif file into a framesheet, it uses an input and an optional output argument (you will need to specify the output directory).
```python
python divide_gif.py -i duck.gif -o assets
#This will output duck-frames.png file in the assets directory
```
- If you want to start the program, you first need to install the dependencies in the requierements.txt file, preferably use a virtual enviroment. Then you will have to run the main.py file parsing the arguments as an specific hour and optionally minutes and even seconds.
```python
pip install -r requirements.txt
#From the main directory
python main.py 14 -m 15
#This will set up a counter from the time it is started to the time of the day you want the timer to count
```
