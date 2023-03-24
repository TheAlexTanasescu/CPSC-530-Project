import cv2
import random


file = open("MattPicPasswords.txt", "a")
def captureEvent(event, x, y, flags, param):
    global clicked 
    if event == cv2.EVENT_LBUTTONDOWN and not clicked:
        clicked = True

        cell_width = img.shape[1] // 3
        cell_height = img.shape[0] // 3

        row = y // cell_height
        col = x // cell_width

        cell_num = (row * 3 + col) + 1

        file.write(f"({x}, {y}), Cell {cell_num}")
        file.write("\n")
        cv2.destroyAllWindows


start = 1
stop = 6

nums = random.sample(range(start, stop+1), 3)
images = ["image" + str(num)+".jpg" for num in nums]

clicked = False
for image in images:
    clicked = False
    file.write(image)
    img = cv2.imread(image)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", captureEvent)
    cv2.waitKey(0)
cv2.destroyAllWindows()
file.write("\n")
file.close()
