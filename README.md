# Reconhecimento Facial com Python

## Introdução - Introduction
Projeto Python para reconhcer pessoas na webCam.

## Dependências - Dependencies
pip list
Package                 Version
----------------------- -----------
*absl-py                 2.1.0
*astunparse              1.6.3
*beautifulsoup4          4.12.3
*blinker                 1.8.2
*certifi                 2024.7.4
*charset-normalizer      3.3.2
*click                   8.1.7
*deepface                0.0.92
*dlib                    19.24.4
*face-recognition        1.3.0
*face_recognition_models 0.3.0
*filelock                3.15.4
*fire                    0.6.0
*Flask                   3.0.3
*flatbuffers             24.3.25
*gast                    0.6.0
*gdown                   5.2.0
*google-pasta            0.2.0
*grpcio                  1.64.1
*gunicorn                22.0.0
*h5py                    3.11.0
*idna                    3.7
*itsdangerous            2.2.0
*Jinja2                  3.1.4
*keras                   3.4.1
*libclang                18.1.1
*Markdown                3.6
*markdown-it-py          3.0.0
*MarkupSafe              2.1.5
*mdurl                   0.1.2
*ml-dtypes               0.3.2
*mtcnn                   0.1.1
*namex                   0.0.8
*numpy                   1.26.4
*opencv-python           4.10.0.84
*opencv-python-headless  4.10.0.84
*opt-einsum              3.3.0
*optree                  0.12.1
*packaging               24.1
*pandas                  2.2.2
*pillow                  10.4.0
*pip                     24.1.2
*protobuf                4.25.3
*Pygments                2.18.0
*PySocks                 1.7.1
*python-dateutil         2.9.0.post0
*pytz                    2024.1
*requests                2.32.3
*retina-face             0.0.17
*rich                    13.7.1
*setuptools              70.2.0
*six                     1.16.0
*soupsieve               2.5
*tensorboard             2.16.2
*tensorboard-data-server 0.7.2
*tensorflow              2.16.2
*termcolor               2.4.0
*tf_keras                2.16.0
*tqdm                    4.66.4
*typing_extensions       4.12.2
*tzdata                  2024.1
*urllib3                 2.2.2
*Werkzeug                3.0.3
*wheel                   0.43.0
*wrapt                   1.16.0

## Instalação - Installation

Primeiro, clone o repositório - First, clone the repository:
```
git clone https://github.com/Macelot/python-face-recognition
```

Entre no diretório do projeto - Enter the project directory:
```
cd python-face-recognition
```

Crie o ambiente Python - Create the Python environment:
```
python3 -m venv venv

Ative o ambiente - Activate environment
win
.\venv\Scripts\activate 
Mac Linux
source ./venv/bin/activate
```


Instalar dependências - Install dependencies:
```
pip3 install opencv-python-headless 
pip install --upgrade pip
pip3 install face_recognition
pip3 install git+https://github.com/ageitgey/face_recognition_models
pip3 install --upgrade setuptools wheel
pip3 install dlib numpy
pip3 cache purge
pip3 install deepface
pip3 install tf-keras
```

Criar o diretório "pessoas" e colocar algumas fotos PNG das pessoas que deseja reconhecer

Rodar o projeto - Run project
```
python3 reconhecimento_facial.py
```
