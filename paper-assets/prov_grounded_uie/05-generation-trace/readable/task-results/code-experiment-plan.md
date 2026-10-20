# code experiment plan

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_experiment-plan_20260512T114557_result.json`
- **Structured JSON:** [`ba369357a5d8337c63e1.json`](../../sessions/ba/ba369357a5d8337c63e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`experiment_plan.yaml` 已写入项目目录，包含 4 个实验计划：

1. **exp_sft_baseline** — SFT 基线，无依赖
2. **exp_posthoc_nli** — Post-hoc NLI reranking，依赖 exp_sft_baseline
3. **exp_grpo_provenance** — GRPO 证据溯源奖励训练，依赖 exp_sft_baseline
4. **exp_comparison** — 三组对比 + 退化检查，依赖前三个实验

---
