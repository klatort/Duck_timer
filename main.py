from src.game_manager import GameManager
import os
import sys
import argparse

assets_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

parser = argparse.ArgumentParser(description='At what time do you want the ducks to stop dancing? (24h format)')
parser.add_argument('hours', type=int, help='hours')
parser.add_argument('-m', '--minutes', type=int, default=0, help='minutes')
parser.add_argument('-s', '--seconds', type=int, default=0, help='seconds')

args = parser.parse_args()

game = GameManager(args.hours, args.minutes, args.seconds, assets_path)
game.run()