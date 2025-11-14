import pytest
from UnionFind import UnionFind  # adjust to your file name

def test_initial_parents():
    uf = UnionFind(5)
    assert uf.parent == [0, 1, 2, 3, 4]

def test_find_initial():
    uf = UnionFind(5)
    for i in range(5):
        assert uf.find(i) == i

def test_union_simple():
    uf = UnionFind(5)
    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)

def test_union_chain():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)

    root = uf.find(0)
    for i in range(1, 4):
        assert uf.find(i) == root

def test_path_compression():
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)

    # Before compression, 3's parent might not be root
    root_before = uf.parent[3]
    root = uf.find(3)
    # After compression, 3's parent should be root
    assert uf.parent[3] == root

def test_union_already_connected():
    uf = UnionFind(3)
    uf.union(0, 1)
    root_before = uf.find(0)
    uf.union(0, 1)  # repeated union
    root_after = uf.find(1)
    assert root_before == root_after
