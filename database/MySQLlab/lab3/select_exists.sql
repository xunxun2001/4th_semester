SELECT * 
FROM student AS a
WHERE EXISTS (select  1 from student as b where b.`college` = a.`college` and b.`name` = "张三" )
