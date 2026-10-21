# fix sweep isr b005 s42 restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sweep-isr-b005-s42-restart_20260516T024718_result.json`
- **Structured JSON:** [`f97d7a949e3a0be921de.json`](../../sessions/f9/f97d7a949e3a0be921de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**sweep-isr-b005-s42 已经在正常训练，无需修复。**

当前状态：
- **GPU 0**: `sweep-isr-b01-s45` (β=0.1, seed=45) — 正常运行
- **GPU 1**: `sweep-isr-b005-s42` (β=0.05, seed=42) — 正常运行，已完成 47 步，reward_log 持续更新

命令路径已经是正确的 `scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml` 格式。看起来之前的失败已被修复并成功重启。

唯一的问题是 registry 中没有该实验的条目（可能是手动启动的），但训练本身在正常推进。需要我补注册 registry 条目吗？

---
