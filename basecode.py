import cv2


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        cv2.namedWindow(windowName)
        windowName2= "Sample Feed from Camera 2"
        cv2.namedWindow(windowName2)
        windowName3 = "Sample Feed from Camera 3"
        cv2.namedWindow(windowName3)
        capture1 = cv2.VideoCapture(0)  # laptop's camera
        capture2 = cv2.VideoCapture("https://10.130.139.181:8080/video")   # sample code for mobile camera video capture using IP camera
        capture3 = cv2.VideoCapture("https://10.130.7.193:8080/video")

        # define size for recorded video frame for video 1
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

        
        w = int(capture2.get(3))
        h = int(capture2.get(4))
        size2 = (w,h)

        optputFile2 = cv2.VideoWriter(
            'Stream1Recording2.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size2)

        
        wid = int(capture3.get(3))
        hig = int(capture3.get(4))
        size3 = (wid,hig)

        optputFile3 = cv2.VideoWriter(
            'Stream1Recording3.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size3)
        
        # check if feed exists or not for camera 1
        if capture1.isOpened():
            ret1, frame1 = capture1.read()
        else:
            ret1 = False
        if capture2.isOpened():
            ret2, frame2 = capture2.read()
        else:
            ret2 = False
        if capture3.isOpened():
            ret3, frame3 = capture3.read()
        else:
            ret3 = False


        

        
        while ret1 and ret2 and ret3:
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()

        #     # saves the frame from camera 1
        #     optputFile3.write(frame3)

            
            cv2.imshow(windowName, frame1)
            cv2.imshow(windowName2, frame2)
            cv2.imshow(windowName3, frame3)

            # saves the frame from camera 1
            optputFile2.write(frame2)
            optputFile1.write(frame1)
            optputFile3.write(frame3)

            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        optputFile1.release()
        capture2.release()
        optputFile2.release()
        capture3.release()
        optputFile3.release()
        cv2.destroyAllWindows()
        



    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)

        capture1 = cv2.VideoCapture(0)  # laptop's camera

        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        while ret1:  # and ret2 and ret3:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)

            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
