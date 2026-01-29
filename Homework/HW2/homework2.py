from byuimage import Image

def flipped(filename):
    # Load the original image
    original_image = Image(filename)

    # Get the dimensions of the original image
    width = original_image.width
    height = original_image.height

    # Create a new blank image of the same size
    new_image = Image.blank(width, height)

    # Loop over each pixel in the original image and copy it to the correct flipped position
    for y in range(height):
        for x in range(width):
            # Get the pixel from the original image
            pixel = original_image.get_pixel(x, y)

            # Get a reference to the corresponding pixel in the new image (vertically flipped)
            new_pixel = new_image.get_pixel(x, height - y - 1)

            # Set the new pixel's RGB values to match the original pixel
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue

    # Return the flipped image
    return new_image

def make_borders(filename, thickness, red, green, blue):
    # Load the original image
    original_image = Image(filename)

    # Get the dimensions of the original image
    width = original_image.width
    height = original_image.height

    # Calculate the new dimensions (accounting for the border thickness)
    new_width = width + 2 * thickness
    new_height = height + 2 * thickness

    # Create a new blank image with the new dimensions
    new_image = Image.blank(new_width, new_height)

    # Fill the border region with the specified color
    # Top and bottom border
    for y in range(thickness):
        for x in range(new_width):
            # Set the top border pixel color
            top_pixel = new_image.get_pixel(x, y)
            top_pixel.red = red
            top_pixel.green = green
            top_pixel.blue = blue

            # Set the bottom border pixel color
            bottom_pixel = new_image.get_pixel(x, new_height - y - 1)
            bottom_pixel.red = red
            bottom_pixel.green = green
            bottom_pixel.blue = blue

    # Left and right border
    for y in range(thickness, new_height - thickness):
        for x in range(thickness):
            # Set the left border pixel color
            left_pixel = new_image.get_pixel(x, y)
            left_pixel.red = red
            left_pixel.green = green
            left_pixel.blue = blue

            # Set the right border pixel color
            right_pixel = new_image.get_pixel(new_width - x - 1, y)
            right_pixel.red = red
            right_pixel.green = green
            right_pixel.blue = blue

    # Copy the original image pixels to the new image with the offset for the border
    for y in range(height):
        for x in range(width):
            # Get the pixel from the original image
            pixel = original_image.get_pixel(x, y)

            # Get a reference to the corresponding pixel in the new image (offset by the border thickness)
            new_pixel = new_image.get_pixel(x + thickness, y + thickness)

            # Set the new pixel's RGB values to match the original pixel
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue

    # Return the new image with borders
    return new_image

# Main block to test the functions
if __name__ == "__main__":
    # Flip an image and show the result
    flipped_image = flipped("landscape.png")
    flipped_image.show()

    # Add a border to an image and show the result
    bordered_image = make_borders("landscape.png", 30, 0, 255, 0)
    bordered_image.show()