from client import DAGResolver

tasks = ["init", "build", "test", "deploy"]
deps = {"build": ["init"], "test": ["build"], "deploy": ["test"]}
res = DAGResolver.resolve_order(tasks, deps)
print("Resolved execution order:", " -> ".join(res["execution_order"]))
