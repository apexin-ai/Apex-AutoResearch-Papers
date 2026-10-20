# exp check dpo training

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_check-dpo-training_20260512T153432_result.json`
- **Structured JSON:** [`fd27e02d4519708c95c4.json`](../../sessions/fd/fd27e02d4519708c95c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练状态: RUNNING**

| 项目 | 值 |
|------|-----|
| 进度 | **331/1077 steps (31%)** |
| 已运行 | 23 分 36 秒 |
| 剩余预估 | ~57 分钟 |
| Epoch | 0.89 / 3.0 |

**最近 metrics (step ~331):**
- loss: 0.67–0.70 (波动正常)
- rewards/accuracies: 0.25–0.75 (不稳定，仍在早期)
- rewards/margins: -0.02 ~ +0.06 (margin 很小，chosen/rejected 区分度还不高)

**GPU 3**: 23105 / 24564 MiB (94%), utilization 100%

速度约 4.1–4.9 s/it，预计还需 ~57 分钟完成。

---
