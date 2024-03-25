# ImageClassification

This project demonstrates how to classify images using the ImageNet dataset with a pre-trained MobileNetV2 model in Google Colab. It involves syncing your files with Google Drive for a streamlined workflow.

## Getting Started

To use this image classification project, you'll need to have a Google account and access to Google Colab.

### Prerequisites

- Google account
- Access to Google Colab

### Setting Up Your Google Drive

1. Create a folder in your Google Drive and name it `images-board`. This folder will contain the images you wish to classify.
2. Create another folder in your Google Drive named `sorted-images`. This folder will be used to store the classified images.

### Running the Script

1. Open Google Colab and sign in with your Google account.
2. Upload the `ImageClassification.py` script to your Colab workspace.
3. Mount your Google Drive by adding the following code to a new cell in your Colab notebook:

```python
from google.colab import drive
drive.mount('/content/drive')

Run the entire script. The script will automatically categorize the images in 'images-board' based on their predicted classes and move them to the 'sorted-images' folder, organized into subfolders by category.