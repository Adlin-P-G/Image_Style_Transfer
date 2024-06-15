import cv2

img = cv2.imread("./images/inputs/content/tubingen.jpg")
cv2.imshow("Input content Image ", img)

simg = cv2.imread("./images/inputs/style/starry_night.jpg")
cv2.imshow("Input Style Image ", simg)

img1 = cv2.imread("./images/output/result_at_iteration_1.png")
cv2.imshow("Iteration 1", img1)

img2 = cv2.imread("./images/output/result_at_iteration_2.png")
cv2.imshow("Iteration 2", img2)

img3 = cv2.imread("./images/output/result_at_iteration_3.png")
cv2.imshow("Iteration 3", img3)

img4 = cv2.imread("./images/output/result_at_iteration_4.png")
cv2.imshow("Iteration 4", img4)

img5 = cv2.imread("./images/output/result_at_iteration_5.png")
cv2.imshow("Iteration 5", img5)

img6 = cv2.imread("./images/output/result_at_iteration_6.png")
cv2.imshow("Iteration 6", img6)

img7 = cv2.imread("./images/output/result_at_iteration_7.png")
cv2.imshow("Iteration 7", img7)

img8 = cv2.imread("./images/output/result_at_iteration_8.png")
cv2.imshow("Iteration 8", img8)

img9 = cv2.imread("./images/output/result_at_iteration_9.png")
cv2.imshow("Iteration 9", img9)

img10 = cv2.imread("./images/output/result_at_iteration_10.png")
cv2.imshow("Iteration 10", img10)

cv2.waitKey(0)