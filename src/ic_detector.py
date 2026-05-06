def detect_circular_ic(entries):
    graph = {}

    for entry in entries:

        # 🔥 Skip bad entries safely
        if not isinstance(entry, dict):
            continue

        if entry.get("type") == "intercompany":
            src = entry.get("from")
            dst = entry.get("to")

            if src and dst:
                graph.setdefault(src, []).append(dst)

    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False