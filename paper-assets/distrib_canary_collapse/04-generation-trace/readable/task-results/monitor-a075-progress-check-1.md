# monitor a075 progress check 1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_a075_progress_check_1_20260516T112633_result.json`
- **Structured JSON:** [`ecf988f13362a01903c2.json`](../../sessions/ec/ecf988f13362a01903c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控结果

| 指标 | a075_s43 (cuda:1) | a075_s44 (cuda:0) |
|------|-------------------|-------------------|
| **状态** | ALIVE (1h29m) | ALIVE (1h28m) |
| **当前** | Gen 4/10 — 合成数据生成中 | Gen 4/10 — 合成数据生成中 |
| **已完成** | Gen 0(baseline）+ Gen 1-3 | Gen 0(baseline）+ Gen 1-3 |
| **Gen 3 指标** | ppl=50.41, entropy=2.11, eff_rank=82.7, mauve=0.031 | 同上（同配置 seed 不同） |

**GPU**: 两卡均 42% 利用率，14.4GB / 97.9GB 显存 — 正常（当前在推理生成阶段）

**磁盘**: 37GB / 250GB used (15%) — 充裕

**预估完成时间**: 已用 ~89 min 完成 3 个训练 gen（~30 min/gen）。剩余 ~6.5 gen（gen 4 剩余 + gen 5-10）≈ **3 小时后**，约 UTC 22:30。

---
