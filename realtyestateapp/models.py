from django.db import models

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    period = models.CharField('Период рождения', blank=True, max_length=100)
    period1 = models.CharField('Влияние: ', blank=True, max_length=200) #вставки
    period2 = models.CharField('Символы: ', blank=True, max_length=200)
    period3 = models.CharField('Цвета:', blank=True, max_length=200)
    period4 = models.CharField('Камни:', blank=True, max_length=200)
    period5 = models.CharField('Металл:', blank=True, max_length=200)
    period6 = models.CharField('Талисман:', blank=True, max_length=200)
    period7 = models.CharField('Благоприятные числа:', blank=True, max_length=200)





    text = models.TextField('Начало статьи')

    pub_date = models.DateTimeField('Дата публикации')
    image = models.ImageField(verbose_name='Изображение', upload_to='media/', null=True, blank=True)

    text1 = models.TextField('Продолжение статьи 1', blank=True)
    text2 = models.TextField('Продолжение статьи 2', blank=True)

    image2 = models.ImageField(verbose_name='Изображение в середине статьи', upload_to='media/', null=True, blank=True)

    text3 = models.TextField('Продолжение статьи 3', blank=True)
    text4 = models.TextField('Продолжение статьи 4', blank=True)
    text5 = models.TextField('Продолжение статьи 5', blank=True)
    text6 = models.TextField('Продолжение статьи 6', blank=True)
    text7 = models.TextField('Продолжение статьи 7', blank=True)
    text8 = models.TextField('Продолжение статьи 8', blank=True)
    text9 = models.TextField('Продолжение статьи 9', blank=True)
    text10 = models.TextField('Продолжение статьи 10', blank=True)
    text11 = models.TextField('Продолжение статьи 11', blank=True)
    text12 = models.TextField('Продолжение статьи 12', blank=True)
    text13 = models.TextField('Продолжение статьи 13', blank=True)
    text14 = models.TextField('Продолжение статьи 14', blank=True)
    text15 = models.TextField('Продолжение статьи 15', blank=True)
    text16 = models.TextField('Продолжение статьи 16', blank=True)
    text17 = models.TextField('Продолжение статьи 17', blank=True)
    text18 = models.TextField('Продолжение статьи 18', blank=True)
    text19 = models.TextField('Продолжение статьи 19', blank=True)
    text20 = models.TextField('Продолжение статьи 20', blank=True)
    text21 = models.TextField('Продолжение статьи 21', blank=True)
    text22 = models.TextField('Продолжение статьи 22', blank=True)
    image1 = models.ImageField(verbose_name='Изображение в середине статьи', upload_to='media/', null=True, blank=True)
    text23 = models.TextField('Продолжение статьи 23', blank=True)
    text24 = models.TextField('Продолжение статьи 24', blank=True)
    text25 = models.TextField('Продолжение статьи 25', blank=True)
    text26 = models.TextField('Продолжение статьи 26', blank=True)
    text27 = models.TextField('Продолжение статьи 27', blank=True)
    text28 = models.TextField('Продолжение статьи 28', blank=True)
    text29 = models.TextField('Продолжение статьи 29', blank=True)
    text30 = models.TextField('Продолжение статьи 30', blank=True)
    text31 = models.TextField('Продолжение статьи 31', blank=True)
    text32 = models.TextField('Продолжение статьи 32', blank=True)
    text33 = models.TextField('Продолжение статьи 33', blank=True)
    text34 = models.TextField('Продолжение статьи 34', blank=True)
    text35 = models.TextField('Продолжение статьи 35', blank=True)
    text36 = models.TextField('Продолжение статьи 36', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.TextField('Комменаткрий', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
