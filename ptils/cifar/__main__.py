""" Main and Console hooks for examining cifar10 """

from io import SEEK_CUR
import sys

# import argparse
from importlib import resources

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Make dataclass when you have time TODO:
LABEL_SIZE = 1
DATA_SIZE = 3072
CHUNK_SIZE = 3073  # LABEL_SIZE + DATA_SIZE
BATCH_FILE_SIZE = 30730000  # CHUNK_SIZE * 10000
BATCH_DATA_SIZE = 30720000  # All Data without labels
CIFAR10_SHAPE = (32, 32, 3)


#TODO: Do somethin proper later
def main():
    data_batch1 = resources.files("ptils.cifar.data").joinpath("data_batch_1.rgb")

    # data_arr = bytearray(BATCH_DATA_SIZE)
    data_arr = bytearray()
    data_added = 0
    # Annoying to have double with but is this better than reading all at once?
    with resources.as_file(data_batch1) as data_file:
        with open(data_file, mode="rb") as f:
            # finally get to use walrus op :)
            while label := f.read(LABEL_SIZE):
                if label != b"\x03":
                    f.seek(DATA_SIZE, SEEK_CUR)
                else:

                    # data_arr[data_added*DATA_SIZE:
                    data_arr.extend(f.read(DATA_SIZE))
                    data_added += 1

    # for i in range(data_added):
    #     img_stream = data_arr[i*DATA_SIZE:(i+1)*DATA_SIZE]
    #     img = np.array(img_stream).reshape(32,32,3)
    #     print(i)
    #     plt.imshow(img)
    #     plt.show()

    img_stream = data_arr[39 * DATA_SIZE : 40 * DATA_SIZE]
    img = np.array(img_stream).reshape(CIFAR10_SHAPE)
    im = Image.fromarray(img)
    im.save("cifar10_example_cat_image.png")

    return 0


if __name__ == "__main__":
    sys.exit(main())
