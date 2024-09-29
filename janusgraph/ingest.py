# pip install --upgrade async-timeout

import csv

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph


# Load vertices from CSV
def load_vertices(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            g.addV(row["label"]).property("id", row["id"]).property("name", row["name"]).property(
                "age", int(row["age"])
            ).iterate()


# Load edges from CSV
def load_edges(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            g.V().has("id", row["source"]).as_("a").V().has("id", row["target"]).addE(row["label"]).from_(
                "a"
            ).iterate()

if __name__ == '__main__':
    # Connect to the Gremlin server
    graph = Graph()
    print("Connecting to the server!")
    connection = DriverRemoteConnection("ws://localhost:8182/gremlin", "g")
    g = graph.traversal().withRemote(connection)

    # Drop all vertices and edges
    print("Dropping all vertices and edges...")
    g.V().drop().iterate()
    g.E().drop().iterate()

    # Bulk load vertices and edges
    print("Bulk loading vertices...")
    load_vertices("./data/vertices.csv")
    print("Bulk loading edges...")
    load_edges("./data/edges.csv")

    # Close the connection
    print("Closing the connection!")
    connection.close()
