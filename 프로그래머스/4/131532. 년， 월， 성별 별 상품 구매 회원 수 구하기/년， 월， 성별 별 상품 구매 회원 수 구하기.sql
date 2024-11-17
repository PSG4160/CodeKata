SELECT 
YEAR(o.SALES_DATE) as YEAR,
MONTH(o.SALES_DATE) AS MONTH,
u.GENDER,
COUNT(DISTINCT o.user_id) AS USERS
FROM ONLINE_SALE o left join USER_INFO u on o.user_id = u.user_id
where u.GENDER is not null
group by 1,2,3
order by 1,2,3