from bash import run

def init():
  run("sudo pacman -Syy --needed - < pkg.txt")

def deck_ui(flags):
  gamescope -e
