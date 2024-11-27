select m.MEMBER_NAME,	w.REVIEW_TEXT,	date_format(w.REVIEW_DATE, '%Y-%m-%d')
FROM REST_REVIEW w left join MEMBER_PROFILE m on w.MEMBER_ID = m.MEMBER_ID
WHERE w.MEMBER_ID = (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by COUNT(*) DESC
    LIMIT 1
    )
order by w.REVIEW_DATE, w.REVIEW_TEXT