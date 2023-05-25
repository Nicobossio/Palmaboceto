#Librerias a usar para el escaneo de los QR
import cv2
import numpy as np

#Toma de la foto y escaneo de la imagen
captura = cv2.VideoCapture(0)

#Bucle mientras la camara esta activa
while(captura.IsOpened()):
    ret, frame = captura.read()

    ##salida del programa cuando se tiene la entrada del usuario
    if (cv2.waitKey(1) == ord('s')):
        break
    
    qrdetection = cv2.QRCodeDetector()
    data, bbox, RectifiedImage == qrdetection.detectAndDecode(frame)#Datos que nos va a devolver el escaneo del QR


    #Si el codigo tiene un valor, se va a imprimir por pantalla
    #Tambien se valida el frame para que se escanee el QR
    if len(data) > 0:
        print(f'Dato: {data}')
        cv2.imshow('Webcam', RectifiedImage)
    else:
        cv2.imshow('Webcam', frame)


#Liberacion de la camara para el escaneo
captura.release()
cv2.destroyAllWindows   