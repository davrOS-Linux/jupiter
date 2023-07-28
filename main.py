from steam import deck_ui

flags = {}

print("starting initial configuration")

game_width = input("Enter Width of game output: ")
game_height = input("Enter Height of game output: ")

window_width = input("Enter Width of rendered window: ")
window_height = input("Enter Height of rendered window: ")

upscaling_methods = ()

upscaling = input("Would you like to use an upscaling method?\n1. AMD FidelityFX Super Resolution\n2. NVIDIA Image Scaling\n3. Integer Scaling (Fit)\n4. Stretch Scaling")

flags = {
  "game_width":game_width,
  "game_height":game_height,
  "window_width":window_width,
  "window_height":window_height,
  "upscaling":upscaling
}

deck_ui(flags)
