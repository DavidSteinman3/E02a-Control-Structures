
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  I would expect main01.py to greet the player and ask their favorite color.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    I ran the file and no response was given back to me, almost as if the game ended.
  - What do you think the program did with what you typed in answer to the question?
    I don't think it did anything because it was not programmed to give me a response

- Open main02.py. Before running it, describe how this is different than main01.py.
  There is one extra line of code with the print command.
  - What do you think the color = input() will do?
    I think the color input will read back our favorite color to the player
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    Yes, the program read my answer back to me, which is what I expected.

- Open main03.py. Before running it, describe how this is different than main02.py.
  Instead of asking the player their favorite color, it is a guessing game where you must guess the programs favorite color
  - What is happening on lines 9–12?
  It is code that determines the response based on the players answer, with red being the only correct answer
  - Why are lines 10 and 12 indented?
    Because lines 9-12 are dependednt on the question asked in line 8.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
    The answer is incorrect unless you capitalize the word 'red'
  - What does this tell you about "color"?
    The answer is less about color and more text based, case sensitive matters in this instance

- Open main04.py. Before running it, describe how this is different than main03.py.
  Correct answer options are both capitalized and lowercase for the letter 'red'
  - What problem is this trying to solve?
    Solving the issue of players who are unaware the answers are case sensitive
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    The answer is incorrect unless you use the same capitalization schemes that appear in main04.py

- Open main05.py. What do you expect line 9 to do?
    Make the color red the correct answer
  - What problem is it trying to solve?
    To reward people for being correct regardless of their capitalization.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    spaces make it so the answer is not correct even though capitalization no longer matters

 - Open main06.py. How is line 9 different than in main05.py?
  a .strip function has been added to the code
   - What would you guess .strip() is doing?
    fixing the problem of people adding spaces to their correct answers.
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
    adding spaces in between the three letters makes the answer incorrect

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
    Adding a feature of letting the player know if they are close to the right color
   - What is happening on line 12?
    hinting towards the player that they are close to guessing the right answer by adding the repsonse "close" for pink
   - Run the program and answer the question.

 - Open main08.py. What is the purpose of line 9?
   - Why are lines 10–17 indented?
    Because red has been established as the only correct answer, and lines 10-17 are functions revolving around red being the correct answer.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
    The answer "Close!" repeatedly spams the terminal and the program won't run properly.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)

 - Open main09.py. What is happening on line 13?
   - What is the purpose of “count”?
    The count feature counts how many times the player tried to answer the question
   - What is happening on line 22?
    The programs is able to let the player know how many attempts they used to answer the question.
   - Run the program.

 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
  lines 6-11 make it so the program's color choice is randomized after the last game played
