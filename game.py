import tkinter as tk
import random

choices = ["Rock","Paper","Scissors"]


def play(user):

    computer = random.choice(choices)

    result.config(
        text=
        f"You: {user}\nComputer: {computer}"
    )

    if user == computer:
        winner.config(text="Tie")

    elif (
(user=="Rock" and computer=="Scissors")
or
(user=="Paper" and computer=="Rock")
or
(user=="Scissors" and computer=="Paper")
):
        winner.config(
            text="You Win 🎉"
        )

    else:
        winner.config(
            text="Computer Wins 😔"
        )


root = tk.Tk()

root.title(
"Rock Paper Scissors"
)

root.geometry("450x400")

root.config(bg="#222")

tk.Label(
root,
text="ROCK PAPER SCISSORS",
font=("Arial",18,"bold"),
bg="#222",
fg="white"
).pack(pady=20)


for item in choices:

    tk.Button(
root,
text=item,
width=15,
height=2,
font=("Arial",12),
command=lambda x=item:
play(x)
).pack(pady=10)


result = tk.Label(
root,
text="",
font=("Arial",14),
bg="#222",
fg="yellow"
)

result.pack()

winner = tk.Label(
root,
text="",
font=("Arial",18),
bg="#222",
fg="lightgreen"
)

winner.pack()

root.mainloop()
