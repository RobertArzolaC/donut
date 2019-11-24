from py2neo import Graph, Node, Relationship
from django.conf import settings


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WorkSpaceGraph(Graph, metaclass=Singleton):
    def _get_subgraph(self, query):
        cursor = self.run(query)
        data = next(cursor, None)
        if data:
            return data.to_subgraph()
        return None

    def find_node(self, id_):
        id_ = int(id_)
        qs = 'MATCH (n) WHERE n.id={0} RETURN n'.format(id_)
        return self._get_subgraph(qs)

    def find_relationship(self, id_):
        id_ = int(id_)
        qs = 'MATCH ()-[r]-() WHERE r.id={0} RETURN r'.format(id_)
        return self._get_subgraph(qs)

    def add_entity(self, entity):
        node = self.find_node(entity.id)

        if node is None:
            tx = self.begin()
            graph_id = entity.workspace.id
            node = Node(
                "Entity", id=entity.id, graph_id=graph_id, name=entity.name)
            tx.create(node)
            tx.push(node)
            tx.commit()

    def add_association(self, association):
        node_1 = self.find_node(association.entity_1.id)
        node_2 = self.find_node(association.entity_2.id)
        relation = self.find_relationship(association.id)

        assert node_1 is not None
        assert node_2 is not None

        tx = self.begin()
        if relation is None:
            graph_id = association.workspace.id
            relation = Relationship(
                node_1, association.relationship.name, node_2,
                id=association.id, graph_id=graph_id
            )
            tx.create(relation)
        tx.push(relation)
        tx.commit()


graph = WorkSpaceGraph(**settings.NEO4J_CONFIG)
