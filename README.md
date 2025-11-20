# HW05 — Warehouse Robot Path (BFS on Grid)

**Story intro.**  
A warehouse robot moves in a grid of aisles. `#` is a blocked shelf, `.` is open floor. `S` is the start. `T` is the target. Move up/down/left/right only. Find a shortest path by steps.

**Technical description.**  
- **Input:** `lines` list of equal-length strings. Example:
S..
.#.
..T

markdown
Copy code
- **Outputs:**  
- `parse_grid(lines)` → `(graph, start, target)` where `graph` is adjacency list of cells like `"(r,c)"` strings, `start` and `target` are cell ids.  
- `grid_shortest_path(lines)` → list of cell ids from start to target; `None` if unreachable.  
- **Constraints:**  
- 4-direction moves; no diagonals.  
- Exactly one `S` and one `T`.  
- **Expected complexity:** **O(R*C)** time, **O(R*C)** space.

## Prompts (minimal)
- Design the neighbors for each open cell.  
- Reuse BFS with a queue and a parent map.  
- Rebuild the path from `T` back to `S`.

## Hints
- Use a helper `cell_id(r,c)` that returns `"r,c"`.  
- Skip `#`. Do bounds checks.  
- Early return if `S == T`.

## Run tests locally
```bash
python -m pytest -q
```

## FAQ

Q: Can there be multiple S or T? A: No. Tests assume exactly one of each.

Q: Output format? A: A list like ["0,0","0,1","1,1",...].

Q: Ties in path length? A: Any shortest path is fine.

Q: Big-O? A: O(R*C) time and space.

Q: Read stdin? A: No. Use the functions.

Q: Diagonals? A: Not allowed.


# Trigger Autograder Run