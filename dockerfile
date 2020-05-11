FROM python:3.6
  WORKDIR /usr/src/work
  ADD ./work /usr/src/work
  ADD ./data /usr/src/data
  RUN pip install --upgrade pip
  RUN pip install -r requirements.txt
  RUN pip install -U ckiptagger[tf,gdown]
  RUN mkdir /usr/src/vol
  VOLUME result:/usr/src/vol
  CMD ["python","tagger.py"]
