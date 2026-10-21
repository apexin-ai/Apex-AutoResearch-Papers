# ssh search step5 checkpoints westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_search_step5_checkpoints_westd_20260522T231505_result.json`
- **Structured JSON:** [`9169f9b384d6891e7c3d.json`](../../sessions/91/9169f9b384d6891e7c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**seed4/5/6 的 step5 checkpoint 均不存在**，无论 HF 还是 FSDP 格式，两台服务器都没有。

### 详细情况

| Seed | 服务器 | FSDP 训练目录 | 最新 step | step5 存在？ |
|------|--------|---------------|-----------|-------------|
| seed4 | bjb1-17606 | `exp029-seed4/` | global_step_15 | **否**（仅保存了 step15） |
| seed4 | westd-47453 | 不存在 | — | **否** |
| seed5 | westd-47453 | `exp029-seed5/` | global_step_10 | **否**（仅保存了 step10） |
| seed5 | bjb1-17606 | 不存在 | — | **否** |
| seed6 | 两台均无 | 不存在 | — | **否**（无训练记录） |

### 已有的 HF checkpoint（非 step5）

- **westd**: `qwen_exp029_seed4_step15_hf`, `qwen_exp029_seed5_step10_hf`, `qwen_exp029_seed6_step15_hf`
- **bjb1**: `qwen_exp029_seed4_step15_hf`

### 缺失清单

- **seed4 step5**: FSDP 目录在 bjb1 但只存了 step15，step5 未保存（save_steps 间隔大于 5）
- **seed5 step5**: FSDP 目录在 westd 但只存了 step10，step5 未保存
- **seed6 step5**: 无任何 FSDP 训练目录（仅有 westd 上的 step15 HF），step5 不可恢复

---
