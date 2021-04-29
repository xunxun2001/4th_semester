SELECT s.`sno`,`name`,`age`,`coursename`,`score`
FROM (student as s LEFT JOIN choose as ch ON  s.SNO = ch.SNO)
LEFT JOIN course as co ON ch.courseid = co.CourseID;
