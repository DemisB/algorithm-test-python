def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """
    from collections import deque, namedtuple

    Node = namedtuple("Node", ["x", "y"])

    def get_neighbours(_node: namedtuple):
        _neighbours = []
        for step in (-1, 1):
            horizontal_neighbour_y = _node.y + step
            if -1 < horizontal_neighbour_y < len(maze[0]) and maze[_node.x][horizontal_neighbour_y] == 1:
                _neighbours.append(Node(x=_node.x, y=horizontal_neighbour_y))

            vertical_neighbour_x = _node.x + step
            if -1 < vertical_neighbour_x < len(maze) and maze[vertical_neighbour_x][_node.y] == 1:
                _neighbours.append(Node(x=vertical_neighbour_x, y=_node.y))

        return _neighbours

    root_node = Node(*start)
    goal_node = Node(*end)

    if maze[root_node.x][root_node.y] != 1:
        return False

    q = deque([root_node])
    explored_node_parents = {root_node: None}
    try:
        while node := q.popleft():
            if node == goal_node:
                break

            for neighbour in get_neighbours(node):
                if neighbour not in explored_node_parents:
                    explored_node_parents[neighbour] = node
                    q.append(neighbour)
    except IndexError:
        print("Queue is empty")

    node = goal_node
    path = [node]
    while node != root_node:
        node = explored_node_parents[node]
        path.append(node)

    path.reverse()
    return [tuple(n) for n in path]

