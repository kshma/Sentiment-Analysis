from textblob import TextBlob
from tkinter import *

def detect_sentiment():

    sentence = textArea.get("1.0", "end")
    pol=TextBlob(sentence).sentiment.polarity
    sub=TextBlob(sentence).sentiment.subjectivity

    if pol>0 and sub>0.3:
        answer="Positive"

    elif pol<0 and sub>0.3:
        answer="Negative"

    else:
        answer="Neutral"

    overallField.insert(10, answer)

if __name__ == "__main__" :

    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background = "light green")

    # set the name of tkinter GUI window
    gui.title("Sentiment Detector")

    # Set the configuration of GUI window
    gui.geometry("250x400")

    # create a label : Enter Your Task
    enterText = Label(gui, text = "Enter Your Sentence", bg = "light green")

    # create a text area for the root
    # with lunida 13 font
    # text area is for writing the content
    textArea = Text(gui, height = 5, width = 25, font = "lucida 13")

    # create a Submit Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed
    check = Button(gui, text = "Check Sentiment", fg = "Black", bg = "Red", command = detect_sentiment)

    # Create a overall : label
    overall = Label(gui, text = "Sentence Overall Rated As: ", bg = "light green")

    # create a text entry box
    overallField = Entry(gui)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    enterText.grid(row = 0, column = 2)

    textArea.grid(row = 1, column = 2, padx = 10, sticky = W)

    check.grid(row = 2, column = 2)

    overall.grid(row = 9, column = 2)

    overallField.grid(row = 10, column = 2)

    gui.mainloop()
