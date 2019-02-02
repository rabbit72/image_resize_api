from PIL import Image

from celery import Celery

app = Celery('tasks', backend='redis://redis', broker='redis://redis')


@app.task
def add(x, y):
    return x + y

# def resize_image(image: bytes):
#     # args = get_args()
#     error = check_args(args)
#     if error:
#         exit(error)
#     path_to_img = args.path_to_img
#     dir_for_save = args.output
#     image = Image.open(path_to_img)
#     size_for_new_file = get_size_for_new_img(image.size, args)
#     if get_ratio(image.size) != get_ratio(size_for_new_file):
#         print('A new proportion of the image is different from the original')
#     resized_img = image.resize(size_for_new_file)
#     path_for_save = get_path_for_save(path_to_img, dir_for_save, size_for_new_file)
#     resized_img.save(path_for_save)
