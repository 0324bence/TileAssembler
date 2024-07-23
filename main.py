from PIL import Image
import os
import re

# file path (later change to user input)
path = "./images/"

# file name regex (later change to user input)
file_name = "^([\d]*)_([\d]*)"

files = os.listdir(path)

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
