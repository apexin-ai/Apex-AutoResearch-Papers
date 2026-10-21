# analyze exp 042 completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_042_completion_20260522T102742_result.json`
- **Structured JSON:** [`7614452ed54a36db72be.json`](../../sessions/76/7614452ed54a36db72be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。所有操作完成。

---

## exp_042_frozen_dt_emb_walker 诊断结果

**状态：正常完成 → SUCCESS**

| 指标 | 值 |
|------|-----|
| 总步数 | 224K（目标 210K，已超额完成） |
| eval_final (215K) | **612.45** |
| eval_peak (205K) | **682.38** |
| NVE peak (35K) | **0.194** |
| NVE final (215K) | **0.051** |
| civo/alert | 全程 0.0 |

**结论判断依据：**
- NVE 全程最高仅 0.194，远低于 1.5 阈值 → **无 CIVO collapse**
- eval_return 持续上升至 682 峰值，末期稳定在 612 → eval 健康
- civo/alert 从未触发
- 无 traceback、无异常退出

**假设验证：** frozen dt_emb（随机初始化 + requires_grad=False）成功阻止了 CIVO collapse，确认 dt_embedding 的**训练过程**（而非其存在本身）是 CIVO 的必要条件。

Registry 已更新为 DONE/success，metrics 已记录。

---
