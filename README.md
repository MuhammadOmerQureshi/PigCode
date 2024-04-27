# PigCode

# Pig Game - Examination 2

# Guide to help new user execute the application OR for a developer to work on as project.

This is a Python implementation of the classic dice game Pig. The game is designed to be played in the terminal and offers a simple yet entertaining experience.

## Table of Contents
- [Introduction](#introduction)
- [Technical Requirements](#technical-requirements)
- [Installation](#installation)
- [Usage & Game Rules](#usage)
- [How to generate Documentation from docsstrings and UML diagrams](#documentation)
- [Syntax and Conventions.](#flake8)(#lint)
- [Running tests and generating the Test coverage report](#tests-and-coverage)

## Introduction
Pig Game is a text-based game where players take turns rolling a die to accumulate points. The objective is to reach a score of 100 before your opponent. The game can be played against the computer or with two players.
This guide is to help with the setup proces for being able to run the game and also provide some guidance about the rules of game & some funcionalities.

## Technical requirements
- A package manager (brew for Chocolatey for Windows)
- How to install Chocolatey for Windows: https://docs.chocolatey.org/en-us/choco/setup
- A computer with a Python installed version 3.
- To check if you have Python installed, open the terminal and execute the command 
```bash
python --version

```
- To install the latest version of Python with a package manager (Chocolatey) use 
```bash
choco install python #for Windows
```
- Git Bash, information found here: https://git-scm.com/downloads
- To install Make tool: 
```bash
choco install make #for Windows
```
- Graphviz package is needed to generate UML diagrams from our code. Install with: 
```bash
choco install graphviz #for Windows
```
## Installation
To run the Pig Game, follow these steps:

### Step 1:
Clone the repository to your computer using the terminal provided by Git Bash: 
```bash
git clone https://github.com/MuhammadOmerQureshi/PigCode.git
```
The repository and the .zip file include the source code that contains the Python files for executing the game and also other files for testing and executing other functionalities.

### Step 2: 
Navigate to the project directory.
At the root folder `PigCode` open a new terminal.

### Step 3:
Create and activate a virtual environment by running the comands:
```bash
make venv
. .venv/Scripts/activate #for Windows
```
The command line will start with a `(.venv)` after activation.

### Step 4:
Install dependencies specified in the requirements.txt file by running the comand:
```bash
make install
```
To exit the virtual enviroment, run: 
```bash
deactivate
```
## Usage & Game Rules
To play the Pig Game, execute the following command in the terminal:

The class `game.py` is the entrypoint for our game.
You will first be promped to introduce player name in the terminal and press Enter.

Next you will be asked if you want to play against the computer or against another player.
If you choose to play against the computer it will ask you for the difficulty level which is from 1-30 (1 : Very Easy, 30 Max Difficulty).
After that the turns will start. On each turn each player will have 4 options: roll, hold, cheat or quit.
If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
A cheat option has also been introduced to give 20 extra point.
Every turn shows the dice number and also total score in that turn, accumalting the score in each turn, showing final score for each particular iteration.
The first player that reaches 100 or more wins the game, and its name and punctuation gets saved in the .json file called `highscores.json`
You can read more about the game and other variants at https://en.wikipedia.org/wiki/Pig_(dice_game)

## How to generate Documentation from docsstrings and UML diagrams.

This needs to be executed in the command 
```bash
make install
```
in our virtual environment and installed the Python modules from `requirements.txt`.

In order to generate the documentation, You need to execute in the terminal the command:
```bash
make doc
```
This command will create a `.html` file in the `doc/api` folder for each Python class in `src/`.

You can also generate UML diagrams from our classes in `src/` by running the command: 
```bash
make uml
```
After running, two new `.png` files called `classes.png` and `packages.png` will be created.

There will also be created 2 files called classes.dot and packages.dot which are used from the tool `graphviz` to generate the `.png` files

## Syntax and Conventions.

Linters are tools that help identify inconsistencies in code by applying specific rules. These rules are incorporated into `.flake8` and `.pylint` files. To obtain a list of all syntax issues in the code that correspond to these rules, execute the following command:
```bash
make flake8
```
OR

```bash
make lint
```

## Running tests and generating the Test coverage report
This functionality requires to have executed the command 
```bash
make install
```
in your virtual environment and installed the Python modules from `requirements.txt`.

You can execute in the terminal the command: 
```bash
make test
```
The results of the test coverage will get displayed on the terminal if all the tests execute successfully.
A new folder called `htmlcov` will get created at the root of the project. It will include an `index.html` file, which You can open with our browser and see the coverage percentages per class and the total average.

