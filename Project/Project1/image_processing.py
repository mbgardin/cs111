from byuimage import Image
import sys


def validate_commands():
    if len(sys.argv) == 3 and sys.argv[1] == '-d':
        return display()
    elif len(sys.argv) == 5 and sys.argv[1] == '-k':
        percentage = float(sys.argv[4])
        print(sys.argv[3])
        filename = sys.argv[2]
        input_file = Image(filename)
        return darken(input_file, percentage)
    elif len(sys.argv) == 4 and sys.argv[1] == '-s':
        filename = sys.argv[2]
        input_file = Image(filename)
        return sepia(filename)
    elif len(sys.argv) == 4 and sys.argv[1] == '-g':
        filename = sys.argv[2]
        input_file = Image(filename)
        return grayscale(filename)
    elif len(sys.argv) == 8 and sys.argv[1] == '-b':
        filename = sys.argv[2]
        input_file = Image(filename)
        thickness = sys.argv[4]
        red = sys.argv[5]
        green = sys.argv[6]
        blue = sys.argv[7]
        return make_borders(input_file, thickness, red, green, blue)
    elif len(sys.argv) == 4 and sys.argv[1] == '-f':
        return flipped()
    elif len(sys.argv) == 4 and sys.argv[1] == '-m':
        return mirror()
    elif len(sys.argv) == 8 and sys.argv[1] == '-c':
        return collage()
    elif len(sys.argv) == 7 and sys.argv[1] == '-y':
        return green_screen()
    else:
        return False


# file not found error for some reason
def darken(filename, percentage):
    filename = sys.argv[2]
    input_file = Image(filename)
    output = sys.argv[3]
    # output_file = Image(output)
    # print(output_file)
    percentage = 1 - percentage
    for pixel in input_file:
        pixel.red = pixel.red * percentage
        pixel.green = pixel.green * percentage
        pixel.blue = pixel.blue * percentage
    input_file.save(output)


def sepia(filename):
    filename = sys.argv[2]
    input_file = Image(filename)
    output_file = sys.argv[3]
    for pixel in input_file:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        pixel.red = true_red
        pixel.green = true_green
        pixel.blue = true_blue
    input_file.save(output_file)


def grayscale(filename):
    filename = sys.argv[2]
    input_file = Image(filename)
    output_file = sys.argv[3]
    for pixel in input_file:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    input_file.save(output_file)


# getting assertion error
def make_borders(input_file, thickness, red, green, blue):
    filename = sys.argv[2]
    input_file = Image(filename)
    output_file = sys.argv[3]
    int_thickness = int(thickness)

    bordered = Image.blank(input_file.width + (int_thickness * 2), input_file.height + (int_thickness * 2))

    for y in range(0, bordered.height):
        for x in range(0, bordered.width):
            borderedPixel = bordered.get_pixel(x, y)
            borderedPixel.red = red
            borderedPixel.green = green
            borderedPixel.blue = blue

    for y in range(0, input_file.height):
        for x in range(0, input_file.width):
            ogPixel = input_file.get_pixel(x, y)
            borderedPixel = bordered.get_pixel(x + int_thickness, y + int_thickness)

            borderedPixel.red = ogPixel.red
            borderedPixel.green = ogPixel.green
            borderedPixel.blue = ogPixel.blue
    bordered.save(output_file)
    return bordered


def flipped():
    original = Image(sys.argv[2])
    output_file = sys.argv[3]
    flippedImage = Image.blank(original.width, original.height)
    for y in range(0, original.height):
        for x in range(0, original.width):
            pixel = original.get_pixel(x, y)
            pixel_new = flippedImage.get_pixel(x, original.height - y - 1)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    flippedImage.save(output_file)
    return flippedImage


def mirror():
    original = Image(sys.argv[2])
    output_file = sys.argv[3]
    mirrorImage = Image.blank(original.width, original.height)
    for y in range(0, original.height):
        for x in range(0, original.width):
            pixel = original.get_pixel(x, y)
            pixel_new = mirrorImage.get_pixel(original.width - x - 1, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    mirrorImage.save(output_file)
    return mirrorImage


def collage():
    input1 = sys.argv[2]
    input2 = sys.argv[3]
    input3 = sys.argv[4]
    input4 = sys.argv[5]
    image1 = Image(input1)
    image2 = Image(input2)
    image3 = Image(input3)
    image4 = Image(input4)
    output_file = sys.argv[6]
    thickness = int(sys.argv[7])

    composite = Image.blank((image1.width * 2) + (thickness * 3), (image1.height * 2) + (thickness * 3))

    for y in range(0, composite.height):
        for x in range(0, composite.width):
            compositePixel = composite.get_pixel(x, y)
            compositePixel.red = 0
            compositePixel.green = 0
            compositePixel.blue = 0

    for y in range(0, image1.height):
        for x in range(0, image1.width):
            image1Pixel = image1.get_pixel(x, y)
            composite1pixel = composite.get_pixel(x + thickness, y + thickness)

            composite1pixel.red = image1Pixel.red
            composite1pixel.green = image1Pixel.green
            composite1pixel.blue = image1Pixel.blue

    for y in range(0, image2.height):
        for x in range(0, image2.width):
            image2Pixel = image2.get_pixel(x, y)
            composite2pixel = composite.get_pixel((x + image1.width + (2 * thickness)), (y + thickness))

            composite2pixel.red = image2Pixel.red
            composite2pixel.green = image2Pixel.green
            composite2pixel.blue = image2Pixel.blue

    for y in range(0, image3.height):
        for x in range(0, image3.width):
            image3Pixel = image3.get_pixel(x, y)
            composite3pixel = composite.get_pixel(x + thickness, (y + image1.height + (thickness * 2)))

            composite3pixel.red = image3Pixel.red
            composite3pixel.green = image3Pixel.green
            composite3pixel.blue = image3Pixel.blue

    for y in range(0, image4.height):
        for x in range(0, image4.width):
            image4Pixel = image4.get_pixel(x, y)
            composite4Pixel = composite.get_pixel((x + image3.width + (2 * thickness)),
                                                  (y + image2.height + (2 * thickness)))

            composite4Pixel.red = image4Pixel.red
            composite4Pixel.green = image4Pixel.green
            composite4Pixel.blue = image4Pixel.blue

    composite.save(output_file)
    return composite


def detect_green(pixel):
    factor = float(sys.argv[6])
    threshold = float(sys.argv[5])
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False


def green_screen():
    foreground = Image(sys.argv[2])
    background = Image(sys.argv[3])
    output_file = sys.argv[4]
    final = Image.blank(background.width, background.height)
    for y in range(background.height):
        for x in range(background.width):
            np = final.get_pixel(x, y)
            bp = background.get_pixel(x, y)
            np.red = bp.red
            np.green = bp.green
            np.blue = bp.blue

    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp):
                np = final.get_pixel(x, y)
                np.red = fp.red
                np.green = fp.green
                np.blue = fp.blue
    final.save(output_file)
    return final


# this code works just fine and passes every time
def display():
    filename = sys.argv[2]
    input_file = Image(filename)
    input_file.show()


print(validate_commands())

if __name__ == "__main__":
    pass