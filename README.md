# Breakdown

Breakdown is a classic shooter game where you're trying to shoot the falling objects
before they reach the bottom. Points are scored when you shoot an object, and points are
lost if the object reaches the bottom.

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 breakdown

```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.
```

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- breakdown           (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

# Rules

---

- Player can move left and right, and shoot the ball.
- Player moves left and right using the arrow keys.
- Player shoots the ball using the space bar.
- Player gains 100 points when an object is hit.
- Player loses 200 points when an object reaches the bottom.
- Player starts with 3 lives.
- Player loses a life if an object collides with the player.
- Game is over when player has no more lives.

## Required Technologies

---

- Python 3.8.0
- Raylib Python CFFI 3.7

## Authors

---

- Carina Aguero (agu21022@byui.edu)
- Rob Cox (cox21008@byui.edu)
- Brianna Dayley (col04002@byui.edu)
- Eduardo Pulido (pul21010@byui.edu)
