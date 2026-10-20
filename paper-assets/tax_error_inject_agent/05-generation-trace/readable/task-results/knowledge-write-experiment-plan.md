# knowledge write experiment plan

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_write-experiment-plan_20260514T220305_result.json`
- **Structured JSON:** [`5187da98f1c4312998a9.json`](../../sessions/51/5187da98f1c4312998a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存 `experiment_plan.yaml` 到 artifacts 并注册。

汇总：
- **P1 (8 个实验)**: multi-seed 补齐 (running) → eval → 3-seed 统计 → injection ratio ablation 数据生成 → 10%/25% 训练 (4 runs) → eval (4 runs) → training dynamics 分析。预计 P1 全部完成需 ~5-6 小时，4 卡可全并行。
- **P2 (2 个)**: WebShop 第二环境 (工程量大，3-5 天) + 定性 failure 分析 (20+ cases 标注)。
- **P3 (3 个)**: scale ablation / few-shot recovery / per-operator deep dive。

50% injection 的结果可复用已有 v4 seed=42 数据，ablation 实际只需 4 组新训练。

---
