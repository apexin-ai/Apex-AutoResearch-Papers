# ops check 28034 and s2 ckpt3000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-28034-and-s2-ckpt3000_20260523T103013_result.json`
- **Structured JSON:** [`594426df283ef9c36503.json`](../../sessions/59/594426df283ef9c36503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

1. **28034 连通性：OFFLINE**（端口无法连接）
2. **s2 ckpt-3000：NOT_FOUND**
   - 29046 上无任何包含 `s2` 的 checkpoint-3000 目录
   - 29046 上现有的 checkpoint-3000 均为其他实验：
     - `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-3000`
     - `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-3000`
     - `/root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine/checkpoint-3000`

s2 ckpt-3000 留在了已下线的 28034 上，未迁移到 29046。

---
