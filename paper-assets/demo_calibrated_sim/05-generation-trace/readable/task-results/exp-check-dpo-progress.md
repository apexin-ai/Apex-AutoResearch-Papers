# exp check dpo progress

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_check-dpo-progress_20260512T161519_result.json`
- **Structured JSON:** [`107a7a8e21e71236aa3d.json`](../../sessions/10/107a7a8e21e71236aa3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## dpo-001 训练状态

| 项目 | 状态 |
|------|------|
| **进度** | **928/1077 steps (86%)**, epoch 2.58/3.0 |
| **运行时间** | 1h 04m 30s |
| **当前 loss** | 0.65–0.70 区间，最近一条 0.6924 |
| **速度** | ~4.7–5.0 s/step |
| **预估剩余** | 149 steps × ~4.8s ≈ **~12 分钟** |
| **进程** | PID 170853 存活，GPU 3 利用率 100%，显存 23105/24564 MiB |
| **Checkpoints** | checkpoint-359 (epoch 1), checkpoint-718 (epoch 2) 已保存 |
| **rewards/margins** | 从早期 ~0.008 上升到 ~0.03–0.09，chosen/rejected 分离趋势正常 |
| **rewards/accuracies** | 多数 0.75，偶有 1.0 和 0.5 |
| **cuda:2** | `/dev/nvidia2` 不存在（GPU 编号从 0,1,2,3,4,5 → 设备文件可能映射不同），nvidia-smi 显示 GPU 2 使用 0 MiB，**已空闲** |

训练正常推进，约 12 分钟后完成第 3 epoch。GPU 0/1/2 均空闲，GPU 4/5 有其他任务占用。

---
