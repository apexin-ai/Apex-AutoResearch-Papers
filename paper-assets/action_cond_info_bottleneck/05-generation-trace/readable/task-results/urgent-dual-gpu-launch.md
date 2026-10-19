# urgent dual gpu launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_dual-gpu-launch_20260516T114947_result.json`
- **Structured JSON:** [`504d57e6f08f42b58e88.json`](../../sessions/50/504d57e6f08f42b58e88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 满载恢复。

---

**总结：**

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| 0 (99% util, 16.2GB) | v7 log-barrier 训练 | 960110 | Step 600+/20000, 1.7 steps/s, `--conditioning_mode concat` |
| 1 (4% util, 6.5GB) | v5 eval ckpt-10000 | 970634 | libero_spatial rollout 进行中 |

**修复事项：**
1. config.py 默认从 `"film"` 改回 `"concat"`（v8 FiLM worker 留下的）
2. 杀掉旧进程 PID 959189（无 `--conditioning_mode` 参数的残留训练，占用 GPU 1）
3. v5 eval 首次因 scorer shape mismatch 全部失败（config 默认 film 导致 input_dim=960 vs checkpoint 的 1920），修复后重启成功

**验证：** v5 checkpoint 使用 concat 模式确认 — scorer.mlp.0.weight shape 为 [64, 1920]（=960+960 concat）。

---
