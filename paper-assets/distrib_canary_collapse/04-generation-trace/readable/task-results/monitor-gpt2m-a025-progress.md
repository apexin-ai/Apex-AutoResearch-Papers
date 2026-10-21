# monitor gpt2m a025 progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpt2m_a025_progress_20260516T031250_result.json`
- **Structured JSON:** [`5fa5d20f19b1d251a850.json`](../../sessions/5f/5fa5d20f19b1d251a850.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告：gen_wiki_gpt2m_a025_s42

| 指标 | 值 |
|------|-----|
| **当前位置** | Generation 5/10, step 3300/5000 (66%) |
| **总进度** | ~28,300 / 50,000 steps (56.6%) |
| **训练速度** | 2.06 it/s（稳定） |
| **最新 loss** | 1.7369 (step 3300, epoch 5.28) |
| **进程状态** | PID 149202 存活，已运行 4h 50m |
| **GPU 利用率** | 90%, 显存 55.5 / 97.9 GB (57%) |

**预估剩余时间**：~4 小时
- 当前 gen 剩余：~14 分钟
- 剩余 4 个 generation（gen 6-9）：每个约 52 分钟（40 分钟训练 + 12 分钟 generation 间 overhead）

**异常检查**：无异常。Loss 正常下降（step 3200: 1.7897 → step 3300: 1.7369），无 NaN/OOM/spike。

---
