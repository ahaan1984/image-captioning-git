# Image Captioning for Chest X-Ray Images 

This project focuses on fine-tuning the Microsoft GenerativeImage2Text model for the specific task of generating captions for radiology images, particularly Chest X-Ray images.

## Project Overview

The goal of this project is to finetune a pre-existing multimodal model (Microsoft GenerativeImage2Text or GIT, in this case) to make it capable of generating accurate and descriptive captions for radiology images. This can potentially assist radiologists by providing initial impressions of the images.

## Installation

To set up this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Data

The project uses the ROCO (Radiology Objects in COntext) dataset. The data is expected to be organized in the following structure:

```
dataset/
    roco-dataset/
        all_data/
            train/
                radiologytraindata.csv
            test/
                radiology/
                    testdata.csv
                    images/
```

## Usage

The main notebook for training the model is `main.ipynb`. This Jupyter notebook contains the entire pipeline from data loading to model training and evaluation.

To run the notebook:

1. Ensure you have Jupyter installed
2. Navigate to the project directory
3. Run `jupyter notebook`
4. Open `main.ipynb`

## Model

The project uses the Microsoft GenerativeImage2Text model, which is a multi-modal model capable of generating text descriptions from images. The model is fine-tuned on the radiology dataset to specialize in captioning medical images.

## Training

The training process involves:

1. Loading and preprocessing the data
2. Initializing the pre-trained model
3. Fine-tuning the model on the radiology dataset
4. Evaluating the model's performance

The training progress is logged using Weights & Biases (wandb).

## Results

The model's performance is evaluated by generating captions for a set of test images and visualizing the results. The notebook includes code to display a grid of images along with their generated captions.
