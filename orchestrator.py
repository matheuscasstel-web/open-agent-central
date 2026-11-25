"""Minimal dependency-aware orchestration for synchronous Python tasks."""
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Task:
    name: str
    run: Callable[[dict], object]
    depends_on: tuple[str, ...] = ()

def execute(tasks: list[Task]) -> dict:
    pending = {t.name: t for t in tasks}
    if len(pending) != len(tasks):
        raise ValueError('Duplicate task names')
    for task in tasks:
        if set(task.depends_on) - pending.keys():
            raise ValueError(f'Unknown dependency: {task.name}')
    # Validate the complete graph before executing any task.
    order = []
    ready = set()
    while len(order) < len(tasks):
        batch = [t for t in tasks if t.name not in ready and set(t.depends_on) <= ready]
        if not batch:
            raise ValueError('Dependency cycle')
        for task in batch:
            order.append(task)
            ready.add(task.name)
    results = {}
    for task in order:
        results[task.name] = task.run({k: results[k] for k in task.depends_on})
    return results
