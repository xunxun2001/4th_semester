SELECT MAX(score),MIN(score),SUM(score),AVG(score)
FROM `choose`
GROUP BY `courseid`
HAVING `courseid` = "C1";