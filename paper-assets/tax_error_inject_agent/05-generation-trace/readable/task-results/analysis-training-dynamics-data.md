# analysis training dynamics data

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics-data_20260515T021019_result.json`
- **Structured JSON:** [`c1f1d45a1c237a3eda35.json`](../../sessions/c1/c1f1d45a1c237a3eda35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已注册 artifact `art_20260515_5574fc`，路径：`artifacts/_project/data/training_dynamics_dose_response.json`

**收集结果汇总：**

| 实验 | 数据点 | Loss 范围 | Token Acc 范围 |
|------|--------|-----------|---------------|
| vanilla | 328 | 4.043 → 0.294 | 0.594 → 0.899 |
| taxei_50 | 328 | 3.973 → 0.259 | 0.589 → 0.911 |
| random_10 | 328 | 4.169 → 0.308 | 0.587 → 0.882 |
| random_25 | 328 | 4.175 → 0.286 | 0.603 → 0.892 |
| random_50 | 328 | 3.973 → 0.262 | 0.589 → 0.906 |

**缺失数据：** taxei_10 和 taxei_25 训练时 OOM 崩溃，无训练日志。需要重跑这两个实验才能补全 dose-response 曲线。

---
