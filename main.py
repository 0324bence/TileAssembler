from PIL import Image
import os
import re
import getopt, sys

def_path = "./images/"
def_file_name = "^([\\d]*)_([\\d]*)"

path = ""
file_name = ""

arguments = sys.argv[1:]

options = "hp:f:"

long_options = ["help", "path=", "file_name="]

try:
    arguments, values = getopt.getopt(arguments, options, long_options)

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print("Usage: python main.py -p <path> -f <file_name>")
            print("Path: path to the folder containing the images (default: ./images/)")
            print("File_name: regex to match the file name (default: ^([\\d]*)_([\\d]*)")
            sys.exit(0)
        elif current_argument in ("-p", "--path"):
            path = current_value
        elif current_argument in ("-f", "--file_name"):
            file_name = current_value
except getopt.error as err:
    print(str(err))
    sys.exit(2)

if path == "":
    inp = input("Path to the folder containing the images (default: ./images/): ")
    if inp == "":
        path = def_path
    else:
        path = inp

if file_name == "":
    inp = input("Regex to match the file name (default: ^([\\d]*)_([\\d]*): ")
    if inp == "":
        file_name = def_file_name
    else:
        file_name = inp


files = os.listdir(path)

for file in files:
    print("Found file: " + file)
input("Press Enter to continue...")

size = 0, 0

with Image.open(path + files[0]) as img:
    size = img.size

result_grid_size = 0, 0

for file in files:
    match = re.search(file_name, file)
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        result_grid_size = max(result_grid_size[0], x), max(result_grid_size[1], y)

result_image = Image.new("RGB", (result_grid_size[0] * size[0], result_grid_size[1] * size[1]))

for file in files:
    with Image.open(path + file) as img:
        match = re.search(file_name, file)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            result_image.paste(img, (x * size[0], y * size[1]))

result_image.save("result.jpg")
print("Result image saved as result.jpg")
with result_image as img:
    img.show()
