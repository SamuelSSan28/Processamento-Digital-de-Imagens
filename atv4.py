import cv2
import numpy as np
from Compressao_Class import Compressao

cap = cv2.VideoCapture('atividade05.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

string = "Frame"
Video = {}
x = 1
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        nome = "frames_video\Frame"+str(x)+".png"
        cv2.imshow('video',frame)
        cv2.imwrite(nome, frame,[cv2.IMWRITE_PNG_COMPRESSION ,16])
        print(x)
        x += 1
        '''
        m, n = median.shape[0], median.shape[1]
r, g, b = [], [], []
for i in range(m):
    for j in range(n):
        rgb = median[i][j]
        r.append(str(rgb[0]))
        g.append(str(rgb[1]))
        b.append(str(rgb[2]))

saidaR, tamR,comR = Compressao.compressao_lzw(Compressao, r)
saidaG, tamG,comG = Compressao.compressao_lzw(Compressao, g)
saidaB, tamB,comB = Compressao.compressao_lzw(Compressao, b)

print(tamR,comR,((tamR/3))/comR)
print( tamG,comG,((tamG/3))/comG)
print(tamB,comB,((tamB/3))/comB)

        key = string+str(x)
        Video.update({key : [tamR,tamG,tamB,comR,comG,comB]})
        x += 1

    '''
    else: break
        # Press Q on keyboard to  exit

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
'''
file = open("video_frames.txt","a+")

for i in Video:
    frase = i + " " + str(Video[i]) + "\n"
    file.write(frase)

file.close()
'''