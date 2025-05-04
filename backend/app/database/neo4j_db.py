from neo4j import GraphDatabase
import os

class Neo4jDriver:
    def __init__(self):
        self.driver = GraphDatabase.driver("neo4j://neo4j:7687", auth=("neo4j", "password"))

    def close(self):
        self.driver.close()

    def init_graph_data(self):
        with self.driver.session() as session:
            result = session.run("MATCH (n) RETURN count(n) as count")
            if result.single()["count"] == 0:
                session.run("CREATE (a:Node {name: 'A'})")
                session.run("CREATE (b:Node {name: 'B'})")
                session.run("CREATE (c:Node {name: 'C'})")
                session.run("MATCH (a:Node {name: 'A'}), (b:Node {name: 'B'}) CREATE (a)-[:REL {weight: 1}]->(b)")
                session.run("MATCH (b:Node {name: 'B'}), (c:Node {name: 'C'}) CREATE (b)-[:REL {weight: 2}]->(c)")
                session.run("MATCH (c:Node {name: 'C'}), (a:Node {name: 'A'}) CREATE (c)-[:REL {weight: 1}]->(a)")

    def get_graph_data(self):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (n)-[r]->(m) RETURN n.name AS source, m.name AS target, r.weight AS weight"
            )
            return [{"source": record["source"], "target": record["target"], "weight": record["weight"]} for record in result]

def get_neo4j_data():
    driver = Neo4jDriver()
    driver.init_graph_data()
    data = driver.get_graph_data()
    driver.close()
    return data