SELECT platform, count(*) FROM sales GROUP BY platform;
-- Finding the  average of na_sales:  
-- Sales.objects.filter(na_sales__gte=0).aggregate(Avg('na_sales'))

SELECT platform, count(*) from sales group by platform;
-- Sales.objects.values('platform').annotate(Count('platform'))
-- Sales.objects.filter(platform__in =['PS3', 'PC']).values('platform').annotate(Count('platform'))

Select distint(platform) on sales 
--  Sales.objects.values('platform').distinct()

-- The average function is count for each group
select platform, avg([NA_Sales]) as 'Average', avg([JP_Sales]) as 'av_jp' from sales group by platform
-- Dont forget to import Avg
-- from django.db.models import Avg
-- Sales.objects.filter(platform__in =['PS3', 'PC']).values('platform').annotate(na_sales = Avg('na_sales'), jp_sales=Avg('jp_sales'))


select sum(na_sales), year_of_release, platform  from sales  where platform in ('PS3', 'PS4', 'PC', 'X360') group by year_of_release, platform
-- Sales.objects.filter(platform__in =['PS3', 'PC']).values('platform','year_of_release').annotate(total = Sum(F('na_sales') + F('jp_sales')))
-- Sales.objects.filter(platform__in =['PS3', 'PC']).values('platform','year_of_release').annotate(
-- 	na_sales = Sum('na_sales'),
-- 	jp_sales = Sum('jp_sales'),
-- 	eu_sales = Sum('eu_sales'),
-- 	other_sales = Sum('other_sales'),
-- 	global_sales = Sum('global_sales'),
-- ).all()