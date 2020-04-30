import boto3

#create files here


def detect_emotions(photo):
	client = boto3.client('rekognition')

	with open(photo, 'rb') as image:
        	response = client.detect_faces(Image={'Bytes': image.read()}, Attributes = ['ALL'])

	con = 0
	emo = {}
	for face in response['FaceDetails']:
		for emotion in face['Emotions']:
			if(con < emotion['Confidence']):
				con = emotion['Confidence']
				if(emotion['Type'] == 'HAPPY' or emotion['Type'] == 'SAD'):
					emo = emotion['Type']
			#Maddies code goes here that writes emotions to files
			#print"  {Type} : {Confidence}%".format(**emotion)

	f = open("emotion.txt", "w+")
	f.write(emo)		
def main():
	photo = '/home/pi/pi-detector/faces/smile.jpeg'
	detect_emotions(photo)

if __name__ == '__main__':
    main()
