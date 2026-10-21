# code 010b cheetah collapse prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_010b-cheetah-collapse-prep_20260515T233231_result.json`
- **Structured JSON:** [`447e22c1adaf401d491f.json`](../../sessions/44/447e22c1adaf401d491f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**

1. **脚本路径：**
   - `scripts/submit_010b_cheetah_collapse.sh`
   - `scripts/submit_010c_cheetah_no_embed.sh`

2. **命令确认：**
   - **010b**: `--gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 105000 --seed 1`（dt_embed_dim 保持默认 32）
   - **010c**: 同上 + `--gate_dt_embed_dim 0`

3. **Dry-run 结果：** 所有 gate 参数在 `configs.yaml` defaults 中均存在且可覆盖：
   - `gate_enabled: False` → 覆盖为 True
   - `gate_fixed_dt: 0` → 覆盖为 2
   - `gate_subsample_max_dt: 0` → 覆盖为 2
   - `gate_dt_embed_dim: 32` → 010c 覆盖为 0
   - `imag_horizon: 15` → 覆盖为 8

渲染后端已与 010a 对齐（osmesa），未提交训练。

---
