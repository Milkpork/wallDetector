from django.db import models


class DetectDetails(models.Model):
    recode_time = models.CharField(verbose_name="记录的时间", max_length=14)  # 20020101162334
    record_details = models.CharField(verbose_name="记录", max_length=128)

