import socket

# 수신 서버의 IP 주소와 포트 번호 설정
UDP_IP = "192.168.1.105"  # 수신 서버의 IP 주소를 입력하세요
UDP_PORT = 6666  # 수신 서버의 포트 번호를 입력하세요

# 전송할 데이터
message = "Hello, UDP Server!"
data = message.encode('utf-8')

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # 데이터 전송
    sock.sendto(data, (UDP_IP, UDP_PORT))
    print(f"데이터를 {UDP_IP}:{UDP_PORT}로 전송했습니다: {message}")
finally:
    sock.close()
