from django.db import models
from django.conf import settings
from random import randint


class Board(models.Model):
    ACCESS_STATUS = (
        (0, 'Открытая'),
        (1, 'Закрытая')
    )
    name = models.CharField(verbose_name='Название доски', max_length=50)
    access = models.IntegerField(verbose_name='Право', choices=ACCESS_STATUS, blank=True, default=0)
    user_righs_board = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='UserRightBoard')

    def __str__(self):
        return f"{self.name}"

    def random_pin(self):
        ret = None
        queryset = Pin.objects.all().filter(board=self.id)
        count = queryset.values_list('id')
        if(len(count)-1>0):
            queryset = queryset.filter(id = count[randint(0, len(count) - 1)][0]).first()
            ret = queryset.image
        return ret

class UserRightBoard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Права пользователя на доску'
        verbose_name_plural = 'Права пользователя на доску'


class PinCategory(models.Model):
    name_category = models.CharField(verbose_name='Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категории пинов'
        verbose_name_plural = 'Категории пинов'

    def __str__(self):
        return f"{self.name_category}"


class Pin(models.Model):
    name = models.CharField(verbose_name='Название пина',max_length=50)
    description = models.TextField(verbose_name='Описание',null=True, blank=True)
    image = models.FileField(verbose_name='Изображение', upload_to="images", editable=True)
    upload_date = models.DateTimeField(verbose_name='Дата загрузки пина')
    category = models.ManyToManyField(to=PinCategory, verbose_name='Категория')
    board = models.ManyToManyField(to=Board, through='BoardPin')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Пины'
        verbose_name_plural = 'Пины'

    def __str__(self):
        return f"{self.name} {self.category}"

class BoardPin(models.Model):
    pin = models.ForeignKey(to=Pin, verbose_name='Картинка', on_delete=models.CASCADE)
    board = models.ForeignKey(to=Board,verbose_name='Доска', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь пинов с доской'
        verbose_name_plural = 'Связь пинов с доской'

    def __str__(self):
        return f"{self.pin.name} {self.board.name}"