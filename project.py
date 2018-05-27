from tkinter import * # imports the entire tkinter module to allow me to create the interface
import tkinter.messagebox # imports message box to allow me to display errors or messages
import pickle # imports pickle to allow me to store the highscores
import operator # imports operator to allow me to sort the highscores file
import pygame # imports pygame to allow me to play the words
import time # imports time to allow me to cause the program to sleep to enable me to play the words
root=Tk() # gives the tkinter module the variable name root
root.geometry("550x500") # creates the tkinter window 550 by 500 pixels
root.configure(bg="#3366ff") # sets the background colour of the window to blue
root.title("Spelling Game") # sets the title of the program to Spelling Game
import random # imports random to enable me to choice 5 words from the word list at random
word_file=open('words.txt','r') # opens the file containing the list of words giving it the variable name word_file
lines=word_file.read().split('\n') # reads the words file into a list called lines splitting items by each line

number_of_words=5 # sets the number of words to be used in the game
word_list=[] # creates an empty list called word_list, this list will stores the words used by the game
sound_list=[] # creates am empty list called sound_list, this list will store the file names of the sounds to be played
for i in range(number_of_words): # creates a loop which will iterate as many times as the variable number_of_words
    word=random.choice(lines) # chooses a word at random from the word list
    lines.remove(word) # removes the word from the word list so it won't be chosen again
    word_list.append(word) # adds the word to the word_list
    sound_list.append(word+".wav") # adds the word with .wav on the end to enable the sound file to be opened

current_question=1 # sets the question that the user is currently on to 1

score=0 # sets the score to 0
user="" # creates the variable, user
sec=0 # sets the amount of seconds the user has took to 0
switch=False # sets the variable switch to false to prevent the timer from starting

def load_scores(): # creates a function to load the top 10 highscores
    highscores=[] # creates an empty list called highscores
    file=open('highscores.txt', 'rb') # opens the file which stores highscores in read binary mode
    highscores=pickle.load(file) # loads the highscores file using pickle into the list called highscores
    sorted_scores=sorted(highscores, key=operator.itemgetter(1), reverse=True) # sorts the highscores by their score instead of their name in reverse order meaning the highest score will be at the top

    highscores_list=("Username  Score"+
                     "\n"+"\t".join(map(str,sorted_scores[0]))+
                     "\n"+"\t".join(map(str,sorted_scores[1]))+
                     "\n"+"\t".join(map(str,sorted_scores[2]))+
                     "\n"+"\t".join(map(str,sorted_scores[3]))+
                     "\n"+"\t".join(map(str,sorted_scores[4]))+
                     "\n"+"\t".join(map(str,sorted_scores[5]))+
                     "\n"+"\t".join(map(str,sorted_scores[6]))+
                     "\n"+"\t".join(map(str,sorted_scores[7]))+
                     "\n"+"\t".join(map(str,sorted_scores[8]))+
                     "\n"+"\t".join(map(str,sorted_scores[9]))) # creates the text to show highscores by getting the top 10 scores the creates a string by combining the username and the score with a tab inbetween
    highscores_label.configure(text=highscores_list) # displays the highscores text within the highscores label

def highscores(): # creates a function to navigate to the highscores menu
    load_scores() # calls the load_scores function ensure the highscores are updated and ready to be displayed
    highscores_label.place(x=50, y=140) # places the label containing the highscores on screen
    title_label.configure(text="Highscores") # changes the text of the title label from Spelling Game to Highscores
    menu_button.place(x=2, y=450) # places the menu button in the bottom left corner to enable the user to navigate back to the menu screen
    username_label.place_forget() # hides the username label as it isn't required on the highscores screen
    username_entry.place_forget() # hides the username entry as it isn't required on the highscores screen
    register_button.place_forget() # hides the register button as it isn't required on the highscores screen
    login_button.place_forget() # hides the log in button as it isn't required on the highscores screen
    highscores_button.place_forget() # hides the highscores button as it isn't required on the highscores screen

def menu(): # creates a function to navigate to the menu screen
    title_label.place(x=50, y=50) # places the label containing the title on the screen
    title_label.configure(text="Spelling Game") # changes the text of the title label to Spelling Game
    username_label.place(x=35, y=150) # places the label which informs the user to enter their username
    username_entry.place(x=50, y=210) # places the entry box which enables the user to enter or register their username
    register_button.place(x=50, y=280) # places the button which enables the user to register their username
    login_button.place(x=280, y=280) # places the button which enables the user to log in using their username
    highscores_button.place(x=51, y=350) # places the button which enables the user to navigate to the highscores screen
    highscores_label.place_forget() # hides the label which displays the highscore as it isn't required on the menu screen
    menu_button.place_forget() # hides the button which allows you navigates to the menu screen as it isn't requierd on the menu screen
   
