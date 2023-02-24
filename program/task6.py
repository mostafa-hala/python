# Ahmed Ashraf : draw_rectangle function, assigned global variables
# Ahmed Dusuki : try except, main while loop, draw_options function
# Mostafa Mohamed : choose image loop, with user options on screen


import cv2
import numpy as np

# Color array for all the available colors to user to choose from with an index
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_choice = 0
draw = False
# Initial value of x and y of the rectangle edges
initial_x, initial_y = -1, -1
img_menu = np.zeros((512, 512, 3), np.uint8)

cv2.putText(img_menu, "Select image to compare:", (0, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "1=coral1.jpg", (0, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "2=coral2.jpg", (0, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "3=coral3.jpg", (0, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "4=coral4.jpg", (0, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "5=coral5.jpg", (0, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.putText(img_menu, "6=coral6.jpeg", (0, 210), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
cv2.imshow("Image", img_menu)
while True:
    key = cv2.waitKey(1)
    if key == ord("1"):
        show = cv2.imread("task_6/coral1.jpg")
        break

    elif key == ord("2"):
        show = cv2.imread("task_6/coral2.jpg")
        break

    elif key == ord("3"):
        show = cv2.imread("task_6/coral3.jpg")
        break

    elif key == ord("4"):
        show = cv2.imread("task_6/coral4.jpg")
        break

    elif key == ord("5"):
        show = cv2.imread("task_6/coral5.jpg")
        break

    elif key == ord("6"):
        show = cv2.imread("task_6/coral6.jpeg")
        break

cv2.destroyWindow("Image")


def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (0, 0), None, scale, scale
                    )
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y],
                        (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                        None,
                        scale,
                        scale,
                    )
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x],
                    (imgArray[0].shape[1], imgArray[0].shape[0]),
                    None,
                    scale,
                    scale,
                )
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def draw_rectangle(event, x, y, flags, params):
    global draw, initial_x, initial_y, color_choice, img, cache
    current_color = colors[color_choice]

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        cache = img.copy()  # Saves the last image before drawing a rectangle also allows rectangle to be drawn from any point to any point
        initial_x, initial_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            # removes previously drawn rectangles during the drawing to show only the last drawn rectangle
            img = cache.copy()
            cv2.rectangle(img, (initial_x, initial_y), (x, y), current_color, 2)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(img, (initial_x, initial_y), (x, y), current_color, 2)


def draw_options():
    global img

    cv2.putText(
        img,
        "Q to quit",
        (10, 20),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (0, 0, 0),
        1,
    )
    cv2.putText(
        img,
        "B for blue color",
        (10, 40),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        colors[0],
        1,
    )
    cv2.putText(
        img,
        "G for green color",
        (10, 60),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        colors[1],
        1,
    )
    cv2.putText(
        img,
        "R for red color",
        (10, 80),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        colors[2],
        1,
    )
    cv2.putText(
        img,
        "Y for yellow color",
        (10, 100),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        colors[3],
        1,
    )


try:

    original = cv2.imread("task_6/OneYearImage.jpg")
    img = stack_images(1, ([original, show]))
    cache = original.copy()  # sets cache variable to last img available

    cv2.namedWindow("Coral")

    cv2.setMouseCallback("Coral", draw_rectangle)

    draw_options()

    while True:
        cv2.imshow("Coral", img)

        key = cv2.waitKey(1)

        if key == ord("q") or key == ord("Q"):  # quit
            raise Exception("Graceful exit")

        elif key == ord("b") or key == ord("B"):  # choose blue color
            color_choice = 0
        elif key == ord("g") or key == ord("G"):  # choose green color
            color_choice = 1
        elif key == ord("r") or key == ord("R"):  # choose red color
            color_choice = 2
        elif key == ord("y") or key == ord("Y"):  # choose yellow color
            color_choice = 3


except Exception as e:
    text_file = open("task6_log.txt", "w")
    text_file.write(str(e))
    text_file.close()

    # destroy windows
    cv2.destroyAllWindows()
