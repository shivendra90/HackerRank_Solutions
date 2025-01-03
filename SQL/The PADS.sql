/*
Enter your query here.
*/
select Concat(Name, '(',Left(Occupation, 1),')') from OCCUPATIONS
    order by Name;
    
SELECT
    CASE WHEN Occupation = "Doctor" then Concat("There are a total of ", Count(Name), " doctors.")
         WHEN Occupation = "Actor" then Concat("There are a total of ", Count(Name), " actors.")
         WHEN Occupation = "Professor" then Concat("There are a total of ", Count(Name), " professors.")
         WHEN Occupation = "Singer" then Concat("There are a total of ", Count(Name), " singers.")
end as count
from OCCUPATIONS
group by Occupation
order by Count(Name), Occupation;
