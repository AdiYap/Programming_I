COLOR_NAMES = {"AliceBlue": "#f0f8ff", "Beige": "#f5f5dc", "Black": "#000000", "Brown": "#a52a2a",
               "Burlywood": "#deb887", "CadetBlue": "#5f9ea0", "Chocolate": "#d2691e", "Coral": "#ff7f50",
               "CornflowerBlue": "#6495ed", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400"}

color = input("Please Enter the color: ")
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Please Enter the color: ")