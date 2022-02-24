CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.title,
    g.maker,
    g.game_type_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id

CREATE VIEW EVENTS_BY_USER AS
SELECT
    u.first_name || " " || u.last_name as full_name,
    g.id gamer_id,
    e.id,
    e.date,
    e.time,
    game.title game_name
FROM levelupapi_eventgamer eg
JOIN levelupapi_gamer g ON g.id = eg.gamer_id
JOIN levelupapi_event e ON e.id = eg.event_id
JOIN levelupapi_game game ON e.game_id = game.id
JOIN auth_user u ON g.user_id = u.id