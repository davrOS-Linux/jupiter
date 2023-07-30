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
        gamescope_setup = f"gamescope -e -w {flags_gs['game_width']} -h {flags_gs['game_height']} -W {flags_gs['window_width']} -H {flags_gs['window_height']} -{upscaling_flag} {flags_gs['upscaling']} -- steam"
        print(gamescope_setup)
    elif flags_gs['gamescope_version'] == "new":
        flags_gs_upscaling = {
            "fsr": "U",
            "nis": "Y",
            "integer": "i",
            "nearest neighbor filter": "n"
        }

        if flags_gs['upscaling'] == "fsr":
            upscaling_gs_fsr_sharpness = None

            while True:
                upscaling_gs_fsr_sharpness = input("Enter AMD FidelityFX™ Super Resolution sharpness from 0 (max) to 20 (min)")
                if not upscaling_gs_fsr_sharpness.isnumeric():
                    print("Error: Invalid Choice")
                else:
                    if int(upscaling_gs_fsr_sharpness) < 0:
                        print("Error: Invalid Choice")
                    elif int(upscaling_gs_fsr_sharpness) > 20:
                        print("Error: Invalid Choice")
                    else:
                        print(f"FSR Sharpness: {upscaling_gs_fsr_sharpness}")
                        break
            gamescope_setup = f"gamescope -e -w {flags_gs['game_width']} -h {flags_gs['game_height']} -W {flags_gs['window_width']} -H {flags_gs['window_height']} -{flags_gs_upscaling[flags_gs['upscaling']]} -f -b --fsr-sharpness {upscaling_gs_fsr_sharpness} -- steam -tenfoot"
        else:
            gamescope_setup = f"gamescope -e -w {flags_gs['game_width']} -h {flags_gs['game_height']} -W {flags_gs['window_width']} -H {flags_gs['window_height']} -{flags_gs_upscaling[flags_gs['upscaling']]} -f -b -- steam -tenfoot"
        print(gamescope_setup)
    else:
        print("Error: Unknown Gamescope Version")
        sys.exit()
    run(gamescope_setup)
