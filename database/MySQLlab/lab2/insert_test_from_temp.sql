INSERT INTO test(`address`,`age`,`name`,`score`)
SELECT `address`,`age`,`name`,`score`
FROM test_temp;