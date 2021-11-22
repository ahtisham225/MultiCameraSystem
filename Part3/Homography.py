import cv2
import numpy as np


top_points = []
frame_points = []
def clickontop(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        top_points.append([x,y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(top_view,'o', (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('Top', top_view)


def clickonframe(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        frame_points.append([x,y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(sideview,'o', (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('sideview', sideview)


top_view = cv2.resize(cv2.imread('top_view.jpeg'),(700,700))
cv2.imshow('Top', top_view)
cv2.setMouseCallback('Top', clickontop)


sideview = cv2.resize(cv2.imread('File1.jpeg'),(700,700))
cv2.imshow('sideview', sideview)
cv2.setMouseCallback('sideview', clickonframe)


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

top_points = np.array(top_points)
frame_points = np.array(frame_points)
H = cv2.findHomography(frame_points, top_points)[0]
warp = cv2.warpPerspective(sideview, H, (700,700))
# Black out polygonal area in destination image.
cv2.fillConvexPoly(top_view, top_points.astype(int), 0, 16)

# Add warped source image to destination image.
billboard_dst = top_view + warp
cv2.imwrite('wrapped_Image.jpg', billboard_dst)
print(H)

cv2.destroyAllWindows()
x = int(input('1 for Recording 2 for LiveStream'))
if x == 1:
    # print('here')
    cam = cv2.VideoCapture('./vd1.mp4')
    count = 0
    img_array = []
    while True:

        ret, frame = cam.read()
        # layerOutputs = yolo.predict(frame)

        # cv2.imshow('frame', frame)
        try:
            # print('notcm')
            warp = cv2.warpPerspective(frame, H, (700,700))
            # # Black out polygonal area in destination image.
            cv2.fillConvexPoly(top_view, top_points.astype(int), 0, 16)

            # # Add warped source image to destination image.
            warp = top_view + warp
        except:
            break
        cv2.imshow('warp', warp)
        cv2.imwrite("frames/frame%d.jpg" % count, warp)
        img_array.append(warp)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),15,(700,700))
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    cam.release()
    cv2.destroyAllWindows()
elif x == 2:
        top_points = []
        frame_points = []
        # live stream
        top_view = cv2.resize(cv2.imread('Top.jpeg'),(700,700))
        cv2.imshow('Top', top_view)
        cv2.setMouseCallback('Top', clickontop)


        sideview = cv2.resize(cv2.imread('File.jpeg'),(700,700))
        cv2.imshow('sideview', sideview)
        cv2.setMouseCallback('sideview', clickonframe)


        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv2.destroyAllWindows()
        print('coming here')

        top_points = np.array(top_points)
        frame_points = np.array(frame_points)

        H = cv2.findHomography(frame_points, top_points)[0]
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)

        capture1 = cv2.VideoCapture("https://10.130.139.181:8080/video")  # laptop's camera

        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
            
        else:
            ret1 = False

        while ret1:  # and ret2 and ret3:
            ret1, frame1 = capture1.read()
            warp = cv2.warpPerspective(frame1, H, (700,700))
            # Black out polygonal area in destination image.
            cv2.fillConvexPoly(top_view, top_points.astype(int), 0, 16)

            # Add warped source image to destination image.
            billboard_dst = top_view + warp
            # cv2.imwrite('wrapped_Image.jpg', billboard_dst)
            cv2.imshow(windowName1, billboard_dst)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture1.release()
        cv2.destroyAllWindows()

else:
    print("Invalid option entered. Exiting...")



# 