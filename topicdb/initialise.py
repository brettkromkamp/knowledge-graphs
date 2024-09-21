"""
initialise.py file. Part of the Knowledge Graph project.

July 31, 2022
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from topicdb.store.topicstore import TopicStore

MAP_IDENTIFIER = 1
USER_IDENTIFIER_1 = 1


# Instantiate the topic store, create and subsequently populate a topic map
store = TopicStore("init.sqlite")
store.create_database()
store.create_map(USER_IDENTIFIER_1, "Test Map", "A map for testing purposes.")
store.populate_map(MAP_IDENTIFIER, USER_IDENTIFIER_1)

home_topic = store.get_topic(MAP_IDENTIFIER, "home")
for base_name in home_topic.base_names:
    print(base_name.name)
