from PIL import Image


def func_resize_picture(file, width, height):
    pic = Image.open(file)
    pic_width, pic_height = pic.size
    if height is None:
        pic_height = pic_height // (pic_width // width)
        height = pic_height
    elif height < pic_height:
        pic_height = height
    if width < pic_width:
        pic_width = width
    output_size = (pic_width, pic_height)
    pic_resized = pic.resize(output_size, Image.ANTIALIAS)
    return pic_resized, width, height
