with base_table as (
select 
	*, 
	row_number() over (partition by id) as rn
from snapshots.twitch_streams_all
)

, deduplicate as (
select * from base_table
where rn = 1
)

, calculate_volume as (
select 
	game_name,
	SUM(CASE WHEN viewer_count < 5  THEN 1 ELSE 0 END)				 as nb_steam_less_than_5_viewers,
	SUM(CASE WHEN viewer_count between 5 and 10 THEN 1 ELSE 0 END) 	as nb_steam_5_10_viewers,
	COUNT(*) as nb_steam
from deduplicate
group by game_name
order by 2 desc
)

select 
	*, 
	nb_steam_5_10_viewers::float / nb_steam::float as prct_steam_less_than_10viewers
from calculate_volume
where nb_steam > 100
order by prct_steam_less_than_10viewers desc