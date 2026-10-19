# Dual Harness Resource Checklist

## Required for the offline architecture fixture

- Python 3.11 or newer.
- `pytest` for contract tests.
- No API key, GPU, benchmark server, or external network access.

The fixture uses deterministic fake model generators and validates artifact versioning, lower-Harness execution, Builder inspection, validation, rollback, and commit.

## Repository CI prerequisite

- GitHub Actions must be enabled for `apexin-ai/apex-moss`.
- The organization billing account must have a valid payment method and enough Actions spending limit for an `ubuntu-latest` job.

The first branch run on 2026-08-24 was rejected before any step started because GitHub reported failed recent payments or an insufficient spending limit. This is an account-level runner blocker, not a test failure. After billing is restored, rerun the `dual-harness` workflow; it needs only a standard GitHub-hosted Linux runner and no GPU.

## Required for real model calls through the existing Codex transport

- A working `codex` CLI executable.
- A logged-in ChatGPT/Codex session on the execution host.
- Access to the configured model ID. The current experiment default is `gpt-5.6-sol`.
- Two isolated operation roots: one for Builder calls and one for Solver calls.

No API key is stored in the repository. The existing `CodexExecGenerator` invokes `codex exec --ephemeral --ignore-user-config --ignore-rules --sandbox read-only` and records the returned usage events.

## Alternative: direct OpenAI API transport

- `OPENAI_API_KEY` supplied only through the process environment or a secret manager.
- The `openai` Python package installed in the experiment environment.
- An API model ID that is actually enabled for the account. Do not assume the Codex CLI model ID is also an API model ID.
- The OpenAI Responses API client and account rate limits sufficient for separate Builder and Solver calls.
- Optional native tool calling. It is not required by the Moss contracts.

Moss defaults to `controller_json`: the model emits typed JSON or text, while trusted Python executes tools. The included `OpenAIResponsesGenerator` deliberately sends no `tools` field. A future `native_tool_calling` adapter may map Responses API tool calls onto the same allowlisted tools, but it must not expand permissions or expose evaluator-private data.

This means the first canary does not require a model with native tool calling. The current Task Harness chooses a fixed, ordered set of tool nodes; the model supplies their inputs and Moss executes them. Dynamic model-selected tools should be introduced later as a separate ablation, using a typed request that is still validated and executed by the controller.

The existing Codex CLI path is not a pure model API: Codex itself is an agent Harness. Use it for engineering canaries and product-level comparisons. For the main causal experiment, prefer the direct Responses API adapter with native tools disabled, so any tool use comes from Moss rather than Codex's own Harness.

## Benchmark resources

The architecture fixture needs no benchmark server. Formal experiments add resources by suite:

- LCBench/YAHPO: CPU-only Python environment and local benchmark data.
- CompilerGym: Linux CPU environment with LLVM/CompilerGym dependencies and isolated subprocess execution.
- SWE-bench Verified: Linux Docker host, benchmark images, substantial disk, CPU, and memory. GPU is normally unnecessary.
- KernelBench or GPU-kernel experiments: a separate CUDA host such as A100, only if that experiment is enabled.

## Recommended first real canary

- Linux host with 8 CPU cores, 32 GB RAM, and 100 GB free disk.
- No GPU for the dual-Harness control-flow canary.
- One Builder call and one or more Solver calls per round, capped before execution.
- Start with one public fixture task and one benchmark instance before reserving the full experimental budget.
- A frozen execution-contract manifest whose SHA-256 binds both transports and generation settings, the allowed tools, evaluator public projection, and probe. Pass that digest as `execution_contract_sha256` for every round.
- An operator recovery rule: an uncertain external call blocks later rounds. Audit the provider record first, then either resume the same `run_id` from its durable result or explicitly abandon an uncommitted round; a round that already owns a Harness commit cannot be abandoned.

Environment variables for that canary:

```text
MOSS_BUILDER_MODEL=<enabled-model-id>
MOSS_SOLVER_MODEL=<enabled-model-id>
MOSS_BUILDER_TRANSPORT=openai_responses
MOSS_SOLVER_TRANSPORT=openai_responses
MOSS_TOOL_PROTOCOL=controller_json
OPENAI_API_KEY=[REDACTED]
```
