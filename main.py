from modules.steam import deck_ui

print("Initializing First-Time Setup")

game_width = input("Enter Width of game output: ")
game_height = input("Enter Height of game output: ")

window_width = input("Enter Width of rendered window: ")
window_height = input("Enter Height of rendered window: ")

upscaling_methods_list = [
    "AMD FidelityFX Super Resolution",
    "NVIDIA Image Scaling",
    "Integer Scaling",
    "Stretch Scaling",
    "none"
]

upscaling_method_number = 0
upscaling_method_numbers = []

for upscaling_method in upscaling_methods_list:
    upscaling_method_number = upscaling_method_number + 1
    upscaling_method_numbers.append(upscaling_method_number)
    print(str(upscaling_method_number) + ". " + str(upscaling_method))

upscaling_method = None

while True:
    upscaling_method = input(f"Enter Upscaling Method (1-{upscaling_method_number}): ")
    upscaling_method_valid = True
    if not upscaling_method.isnumeric():
        print("Error: Invalid Choice")
        upscaling_method_valid = False
    if upscaling_method_valid:
        if int(upscaling_method) not in upscaling_method_numbers:
            print("Error: Invalid Choice")
            upscaling_method_valid = False
        else:
            print(f"Upscaling Method: {upscaling_methods_list[int(upscaling_method)]}")
            break

flags = {
    "game_width": game_width,
    "game_height": game_height,
    "window_width": window_width,
    "window_height": window_height,
    "upscaling": upscaling_method
}

deck_ui(flags)
