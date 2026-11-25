from orchestrator import Task, execute

if __name__ == '__main__':
    print(execute([
        Task('collect', lambda _: [12, 18, 24]),
        Task('summarize', lambda d: sum(d['collect']), ('collect',)),
        Task('audit', lambda d: {'valid': d['summarize'] == 54}, ('summarize',)),
    ]))
