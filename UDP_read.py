import socket

# 수신에 사용할 IP 주소와 포트 번호 설정
UDP_IP = "192.168.1.105"  # 여기에 수신할 IP 주소를 입력하세요
UDP_PORT = 6666  # 여기에 수신할 포트 번호를 입력하세요

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP 서버가 {UDP_IP}:{UDP_PORT}에서 실행 중입니다.")

try:
    while True:
        # 데이터 수신
        data, addr = sock.recvfrom(1024)
        print(f"수신된 데이터: {data.decode('utf-8')} (from {addr[0]}:{addr[1]})")
except KeyboardInterrupt:
    print("서버를 종료합니다.")
finally:
    sock.close()
