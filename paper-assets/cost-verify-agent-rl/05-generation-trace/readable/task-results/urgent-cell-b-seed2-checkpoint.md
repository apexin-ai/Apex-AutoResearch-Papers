# urgent cell b seed2 checkpoint

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cell_b_seed2_checkpoint_20260524T234705_result.json`
- **Structured JSON:** [`ca18bee021b7e85b4a6e.json`](../../sessions/ca/ca18bee021b7e85b4a6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Cell B seed2 step5 checkpoint: **不存在**

搜索了 `/root/autodl-tmp/checkpoints` 下所有包含 "h2"、"episodeadv"、"cell_b"、"factorial" 的路径，均无结果。

最接近的是 `hsweep-h10-seed2/global_step_5`（h=**10**, seed2），不是 Cell B（h=2）。

### 2. ScienceWorld SFT 训练进度

- **当前**: step **135/450** (30%)
- **速度**: ~18-19s/step
- **预计剩余**: ~1h38m（约北京时间 09:26 完成）
- 最新 checkpoint: `checkpoint-112`（07:41 保存）

### 3. GPU 显存与 eval 共存判断

```
GPU 0: RTX PRO 6000 (97887 MiB total)
  已用: 49541 MiB (51%)
  空闲: ~48 GB
  利用率: 100%
```

服务器当前只有 **1 张 GPU 可见**（nvidia-smi 仅显示 GPU 0）。

**判断**: 显存有 ~48GB 空余，eval (batch=1, ~20GB) 显存上可以共存。但 GPU compute 利用率 100%，eval 会与 SFT 争抢算力，双方都会变慢。建议等 SFT 完成（~1.5h 后）再跑 eval，或确认第二张卡是否可用。

---
