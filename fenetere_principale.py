from tkinter import Tk, Frame, Button, Label, PhotoImage

from Tic_Tac_Toc.Tic_Tac_Toc import game_tic_tac_toc
from shooter.main import game_shooter
from Machine_a_sous.machine_a_sous import game_machine_a_sous

# from Snake.snake import game_snake


def fenetre():
    def Machine_a_sous():
        # window.destroy()
        game_machine_a_sous()

    def snake():
        window.destroy()
        # game_snake()

    def tic_tac_toc():
        window.destroy()
        game_tic_tac_toc()

    def shooter():
        window.destroy()
        game_shooter()

    def ferme():
        window.destroy()

    window = Tk()
    window.title("OWR GAME")
    window.geometry("720x720")
    window.minsize(720, 700)
    window.iconbitmap("Ducoments_de_fenetere_principale/FYG.ico")
    window.config(background="#2C608C")
    photo = PhotoImage(
        file=r"Ducoments_de_fenetere_principale/tic_tac_toc.png"
    ).subsample(2, 3)
    photo_2 = PhotoImage(
        file=r"Ducoments_de_fenetere_principale/Machine_à_sous.png"
    ).subsample(2, 3)
    photo_3 = PhotoImage(
        file=r"Ducoments_de_fenetere_principale/snake_logo.png"
    ).subsample(2, 3)
    photo_4 = PhotoImage(
        file=r"Ducoments_de_fenetere_principale/shooter_logo.png"
    ).subsample(2, 3)
    photo_5 = PhotoImage(
        file=r"Ducoments_de_fenetere_principale/Quit_logo.png"
    ).subsample(2, 3)

    frame = Frame(window, bg="#2C608C", bd=45)

    label_title = Label(
        frame,
        text="Choose a Game",
        font=("Berlin Sans FB Demi", 40),
        bg="#2C608C",
        fg="black",
    )
    label_title.pack()

    tic_tac_toc_button = Button(
        frame,
        image=photo,
        bg="#2C608C",
        padx=800,
        pady=100,
        width=612,
        borderwidth=0,
        activebackground="#2C608C",
        command=tic_tac_toc,
    )
    tic_tac_toc_button.pack()
    snake_button = Button(
        frame,
        image=photo_2,
        bg="#2C608C",
        padx=80,
        pady=100,
        width=612,
        borderwidth=0,
        activebackground="#2C608C",
        command=snake,
    )
    snake_button.pack()
    shooter_button = Button(
        frame,
        image=photo_3,
        bg="#2C608C",
        padx=80,
        pady=100,
        width=612,
        borderwidth=0,
        activebackground="#2C608C",
        command=shooter,
    )
    shooter_button.pack()
    Machine_a_sous_button = Button(
        frame,
        image=photo_4,
        bg="#2C608C",
        padx=80,
        pady=100,
        width=612,
        borderwidth=0,
        activebackground="#2C608C",
        command=Machine_a_sous,
    )
    Machine_a_sous_button.pack()
    Quit = Button(
        frame,
        image=photo_5,
        bg="#2C608C",
        fg="#41B77F",
        padx=80,
        pady=100,
        width=612,
        command=ferme,
        borderwidth=0,
        activebackground="#2C608C",
    )
    Quit.pack()

    frame.pack()

    window.mainloop()


if __name__ == "__main__":
    fenetre()
