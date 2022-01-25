import hashlib
from django.db import models
from core.function_for_resize.utils import func_resize_picture


class Picture(models.Model):
    pic_name = models.CharField(max_length=25, blank=False, null=False)
    pic_format = models.CharField(max_length=5)
    uploaded_picture = models.ImageField(blank=False, null=False, unique=True, upload_to='media/')
    width = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.pic_name

    def save(self, **kwargs):
        resized_pic, self.width, self.height = func_resize_picture(
            self.uploaded_picture, self.width, self.height
        )
        self.uploaded_picture = f'{(hashlib.md5(self.pic_name.encode())).hexdigest()}_{self.width}x' \
                                f'{self.height}.{self.pic_format}'
        super().save(**kwargs)
        resized_pic.save(self.uploaded_picture.path)
