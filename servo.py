import sys
import paho.mqtt.client as mqtt
from pymata4 import pymata4

board = pymata4.Pymata4()


# 아두이노 핀 번호와 서보모터 초기 각도
board.set_pin_mode_servo(9)
servo_angle = 0

# MQTT 메시지를 받았을 때 실행되는 콜백 함수
def on_message(client, userdata, message):
    global servo_angle
    
    # MQTT로부터 받은 메시지로 서보모터 각도 변경
    servo_angle = int(message.payload.decode())
    board.servo_write(9, servo_angle)

# MQTT 클라이언트 생성 및 연결
client = mqtt.Client()
client.connect('localhost', 1883)

# 구독 시작
client.subscribe('servo', 1)

# MQTT 메시지를 처리하는 루프 실행
client.on_message = on_message
client.loop_forever()