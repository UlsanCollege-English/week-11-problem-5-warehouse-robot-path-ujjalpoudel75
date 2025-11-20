from collections import deque

def parse_grid(lines):
    g = {}
    start = None
    target = None

    rows = len(lines)

    # detect "ST" combined cells (row -> index of 'S' in the "ST" pair)
    st_index = {}
    for r, line in enumerate(lines):
        idx = line.find("ST")
        if idx != -1:
            st_index[r] = idx

    # build nodes (use per-row column length)
    for r in range(rows):
        cols = len(lines[r])
        for c in range(cols):
            ch = lines[r][c]

            # handle combined "ST" cell: set both start and target to same coord
            if r in st_index and c == st_index[r]:
                start = f"{r},{c}"
                target = f"{r},{c}"
                # treat this cell as non-wall below

            else:
                if ch == "S":
                    start = f"{r},{c}"
                elif ch == "T":
                    # if this T is the second char of an "ST" pair we've already handled, skip
                    if not (r in st_index and c == st_index[r] + 1):
                        target = f"{r},{c}"

            if ch != "#":
                g[f"{r},{c}"] = []

    # build edges: only up/down/left/right (no diagonals)
    for r in range(rows):
        cols = len(lines[r])
        for c in range(cols):
            if lines[r][c] == "#":
                continue
            u = f"{r},{c}"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                rr, cc = r+dr, c+dc
                if 0 <= rr < rows and 0 <= cc < len(lines[rr]):
                    if lines[rr][cc] != "#":
                        g[u].append(f"{rr},{cc}")

    return g, start, target


def grid_shortest_path(lines):
    g, s, t = parse_grid(lines)

    # start equals target
    if s == t:
        return [s]

    # BFS
    from collections import deque
    q = deque([s])
    parent = {s: None}
    visited = {s}

    while q:
        node = q.popleft()

        for nei in g[node]:
            if nei not in visited:
                visited.add(nei)
                parent[nei] = node
                q.append(nei)

                if nei == t:
                    # reconstruct
                    path = [t]
                    cur = t
                    while parent[cur] is not None:
                        cur = parent[cur]
                        path.append(cur)
                    path.reverse()
                    return path

    return None
