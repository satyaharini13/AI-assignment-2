# BFS vs DFS Performance Comparison

Breadth First Search (BFS) and Depth First Search (DFS) are uninformed search strategies used in Artificial Intelligence.

## Breadth First Search (BFS)

- Explores nodes level by level
- Uses Queue data structure
- Always finds shortest path
- High memory usage

## Depth First Search (DFS)

- Explores nodes deeply before backtracking
- Uses Stack / Recursion
- Low memory usage
- May not find optimal solution

## Comparison

| Feature | BFS | DFS |
|-------|------|------|
| Data Structure | Queue | Stack |
| Completeness | Complete | Not always |
| Optimal | Yes | No |
| Memory | High | Low |
| Speed | Slower for deep trees | Faster but risky |

## Conclusion

BFS is better when shortest path is required, while DFS is more memory efficient.
