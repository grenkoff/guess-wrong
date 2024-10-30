from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValueError("There is already an instance of this model.")
        return super().save(*args, **kwargs)


class HomePage(SingletonModel):
    domain = models.CharField(max_length=200, default="Default Domain")
    title = models.CharField(max_length=200, default="Default Title")
    name = models.CharField(max_length=200, default="Default Name")
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

    def __str__(self):
        return self.name

    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(id=1)
        return instance
