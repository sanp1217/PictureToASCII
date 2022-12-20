from PIL import Image

def get_pixels(im: Image) -> list:
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
def main():
    im = Image.open("ascii-pineapple.jpg")

    pixels_matrix = get_pixels(im)
    print("pixel matrix length: " + str(len(pixels_matrix)) + " " + str(len(pixels_matrix[0])))


    brightness_matrix = get_brightness_matrix(pixels_matrix)

    print("brightness length: "+ (str(len(brightness_matrix))) + " " + str(len(brightness_matrix[0])))

    print(brightness_matrix)



if __name__ == "__main__":
    main()