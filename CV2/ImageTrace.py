import cv2

img = cv2.imread("Commerzbank-Plan.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 150,150)

cv2.imshow("edges", edges)


if cv2.waitKey(1) & 0xFF == ord("q"):
