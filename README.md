# Timer
### a MGTC28 Python example
This is a timer program written in Python  

![times-up!](https://media.makeameme.org/created/times-up-5923e0.jpg)\
timer.py is a simple Python script allowing users to set timer duration.
Upon timer expiry, the user will see the time-up meme.
timer.py uses the **time library** to help keep track of time and the **pillow library** to facilitate the meme display.

Please see the documentation for the library used:
- [time](https://docs.python.org/3/library/time.html)
- [pillow](https://pypi.org/project/Pillow/)


### Add on by student
The timer program was changed to create a nerves of steel program, used to play the nerves of steel game.\
To play the game: 
1. The program displays "Players stand"
2. The program sleeps for a random time between 5 to 25 seconds.  While the program is sleeping, players can sit down.  Keep track of the last person to sit down.
3. When sleep is over, the program displays "Time Up.  Last to sit down wins."  Players still standing are eliminated, and the winner is the last person to sit down.
