# Used to detect number digits from image

import cv2
import pytesseract
import numpy as np

# Step 1: Load the image
image = cv2.imread('img.png', cv2.IMREAD_COLOR)

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Threshold the image to create a binary image (for better contrast between digits and background)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Step 4: Apply a median blur to reduce noise (helps with thin lines)
blurred = cv2.medianBlur(binary, 3)

# Step 5: Use morphological transformations (remove unwanted lines)
kernel = np.ones((3, 3), np.uint8)  # Smaller kernel size to remove thin lines
morph = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, kernel)  # Close small gaps in digits

# Step 6: Further clean the image by applying an additional dilation operation to enhance the digits
dilated = cv2.dilate(morph, kernel, iterations=1)

# Step 7: Find contours in the dilated image to detect individual digits
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 8: Extract and recognize digits from the contours
digit_bboxes = []
cropped_digits = []
for contour in contours:
    # Get the bounding box for each contour
    x, y, w, h = cv2.boundingRect(contour)
    if w > 10 and h > 20:  # Set a minimum size for the detected digits
        digit_bboxes.append((x, y, w, h))
        digit_image = image[y:y + h, x:x + w]  # Crop the digit image
        cropped_digits.append(digit_image)

# Step 9: Use pytesseract to recognize digits from the cropped regions
recognized_text = ''
for digit_image in cropped_digits:
    # Use pytesseract to recognize the digit
    text = pytesseract.image_to_string(digit_image, config='--psm 6')
    recognized_text += text.strip()  # Concatenate recognized digits

# Print the recognized number
print(f"Recognized number: {recognized_text}")

# Step 10: Optional: Draw bounding boxes and show the result
for (x, y, w, h) in digit_bboxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw bounding box

# Show the image with detected digits
cv2.imshow("Detected Digits", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
