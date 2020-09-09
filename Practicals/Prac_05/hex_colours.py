COLOURS_TO_HEX = {"AliceBlue": "f0f8ff", "AntiqueWhite": "faebd7",
                  "AntiqueWhite1": "ffefdb", "AntiqueWhite2": "eedfcc",
                  "azure1": "f0ffff", "azure2": "e0eeee", "azure2": "#e0eeee",
                  "azure3": "c1cdcd", "azure4": "838b8b", "beige": "f5f5dc", "bisque1": "ffe4c4"}
colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The hex code for {} is {}".format(colour_name, COLOURS_TO_HEX.get(colour_name)))
    colour_name = input("Enter a colour name: ")