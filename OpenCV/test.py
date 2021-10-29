import numpy as np
import cv2
import dlib


cap = cv2.VideoCapture('NBA.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=1, nmixtures=6, backgroundRatio=0.8)
# fgbg2 = cv2.createBackgroundSubtractorMOG2(history=200, detectShadows = True)
# timed = int(cap.get(cv2.CAP_PROP_POS_MSEC)) 
fourcc = cv2.VideoWriter_fourcc(*'MP4V') #avi
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('opencv.mp4',0x00000021,50.0,(width,height))

#Original
while True:
    ret, frame = cap.read()
    if ret==True:
        Original = 'Oringinal'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        #cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        cv2.imshow('frame', frame)
        out.write(frame)
        if 1500>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 1000:
            break
        if cv2.waitKey(1) == 27:
            break
    else:
        break
# BGR
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if ret==True:
        BGR = 'BGR'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)     
        out.write(frame)   
        if 3500>=int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 3000:
            break
        if cv2.waitKey(1) == 27:
            break
    else:
        break
#HSV
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if ret==True:
        HSV ='HSV'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)     
        out.write(frame)   
        if 5500>=int(cap.get(cv2.CAP_PROP_POS_MSEC)) > 5000:
            break 
        if cv2.waitKey(1) == 27:
            break
    else:
        break
#Gray
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==True:
        gray ='GRAY'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if 8550>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 8500:
            break
        if cv2.waitKey(1) == 27:
            break
    else:
        break
#Sobel
while True :
    ret, frame = cap.read()
    
    if ret==True:
        Sobel = 'Sobel'
        sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)
        sobelx = cv2.convertScaleAbs(sobelx)    
        sobely = cv2.convertScaleAbs(sobely)  
        frame = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) 
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,Sobel,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if 11000>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 10500:
                break
        if cv2.waitKey(1) == 27:
                break
    else:
        break
#Laplacian
while True :
    ret, frame = cap.read()
    if ret==True:
        laplacian = 'Laplacian'
        Laplacian = cv2.Laplacian(frame, cv2.CV_64F,ksize=3)
        frame = cv2.convertScaleAbs(Laplacian) 
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,Sobel,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,laplacian,(30,280),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if 13000>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 12500:
                break
        if cv2.waitKey(1) == 27:
                break
    else:
        break
#Canny
while True:
    ret, frame = cap.read()
    frame = cv2.Canny(frame, 100, 50)
    if ret==True:
        Canny = 'Canny'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,Sobel,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,laplacian,(30,280),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.putText(frame,Canny,(30,320),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if 16000>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) > 15800:
            break
        if cv2.waitKey(1) == 27:
            break
    else:
        break
#Original
while True:
    ret, frame = cap.read()
    if ret==True:
        detect = 'Detector'
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,Sobel,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,laplacian,(30,280),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,Canny,(30,320),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,detect,(30,360),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if 17000>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 16800:
            break
        if cv2.waitKey(1) == 27:
            break
    else:
        break
#Analysis
detector = dlib.get_frontal_face_detector()     
while(cap.isOpened()):                           
    ret, frame = cap.read()
    if ret==True:
        cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,Sobel,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,laplacian,(30,280),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,Canny,(30,320),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame,detect,(30,360),cv2.FONT_HERSHEY_TRIPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        face_rects, scores, idx = detector.run(frame, 0, .5)  # 
        for i, d in enumerate(face_rects):               
            x1 = d.left(); y1 = d.top(); x2 = d.right(); y2 = d.bottom()
            text = f'{scores[i]:.2f}, ({idx[i]:0.0f})'
            # text = '1'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA) # 
            cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,         
                        0.7, (255, 255, 255), 1, cv2.LINE_AA)

                                 
        cv2.imshow("frame", frame)        
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
#MOG
# while True :
#     ret, frame = cap.read()
    
#     if ret==True:
#         MOG = 'MOG'
#         cv2.putText(frame,Original,(30,80),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
#         cv2.putText(frame,BGR,(30,120),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
#         cv2.putText(frame,HSV,(30,160),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
#         cv2.putText(frame,gray,(30,200),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
#         cv2.putText(frame,MOG,(30,240),cv2.FONT_HERSHEY_TRIPLEX,1, (225, 225, 225), 1, cv2.LINE_AA)
#         frame = cv2.resize(frame, (width,height), interpolation = cv2.INTER_NEAREST)
#         fgrame = fgbg.apply(frame)            # fgbg
#         cv2.imshow('frame', fgrame)
#         out.write(fgrame)
#         if 11500>= int(cap.get(cv2.CAP_PROP_POS_MSEC)) >= 10500:
#                 break
#         if cv2.waitKey(1) == 27:
#                 break
#     else:
#         break
# #MOG2     
# while True:
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (width,height), interpolation = cv2.INTER_NEAREST)
    
#     frame = fgbg2.apply(frame)
#     cv2.imshow('frame', frame)
#     k = cv2.waitKey(80) & 0xff
#     out.write(frame)
#     if 17500>= time >= 17000:
#         break
#     if k == 27:
#         break
## Release everything if job is finished

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)