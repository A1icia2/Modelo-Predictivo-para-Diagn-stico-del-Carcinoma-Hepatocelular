import cv2
import os

# Carpeta de entrada y salida
input_folder = "Ruta de la carpeta con las imágenes originales"
output_folder = "Ruta de la carpeta para las imágenes recortadas"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Recortar (arriba, abajo, izquierda, derecha)
        crop_img = img[80:-120, 140:-96]

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, crop_img)

print("Recorte completado para todas las imágenes.")
