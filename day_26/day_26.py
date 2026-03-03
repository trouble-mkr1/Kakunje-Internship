# import cv2
# i = cv2.imread("flower.jpg")
# cv2.imshow("flower", i)

# rs = cv2.resize(i, (350, 350))
# cv2.imshow("resized image.jpg", rs)

# import pyautogui as gui
#mouseb the mouse
# gui.moveTo(1500, 500)
# gui.moveTo(600, 700, duration = 5)
############################################################################################
############################################################################################
############################################################################################
############################################################################################
import cv2
print("TASK 1- Smart Campus Vision System (OpenCV)\n")
print("PART 1 - IMAGE PROCESSING MODULE\n")
i = cv2.imread("student_id.jpg")
print("Image Loaded Successfully!")
cv2.imwrite("backup.jpg", i)
r = cv2.resize(i, (300, 300))
print("Image Resized to 300x300")
cv2.imshow("Resized Image", r)
c = r[120:225, 120:250]
print("Cropped Region Displayed")
cv2.imshow("Cropped Image", c)
gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
print("Converted to Grayscale")
cv2.imshow("Grayscale Image", gray)
hsv = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
print("Converted to HSV")
cv2.imshow("HSV Image", hsv)
blur = cv2.GaussianBlur(r, (15, 15), 0)
print("Blur Applied")
cv2.imshow("Blurred Image", blur)
print("Image Processing Module Completed!")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nPART 2 - VIDEO PROCESSING MODULE\n")
cap = cv2.VideoCapture(0)
print("Camera Started...")
print("Press 'q' to Exit")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Look into the Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print("Camera Closed Successfully")

print("======================================================================")
###############################################################################
###############################################################################

print("TASK  2 - Smart Office Automation Bot(Using  PyAutoGUI Module)\n")

import pyautogui
import time

time.sleep(3)

print("Launching Calculator...")

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('calc')
pyautogui.press('enter')

time.sleep(2)
print("Calculator Opened Successfully")

print("Performing Automated Calculation...")

pyautogui.write('1234+5678')
pyautogui.press('enter')

time.sleep(1)

result_screenshot = pyautogui.screenshot(region=(1200, 50, 600, 850))
result_screenshot.save("calculator_result.png")

print("Result Captured Successfully")

print("Mouse Movement Started")

pyautogui.moveTo(600, 300, duration=3)
pyautogui.click()

pyautogui.doubleClick(duration=1)

pyautogui.rightClick(duration=1)

print("Click Actions Completed")

pyautogui.dragTo(1000, 600, duration=3)
print("Drag Operation Completed")

print("Opening Notepad...")

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('notepad')
pyautogui.press('enter')

time.sleep(2)

print("Typing Report...")

pyautogui.write("Daily Automation Report Generated")
pyautogui.press('enter')
pyautogui.write("Date: 03/03/2026")
pyautogui.press('enter')
pyautogui.write("Task 2 completed!!")
pyautogui.press('enter')

time.sleep(1)

pyautogui.hotkey('ctrl', 's')
time.sleep(1)

pyautogui.write("report.txt")
pyautogui.press('enter')
pyautogui.press('enter')
print("Report Saved Successfully")

full_screen = pyautogui.screenshot()
full_screen.save("full_screen.png")
print("Full Screen Captured")

partial_screen = pyautogui.screenshot(region=(200, 200, 1000, 1000))
partial_screen.save("partial_screen.png")

print("Partial Screen Captured")
print("Screenshots Saved Successfully")