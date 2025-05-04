CREATE (a:Node {name: 'A'})
CREATE (b:Node {name: 'B'})
CREATE (c:Node {name: 'C'})
CREATE (a)-[:REL {weight: 1}]->(b)
CREATE (b)-[:REL {weight: 2}]->(c)
CREATE (c)-[:REL {weight: 1}]->(a);