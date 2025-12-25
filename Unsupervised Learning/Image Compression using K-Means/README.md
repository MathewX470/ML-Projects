# Image Compression using K-Means

An implementation of image compression using the K-Means clustering algorithm to reduce the color palette of images while maintaining visual quality.

## Overview

This project demonstrates how unsupervised machine learning can be applied to image compression by reducing the number of unique colors in an image. K-Means clustering groups similar pixel colors together, replacing them with cluster centroids to achieve compression.

## Features

- 📉 Reduces image color palette from millions to K colors
- 📊 Side-by-side comparison of original vs compressed images
- 💾 Displays file size reduction metrics
- 🎨 Maintains visual quality with K=32 clusters

## Requirements

```bash
numpy
matplotlib
scikit-learn
scikit-image
```

## Installation

```bash
pip install numpy matplotlib scikit-learn scikit-image
```

## Usage

1. Place your image file (e.g., `image.jpg`) in the project directory
2. Open and run `image_compression_using_k_means.ipynb`
3. Compressed image will be saved to `output/compressed_k_32.jpg`

## How It Works

1. **Load Image**: Read the input image as a NumPy array
2. **Reshape**: Convert 3D image array (H×W×3) to 2D (pixels×3)
3. **Normalize**: Scale pixel values from [0, 255] to [0, 1]
4. **K-Means Clustering**: Group pixels into K=32 color clusters
5. **Compress**: Replace each pixel with its cluster center color
6. **Save**: Export compressed image and compare file sizes

## Results

- **Original Colors**: ~16.7 million possible colors
- **Compressed Colors**: 32 representative colors
- **Trade-off**: Smaller file size vs. slight quality reduction

## Parameters

- `k = 32`: Number of color clusters (adjustable)
  - Lower K = more compression, lower quality
  - Higher K = less compression, higher quality

## Example Output

The notebook generates:
- Original image visualization
- Compressed image saved to `output/` directory
- File size comparison statistics
- Side-by-side comparison plot

## License

This project is open source and available under the MIT License.

## Author

MathewX470
