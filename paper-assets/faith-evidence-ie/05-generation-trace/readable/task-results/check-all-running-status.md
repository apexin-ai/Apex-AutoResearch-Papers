# check all running status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_running_status_20260515T005723_result.json`
- **Structured JSON:** [`28ce2dea01d57fc6a180.json`](../../sessions/28/28ce2dea01d57fc6a180.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态总结

| # | 进程 | GPU | 状态 | 进度 | 预计剩余 |
|---|------|-----|------|------|---------|
| 1 | PID 90080 — GRPO lr5e6_r1 | cuda:0 (13.3GB, 62%) | **Running** | 184/200 steps (92%) | ~25 min |
| 2 | PID 122144 — RSFT generate | cuda:1 (22.7GB, 88%) | **Running** | 90/1514 batches (6%) | ~14h |
| 3 | PID 111731 — ckpt-80 eval | cuda:2 (0MB, 0%) | **Finished** | — | — |
| 4 | PID 117635 — ckpt-100 eval | cuda:3 (10.4GB, 81%) | **Running** | 49/62 batches (79%) | ~20 min |

### ckpt-80 eval 结果

| 指标 | 值 |
|------|------|
| **rel_f1** | **0.0116** |
| evi_f1 | 0.828 |
| evi_precision | 0.928 |
| evi_recall | 0.748 |
| edcr | 0.991 |
| format_ok_rate | 99.9% |
| n_truncated | 210/985 |

rel_f1 极低 (1.16%)，预测了 13828 个三元组但只有 151 个 TP（gold 12151）。evidence 质量不错（evi_f1=0.828），但关系抽取几乎全错——模型在 ckpt-80 可能出现了关系预测退化。

### GRPO 训练最新指标 (step ~184)

- reward: 0.281, f1_reward: 0.014, ced_reward: 0.015
- format_reward: 0.252
- 最近几步 reward 有波动，f1_reward 和 ced_reward 都在低位

### RSFT generate

- 已完成 90/1514 batches，format_ok_rate 99.6%，truncation_rate 9.2%，diversity 0.9/8（多样性极低）

---
