import paho.mqtt.client as mqtt
import ssl

MQTT_BROKER = "test.mosquitto.org"
PORT = 8883
TOPIC = "iot/secure_updates"

client = mqtt.Client()
client.tls_set(ca_certs="ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(MQTT_BROKER, PORT)

# Publish encrypted data
client.publish(TOPIC, payload=ciphertext.hex())

