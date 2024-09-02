import pgzrun
TITLE = "The anime quiz"
HEIGHT = 600
WIDTH = 600
marqueebox = Rect(0,0,600,100)
questionbox = Rect(0,0,600,100)
timerbox = Rect(0,0,100,100)
optionbox1 = Rect(0,0,180,100)
optionbox2 = Rect(0,0,180,100)
optionbox3 = Rect(0,0,180,100)
optionbox4 = Rect(0,0,180,100)
skipbox = Rect(0,0,100,200)
#variables
colorchange = False
score = 0
timeleft = 10
marqueemessage = ""
gameover1 = False
opeen = open("questions.txt", "r")
f1 = opeen.read()
questions = []
options = [optionbox1,optionbox2,optionbox3,optionbox4]
questioncount = 0
indexquestion = 0
marqueebox.move_ip(0,0)
questionbox.move_ip(0,100)
timerbox.move_ip(450,220)
optionbox1.move_ip(20,220)
optionbox2.move_ip(220,220)
optionbox3.move_ip(20,340)
optionbox4.move_ip(220,340)
skipbox.move_ip(450,350)
def draw():
    global marqueemessage
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(questionbox,"green")
    screen.draw.filled_rect(timerbox,"orange")
    screen.draw.filled_rect(skipbox,"grey")
    for answer in options:
        screen.draw.filled_rect(answer,"pink")
    marqueemessage = "Welcome to the anime quiz!"
    marqueemessage = marqueemessage + f"Q:{indexquestion} of {questioncount}"
    screen.draw.textbox(marqueemessage,marqueebox,color = "White")
    screen.draw.textbox("skip",skipbox,color = "White",angle = -90)
    screen.draw.textbox(question[0].strip(), questionbox, color = "red")
    index = 1
    for answer in options:
        screen.draw.textbox(question[index].strip(),answer, color = "black")      
        index = index+1                
    if colorchange == False:
        screen.draw.textbox(str(timeleft),timerbox,color = "green")
    if colorchange == True:
        screen.draw.textbox(str(timeleft),timerbox,color = "red")
def endtime():
    global timeleft,colorchange
    if timeleft > 0:
        timeleft-=1
        if timeleft <= 3:
            colorchange = True
    else:
        gameover()    
           
def movingtext():
    marqueebox.x = marqueebox.x-2
    if marqueebox.right <0:
        marqueebox.left = WIDTH
def update():
    movingtext()
clock.schedule_interval(endtime,1)
def reading():
    global questions, questioncount
    openn = open("questions.txt", "r")
    for question in openn:
        questions.append(question)
        questioncount = questioncount+1
    openn.close()
def read2():
    global indexquestion
    indexquestion = indexquestion+1
    return questions.pop(0).split(",")
def correct():
    global score, question, timeleft, questions
    score = score+1
    if questions:
        question = read2()
        timeleft = 10
        colorchange = False
    else:
        gameover()
def gameover():
    global question, timeleft, gameover1
    message = f"Game over!\nYou got {score} questions correct!"
    question = [message, "-","-","-","-",5]
    timeleft = 0
    gameover1 = True
def skip():
    global question, timeleft
    if questions and not gameover1:
        question = read2()
        timeleft = 10
        colorchange = False
    else:
        gameover()
def on_mouse_down(pos):
    index = 1
    for answer in options:
        if answer.collidepoint(pos):
            if index is int(question[5]):
                correct()
            else:
                gameover()
        index = index+1
    if skipbox.collidepoint(pos):
        skip()
reading()
question = read2()
pgzrun.go()