from modules.bash import run
import sys


def init():
    run("sudo pacman -Syy --needed - < pkg.txt")


def deck_ui(flags_gs):
    if flags_gs['gamescope_version'] == "old":
        if flags_gs['upscaling'] == "integer" or flags_gs['upscaling'] == "stretch":
            upscaling_flag = "S"
        elif flags_gs['upscaling'] == "fsr" or flags_gs['upscaling'] == "nis":
            upscaling_flag = "F"
        else:
            print("Error: Unknown Upscaling Method")
            sys.exit()
    elif flags_gs['gamescope_version'] == "new":
        if flags_gs['upscaling'] == "fsr":
            upscaling_flag = "S"
        elif flags_gs['upscaling'] == "nis":
            upscaling_flag = "F"
        else:
            print("Error: Unknown Upscaling Method")
            sys.exit()
    else:
        print("Error: Unknown Gamescope Version")
        sys.exit
    gamescope_setup = f"gamescope -e -w {flags_gs['game_width']} -h {flags_gs['game_height']} -W {flags_gs['window_width']} -H {flags_gs['window_height']} -{upscaling_flag} {flags_gs['upscaling']} -- steam"
    print(gamescope_setup)
    run(gamescope_setup)
