# Relax Production Harness Probe Design

## Goal

Allow the Builder to evolve genuinely multi-step Task Harnesses, including multiple model calls, without weakening benchmark answer contracts or tool safety.

## Design

`TaskHarnessSpec.from_dict` remains the general structural authority. It already validates bounded and non-empty node lists, unique safe node ids, supported node kinds, exactly one final `emit`, valid model prompts, and valid tool node shapes.

`production_harness_probe` will stop requiring exactly one `model_call`. It will retain only the experiment-wide checks that are independent of a particular Harness topology:

- at least one `model_call` must exist, so the Task Harness actually invokes a solver;
- every `tool_call` must name an explicitly provided public tool;
- all existing `TaskHarnessSpec` structural validation remains unchanged.

No model-call-specific maximum is introduced. The existing general Task Harness node bound remains unchanged as a payload safety constraint, rather than a topology rule.

## Expected behavior

- `model_call -> emit` passes.
- `draft model_call -> verify model_call -> emit` passes.
- Longer sequences with additional model calls pass when the artifact itself is structurally valid.
- A Harness containing only `emit` fails the production probe.
- A Harness calling an unregistered tool fails the production probe.
- Benchmark Contract Skills and solution codecs remain unchanged.

## Non-goals

- Do not relax benchmark answer parsing or evaluator contracts.
- Do not permit arbitrary Python or unknown tools.
- Do not change the fixed A/B/C, eight-round, freeze, or cross-test experiment protocol.