def register_username(): # creates the function which allows the user to register a new user
    username_file=open('usernames.txt', 'r') # opens the file containing usernames in read mode
    username_to_register=username_entry.get() # gets the contents of the username entry box
    if username_to_register=="": # checks if the user hasn't entered a username
        tkinter.messagebox.showinfo("Enter a username", "You must enter a username!") # displays a message box informing the user that they need to enter a username
    elif username_to_register in username_file.read(): # checks if the username entered in the entry box is already in the usernames file
        tkinter.messagebox.showinfo("Username taken", "The username you have entered has already been taken!") # displays a message box informing the user that the username they entered is already taken
    else: # if none of the other possibilities are true
        username_file.close() # closes the username file
        username_file=open('usernames.txt', 'a') # reopens the username file but in append mode
        username_file.write(username_to_register+"\n") # writes the username entered into the username file followed by a new line
        username_file.close() # closes the username file
        tkinter.messagebox.showinfo("Username saved", "Your username has been saved!") # displays a message box informing the user that their username has been saved

def log_in(): # creates the function which allows the user to log in using their username
    username_file=open('usernames.txt', 'r') # opens the usernames file in read mode
    username_to_login=username_entry.get() # gets the contents of the username entry
    if username_to_login=="": # if the user didn't enter a username
        tkinter.messagebox.showinfo("Enter a username", "You must enter a username!") # displays a message box informing the user to enter a username
    elif username_to_login not in username_file.read(): # if the username enter isn't in the usernames file
        tkinter.messagebox.showinfo("Username invalid", "Please enter a valid username!") # displays a message box informing the user that the username they entered doesn't exist
    else: # if none of the other possibilities are true meaning the username isn't taken
        tkinter.messagebox.showinfo("Log in successful", "You have successfully been logged in!\nThe game will now begin.") # displays a message box informing the user that they have been logged in
        global user # accesses the global variable user
        user=username_to_login # sets the global variable user to the username which was entered
        load_question() # calls the load_question function to start the game

def timer(): # creates the function which creates a timer to show how long the user has taken to complete the game
    if switch==True: # if the variable switch is set to true
        global sec # accesses the global variable, sec
        sec+=1 # adds 1 to the variable sec
        timer_label.configure(text=sec) # sets the contents of the label showing the timer to the variable sec
    root.after(1000, timer) # waits 1000ms/1s then calls the function timer again

def start_timer(): # creates the function to initiate the timer
    global switch # accesses the global variable switch
    switch=True # sets switch to true meaning the timer is started

def stop_timer(): # creates the fucntion to stop the timer
    global switch # accesses the global variable switch
    switch=False # sets swtich to false meaning the timer is stopped

def load_question(): # creates the function to load the questions
    global current_question # acceses the global variable current question
    if current_question==1: # if the global variable current question is 1
        title_label.place_forget() # hides the title tabel as it isn't require within the game
        username_label.place_forget() # hides the username label as it isn't required within the game
        username_entry.place_forget() # hides the username entry as it isn't required within the game
        register_button.place_forget() # hides the register button as it isn't required within the game
        login_button.place_forget() # hides the log in button as it isn't required within the game
        highscores_button.place_forget() # hides the highscores button as it isn't required within the game
        
        word_button.place(x=100, y=100) # places the button which plays each word on the screen
        word_entry.place(x=100, y=200) # places the entry box which enables the user to enter the word on screen
        confirm_button.place(x=100, y=350) # places the button to enable the user confirm their answer on screen
        timer_label.place(x=10, y=450) # places the label which contains the timer on screen
        start_timer() # calls the start_timer function to start the timer
    else: # if the current_question isn't 1
        word_entry.delete(0, END) # deletes the contents of the word entry box ready for the next question

