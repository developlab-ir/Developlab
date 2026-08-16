from django.db import models
from django.utils.timezone import now
from django.urls import reverse


def post_thumbnail_upload_path(instance,filename):
    username = instance.author.username or "new-post"
    return f"blog/post/{username}/{now().strftime("%d-%H-%M-%S")}/{filename}"
    

class Post(models.Model):

    title = models.CharField(verbose_name="موضوع",max_length=120)
    summary = models.TextField(verbose_name="خلاصه",blank=True,null=True)
    description = models.TextField(verbose_name="توضیحات")

    thumbnail = models.ImageField(verbose_name="تصویر شاخص",upload_to=post_thumbnail_upload_path)

    is_active = models.BooleanField(verbose_name="فعال",default=True)

    write_at = models.DateTimeField(auto_now_add=True,verbose_name="نوشته شده در")
    update_at = models.DateTimeField(auto_now=True,verbose_name="ویرایش شده در")

    author = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE,verbose_name="نویسنده")

    class Meta:
        db_table = "post"
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.id})

class Comment(models.Model):
    Statuses = (
        ("delete","حذف شده"),
        ("in_review","در حال بررسی"),
        ("okay","مورد تایید"),
    )
    description = models.TextField(verbose_name="توضیحات")

    reply_to = models.ForeignKey("self",on_delete=models.CASCADE,verbose_name="نسبت به",blank=True,null=True,related_name='replies')
    writer = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE,verbose_name="نویسنده")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="پست")

    status = models.CharField(verbose_name="وضعیت",choices=Statuses,max_length=20,default="in_review")
    is_pin = models.BooleanField(verbose_name="سنجاق شده",default=False)

    write_at = models.DateTimeField(auto_now_add=True,verbose_name="نوشته شده در")

    class Meta:
        db_table = "comment"
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        description_length = len(self.description)
        if description_length >= 40:
            return f"{self.description[:40]}..."
        return self.description

