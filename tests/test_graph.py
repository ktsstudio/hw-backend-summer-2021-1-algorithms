from typing import TypeVar

import tasks

T = TypeVar("T")

Graph = tasks.Graph
Node = tasks.Node


def extract_values(nodes: list[Node[T]]) -> list[T]:
    return [node.value for node in nodes]


class TestDFS:
    def test_dfs_1(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.point_to(b)
        b.point_to(c)
        a.point_to(c)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a", "b", "c"]

    def test_dfs_2(self) -> None:
        a = Node("a")

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a"]

    def test_dfs_3(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.point_to(b)
        b.point_to(c)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a", "b", "c"]

    def test_dfs_4(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d"]

    def test_dfs_5(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        b.point_to(f)
        c.point_to(e)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d", "e", "f"]

    def test_dfs_6(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        b.point_to(f)
        f.point_to(e)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d", "f", "e"]

    def test_dfs_7(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")
        k = Node("k")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        a.point_to(e)
        e.point_to(f)
        e.point_to(g)
        f.point_to(i)
        f.point_to(h)
        g.point_to(k)

        received_nodes = Graph(a).dfs()

        assert extract_values(received_nodes) == [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "i",
            "h",
            "g",
            "k",
        ]


class TestBFS:
    def test_bfs_1(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.point_to(b)
        b.point_to(c)
        a.point_to(c)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a", "b", "c"]

    def test_bfs_2(self):
        a = Node("a")

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a"]

    def test_bfs_3(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.point_to(b)
        b.point_to(c)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a", "b", "c"]

    def test_bfs_4(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d"]

    def test_bfs_5(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        b.point_to(f)
        c.point_to(e)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d", "f", "e"]

    def test_bfs_6(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        b.point_to(f)
        f.point_to(e)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == ["a", "b", "c", "d", "f", "e"]

    def test_bfs_7(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")
        k = Node("k")
        a.point_to(b)
        b.point_to(c)
        c.point_to(d)
        d.point_to(a)
        b.point_to(d)
        a.point_to(e)
        e.point_to(f)
        e.point_to(g)
        f.point_to(i)
        f.point_to(h)
        g.point_to(k)

        received_nodes = Graph(a).bfs()

        assert extract_values(received_nodes) == [
            "a",
            "b",
            "e",
            "c",
            "d",
            "f",
            "g",
            "i",
            "h",
            "k",
        ]
