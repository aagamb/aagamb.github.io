I tried to create a program which when prompted with an instagram image will be able to make a caption for it.
The program took 10 days to create, but yielded an unsuccesful result.
The main flaw of the program may be: 
  It uses the VGG16 classifier which generates a large number of features per picture (4096 features) in its last layer. 
  Or there is too little data, just about 600 images. (The dataset originally contained 9000 images, but due to computational restrictions, only 600 were taken randomly.)
The length of the text (max 500 chars) was appended to this and then inserted into training
I believe that the features extracted from the image overpowered the sequences of text which was appended to it during training.

The dataset used for the project is available here: https://www.kaggle.com/prithvijaunjale/instagram-images-with-captions
I had initially used the entire dataset, but due to system restrictions took a smaller batch of about 600 images only. 
This is because the original dataset took about 3 hours to complete 1 epoch, hence a smaller batch from the dataset was taken.

