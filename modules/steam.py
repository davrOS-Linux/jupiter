import contextlib

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
        gamescope_setup = (f"gamescope -e -w {flags_gs['game_width']} -h {flags_gs['game_height']} "
                           f"-W {flags_gs['window_width']} -H {flags_gs['window_height']} "
                           f"-{upscaling_flag} {flags_gs['upscaling']} -- steam")
        print(gamescope_setup)
    elif flags_gs['gamescope_version'] == "new":
        flags_gs_upscaling = {
            "fsr": "U",
            "nis": "Y",
            "integer": "i",
            "nearest neighbor filter": "n"
        }

        if flags_gs['upscaling'] == "fsr":
            upscaling_gs_fsr_sharpness = get_upscaling_gs_fsr_sharpness()
            fsr_param = f"--fsr-sharpness {upscaling_gs_fsr_sharpness}"
        else:
            fsr_param = ""

        gamescope_setup = (f"gamescope -efb -w {flags_gs['game_width']} -h {flags_gs['game_height']} "
                           f"-W {flags_gs['window_width']} -H {flags_gs['window_height']} "
                           f"{fsr_param} -{flags_gs_upscaling[flags_gs['upscaling']]} -- steam -tenfoot")
        print(gamescope_setup)
    else:
        print("Error: Unknown Gamescope Version")
        sys.exit()

    run("steam -shutdown")
    run(gamescope_setup)


def get_upscaling_gs_fsr_sharpness() -> str:
    while True:
        fsr_sharpness = input("Enter AMD FidelityFX™ Super Resolution sharpness from 0 (max) to 20 (min): ")
        with contextlib.suppress(ValueError):
            if 0 <= int(fsr_sharpness) <= 20:
                print(f"FSR Sharpness: {fsr_sharpness}")
                return fsr_sharpness
        print("Error: Invalid Choice")
