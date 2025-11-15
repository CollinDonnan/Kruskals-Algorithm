
from Kruskal import kruskal  # replace 'your_module' with the name of your kruskal file

def test_basic_graph():
    edges = [
        [1, 0, 1],
        [3, 0, 2],
        [2, 1, 2],
        [4, 1, 3],
        [5, 2, 3]
    ]
    num_of_verts = 4
    mst, total = kruskal(edges, num_of_verts)
    assert sorted(mst) == sorted([[0, 1], [1, 2], [1, 3]])
    assert total == 7

def test_single_edge():
    edges = [
        [10, 0, 1]
    ]
    num_of_verts = 2
    mst, total = kruskal(edges, num_of_verts)
    assert mst == [[0, 1]]
    assert total == 10

def test_single_vertex():
    edges = []
    num_of_verts = 1
    mst, total = kruskal(edges, num_of_verts)
    assert mst == []
    assert total == 0

def test_disconnected_graph():
    edges = [
        [1, 0, 1],
        [2, 2, 3]
    ]
    num_of_verts = 4
    mst, total = kruskal(edges, num_of_verts)
    # MST can't connect all vertices, but edges are included individually
    assert sorted(mst) == sorted([[0, 1], [2, 3]])
    assert total == 3

def test_equal_weights():
    edges = [
        [1, 0, 1],
        [1, 0, 2],
        [1, 1, 2],
        [1, 1, 3]
    ]
    num_of_verts = 4
    mst, total = kruskal(edges, num_of_verts)
    # Total weight should always be 3, MST edges may vary due to tie-breaking
    assert total == 3
    assert len(mst) == num_of_verts - 1

def test_already_mst():
    edges = [
        [1, 0, 1],
        [2, 1, 2],
        [3, 2, 3]
    ]
    num_of_verts = 4
    mst, total = kruskal(edges, num_of_verts)
    assert sorted(mst) == sorted([[0, 1], [1, 2], [2, 3]])
    assert total == 6

def test_large_graph():
    edges = [
        [10, 0, 1], [15, 0, 2], [5, 1, 2], [20, 1, 3],
        [25, 2, 3], [8, 3, 4], [7, 2, 4]
    ]
    num_of_verts = 5
    mst, total = kruskal(edges, num_of_verts)
    # MST edges: [1,2],[2,4],[0,1],[3,4] or equivalent
    assert total == 30
    assert len(mst) == num_of_verts - 1

def test_duplicate_edges():
    edges = [
        [1, 0, 1],
        [1, 0, 1],  # duplicate
        [2, 1, 2],
        [2, 1, 2]   # duplicate
    ]
    num_of_verts = 3
    mst, total = kruskal(edges, num_of_verts)
    assert total == 3
    assert len(mst) == num_of_verts - 1

def test_cycle_graph():
    edges = [
        [1, 0, 1],
        [2, 1, 2],
        [3, 2, 0]  # forms a cycle
    ]
    num_of_verts = 3
    mst, total = kruskal(edges, num_of_verts)
    assert total == 3
    # MST should only include 2 edges
    assert len(mst) == 2
