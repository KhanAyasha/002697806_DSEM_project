# Glaucoma detector ML APP

## About Glaucoma

Glaucoma is a group of eye conditions that damage the optic nerve, which is essential for good vision, often due to high pressure in the eye. It's a leading cause of blindness worldwide. While ongoing studies seek medical interventions to halt or prevent glaucoma progression, early detection remains paramount. Detecting the condition in its early stages allows for interventions aimed at slowing its advancement. Regular eye examinations play a vital role in diagnosing glaucoma and averting vision loss.

Within the retina, the cup region is encircled by the retinal disc. When the retinal disc's radius expands to the extent that the ratio of cup radius to disc radius equals or exceeds 33.33%, it indicates recognizable glaucoma or a Glaucomatous Eye.

![Untitled design](https://github.com/KhanAyasha/002697806_DSEM_assignments-/assets/144647351/07249e32-1688-4141-bf1e-ce75c446b8a1)

ratio = r / R >= 33.33% Ratina could be impacted with Glaucoma.

## Model
View CNN model architecture 

![alt text](<CNN Model.png>)


## Web Page

![alt text](Webpage.png)

## Healthy Eye or Non-Referable Glaucoma which does not need doctor's consultation

![alt text](Healthy-eye.png)

## Referable Glaucoma or Glaucomatous Eye

![alt text](Unhealthy-eye.png)


# Details

## About Dataset
* Collected all the publicly available labelled(RG and NRG) retinal scan of eye from Kaggle.
* Dataset is available: https://www.kaggle.com/datasets/deathtrooper/glaucoma-dataset-eyepacs-airogs-light-v2/data
* Images are full retinal scan of eye. So, we cropped the full fundus images too. See below.
* The dataset is divided into 3 parts: train, test, and validation set.
* These sets are in the approximate ratio of 21:2:2 or 4000 (~84%), 385 (~8%), and 385 (~8%) for train, test, and validation sets.
* Finally, sticked with 9540 total images with 4770 images in each classes.

![alt text](<full to cropped.jpg>)

## About model
* Saved all these images to my local system and trained on various CNN architectures from simple to advanced.
* Augmentated data using keras ImageGenerator to cut down high variance. But there is some bias due to low and bad data.
* Used keras (3.2.1) and tesorflow (2.16.1) on top of python (3.11.5).
* Trained on train set and validated on validation set after each epoch. Finally tested the test set.
* It gave 93 percent AUC score, some good accuracy, precision and recall values. We saved the model file(h5) for further usage.
* Then, built a simple streamlit app for hosting on web.


# How to use this app: 

To use this project - Here: https://glaucoma-detection-app.streamlit.app/

(or)

To run this app

```
pip install -r requirements.txt
streamlit run https://glaucoma-detection-app.streamlit.app/
```

(or)

To run our glaucoma detector on your machine by cloning this repository,
* Type the following in your terminal or cmd:
```
pip install -r requirements.txt
streamlit run glaucoma_app.py
```
* The web app opens up in a local host. Then you can use it for classifying. That's it!

* Upload a (jpg) cropped fundus image of eye(if not cropped, see above). Our model predicts whether affected by glaucoma or not.
* I provided two folders NRG and RG. These contain images from my test set. Use these if you don't have any fundus images with you.

Note: The image should be cropped around the optic nerve part.

# Future Improvement

The convolutional layers are crucial for extracting key features from images, but their effectiveness can be influenced by image quality and noise. However, the primary focus of this model is the retinal ratio (r/R), specifically the ratio of cup radius to disc radius. This feature holds paramount importance for the task at hand.

We can modify the CNN architecture to prioritize the extraction and utilization of this feature. 

To prioritize the retinal ratio feature in CNN models, we can enhance image quality through preprocessing like contrast enhancement and edge detection. We can add a custom layer to calculate cup-to-disc radius ratio directly. Fuse this feature with existing ones via techniques like concatenation. Optimize model performance with a custom loss function penalizing deviation from the desired ratio. 

We can also assess the model's ability to predict this feature alongside traditional metrics during validation and testing. This ensures the model extracts and prioritizes crucial information, enhancing its relevance to the task at hand.
