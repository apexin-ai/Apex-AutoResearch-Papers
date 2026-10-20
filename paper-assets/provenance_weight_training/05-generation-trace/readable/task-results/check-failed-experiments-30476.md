# check failed experiments 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_failed_experiments_30476_20260518T134249_result.json`
- **Structured JSON:** [`7b6e103ef06d296aa956.json`](../../sessions/7b/7b6e103ef06d296aa956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**这 3 个实验并未失败，全部训练完成。**

### 各实验状态

| 实验 | Registry 状态 | 训练进度 | 最终模型 |
|---|---|---|---|
| `detect_remove_q05_seed123` | DONE | 6103/6103 (100%) | ✅ `/root/autodl-tmp/output/models/detect_remove_q05_seed123/final/` |
| `detect_remove_q05_seed456` | DONE | 6103/6103 (100%) | ✅ `/root/autodl-tmp/output/models/detect_remove_q05_seed456/final/` |
| `detect_remove_q09_seed42` | DONE | 6103/6103 (100%) | ✅ `/root/autodl-tmp/output/models/detect_remove_q09_seed42/final/` |

`detect_remove_q05_seed456` 在 `/root/provenance_weight_training/logs/` 中有一个旧日志显示 "Terminated"（7404/8477 步，87%），那是之前某次运行（步数不同，应该是参数不同的旧版本），被 kill 后已重跑并成功完成。

### westd-30476 当前状态

- **GPU**: 4x NVIDIA RTX PRO 6000 (96GB)，GPU 2 正在运行 `detect_remove_q07_seed42`（41.7GB VRAM, 95% 利用率），GPU 0/1/3 空闲
- **磁盘**: root 37% (20GB free), /dev/sda2 3% (816GB free), 充裕
- **活跃进程**: PID 36443，`detect_remove_q07_seed42` 训练中

### 结论

3 个实验全部成功完成，registry 状态也是 DONE。如果有人报告它们 failed，可能是看到了旧的 "Terminated" 日志或 registry 在中间某一刻的状态（后来已被更新为 DONE）。无需重试。

---
