import cv2

img = cv2.imread('kopek.jpg')

while True:
    cv2.imshow('kopek resmi',img)
    
    # Eğer 1 ms beklediyesek ve Esc tuşuna bastıysak
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()