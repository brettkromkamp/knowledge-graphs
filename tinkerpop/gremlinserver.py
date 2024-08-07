from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.graph_traversal import GraphTraversalSource, __
from gremlin_python.process.traversal import (
    Barrier,
    Bindings,
    Cardinality,
    Column,
    Direction,
    Operator,
    Order,
    P,
    Pop,
    Scope,
    T,
    WithOptions,
)
from gremlin_python.process.anonymous_traversal import traversal
from typing import Optional

# Support gremlin event loop in JupyterLab
# import nest_asyncio

# nest_asyncio.apply()


# Set up functions
def add_edge(g: GraphTraversalSource, from_id: int, to_id: int, edge_label: str, param: Optional[str] = None) -> None:
    g.V(from_id).addE(edge_label).to(__.V(to_id)).property("param", param).next()


def add_vertex(g: GraphTraversalSource, vertex_label: str, vertex_id: int, name: Optional[str] = None) -> None:
    g.addV(vertex_label).property(T.id, vertex_id).property("name", name).next()


def init_graph(g: GraphTraversalSource):
    g.V().drop().iterate()  # Drop all vertices
    g.E().drop().iterate()  # Drop all edges

    # Add vertices
    add_vertex(g, "user", 1, name="Olivia")
    add_vertex(g, "user", 2, name="Emma")
    add_vertex(g, "file", 3, name="project.pdf")
    add_vertex(g, "file", 4, name="salary.pdf")
    add_vertex(g, "file", 5, name="demo.py")
    add_vertex(g, "file", 6, name="post.html")
    add_vertex(g, "drive", 7, name="my-drive")

    # Add edges
    add_edge(g, 1, 2, "work-together")
    add_edge(g, 1, 3, "edit")
    add_edge(g, 1, 4, "view")
    add_edge(g, 2, 5, "print")
    add_edge(g, 2, 6, "edit")
    add_edge(g, 2, 7, "located-in")


# Set the graph traversal from the local machine
connection = DriverRemoteConnection("ws://localhost:8182/gremlin", "g")
g = traversal().with_remote(connection)
vertex_count = g.V().count().next()
print(f"Vertex count: {vertex_count}")

# Initialise graph
init_graph(g)

# Traverse graph
print("Vertices: ", g.V().value_map(True).to_list())  # Fetch a list of all vertices
print("Edges: ", g.E().value_map(True).to_list())  # Fetch a list of all edges

print("Files: ", g.V().out("edit").has_label("file").to_list())
print("Path traversal: ", g.V().out("edit").has_label("file").path().to_list())
