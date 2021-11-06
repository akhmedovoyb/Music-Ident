import acrcloud
import sounddevice
from scipy.io.wavfile import write
fs = 44100
num2 = 8
while True:
	print("Music identification")
	print("Recording...")
	record=sounddevice.rec(int(num2*fs),samplerate=fs,channels=2)
	sounddevice.wait()
	write("output.mp3",fs,record)
	config = {
		"key": "6eb29864c1e4751e615adf592b677ffd",
		"secret": "4ycCghC1nRzqzJBVz4CN9EEzacPoOLusdjPDzBtq",
		"host": "identify-eu-west-1.acrcloud.com"
	} 
	audio = "output.mp3"
	acr = acrcloud.ACRcloud(config)
	audio = acr.recognize_audio(audio)
	if audio == {'status': {'code': 1001, 'msg': 'No result', 'version': '1.0'}}:
		print("No result")
	else:
		name = audio["metadata"]["music"][0]["title"]
		artists = audio["metadata"]["music"][0]["artists"][0]['name']
		print(f"Name: {name}")
		print(f"Artists: {artists}")
	yorn = input("Do you want to run an app again ? (yes-y, no-n): ")
	if yorn == "y":
		continue
	elif yorn=="n":
		break
	else:
		yorn = input("Do you want to run an app again ? (yes-y, no-n): ")
