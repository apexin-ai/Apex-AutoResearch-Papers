# monitor hsweep h20 and 7b status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_hsweep_h20_and_7b_status_20260519T100537_result.json`
- **Structured JSON:** [`ffb3ff025a6c69d8766c.json`](../../sessions/ff/ffb3ff025a6c69d8766c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册 (`art_20260519_cf3da9`)。关键发现：

### hsweep_h20_seed1 (bjb1)
- Step 4 已完成，**step 5 rollout 进行中**（超 ETA ~20h）
- Train success: 20.3% → 13.3% → ? → 28.1%
- **无 val 结果**（eval_total=0.0），step 5 可能触发首次 val
- **Checkpoint 目录为空** — 无存档点
- PID 77613 存活

### 7b_cell_a_h2 (westd)
- Step 1 完成，step 2 rollout 进行中
- **强 collapse 信号**：val 28.1% → train 12.5%（一步腰斩），KL=1.92（h=20 仅 0.03），entropy=0.115（极低）
- 与假设一致：h=2 step-independent 在 8B 模型上复现了同样的 information loss + sign misattribution pathology

### 建议
1. **h=20**: 等 step 5 完成。如果触发 val，记录后 kill；如果无 val，仅凭 train metrics kill。注意无 checkpoint。
2. **7b_cell_a**: 继续监控，让 step 2 完成确认 collapse 趋势。这对论文是正面结果。

---
