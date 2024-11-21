SELECT ID,
NAME,
HOST_ID
FROM PLACES
where HOST_ID in (
    select host_id
    from PLACES
    group by HOST_ID
    having count(*) >= 2
)
order by ID
