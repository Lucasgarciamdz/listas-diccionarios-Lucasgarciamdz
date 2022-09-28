FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/listas-diccionarios-Lucasgarciamdz.git
WORKDIR listas-diccionarios-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]