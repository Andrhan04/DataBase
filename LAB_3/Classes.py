import psycopg2
from Base.connect import conn
class TankTree:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor()
    def add_leaf(self, parent_id, name):
        self.cursor.execute(
            "INSERT INTO tanks (parent_id, name) VALUES (%s, %s, %s)",(parent_id, name)
        )
        self.conn.commit()
    def delete_leaf(self, leaf_id):
        self.cursor.execute("DELETE FROM tanks WHERE id = %s", (leaf_id,))
        self.conn.commit()
    def delete_subtree(self, parent_id):
        self.cursor.execute("DELETE FROM tanks WHERE parent_id = %s", (parent_id,))
        self.cursor.execute("DELETE FROM tanks WHERE id = %s", (parent_id,))
        self.conn.commit()
    def delete_node_with_subtree(self, node_id):
        self.cursor.execute(
            "SELECT parent_id FROM tanks WHERE id = %s",
            (node_id,)
        )
        current_parent = self.cursor.fetchone()
        if current_parent is not None:
            current_parent_id = current_parent[0]
            self.cursor.execute(
                "UPDATE tanks SET parent_id = %s WHERE parent_id = %s",
                (current_parent_id, node_id)
            )
        self.cursor.execute(
            "DELETE FROM tanks WHERE id = %s",
            (node_id,)
        )
        self.conn.commit()
    def get_direct_children(self, parent_id):
        self.cursor.execute("SELECT * FROM tanks WHERE parent_id = %s", (parent_id,))
        return self.cursor.fetchall()
    def get_element(self, node_id):
        self.cursor.execute("SELECT * FROM tanks WHERE id = %s",
                            (node_id,))
        return self.cursor.fetchone()
    def get_direct_parent(self, node_id):
        self.cursor.execute("SELECT * FROM tanks WHERE id = (SELECT parent_id FROM tanks WHERE id = %s)",
                            (node_id,))
        return self.cursor.fetchone()
    def get_all_descendants(self, node_id):
        descendants = []
        def fetch_descendants(parent_id, level=0):
            self.cursor.execute("SELECT * FROM tanks WHERE parent_id = %s", (parent_id,))
            children = self.cursor.fetchall()
            for child in children:
                descendants.append((child, level))
                fetch_descendants(child[0], level + 1)
        fetch_descendants(node_id)
        return descendants
    def get_all_ancestors(self, node_id):
        ancestors = []
        def fetch_ancestors(child_id, level=0):
            self.cursor.execute("SELECT * FROM tanks WHERE id = (SELECT parent_id FROM tanks WHERE id = %s)",
                                (child_id,))
            parent = self.cursor.fetchone()
            if parent:
                ancestors.append((parent, level))
                fetch_ancestors(parent[0], level + 1)
        fetch_ancestors(node_id)
        return ancestors
    def close(self):
        self.cursor.close()
        self.conn.close()


