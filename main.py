from game import Game

def main():
    game = Game()
    running = True
    while running:
        game.display_board()
        game.get_inputs()
        running = not game.check_end_condition()
        
if __name__ == "__main__":
    main()