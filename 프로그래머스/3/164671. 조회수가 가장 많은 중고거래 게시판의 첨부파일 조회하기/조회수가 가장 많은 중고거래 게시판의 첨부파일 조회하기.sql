SELECT concat("/home/grep/src/", b.BOARD_ID,"/", f.FILE_ID, f.FILE_NAME, f.FILE_EXT ) as FILE_PATH
FROM USED_GOODS_BOARD b join USED_GOODS_FILE f on b.BOARD_ID = f.BOARD_ID
where b.VIEWS = (
    SELECT MAX(b1.VIEWS)
    FROM USED_GOODS_BOARD b1
)
order by 1 desc

