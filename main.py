from PIL import Image

def get_pixels(im: Image) -> list:
    #resizes the image so it fits on the screen
    im.thumbnail((1000, 200))

    pixels = im.load()

    pixels_2d = []
    for y in range(im.height):
        row = []
        for x in range(im.width):
            row.append(pixels[x,y])
        pixels_2d.append(row)

    return pixels_2d

def get_brightness_matrix(pixel_matrix: list) -> list:
    brightness_matrix = []

    for y in range(len(pixel_matrix)):
        row = []
        for x in range(len(pixel_matrix[0])):
            R = pixel_matrix[y][x][0]
            G = pixel_matrix[y][x][1]
            B = pixel_matrix[y][x][2]
            brightness = (R + G + B) / 3
            row.append(round(brightness))

        brightness_matrix.append(row)

    return brightness_matrix

def get_ASCII_matrix(brightness_matrix: list) -> list:
    characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    min_brightness = min([item for sublist in brightness_matrix for item in sublist])
    max_brightness = max([item for sublist in brightness_matrix for item in sublist])

    ascii_matrix = []

    for row in brightness_matrix:
        ascii_row = []

        for brightness in row:

            #This loop is so the ascii picture stretches out
            #as it looks squashed without it.
            for i in range(3):

                #Using the linear interpolation formula to map the brightness value to an ascii value.
                #The formula used is y = (x - x1) * (y2 -y1) / (x2-x1) + y1.
                #x is the input, x1 and x2 are lower and upper bounds of input range.
                #Same with y1 and y2 except that they are the bounds of the output range.
                #the lower range is 0, which is why there is - and + 0.
                character_index = int((brightness - min_brightness) * (len(characters) - 1 - 0) / (
                                    max_brightness - min_brightness) + 0)
                character = characters[character_index]

                ascii_row.append(character)

        ascii_matrix.append(ascii_row)

    return ascii_matrix


def main():
    im = Image.open("ascii-pineapple.jpg")

    pixels_matrix = get_pixels(im)
    #print("pixel matrix length: " + str(len(pixels_matrix)) + " " + str(len(pixels_matrix[0])))

    brightness_matrix = get_brightness_matrix(pixels_matrix)
    #print("brightness length: "+ (str(len(brightness_matrix))) + " " + str(len(brightness_matrix[0])))
    #print(brightness_matrix)

    ascii_matrix = get_ASCII_matrix(brightness_matrix)
    #To turn the rows in the matrix into a single string with line breaks between each row.
    result = '\n'.join([''.join(row) for row in ascii_matrix])

    print(result)

if __name__ == "__main__":
    main()