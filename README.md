# Road Safety: Detection & Mitigation of Rain, Haze, and Fog using OpenCV

A computer vision pipeline that enhances image visibility under adverse weather conditions (rain, haze, fog), integrated into a Django web application for real-time object detection.

## Overview

Poor visibility caused by haze, fog, and rain significantly degrades the performance of vision-based systems such as autonomous driving and surveillance. This project implements an image enhancement pipeline that restores visibility in degraded images before passing them to an object detection stage, improving downstream detection reliability.

## Techniques Used

- **Dark Channel Prior (DCP)** — estimates and removes haze based on the observation that haze-free outdoor images typically contain very dark pixels in at least one color channel within local patches.
- **Guided Filtering** — refines the transmission map produced by DCP, smoothing noise while preserving sharp edges that a raw DCP estimate tends to blur or blocky-fy.
- **CNN-based Parameter Tuning** — adaptively tunes color and brightness restoration parameters per image using a convolutional neural network, rather than relying on fixed, manually chosen parameters that don't generalize well across varying weather/lighting conditions.

## Architecture

- **Backend:** Django web application (`RainHazeFogDetection`)
- **Core Pipeline:** `RainHazeFog/object_detection` — handles image enhancement and object detection
- **Object Detection:** Real-time detection applied to enhanced output

## Evaluation

Enhancement quality was evaluated using standard, objective image quality metrics rather than visual inspection alone:

- **PSNR (Peak Signal-to-Noise Ratio)** — measures pixel-level fidelity relative to a reference
- **SSIM (Structural Similarity Index)** — measures perceptual/structural similarity relative to a reference

These metrics were used to compare enhancement techniques, identify failure modes, and determine the most reliable method for downstream object detection.

## Tech Stack

- Python
- OpenCV
- Django
- CNN (deep learning-based parameter tuning)

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd RainHazeFogDetection

# Install dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py runserver
```

## Project Structure

```
RainHazeFog/
└── object_detection/
    └── RainHazeFogDetection/   # Django project
```

## Motivation

This project was developed to explore how classical computer vision techniques (Dark Channel Prior, guided filtering) can be combined with deep learning (CNN-based tuning) to improve image quality in real-world adverse weather conditions, with applications in surveillance and autonomous navigation.
