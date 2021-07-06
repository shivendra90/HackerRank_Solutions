 /*
Enter your query here.
*/
select distinct CITY from STATION
    WHERE CITY NOT LIKE "A%"
    AND
    CITY NOT LIKE "E%"
    AND
    CITY NOT LIKE "I%"
    AND
    CITY NOT LIKE "O%"
    AND
    CITY NOT LIKE "U%";
