# knowledge experiment plan yaml

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_experiment-plan-yaml_20260515T015318_result.json`
- **Structured JSON:** [`8b21f8d9f943885870ac.json`](../../sessions/8b/8b21f8d9f943885870ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。experiment_plan.yaml 已重构，包含 15 个逻辑分组：

| 优先级 | 状态 | 计划数 | 覆盖 |
|--------|------|--------|------|
| P0 | done | 3 | baseline、data-collection、v3-pilot |
| P1 | 6 done / 1 in_progress | 7 | 3× multiseed、2× dose-response、recovery-eval |
| P2 | planned | 3 | training-dynamics、second-environment、qualitative-failure-analysis |
| P3 | planned | 3 | scale-ablation、recovery-prompting、per-operator-deepdive |

每个 plan_id 均包含 description、claim (C1-C6)、priority、registry_ids（含训练+eval）、depends_on、results/status。底部注释列出了 20+ 个 failed/killed registry 条目供溯源。唯一未完成的 P1 实验是 dose-response-random（inject25/50 eval 运行中）。

---
