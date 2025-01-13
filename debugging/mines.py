#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))  # Set of mine positions
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Board for display
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Revealed cells tracking

    def print_board(self, reveal=False):
        """Prints the game board."""
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Mine symbol
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Empty space or mine count
                else:
                    print('.', end=' ')  # Hidden cell
            print()

    def count_mines_nearby(self, x, y):
        """Counts the number of mines in the adjacent cells."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Reveals the cell at (x, y). Returns False if a mine was hit, True otherwise."""
        if (y * self.width + x) in self.mines:
            return False  # Game over if mine is revealed
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_victory(self):
        """Checks if all non-mine cells have been revealed."""
        for y in range(self.height):
            for x in range(self.width):
                # Check if the cell is not a mine and is not revealed
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False  # There is still a cell to reveal
        return True  # All non-mine cells are revealed

    def play(self):
        """The main game loop."""
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                # Check for victory after revealing the cell
                if self.check_victory():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
