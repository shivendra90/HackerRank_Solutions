/*
Enter your query here.
*/

select distinct CITY from station
    where CITY regexp "^[^AEIOU]"
    or
    CITY regexp "[^aeiou]$";
