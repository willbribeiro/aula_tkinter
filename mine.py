import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0] * cols for _ in range(rows)]
        self.revealed = [[False] * cols for _ in range(rows)]
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.buttons = [[tk.Button(self.master, width=2, height=1, command=lambda r=r, c=c: self.click(r, c)) 
                         for c in range(self.cols)] for r in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].grid(row=r, column=c)

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and self.board[r + dr][c + dc] == -1:
                                count += 1
                    self.board[r][c] = count

    def click(self, r, c):
        if not self.revealed[r][c]:
            self.reveal(r, c)
            if self.board[r][c] == -1:
                self.reveal_all()
                print("Game Over")
            elif self.board[r][c] == 0:
                self.expand_zeros(r, c)
            self.check_win()

    def reveal(self, r, c):
        self.revealed[r][c] = True
        self.buttons[r][c].config(text=str(self.board[r][c]))

    def reveal_all(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.reveal(r, c)

    def expand_zeros(self, r, c):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and not self.revealed[r + dr][c + dc]:
                    self.click(r + dr, c + dc)

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.revealed[r][c] and self.board[r][c] != -1:
                    return
        print("You win!")


def main():
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, 8, 8, 10)  # Customize rows, cols, and num_mines here
    root.mainloop()

if __name__ == "__main__":
    main()
