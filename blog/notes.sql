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
`
