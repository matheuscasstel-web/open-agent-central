import unittest
from orchestrator import Task, execute

class TestOrchestration(unittest.TestCase):
    def test_dependencies(self):
        self.assertEqual(execute([Task('b', lambda d: d['a']+1, ('a',)), Task('a', lambda _: 2)])['b'], 3)
    def test_cycle(self):
        with self.assertRaises(ValueError):
            execute([Task('a', lambda _: None, ('a',))])
    def test_missing(self):
        with self.assertRaises(ValueError):
            execute([Task('a', lambda _: None, ('b',))])
    def test_duplicate(self):
        with self.assertRaises(ValueError):
            execute([Task('a', lambda _: None)]*2)
