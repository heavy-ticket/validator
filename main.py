from dataset import Dataset
import matplotlib.pyplot as plt


def plot_bboxes(image, bboxes):
    img = image.copy()
    for bbox in bboxes:
        img = bbox.plot(img)
    return img


dataset = Dataset('../cave_annotations')
image, bboxes = dataset.load_dataset_train_item('cave_025.bmp')
img = plot_bboxes(image, bboxes)
plt.imshow(img)
plt.show()
