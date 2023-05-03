import cv2
import os

def separate_sprites(image_path, output_dir):
	# Load the image
	image = cv2.imread(image_path)

	# Convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Threshold the image to separate the sprites from the background
	_, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

	# Find contours in the thresholded image
	contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Create the output directory if it does not exist
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	# Save each sprite as a separate image
	for i, contour in enumerate(contours):
		x, y, w, h = cv2.boundingRect(contour)
		sprite = image[y:y+h, x:x+w]
		sprite_path = os.path.join(output_dir, f"sprite_{i}.png")
		cv2.imwrite(sprite_path, sprite)

if __name__ == '__main__':
	# Replace "source_image.png" with the path to your source image
	image_path = "source_image.png"

	# Replace "output_directory" with the path to your output directory
	output_dir = "sprites"

	separate_sprites(image_path, output_dir)
