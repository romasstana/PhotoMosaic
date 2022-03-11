import numpy as np
import argparse
import cv2
import glob
from itertools import product


def settings():
    parser = argparse.ArgumentParser("Homework 1")
    parser.add_argument("--input", type=str, default="/Users/ramazansakenov/Desktop/image_assignment1/mainpart/input_orig.jpg")
    parser.add_argument("--output", type=str, default="/Users/ramazansakenov/Desktop/image_assignment1/mainpart/output.jpg")
    parser.add_argument("--pool", type=str, default="/Users/ramazansakenov/Desktop/image_assignment1//mainpart/tiles")
    parser.add_argument("--stride", type=int, default=10)
    args = parser.parse_args()
    return args


def get_settings(path, size):
    images = []
    average_colors = []
    for image_path in glob.glob("{}/*.jpg".format(path)):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (size, size))
        images.append(image)
        average_colors.append(np.sum(np.sum(image, axis=0), axis=0) / (pow(size,2)))
    return images, np.array(average_colors)


def main(option):
    input_image = cv2.imread(option.input, cv2.IMREAD_COLOR)
    height, width, num_channels = input_image.shape
    blank_image = np.zeros((height, width, 3), np.uint8)
    images, average_colors = get_settings(option.pool, option.stride)
    for i, j in product(range(int(width / option.stride)), range(int(height / option.stride))):
        partial_input_image = input_image[j * option.stride: (j + 1) * option.stride,i * option.stride: (i + 1) * option.stride, :]
        partial_average_color = np.sum(np.sum(partial_input_image, axis=0), axis=0) / (pow(option.stride,2))
        distance_matrix = np.linalg.norm(partial_average_color - average_colors, axis=1)
        idx = np.argmin(distance_matrix)
        blank_image[j * option.stride: (j + 1) * option.stride, i * option.stride: (i + 1) * option.stride, :] = images[idx]
    cv2.imwrite(option.output, blank_image)


if __name__ == '__main__':
    option = settings()
    main(option)
