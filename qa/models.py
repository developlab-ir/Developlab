from django.db import models
from django.urls import reverse


class Question(models.Model):
    Types = (
        ("programing","برنامه نویسی"),
        ("technical","فنی"),
        ("general","عمومی"),
    )
    title = models.CharField(verbose_name="موضوع",max_length=110)
    type = models.CharField(verbose_name="مدل سوال",max_length=110,choices=Types)
    description = models.TextField(verbose_name="توضیحات")

    user = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE)
    is_active = models.BooleanField("فعال", default=True)
    solved = models.BooleanField("حل شده", default=False)
    is_pin = models.BooleanField("ویژه", default=False)
    write_date = models.DateTimeField("تاریخ مطرح شدن", auto_now_add=True)

    solve_date = models.DateTimeField("تاریخ حل شدن", blank=True, null=True)

    class Meta:
        db_table = "questions"
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse("qa:question-detail", kwargs={"pk": self.id})

class Answer(models.Model):
    description = models.TextField(verbose_name="توضیحات")

    user = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    is_active = models.BooleanField("فعال", default=True)
    is_best = models.BooleanField("بهترین پاسخ", default=False)
    
    write_date = models.DateTimeField("تاریخ مطرح شدن", auto_now_add=True)

    class Meta:
        db_table = "answers"
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"

    def __str__(self):
        description_length = len(self.description)
        if description_length >= 40:
            return f"{self.description[:40]}..."
        return self.description
