import cv2
import os
import numpy as np

dataPath = 'C:/Users/Javi/Documents/OpenCV/Tracking Facial/Data'
modelPath = 'C:/Users/Javi/Documents/OpenCV/Tracking Facial/Models'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Leyendo imagenes')

    for filename in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + filename)
        labels.append(label)
        facesData.append(cv2.imread(personPath + '/' + filename, 0))
        image = cv2.imread(personPath + '/' + filename, 0)
        #cv2.imshow('Images', image)
        #cv2.waitKey(10)
    label += 1

#cap.release()
#cv2.destroyAllWindows()

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()

#Entrenando el reconocedor de rostros
print('Entrenando...')
face_recognizer.train(facesData, np.array(labels))

#Almacenando el modelo
print('Almacenando...')
face_recognizer.write(modelPath + '/' + 'modeloLBPHFace.xml')
print('Modelo almacenado')