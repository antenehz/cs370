CS370-Project
Term project for Operating Systems course (CS 370, Spring 2020) consisting of a group of 4.
Overview:
Our project’s objective is to develop an intelligent music player that recognizes human emotions. It will take an image from a camera when a sensor is triggered. Then, a song will play corresponding to the person's emotion/mood. An example of this would be if a person is smiling then the song Happy by Will Farrell will be played. We plan on using PyTorch to create an image classifier that recognizes different human emotions.

Emotion detecting:
We’ll be using Amazon SageMaker (Amazon’s machine learning service) using AWS Python SDK (API that will give us access to AWS services) with our PyTorch model to do all the training with so that we’ll be able to detect the emotion of a person and then play the song that they’re in the mood for.

Music:
We’ll be using Volumio, a software dedicated to be a music player that will play any file type, can be connected to spotify & downloaded onto a raspberry pi. It will require a SD Card & we’ll be attaching a speaker to the raspberry pi to output the music once emotion is detected.

We want to start off by utilizing spotify’s web API which allows us to get audio analysis of a track and we can use the tempo of a song to determine if it’s happy or sad. We’ll be parsing through the user’s playlists on spotify so that it doesn’t play a random song the user hasn’t heard before.

Autonomous Camera:
We’ll be using a sensor to detect when an individual is at a certain proximity from it and take a picture.The picture will then be uploaded and processed.
