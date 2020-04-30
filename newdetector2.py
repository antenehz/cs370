import boto3
import os

#create files here


def detect_emotions(photo):
	client = boto3.client('rekognition')

	with open(photo, 'rb') as image:
        	response = client.detect_faces(Image={'Bytes': image.read()}, Attributes = ['ALL'])

	con = 0
	emo = ''
	for face in response['FaceDetails']:
		for emotion in face['Emotions']:
			if(con < emotion['Confidence']):
				con = emotion['Confidence']
				if(emotion['Type'] == 'HAPPY' or emotion['Type'] == 'SAD'):
					emo = emotion['Type']
	if emo =='':
		emo = 'HAPPY'
	f = open("emotion.txt", "w+")
	f.write(emo)		
def main():
	photo = '/home/pi/pi-detector/faces/image.jpg'
	detect_emotions(photo)
	os.system("python userTopTracks1.py hi")

if __name__ == '__main__':
    main()
