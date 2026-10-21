# ops gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260519T130604_result.json`
- **Structured JSON:** [`4ebb096408571f56a33e.json`](../../sessions/4e/4ebb096408571f56a33e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态摘要

```
GPU 0: ALIVE  Qwen3-8B CWM eval  6456/9784 (66.0%)  running_acc=64.0%  ETA ~6.5h (≈03:30 May 20)
GPU 1: NEW JOB  DeepSeek CWM e3 eval  24/9784 (0.2%)  batch_size=1  刚启动 ~4min  ETA ~60h+
GPU 2: ALIVE  DeepSeek CWM s42 eval  352/9784 (3.6%)  running_acc=59.3%  ETA ~12h (≈09:00 May 20)
GPU 3: 空闲  0MiB / 0%
磁盘: 数据盘 196G/250G (79%, 余55G)  系统盘 20G/30G (67%, 余11G)
```

### CLS Ablation 结果（全部完成）

PID 830917 已退出，3 个 checkpoint 全部 eval 完成：

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass |
|-----------|----------|----------|---------|---------|
| ckpt-2200 | **85.34%** | **79.04%** | 67.56% | 90.53% |
| ckpt-3600 | 84.48% | 78.17% | 66.43% | 89.91% |
| ckpt-6633 | 85.29% | 78.44% | 66.28% | 90.60% |

**ckpt-2200 是最优 checkpoint**（accuracy 和 f1_macro 均最高）。ckpt-6633 accuracy 接近但 f1_macro 略低（recall_fail 53.4% vs 56.4%）。ckpt-3600 两项指标均最低。

### 关注点

1. **GPU 1** — 有个新的 DeepSeek CWM **e3** eval（非 s42）在跑，batch_size=1，按当前速度跑完需要约 60 小时。这个是谁启动的？是否需要？
2. **GPU 2** — DeepSeek CWM s42 eval 活着，running_acc=59.3%，batch_size=4，约 12 小时跑完。
3. **GPU 3** — 空闲可用。

---
