SELECT st.`SNO`,ch.`score`
FROM student st JOIN choose ch ON st.SNO = ch.SNO
WHERE ch.CourseID = "C1" AND score < (select score from student st right join choose ch on st.`SNO` = ch.`SNO` where st.`name` = "张三" AND ch.CourseID = "C1")
