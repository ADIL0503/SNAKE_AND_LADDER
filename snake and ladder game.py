import tkinter as tk
import random as ra
p1=0
p2=0
turn=2
roll1=0
roll2=0
root=tk.Tk() 
root.title("SNAKE AND LADDER ")#GIVES NAME
root.configure(bg="tan")#CHANGE BACKGROUND COLOUR
ladders= {4: 14,9: 31,20: 38,28: 84,40: 59,51: 67,63: 81,71: 91}
snakes={17: 7,54: 34,62: 19,64: 60,87: 24,93: 73,95: 75,99: 78}
def grid(snakes,ladders):
    board=tk.Canvas(root,width=600,height=600,bg="gray")#SETUP CANVAS
    for i in range(1,11):
        board.create_line(0,60*i,600,60*i,width=2)#creates horizantal line
        board.create_line(60*i,0,60*i,600,width=2)#CREATES VERICAL LINES
    num=1
    for i in range(0,10):#TO SETUP NUMBERS IN MIDDLE OF CELL
        for j in range(0,10):
            y=600-(i*60+30)
            if(i%2==0):
                x=60*j+30
            else:
                x=600-(60*j+30)
            board.create_text(x,y,text=num)
            num+=1
    for i in snakes:#CHANGING COLOUR OF SNAKE CELL
        row=(i-1)//10
        column=(i-1)%10
        if(row%2==0):
            col=column
        else:
            col=9-column
        x1=col*60
        x2=x1+60
        y2=600-row*60
        y1=y2-60
        board.create_rectangle(x1,y1,x2,y2,fill="indianred1")
        board.create_text((x1+x2)//2,(y1+y2)//2,text=i)
    for i in ladders:#CHANGING COLOUR OF LADDER CELL
        row=(i-1)//10
        column=(i-1)%10
        if(row%2==0):
            col=column
        else:
            col=9-column
        x1=col*60
        x2=x1+60
        y2=600-row*60
        y1=y2-60
        board.create_rectangle(x1,y1,x2,y2,fill="lightgreen")
        board.create_text((x1+x2)//2,(y1+y2)//2,text=i)
    board.pack()
    return board
board=grid(snakes,ladders)#CALLING BOARD
def rules():
    rect1 = tk.Frame(root, width=100, height=50, bg="lightgreen", highlightbackground="black", highlightthickness=2)
    rect1.place(x=20, y=90)

    rect2 = tk.Frame(root, width=180, height=50, bg="violet", highlightbackground="black", highlightthickness=2)
    rect2.place(x=150, y=90)

    label2 = tk.Label(rect2, text="REPRESENTS LADDER", bg="violet",font=("arial",8,"bold"))
    label2.place(relx=0.5, rely=0.5, anchor="center")

    rect3=tk.Frame(root,width=100,height=50,bg="indianred1",highlightbackground="black",highlightthickness=2)
    rect3.place(x=20,y=150)

    rect4=tk.Frame(root,width=180,height=50,bg="violet",highlightbackground="black",highlightthickness=2)
    rect4.place(x=150,y=150)

    label4=tk.Label(rect4,text="REPRESENTS SNAKE",bg="violet",font=("arial",8,"bold"))
    label4.place(relx=0.5,rely=0.5,anchor="center")#TO PLACE TEXT AT CENTER

    rect5=tk.Frame(root,width=250,height=50,bg="violet",highlightbackground="black",highlightthickness=2)
    rect5.place(x=20,y=220)

    label5=tk.Label(rect5,text="FIRST PLAYER TO REACH 100 WINS",bg="violet",font=("arial",8,"bold"))
    label5.place(relx=0.5,rely=0.5,anchor="center")
rules()#GIVING INFORMATION
label=tk.Label(root,text="START",width=40,font=("arial",8,"bold"),bg="violet",highlightthickness=2,highlightbackground="black")
label.place(x=1000,y=100)
label1=tk.Label(root,text="",width=40,height=3,font=("arial",10,"bold"),bg="violet",highlightthickness=2,highlightbackground="black")
label1.place(x=1000,y=300)
label2=tk.Label(root,text="NUMBER OF ROLLS OF WINNER",width=30,height=3,font=("arial",10,"bold"),bg="violet",highlightthickness=2,highlightbackground="black")
label2.place(x=1000,y=500)
def clear():
    label1.config(text=f"")#CLEARS THE LABEL
def get_cords(position):
    row = (position-1)//10
    col = (position-1)%10
    if row % 2 == 0:   # left-to-right rows
        col = col
    else:              # right-to-left rows
        col = 9 - col
    x1 = col*60
    y1 = 600 - (row+1)*60
    x2 = x1 + 60
    y2 = y1 + 60
    return (x1, y1, x2, y2)
get_cords(p1)
def draw_players():
    # Clear old tokens
    board.delete("player")
    # P1 (yellow circle)
    if p1 > 0:
        x1,y1,x2,y2 = get_cords(p1)
        board.create_oval(x1+10,y1+10,x1+30,y1+30,fill="yellow",tags="player")
    # P2 (orange circle)
    if p2 > 0:
        x1,y1,x2,y2 = get_cords(p2)
        board.create_oval(x1+30,y1+30,x1+50,y1+50,fill="orange",tags="player")
def game():
    clear()
    global p1,p2,turn,roll1,roll2
    ladders= {4: 14,9: 31,20: 38,28: 84,40: 59,51: 67,63: 81,71: 91}
    snakes={17: 7,54: 34,62: 19,64: 60,87: 24,93: 73,95: 75,99: 78}
    if((turn%2)==0):
        a=ra.randint(1,6)
        if(p1+a <= 100):
            p1+=a
        if(p1 in snakes):
            s1=p1
            p1=snakes.get(p1)
            label1.config(text=f"OOPS! P1 STEPPED  SNAKE ({s1})-->{p1}")
        if(p1 in ladders):
            l1=p1
            p1=ladders.get(p1)
            label1.config(text=f"HURRAY P1 STEPPED LADDER ({l1})-->{p1}")
        label.config(text=f"P1 ROLLED {a},P1 IS AT {p1}")
        if(p1>=100):
            label2.config(text=f"P1 WINS IN {roll1} ROLLS")
            return
        draw_players()
        turn+=1
        roll1 +=1
    elif((turn%2)==1):
        b=ra.randint(1,6)
        if(p2+b <= 100):
            p2+=b
        if(p2 in snakes):
            s2=p2
            p2=snakes.get(p2)
            label1.config(text=f"OOPS! P2 STEPPED  SNAKE ({s2})-->{p2}")
        if(p2 in ladders):
            l2=p2
            p2=ladders.get(p2)
            label1.config(text=f"HURRAY P1 STEPPED LADDER ({l2})-->{p2}")
        label.config(text=f"P2 ROLLED {b},P2 IS AT {p2}")
        if(p2>=100):
            label2.config(text=f"P2 WINS IN {roll2} ROLLS")
            return
        draw_players()
        turn+=1
        roll2 +=1
game()
btn=tk.Button(root,text="ROLL",bg="violet",highlightbackground="black",highlightthickness=2,command=game,width=20,height=3)
btn.place(x=600,y=620)
labelp1=tk.Label(root,text="P1 is YELLOW",bg="violet",height=3,highlightbackground="black",highlightthickness=2)
labelp1.place(x=50,y=300)
labelp2=tk.Label(root,text="P2 is ORANGE",bg="violet",height=3,highlightbackground="black",highlightthickness=2)
labelp2.place(x=50,y=400)
draw_players()
root.mainloop()


