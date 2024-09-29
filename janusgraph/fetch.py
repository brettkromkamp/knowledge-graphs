from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

if __name__ == '__main__':
    # Connect to the Gremlin server
    graph = Graph()
    print("Connecting to the server!")
    connection = DriverRemoteConnection("ws://localhost:8182/gremlin", "g")
    g = graph.traversal().withRemote(connection)

    # Execute a Gremlin query to retrieve vertices with the "person" label
    print("Retrieving vertices with the 'person' label...")
    result = g.V().hasLabel("person").valueMap().toList()
    print(result)

    # Close the connection
    print("Closing the connection!")
    connection.close()