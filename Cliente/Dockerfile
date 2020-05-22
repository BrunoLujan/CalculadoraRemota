FROM ubuntu:20.04
COPY . ./Cliente
WORKDIR /Cliente
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install thrift
EXPOSE 8080
CMD ["python3", "CalculadoraRemotaCliente.py"]