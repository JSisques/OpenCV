import cv2
import numpy as np

def dibujar(mask, color):
    #Buscamos todos los contornos que haya en la mascara
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        #Guardamos el area del contorno
        area = cv2.contourArea(c)
        if area > 3000:
            #Calculamos el centro del contorno y lo etiquetamos
            M = cv2.moments(c)
            if M["m00"] == 0:
                M["m00"] = 1
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            #Creamos un circulo en el centro
            cv2.circle(frame, (x,y), 7, (0,0,0), -1)
            #Etiquetamos el centro
            cv2.putText(frame, '{},{}'.format(x,y), (x+10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1, cv2.LINE_AA )

            #Suavizamos el contorno
            contornoSuavizado = cv2.convexHull(c)
            cv2.drawContours(frame, [contornoSuavizado], 0, color, 3)

cap = cv2.VideoCapture(0)

#Valores en HSV
#Para el color rojo deberemos de crear 2 rangos de mascaras ya que se repite 2 veces
rojoBajo1 = np.array([0, 150, 40], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([170, 150, 40], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)


#Verde
verdeBajo1 = np.array([35, 100, 20], np.uint8)
verdeAlto1 = np.array([85, 255, 255], np.uint8)

#Azul
azulBajo1 = np.array([100, 100, 20], np.uint8)
azulAlto1 = np.array([125, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == False: break

    #Transformamos de BGR a HSV
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Creamos la mascara de color rojo
    maskRed1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
    maskRed2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)

    #Creamos una mascara con el rango de las dos mascaras anteriores
    maskRed = cv2.add(maskRed1, maskRed2)
    maskRed = cv2.medianBlur(maskRed, 13) # Filtro para suavizar imagenes

    #Creamos la mascara de color verde
    maskGreen = cv2.inRange(frameHSV, verdeBajo1, verdeAlto1)
    maskGreen = cv2.medianBlur(maskGreen, 13)

    #Creamos la mascara de color azul
    maskBlue = cv2.inRange(frameHSV, azulBajo1, azulAlto1)
    maskBlue = cv2.medianBlur(maskBlue, 13)

    #dibujar(maskRed, (0,0,255))
    dibujar(maskGreen, (0,255,0))
    dibujar(maskBlue, (255,0,0))

    cv2.imshow('Frame', frame)
    #cv2.imshow('Mask Red', maskRed)
    #cv2.imshow('Mask Green', maskGreen)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()