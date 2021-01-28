FROM alpine
RUN apk add python3
RUN apk add sqlite
COPY /BancoServicios.py /
COPY /alcohlesserveudp.py /
COPY /Alcoholes /
COPY /AlcoholStore.py /
COPY /bancoserverudp.py /
COPY /base_datos.py /
COPY /clientes_banco /
COPY /clientes_licoreria /
COPY /objetos.py /
COPY /pro.py /
