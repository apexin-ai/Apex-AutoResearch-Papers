# train v4 taxei fixed inject25 r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_v4-taxei-fixed-inject25-r2_20260514T223342_result.json`
- **Structured JSON:** [`3f80538c47e8569b2be1.json`](../../sessions/3f/3f80538c47e8569b2be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 诊断结论：无需重试

inject25 (PID 96835) **已经在 cuda:3 上正常训练**，`CUDA_VISIBLE_DEVICES=3` 已正确设置。

| 项目 | 状态 |
|------|------|
| PID | 96835 (存活) |
| CUDA_VISIBLE_DEVICES | `3` ✓ (从 `/proc/96835/environ` 确认) |
| GPU 显存 | 19147 MiB / 95% 利用率 |
| 训练进度 | 71/1635 steps (4%), ~1.97s/it |
| 预计剩余 | ~51 分钟 |
| tmux | `v4-fixed-inject25` |
| 输出目录 | `output/v4-fixed-inject25/v0-20260515-063144/` |
| Registry | `v4-taxei-fixed-inject25-r2` → RUNNING |

4 张 GPU 全部在跑，无冲突。

---
