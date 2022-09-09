from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()
    while game.running:
        if not game.playing:
            game.menu(game.death_count)
    
    print("hello there...")
