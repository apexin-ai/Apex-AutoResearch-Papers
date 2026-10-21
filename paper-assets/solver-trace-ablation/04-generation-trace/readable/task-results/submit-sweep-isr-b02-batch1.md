# submit sweep isr b02 batch1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sweep-isr-b02-batch1_20260516T034907_result.json`
- **Structured JSON:** [`3c6b7526c3a2377326b2.json`](../../sessions/3c/3c6b7526c3a2377326b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法立即提交，两块 GPU 均被占用：**

| GPU | 当前实验 | 详情 |
|-----|---------|------|
| cuda:0 | sweep-isr-b01-s45-r3 | β=0.1, seed=45, ~80GB |
| cuda:1 | sweep-isr-b005-s42-r3 | β=0.05, seed=42, ~80GB |

**准备工作已就绪：**
- `configs/grpo_additive_bonus_b02.yaml` 已存在，beta=0.2，参数正确
- D098 修复已确认（`--seed` argparse default=None），CLI `--seed` 可覆盖 config 里的 seed 值
- 提交命令格式确认：`--seed 42` / `--seed 43` 通过 CLI 传入即可

需要等当前实验完成后再提交。要我检查当前实验的进度（W&B 或训练日志），还是等 GPU 空闲后再提交？

---
