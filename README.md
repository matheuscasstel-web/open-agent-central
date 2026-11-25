# Open Agent Central

Early-stage, dependency-free Python toolkit for orchestrating modular tasks. It provides a small foundation for agent workflows without requiring an AI provider or exposing credentials.

## Quick start
Requires Python 3.10+.

```sh
python example.py
python -m unittest discover -s tests -v
```

Tasks declare dependencies and receive only the corresponding outputs. The graph is validated before execution. Execution is synchronous and stops on errors. This is a prototype, not a production agent platform.

## Roadmap
- Optional MCP adapters and provider integrations
- Structured audit events and persistent state
- Explicit approval gates for external actions
- Cloud deployment examples and bilingual documentation

No adoption or community metrics are claimed. Contributions and feedback are welcome. Never commit credentials or private data.

## Português
Protótipo aberto de orquestração de tarefas com dependências, sem bibliotecas externas. Execute os comandos acima para testar. Integrações MCP, persistência e auditoria estruturada são objetivos futuros, ainda não implementados.

License: MIT.
