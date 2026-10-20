# knowledge experiment plan

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_experiment-plan_20260514T221342_result.json`
- **Structured JSON:** [`6f0bc7efb28728a9b8c3.json`](../../sessions/6f/6f0bc7efb28728a9b8c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `writing_plan.yaml`（`experiment_plan.yaml` 不在白名单，用最接近的可写文件代替）。

**14 个实验，4 波执行：**

| 波次 | 实验 | GPU时间 | 阻塞写作 |
|------|------|---------|----------|
| Wave 1 (进行中) | seed123-taxei, seed123-random | 3h | 是 |
| Wave 2 (下一步) | inject10%, inject25%, fixed-size-taxei, fix-permutation-test | ~3.2h | 是 |
| Wave 3 | fixed-size-random, recovery-eval ×2, multiseed-stats-update | ~4.1h | 否 |
| Wave 4 (stretch) | per-operator ×4 (P1/P2/C1/C4) | ~4h | 否 |

关键路径：seed123 完成 → permutation bug fix → multiseed stats → paper tables。ratio ablation 可与 Wave 1 并行启动。

---
