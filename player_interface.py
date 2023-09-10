from tkinter import *
from tkinter import messagebox


class PlayerInterface:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Aera")
        self.main_window.geometry("860x680")
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "#ccc"

        # criando os frames
        self.gray_frame = Frame(self.main_window, padx=0, pady=0, bg="#ccc")
        self.gray_frame.grid(row=0, column=0)
        self.main_frame = Frame(self.main_window, padx=100, pady=20, bg="#ccc")
        self.main_frame.grid(row=0, column=1)
        self.pink_frame = Frame(self.main_window, padx=0, pady=0, bg="#ccc")
        self.pink_frame.grid(row=0, column=2)

        self.empty = PhotoImage(file="empty.png")

        self.gray_pieces = [
            PhotoImage(file="gray_pieces/gray_1.png"),
            PhotoImage(file="gray_pieces/gray_2.png"),
            PhotoImage(file="gray_pieces/gray_3.png"),
            PhotoImage(file="gray_pieces/gray_4.png"),
            PhotoImage(file="gray_pieces/gray_5.png"),
            PhotoImage(file="gray_pieces/gray_6.png")
        ]

        self.pink_pieces = [
            PhotoImage(file="pink_pieces/pink_1.png"),
            PhotoImage(file="pink_pieces/pink_2.png"),
            PhotoImage(file="pink_pieces/pink_3.png"),
            PhotoImage(file="pink_pieces/pink_4.png"),
            PhotoImage(file="pink_pieces/pink_5.png"),
            PhotoImage(file="pink_pieces/pink_6.png")
        ]

        # criando a matriz de peças cinzas
        self.gray_view = []
        for y in range(6):
            gray_label = Label(self.gray_frame, bd=0,
                               image=self.gray_pieces[y])
            gray_label.grid(column=0, padx=2, pady=2)
            gray_label.bind("<Button-1>", lambda event, color='cinza',
                            number=y+1: self.select_piece(color, number))
            self.gray_view.append(gray_label)

        # criando a matriz de peças rosas
        self.pink_view = []
        for y in range(6):
            pink_label = Label(self.pink_frame, bd=0,
                               image=self.pink_pieces[y])
            pink_label.grid(column=2, padx=2, pady=2)
            pink_label.bind("<Button-1>", lambda event, color='rosa',
                            number=y+1: self.select_piece(color, number))
            self.pink_view.append(pink_label)

        # criando a matriz do tabuleiro
        self.board_view = []
        for y in range(4):
            view_tier = []
            for x in range(4):
                a_label = Label(self.main_frame, bd=2,
                                relief="solid", image=self.empty)
                a_label.grid(row=x, column=y, padx=2, pady=2)
                a_label.bind("<Button-1>", lambda event, line=y+1,
                             column=x+1: self.click(event, line-1, column-1))
                view_tier.append(a_label)

            self.board_view.append(view_tier)

        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar
        # Adicionar menu(s) à barra de menu:
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='Arquivo')
        # Adicionar itens de menu a cada menu adicionado à barra de menu:
        self.menu_file.add_command(
            label='Iniciar jogo', command=self.start_match)
        self.menu_file.add_command(
            label='Restaurar estado inicial', command=self.start_game)

        self.main_window.mainloop()

    def start_match(self):
        messagebox.showinfo(title='Início', message='O jogo foi iniciado!')

    def start_game(self):
        print('start_game')

    def click(self, event, line, column):
        label = self.board_view[line-1][line-1]
        messagebox.showinfo(title='Casa selecionada!',
                            message='Casa {} {} selecionada'.format(column, line))

    def select_piece(self, color, number):
        messagebox.showinfo(
            'Peça selecionada', message='Jogador {} selecionou a peça {}'.format(color, number))


PlayerInterface()
