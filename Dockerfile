FROM ubuntu:18.04

RUN apt-get update && apt-get install nginx -y && apt-get upgrade -y
RUN apt-get install build-essential
# Baixando o pip e outros
RUN apt-get install -y python3.7 \
                    python3-pip \
                    python-dev \
                    apt-utils
# Baixa o DeepSpeech (Verifique se não há uma versão mais recente)
RUN git clone https://github.com/mozilla/DeepSpeech --branch v0.7.4
# Instala uns necessários
RUN pip3 install --upgrade pip==20.0.2 wheel==0.34.2 setuptools==46.1.3
#
RUN cd DeepSpeech
# Instala as depêndencias do DeepSpeech
RUN pip3 install --upgrade -e .
# Troca para a versão acelerada com GPU
RUN pip3 uninstall tensorflow
RUN pip3 install 'tensorflow-gpu==1.15.2'
#
RUN apt-get install sox libsox-fmt-mp3
# Baixa o Dataset (Verifique se não há uma versão mais recente no Mozilla Common Voice)
RUN wget https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-7.0-2021-07-21/cv-corpus-7.0-2021-07-21-pt.tar.gz
# Extrai o dataset
RUN tar xvzf cv-corpus-10.0-2022-07-04-pt.tar.gz
# Converte as tabelas de transcrições e cria os arquivos wav
RUN bin/import_cv2.py cv-corpus-7.0-2021-07-21/pt
# Baixa a biblioteca para limpeza ddo texto das falas
RUN git clone https://github.com/wlfoj/train-DeepSpeech-Docker.git
# Realiza o tratamento das falas
RUN cd train-DeepSpeech-Docker
#
CMD bash
