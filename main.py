import cv2
import os

# Abre o vídeo para leitura
cap = cv2.VideoCapture('/home/rafhael/Vídeos/2023.02.17/fiscalizacao2.mp4')

# Define a taxa de quadros (fps) do vídeo
fps = cap.get(cv2.CAP_PROP_FPS)

# Define o intervalo de tempo para cortar os frames (10 segundos)
intervalo = int(fps * 15)

# Cria uma pasta para armazenar as imagens cortadas
if not os.path.exists('frames'):
    os.makedirs('frames')

# Inicializa o contador de frames
count = 0

# Loop através do vídeo
while cap.isOpened():
    # Lê o próximo frame do vídeo
    ret, frame = cap.read()

    if not ret:
        break

    # Verifica se é hora de cortar o frame
    if count % intervalo == 0:
        # Salva o frame cortado na pasta
        cv2.imwrite(f'frames/frame_2_{count}.jpg', frame)

    # Incrementa o contador de frames
    count += 1

# Fecha o vídeo
cap.release()