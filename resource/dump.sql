BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,         username TEXT, email TEXT, tel TEXT, website TEXT, reg_date TEXT);
INSERT INTO "users" VALUES(1,'KIM','test@naver.com','010-1234-1234','www.test.com','2020-08-18 17:24:59');
INSERT INTO "users" VALUES(2,'Park','test2@naver.com','010-1234-1234','www.test.com','2020-08-18 17:24:59');
INSERT INTO "users" VALUES(3,'Choi','test3@google.com','010-1234-1234','www.test.com','2020-08-18 17:25:14');
INSERT INTO "users" VALUES(4,'Lee','test4@google.com','010-1234-1234','www.test.com','2020-08-18 17:25:14');
INSERT INTO "users" VALUES(5,'Joo','test5@google.com','010-1234-1234','www.test.com','2020-08-18 17:25:14');
COMMIT;
