# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image


def iron_puzzle(filename):
    # Load the image
    image = Image(filename)

    # Iterate over each pixel to undo the distortions
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue *= 10  # Scaling blue values back to their proper value

    # Return the modified image
    return image




def west_puzzle(filename):
    # Load the image
    image = Image(filename)

    # Iterate over each pixel to reveal the image
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
        if pixel.blue < 16:
            pixel.blue *= 16
        else:
            pixel.blue = 0

    # Return the modified image
    return image



def darken(filename, percent):
    # Load the image
    image = Image(filename)

    # Iterate over each pixel to darken it
    for pixel in image:
        pixel.red = int(pixel.red * (1 - percent))
        pixel.green = int(pixel.green * (1 - percent))
        pixel.blue = int(pixel.blue * (1 - percent))

    # Return the modified image
    return image




def grayscale(filename):
    # Load the image
    image = Image(filename)

    # Iterate over each pixel to convert it to grayscale
    for pixel in image:
        average = int((pixel.red + pixel.green + pixel.blue) / 3)
        pixel.red = average
        pixel.green = average
        pixel.blue = average

    # Return the modified image
    return image


def sepia(filename):
    # Load the image
    image = Image(filename)

    # Iterate over each pixel to apply the sepia filter
    for pixel in image:
        true_red = int(0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue)
        true_green = int(0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue)
        true_blue = int(0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue)

        pixel.red = min(255, true_red)
        pixel.green = min(255, true_green)
        pixel.blue = min(255, true_blue)

    # Return the modified image
    return image


def create_left_border(filename, weight):
    # Load the original image
    original = Image(filename)

    # Create a new blank image with increased width
    new_image = Image.blank(original.width + weight, original.height)

    # Set the left border to blue
    for y in range(new_image.height):
        for x in range(weight):
            pixel = new_image.get_pixel(x, y)
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 255

    # Copy the original image to the new image, starting after the border
    for y in range(original.height):
        for x in range(original.width):
            original_pixel = original.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + weight, y)
            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    # Return the modified image
    return new_image


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    "*** YOUR CODE HERE ***"


def copper_puzzle(filename):
    "*** YOUR CODE HERE ***"
