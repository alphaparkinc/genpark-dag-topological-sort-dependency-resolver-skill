"""DAG Topological Sort & Dependency Resolver.
100% Python Standard Library.
"""

from collections import defaultdict, deque

class DAGResolver:
    """Computes valid execution orders and detects cyclic dependencies in task DAGs."""
    @staticmethod
    def resolve_order(tasks: list, dependencies: dict) -> dict:
        in_degree = {t: 0 for t in tasks}
        adj = defaultdict(list)

        for t, parents in dependencies.items():
            for p in parents:
                adj[p].append(t)
                in_degree[t] = in_degree.get(t, 0) + 1

        queue = deque([t for t in tasks if in_degree[t] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        has_cycle = len(order) != len(tasks)
        unresolved = [t for t in tasks if t not in order]

        return {
            "has_cycle": has_cycle,
            "execution_order": order if not has_cycle else [],
            "unresolved_tasks": unresolved
        }
