# ssh check v7 tg s123 status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_v7_tg_s123_status_20260521T194257_result.json`
- **Structured JSON:** [`6079dfb7c1b92ad31131.json`](../../sessions/60/6079dfb7c1b92ad31131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7_tg_s123 训练状态：**仍在运行**

**进程**: PID 245628, 状态 S, 已运行 4h27m

### 配置
- 模型: Qwen2.5-7B-Instruct, GPU: RTX PRO 6000 Blackwell (102GB)
- Gate type: threadgate, Dataset: ultrachat_8k (8000 samples)
- Total optimizer steps: 3000 (3 epochs × 1000 steps), Grad accum: 8
- Trainable: 6.7M params (0.09%), Gate LR: 0.002 (10× multiplier)

### 进度
| Epoch | Status | Avg Loss | Avg NTP | Avg GAR | Avg DIV |
|-------|--------|----------|---------|---------|---------|
| 0 | Done | 1.0027 | 0.9759 | 0.0263 | 0.0006 |
| 1 | Done | 0.9447 | 0.9434 | 0.0013 | 0.0000 |
| 2 | **Running** (Step 1900/8000 data, ~2244/3000 optimizer) | — | — | — | — |

**总进度**: ~75% (2244/3000 optimizer steps)

### 预估剩余时间
- 速率: ~8.4 optimizer steps/min
- 剩余: ~756 steps → **约 1.5 小时完成**

### 最新 Gate 状态 (step=2200)
- mean=0.9495, std=0.0530, min=0.7930, max=1.0000
- Gate profile (per-layer):
  ```
  L0:0.887 L1:0.793 L2:0.996 L3:0.992 L4:0.988 L5:0.793
  L6:0.969 L7:0.930 L8:0.965 L9:0.934 L10:0.973 L11:0.910
  L12:0.910 L13:0.934 L14:0.926 L15:0.977 L16:0.938 L17:0.930
  L18:0.957 L19:0.977 L20:0.988 L21:0.992 L22:0.980 L23:0.988
  L24:0.984 L25:0.988 L26:0.988 L27:1.000
  ```
- L1 和 L5 gate 值最低 (~0.79)，深层接近 1.0 — 与 s42 seed 的 pattern 一致

### Checkpoints
- `runs/phase2_tg_s123_v7/epoch_0/` ✓
- `runs/phase2_tg_s123_v7/epoch_1/` ✓
- epoch_2 checkpoint 待训练完成后生成

---