def end_screen(): # creates the function which displays the end screen
    stop_timer() # calls the stop_timer function to stop the timer
    word_button.place_forget() # hides the button which plays each word as it isn't required on the end screen
    timer_label.place_forget() # hides the label which stores the timer as it isn't required on the end screen
    word_entry.place_forget() # hides the entry where the user enters their answer as it isn't required on the end screen
    confirm_button.place_forget() # hides the button where the user confirms their answer as it isn't required on the end screen
    score_text=str(score) # creates a string of the score the user got
    score_label.configure(text=str("Your final score is "+score_text)) # sets the contents of the score label to "Your final score is" followed by their score
    score_label.place(x=100, y=250) # places the scores label as it is required on the end screen
    quit_button.place(x=100, y=400) # places the quit button to enable the user to quit the program
    write_score() # calls the write_score function to write the score the user got to the highscores file

def play_word(): # creates a function to play the words
    pygame.init() # initiates pygame
    global sound_list # accesses the global list sound_list
    global current_question # accesses the global variable current_question
    sound=pygame.mixer.Sound(sound_list[current_question-1]) # loads the correct word file by getting the file name from the sound list depending on the current question
    create_display=pygame.display.set_mode((1, 1)) # creates the pygame display but only 1 by 1 so it isn't visible
    sound.play() # plays the sound file
    time.sleep(2) # causes the program to pause for 2 seconds to enable the word to be played
    sound.stop() # stops the sound file
    pygame.display.quit() # quits the pygame display
  

def confirm_answer(): # checks if what the user answered is correct
    global current_question # accesses the global variable current_question
    global word_list # accesses the global variable word_list
    answer=word_entry.get() # gets the text from the entry box
    if answer==word_list[current_question-1]: # checks if the answer entered is correct
        global score # accesses the global variable score
        score+=50 # adds 50 to the current score
    if current_question==5: # checks if the current question is 5
        global sec # accesses the global variable sec
        score-=sec # subtracts the amount of time taken in seconds from the total score
        end_screen() # calls the end_screen function to go to the end screen
    else: # if the current question is not 5
        current_question+=1 # adds 1 to the variable current question
        load_question() # calls the load_question function to go to the next question


def write_score(): # appends the score to the highscores file
    scores=[] # creates a blank list called scores
    scores_file=open('highscores.txt', 'rb') # opens the highscores file in read binary mode
    scores=pickle.load(scores_file) # loads the highscores file in to the scores list
    scores_file.close() # closes the scores file
    userandscore=(user,score) # combines the user's username with their score
    scores.append(userandscore) # appends the user's username and score to the scores list
    scores_file=open('highscores.txt','wb') # opens the highscores file in write binary mode
    pickle.dump(scores, scores_file) # writes the scores list to the highscores file
    scores_file.close() # closes the highscores file
    tkinter.messagebox.showinfo("Score saved", "Your score has been saved!") # displays a message box to inform the user that their score has been saved
    
def quit(): # closes the window
    root.destroy()

# creates all the widgets required for the menu
title_label=Label(root, font="Arial 52", fg="#ffffff", bg="#3366ff", text="Spelling Game")

username_label=Label(root, font="Arial 22", fg="#ffffff", bg="#3366ff", text="Enter Username to Register or Log in")

username_entry=Entry(root, font="Arial 24", width=25)

register_button=Button(root, font="Arial 18", width=15, fg="#ffffff", bg="#3366ff", text="Register", command=register_username)

login_button=Button(root, font="Arial 18", width=15, fg="#ffffff", bg="#3366ff", text="Log in", command=log_in)


# creates all the widgets required for the highscores screen
highscores_button=Button(root, font="Arial 18", width=31, fg="#ffffff", bg="#3366ff", text="Highscores", command=highscores)

menu_button=Button(root, font="Arial 18", fg="#ffffff", bg="#3366ff", text="Back", command=menu)

highscores_label=Label(root, font="Arial 18", fg="#ffffff", bg="#3366ff")


# creates all the widgets required for the actual game
word_button=Button(root, font="Arial 28", fg="#ffffff", bg="#3366ff", text="Play word", command=play_word)

word_entry=Entry(root, font="Arial 24")

confirm_button=Button(root, text="Confirm", font="Arial 24", command=confirm_answer)

timer_label=Label(root, font="Arial 24", fg="#ffffff", bg="#3366ff")


# creates all the widgets required for the end screen
score_label=Label(root, font="Arial 28", fg="#ffffff", bg="#3366ff")

quit_button=Button(root, text="Quit", font="Arial 24", fg="#ffffff", bg="#3366ff", command=quit)


menu() # calls the menu function to make the menu appear as soon as the program is run
timer() # starts the timer ready for the game
