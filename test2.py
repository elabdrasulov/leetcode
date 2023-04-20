# import datetime

# date = '31/12/2021'

# # now_1 = datetime.datetime.now()
# now_1 = datetime.date.today()


# res2 = date.split('/')
# res2 = list(reversed(res2))
# res2 = [int(i) for i in res2]
# res3 = datetime.date(res2[0], res2[1], res2[2])

# tdelta = now_1 - res3
# tdelta = res3 - now_1
# print(now_1)
# print(res3)
# print(tdelta.days)

#1
"""
SELECT plaintext FROM wordform LIMIT 10;

SELECT plaintext FROM wordform ORDER BY wordformid FETCH FIRST 10 ROW ONLY;

SELECT plaintext FROM wordform ORDER BY occurences DESC LIMIT(10);
"""

#2
"""
SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

SELECT plaintext FROM wordform WHERE stemtext ILIKE 'a%';

SELECT plaintext FROM wordform WHERE plaintext LIKE 'a%' OR plaintext LIKE 'A%';
"""

#3
"""
SELECT title, genretype FROM work WHERE genretype = 'p';

SELECT title, genretype FROM work WHERE genretype IN ('p');

SELECT title, genretype FROM work WHERE genretype LIKE 'p';
"""

#4
"""
SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype = 't';

SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype = 't' GROUP BY genretype;

SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype LIKE 't';
"""

#5
"""
SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);
select title from work where totalwords > (select (avg(totalwords) from work);

SELECT title FROM work WHERE totalwords > (SELECT SUM(totalwords) FROM work) / (SELECT COUNT(*) FROM work);
"""

#6
"""
SELECT character.charname, character.speechcount, work.title FROM character JOIN character_work ON character_work.charid = character.charid JOIN work ON character_work.workid = work.workid;

SELECT c.charname, c.speechcount, w.title FROM character as c INNER JOIN character_work as cw ON c.charid = cw.charid INNER JOIN work as w ON cw.workid = w.workid;

SELECT ROUND(avg(speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid WHERE work.title = 'Romeo and Juliet' GROUP BY work.title;
"""

#7
"""
SELECT ROUND(AVG(character.speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON work.workid = character_work.workid GROUP BY title HAVING title = 'Romeo and Juliet';

SELECT ROUND(AVG(c.speechcount)), w.title FROM character c INNER JOIN character_work cw ON c.charid = cw.charid INNER JOIN work w ON cw.workid = w.workid GROUP BY title HAVING title LIKE 'Romeo and Juliet';
"""

#8
"""
SELECT section, SUM(wordcount) FROM paragraph GROUP BY section;
"""

#9
"""
SELECT charname, speechcount FROM character WHERE speechcount BETWEEN 15 AND 30;

SELECT charname, speechcount FROM character WHERE speechcount >= 15 AND speechcount <= 30;

SELECT charname, speechcount FROM character WHERE speechcount IN (SELECT * FROM GENERATE_SERIES(15, 30));
"""

#10
"""
SELECT title, year FROM work WHERE year BETWEEN 1601 AND 1700;

SELECT title, year FROM work WHERE year >= 1601 AND year <= 1700;

SELECT title, year FROM work WHERE year IN (SELECT * FROM GENERATE_SERIES(1601, 1700));
"""

#11
"""
SELECT longtitle FROM work WHERE longtitle ~ 'the';

SELECT longtitle FROM work WHERE longtitle LIKE '%the%';
"""

#12
"""
SELECT DISTINCT section FROM paragraph;

SELECT section FROM paragraph GROUP BY section;
"""

#13
"""
SELECT chapter.chapterid, chapter.description, work.title FROM chapter JOIN work ON chapter.workid = work.workid;

SELECT c.chapterid, c.description, w.title FROM chapter AS c INNER JOIN work AS w ON c.workid = w.workid;

SELECT c.chapterid, c.description, w.title FROM chapter c FULL JOIN work w ON c.workid = w.workid;
"""

#14
"""
SELECT paragraph.paragraphnum, character.charname, character.speechcount FROM paragraph JOIN character ON character.charid = paragraph.charid;

SELECT p.paragraphnum, c.charname, c.speechcount FROM paragraph AS p INNER JOIN character AS c ON c.charid = p.charid;
"""

#15
"""
SELECT paragraph.paragraphnum, work.title, work.year FROM paragraph JOIN work ON paragraph.workid = work.workid;

SELECT p.paragraphnum, w.title, w.year FROM paragraph p INNER JOIN work w ON p.workid = w.workid;
"""