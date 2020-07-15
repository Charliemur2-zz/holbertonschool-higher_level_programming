-- script that lists all shows contained in hbtn_0d_tvshows 
-- that have at least one genre linked.
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    INNER JOIN tv_shows_genres  tv_shows.tv_shows_genres_id = tv_shows_genres.id
ORDER BY tv_shows.title AND tv_show_genres.genre_id;
