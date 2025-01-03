/*
Enter your query here.
*/
SELECT
    CASE
        WHEN A + B <= C THEN "Not A Triangle"
        WHEN A = B AND B = C AND A + B > C THEN "Equilateral"
        WHEN (A = B AND B != C) OR (A = C AND A != B) AND A + B > C THEN "Isosceles"
        WHEN (A != B AND B != C AND A != C) AND A + B > C THEN "Scalene"
END
FROM TRIANGLES;
