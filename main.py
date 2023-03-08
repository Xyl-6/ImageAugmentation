import os
import cv2
from my_utils.change import *
from my_utils.blur import *
from my_utils.brighten import *
from my_utils.sharpen import *
from my_utils.cutout import *
from my_utils.flip import *


if __name__ == '__main__':
    # input_img_dir = './raw_images/changed_imgs'
    # input_label_dir = './raw_images/changed_labels'
    # save_img_dir = './aug_images/images'
    # save_label_dir = 'aug_images/labels'
    raw_img_dir = './raw_images/images'
    save_img_dir = './raw_images/changed_imgs'
    raw_label_dir = './raw_images/labels'
    save_label_dir = './raw_images/changed_labels'

    change(raw_img_dir, save_img_dir, raw_label_dir, save_label_dir)

    img_list = os.listdir(save_img_dir)
    for index, img_name_with_extension in enumerate(img_list, 1):
        name = os.path.splitext(img_name_with_extension)[0]

        input_img_dir = './raw_images/changed_imgs'
        input_label_dir = './raw_images/changed_labels'
        save_img_dir = './aug_images/images'
        save_label_dir = 'aug_images/labels'

        blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        gussian_blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        sharpen(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        brighten(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        cutout(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip1(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip2(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip3(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip4(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip5(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)








