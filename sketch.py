import cv2
image = cv2.imread("my.jpg")                  # read the original image


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #coverting the image to greyscale                                                    


inverted_image = 255 - gray_image  #inverting the image


blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)  #blur the image

inverted_blurred = 255 - blurred  #invert the blurred image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=250.0) 


#to look at both the original image and the sketch
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)

