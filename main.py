from src.game_manager import GameManager
import argparse

parser = argparse.ArgumentParser(description='At what time do you want the ducks to stop dancing? (24h format)')
parser.add_argument('hours', type=int, help='hours')
parser.add_argument('--m', type=int, default=0, help='minutes')
parser.add_argument('--s', type=int, default=0, help='seconds')

args = parser.parse_args()

game = GameManager(args.hours, args.m, args.s)
game.run()