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

def main():
    im = Image.open("ascii-pineapple.jpg")
    pixels_matrix = get_pixels(im)


if __name__ == "__main__":
    main()