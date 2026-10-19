# ops post restart4 28034 eval survival

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart4-28034-eval-survival_20260519T135321_result.json`
- **Structured JSON:** [`8ecb53f4c4e7fed2ca07.json`](../../sessions/8e/8ecb53f4c4e7fed2ca07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 状态总览

| 任务 | GPU | 状态 | 详情 |
|------|-----|------|------|
| **exp-004 trimmed eval** | 0 | **已死** | 服务重启时被杀 |
| **exp-016 ActAdd re-eval** | 3 | **存活** | alpha=2.0, 进度 220/362 |
| **exp-008v3 training** | 1+2 | **存活** | step 1334/8000 (17%), ~23s/it |

### GPU 状态
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 17.7/32.6 GB (残留显存，无活跃进程) |
| 1 | 0% | 31.4/32.6 GB |
| 2 | 0% | 30.7/32.6 GB |
| 3 | 23% | 16.5/32.6 GB |

### exp-004 eval 详情
- **ckpt-500**: 已完成 (ToF=0.0939, NoF=0.8895, SYCONScore=0.1699)
- **ckpt-2000**: 日志显示模型已加载、开始跑 362 pairs，但结果目录只有 eval.log，无 json — **跑到一半被杀**
- **ckpt-8000**: 未开始
- 需要重启，从 ckpt-2000 继续

### exp-016 re-eval 详情
- 已完成 alpha=0, 0.5, 1.0；当前跑 alpha=2.0 (220/362)，还剩 alpha=5.0
- 预计再需 ~1-2 小时

### exp-008v3 training 详情
- Step 1334/8000, ETA ~42h
- GPU util 显示 0% 但进程活跃且持续出 log（可能刚好在 CPU 阶段）
- combined_mean reward ≈ 0.5

---

**需要重启 exp-004 eval。** 要现在重启吗？可以跳过 ckpt-500（已完成），只跑 ckpt-2000 和 ckpt-8000。

---
