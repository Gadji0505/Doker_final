

1. MATCH (m:Movie {title: "The Matrix"})<-[:DIRECTED]-(d:Director)
RETURN d.name AS DirectorName

2. Количество фильмов для каждого актера
     MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
   RETURN p.name AS Actor, COUNT(m) AS MoviesCount
   
3. Человек, участвовавший в наибольшем количестве фильмов в качестве актера

     MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
   RETURN p.name AS Actor, COUNT(m) AS MoviesCount
   ORDER BY MoviesCount DESC
   LIMIT 1
   
4. Фильм с наибольшим количеством актеров и режиссеров

     MATCH (m:Movie)<-[:ACTED_IN]-(p:Person)
   WITH m, COUNT(p) AS ActorCount
   MATCH (m)<-[:DIRECTED]-(d:Person)
   RETURN m.title AS MovieTitle, (ActorCount + COUNT(d)) AS TotalParticipants
   ORDER BY TotalParticipants DESC
   LIMIT 1
