# socketMonitor

\Carregar conteiner na máquina do server

(using the docker network on the same host)

docker run -it -mateusmantoan/socketserver:1.0

(using the local network on different hosts)

docker run -it --network host mateusmantoan/socketserver:1.0


\Baixar programa do client nas máquinas client

git clone https://github.com/mateusmantoan/socketMonitor
