-- lists all cities with their state name, using a single SELECT with JOIN
SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
