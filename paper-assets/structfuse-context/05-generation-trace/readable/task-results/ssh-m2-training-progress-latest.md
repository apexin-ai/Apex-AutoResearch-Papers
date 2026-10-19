# ssh m2 training progress latest

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m2_training_progress_latest_20260514T014638_result.json`
- **Structured JSON:** [`04c2521ac7164a697e29.json`](../../sessions/04/04c2521ac7164a697e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M2 训练状态 (2026-05-14 ~09:47 CST)

### 1. Qwen (cuda:0, random_s42)

| Checkpoint | val_loss | R@1 | R@5 |
|-----------|----------|------|------|
| eval@500 | 0.4869 | 0.5332 | 0.9540 |
| eval@1000 | **0.4651** | **0.5527** | 0.9594 |
| eval@1500 | 0.5365 | 0.5228 | 0.9550 |
| eval@2000 | **未出** | — | — |

- **Current step**: 2000，刚打完 step log，eval@2000 正在跑（日志末尾停在 `step 2000 loss=0.0429`，尚无 eval 输出）
- eval@1500 出现回退（R@1 从 0.5527→0.5228, val_loss 从 0.4651→0.5365），但仍 **高于 0.50 阈值**
- Best checkpoint: eval@1000 (R@1=0.5527, val_loss=0.4651)
- 仍在 random_s42（1/9 strategies）

### 2. StarCoder (cuda:1, random_s42)

| Checkpoint | val_loss | R@1 | R@5 |
|-----------|----------|------|------|
| eval@500 | 0.6194 | 0.4352 | 0.9054 |
| eval@1000 | **0.6134** | **0.4537** | 0.9201 |

- **Current step**: ~1350，尚未到 eval@1500
- Best checkpoint: eval@1000 (R@1=0.4537)
- 仍在 random_s42（1/9 strategies）

### 3. m1_reextract_v2
- 活跃运行中，当前并行处理 sunpy/sunpy (400/722), pylint-dev/astroid, encode/starlette, tkrajina/gpxpy

### 4. GPU

| GPU | Util | VRAM | Temp |
|-----|------|------|------|
| 0 (Qwen) | 100% | 51.6/97.9 GB | 74°C |
| 1 (StarCoder) | 100% | 55.2/97.9 GB | 73°C |

### 关键决策点

- **eval@2000 尚未出**，预计几分钟内出结果。eval@1500 已有回退趋势（train loss 持续降到 0.04 而 val_loss 反弹），eval@2000 的 R@1 是否跌破 0.50 需要等结果。
- 如果需要我稍后再查 eval@2000 结果，告诉我。

---
