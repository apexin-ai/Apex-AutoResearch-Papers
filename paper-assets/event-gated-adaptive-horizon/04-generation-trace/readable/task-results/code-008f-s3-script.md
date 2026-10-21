# code 008f s3 script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_008f_s3_script_20260516T160507_result.json`
- **Structured JSON:** [`e84fd8cb2422a218d471.json`](../../sessions/e8/e84fd8cb2422a218d471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并注册。

关键配置：
- 参数名确认为 `--checkpoint_every 25000`（configs.yaml 第17行，默认值 0）
- 添加了 `CUDA_VISIBLE_DEVICES=1` 确保物理 GPU 映射正确，`--device cuda:0` 指向 CVID 映射后的逻辑设备
- seed=3 未被 008f 系列使用过（0=009h, 1=008f, 2=009c）
- 脚本注释中已标注 `chmod +x before running`

---
