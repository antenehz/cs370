import boto3

#create files here


def detect_emotions(photo):
	client = boto3.client('rekognitions')

	with open(photo, 'rb') as image:
        	response = client.detect_faces(Image={'Bytes': image.read()}, Attributes = ['ALL'])
	
	for emotion in response['Emotion']:
		#Maddies code goes here that writes emotions to files
	


def main():
	photo = '/home/pi/pi-detector/faces/image.jpg'
	response = detect_emotions(photo)
	print(response)

if __name__ == '__main__':
    main()
