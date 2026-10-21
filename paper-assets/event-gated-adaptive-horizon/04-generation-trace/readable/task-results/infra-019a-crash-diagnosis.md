# infra 019a crash diagnosis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_019a-crash-diagnosis_20260516T225253_result.json`
- **Structured JSON:** [`b2609a7a877990d28157.json`](../../sessions/b2/b2609a7a877990d28157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原因已定位。

**Crash 原因：`CUDA_VISIBLE_DEVICES` 与 `--device` 参数不匹配**

`envs/maniskill.py:46` 的 `resolve_physical_device` 逻辑：
1. 读取 `CUDA_VISIBLE_DEVICES`（假设是 `"1"`）→ `physical_gpus = ["1"]`（长度 1）
2. 从 `--device cuda:1` 解析 `logical_idx = 1`
3. `physical_gpus[1]` → **IndexError**，因为列表只有 index 0

对比成功运行的实验（010b, 008d）都用 `CUDA_VISIBLE_DEVICES=0 --device cuda:0`，匹配正确。

**修复方式（二选一）：**

**方案 A**（推荐）：不设 CVD，直接指定物理 GPU：
```bash
# 不设 CUDA_VISIBLE_DEVICES，--device cuda:1 会被 resolve_physical_device 直接透传
python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 \
  --logdir logdir/exp_019a_v2_pickcube_baseline --device cuda:1 ...
```

**方案 B**：设 CVD 但 device 用逻辑 0：
```bash
CUDA_VISIBLE_DEVICES=1 python -u dreamer.py --configs defaults maniskill_state \
  --task maniskill_PickCube-v1 --logdir logdir/exp_019a_v2_pickcube_baseline \
  --device cuda:0 ...
```

两种方案最终都会解析到物理 GPU 1。是否需要我用修正后的命令重新提交？

---
