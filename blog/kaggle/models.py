from django.db import models

class Sales(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    year_of_release = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    na_sales = models.FloatField(blank=True, null=True)
    eu_sales = models.FloatField(blank=True, null=True)
    jp_sales = models.FloatField(blank=True, null=True)
    other_sales = models.FloatField(blank=True, null=True)
    global_sales = models.FloatField(blank=True, null=True)
    critic_score = models.FloatField(blank=True, null=True)
    critic_count = models.FloatField(blank=True, null=True)
    user_score = models.FloatField(blank=True, null=True)
    user_count = models.IntegerField(blank=True, null=True)
    developer = models.CharField(max_length=100, blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'sales'
