from modules.steam import deck_ui

print("starting initial configuration")

game_width = input("Enter Width of game output: ")
game_height = input("Enter Height of game output: ")

window_width = input("Enter Width of rendered window: ")
window_height = input("Enter Height of rendered window: ")

upscaling_methods_list = [
    "AMD FidelityFX Super Resolution",
    "NVIDIA Image Scaling",
    "Integer Scaling",
    "Stretch Scaling"
]

upscaling_method_number = 0
upscaling_method_numbers = []

for upscaling_method in upscaling_methods_list:
    print(upscaling_method)
    upscaling_method_number = upscaling_method_number + 1
    upscaling_method_numbers.append(upscaling_method_number)

upscaling_method = None

while upscaling_method not in upscaling_method_numbers:
    upscaling_method = input(f"Enter Upscaling Method (1-{upscaling_method_number}): ")
    if upscaling_method not in upscaling_method_numbers:
        print("Error: Invalid Choice")
    else:
        print(f"Upscaling Method: {upscaling_method}")

flags = {
    "game_width": game_width,
    "game_height": game_height,
    "window_width": window_width,
    "window_height": window_height,
    "upscaling": upscaling
}

deck_ui(flags)
