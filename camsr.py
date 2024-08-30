import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:\Users\sriva\Downloads\video-meeting-zego-main\video-meeting-zego-main\3.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get the floor area (assuming bright areas are the floor)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Define the regions for left, center, and right
height, width = thresh.shape
left_region = thresh[:, :width // 3]
center_region = thresh[:, width // 3: 2 * width // 3]
right_region = thresh[:, 2 * width // 3:]

# Calculate the percentage of the floor in each region
left_floor = np.sum(left_region == 255) / left_region.size * 100
center_floor = np.sum(center_region == 255) / center_region.size * 100
right_floor = np.sum(right_region == 255) / right_region.size * 100

# Determine the directions
directions = []
if left_floor > 10:  # Adjust threshold as needed
    directions.append("left")
if center_floor > 10:
    directions.append("straight")
if right_floor > 10:
    directions.append("right")

# Print the directions
if directions:
    print("The rover can move in the following directions:", ", ".join(directions))
else:
    print("No clear path available.")

# Save the thresholded image to a file or use matplotlib to display it
cv2.imwrite('thresholded_image.png', thresh)
print("Thresholded image saved as 'thresholded_image.png'")

# Alternatively, display using matplotlib
plt.imshow(thresh, cmap='gray')
plt.title('Thresholded Image')
plt.show()
