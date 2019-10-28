# socketMonitor

Carregar conteiner na máquina do server

(usando a rede do docker no próprio host)

docker run -it -mateusmantoan/socketserver:1.0

(usando a rede local em diferentes hosts)
docker run -it --network host mateusmantoan/socketserver:1.0

Baixar programa do client nas máquinas client

git clone https://github.com/mateusmantoan/socketMonitor
cd socketMonitor
python socketClient.py
