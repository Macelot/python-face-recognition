import cv2
import face_recognition
import os
import numpy as np

# brew install cmake
# brew install boost
# brew install boost-python3
# brew install pkg-config
# brew install openblas
# brew install lapack
# brew install xquartz
# brew install python3
# pip install dlib
# pip install git+https://github.com/davisking/dlib.git
# pip install face_recognition

# brew link --overwrite cmake --dry-run
# Would remove:
# /opt/homebrew/bin/cmake
# /opt/homebrew/bin/cpack
# /opt/homebrew/bin/ctest

# Pasta com as imagens conhecidas (pessoas que você deseja reconhecer)
pasta_conhecidos = 'pessoas'

# Carregar as imagens conhecidas e mapear seus nomes
conhecidos = {}
for arquivo in os.listdir(pasta_conhecidos):
    if arquivo.endswith(".png"):
        print (arquivo)
        nome_pessoa = os.path.splitext(arquivo)[0]
        imagem_pessoa = face_recognition.load_image_file(os.path.join(pasta_conhecidos, arquivo))
        
        rgb_image = cv2.cvtColor(imagem_pessoa, cv2.COLOR_BGR2RGB)
        rgb_image.astype('uint8')

        encoding_pessoa = face_recognition.face_encodings(rgb_image)[0]
        conhecidos[tuple(encoding_pessoa)] = nome_pessoa 

# Inicializar a câmera
camera = cv2.VideoCapture(0)  # Use 0 para a câmera padrão (geralmente a webcam)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Erro ao capturar quadro da câmera.")
        break

    # Detectar rostos na imagem da câmera
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(cinza)

    for (top, right, bottom, left) in faces:
        # Desenhar um retângulo verde ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Codificar o rosto detectado
        face_encodings = face_recognition.face_encodings(frame, [(top, right, bottom, left)])
        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]

            # Compare o rosto com os rostos conhecidos
            resultados = face_recognition.compare_faces(list(conhecidos.keys()), face_encoding, tolerance=0.5)
            fontScale = 4
            if True in resultados:
                nome = conhecidos[list(conhecidos.keys())[resultados.index(True)]]
                # Exibir o nome da pessoa na imagem
                cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (255,255, 255), 5)
                print(f"Pessoa reconhecida detectada: {nome}")

    cv2.imshow("Reconhecimento de Rosto", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
