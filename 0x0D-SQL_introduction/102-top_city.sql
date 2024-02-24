-- Displays the average temperature and month 7-8 by city ordered by temperature top 3 (descending).
SELECT `city`, AVG(value) as `avg_temp` FROM temperatures
WHERE `month` = 7 or `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC LIMIT 3;