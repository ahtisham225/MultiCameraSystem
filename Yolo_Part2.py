import cv2
import numpy as np
import matplotlib as plt




def YOLO(img):
    yolo = cv2.dnn.readNet('yolov3.weights', 'maskunmaskyolov3.cfg')
    classes = []

    with open('./mask-unmask-obj.names', 'r') as f:
        classes = f.read().splitlines()
    model = cv2.dnn.blobFromImage(img, 1/255, (400, 400),(0,0,0), swapRB=True, crop= False)
    yolo.setInput(model)
    
    layers = yolo.getLayerNames()
    output_layer = [layers[i[0] - 1] for i in yolo.getUnconnectedOutLayers()]
    layeroutput = yolo.forward(output_layer)

    # bounding boxes
    width = 400
    height = 400
    boxes = []
    confidences = []
    class_ids = []

    for output in layeroutput:
        for detect in output:
            score = detect[5:]
            class_id = np.argmax(score)
            confidence = score[class_ids]

            if confidence > 0.7:
                center_x = int(detect[0]*width)
                center_y = int(detect[0]*height)
                w = int(detect[0]*width)
                h = int(detect[0]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    return boxes, confidences, classes, class_ids
def main():
    choice = int(input("Enter 1 for live streaming the video or 2 to read recorded videos = "))
    if(choice == 2):
        vd1 = cv2.VideoCapture('vd1.mp4')
        # vd2 = cv2.VideoCapture('vd2.mp4')
        # vd3 = cv2.VideoCapture('vd3.mp4')
        if(vd1.isOpened() == False):
            print("Error opening the stream")

        while(vd1.isOpened()):
            ret1, frame1 = vd1.read()
            # print(frame1)

            if ret1 == True:
                boxes, confidences,classes, class_ids = YOLO(frame1)
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                font = cv2.FONT_HERSHEY_PLAIN
                colors = np.random.uniform(0, 255, size=(len(boxes),3))
                
                for i in indexes.flatten():
                    x,y,w,h = boxes[i]

                    label = str(classes[class_ids[i]])
                    confi = str(round(confidences[i], 2))
                    color = colors[i]
                    cv2.rectangel(frame1, (x, y), ( x+w), (y+h), color, 1)
                    cv2.putText(frame1, label+ " " + confi, (x, y+20), font, 2, (255, 255,255), 1)
                plt.imshow(frame1)
            
            # if cv2.waitkey(1) == 27:
                # break
            else:
                break
        vd1.release()
        cv2.destroyAllWindows()
    elif(choice == 1):
        print("Live streaming")

main()