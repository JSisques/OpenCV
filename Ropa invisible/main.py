import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#El frame que utilizaremos más adelante como fondo
bg = None

#Valores en HSV
#Para el color rojo deberemos de crear 2 rangos de mascaras ya que se repite 2 veces
colorBajo1 = np.array([0, 150, 40], np.uint8)
colorAlto1 = np.array([8, 255, 255], np.uint8)
colorBajo2 = np.array([170, 150, 40], np.uint8)
colorAlto2 = np.array([180, 255, 255], np.uint8)


#Verde
#colorBajo1 = np.array([35, 100, 20], np.uint8)
#colorAlto1 = np.array([85, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == False: break

    # Asignamos el primer frame como fondo
    if bg is None:
        bg = frame

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Creamos la primera mascara con el primer rango 
    maskRojo1 = cv2.inRange(frameHSV, colorBajo1, colorAlto1)
    #Creamos la segunda mascara en el caso de estar buscando el color rojo
    #maskRojo2 = cv2.inRange(frameHSV, colorBajo2, colorAlto2)
    maskRojo2 = cv2.inRange(frameHSV, colorBajo2, colorAlto2)

    #Creamos una mascara con el rango de las dos mascaras anteriores
    mask = cv2.add(maskRojo1, maskRojo2)
    mask = cv2.medianBlur(mask, 13) # Filtro para suavizar imagenes

    areaColor = cv2.bitwise_and(bg, bg, mask=mask)
    maskInv = cv2.bitwise_not(mask)
    sinAreaColor = cv2.bitwise_and(frame, frame, mask=maskInv)
    finalFrame = cv2.addWeighted(areaColor, 1, sinAreaColor, 1, 0)

    cv2.imshow('Frame', frame)
    #cv2.imshow('Mask', mask)
    #cv2.imshow('areaColor', areaColor)
    #cv2.imshow("Mask invertida", maskInv)
    #cv2.imshow("Sin area color", sinAreaColor)
    cv2.imshow("Final frame", finalFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()