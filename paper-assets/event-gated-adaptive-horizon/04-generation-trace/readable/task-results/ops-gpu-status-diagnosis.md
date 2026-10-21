# ops gpu status diagnosis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-diagnosis_20260515T073645_result.json`
- **Structured JSON:** [`4b6f1f049dcb410d3a0d.json`](../../sessions/4b/4b6f1f049dcb410d3a0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fig1 updated — 008e_v3 s2 (浅蓝色虚线) 现在有三角形 marker，灰度打印下可区分。

---

## GPU 诊断结果

| | cuda:0: exp_009d_baseline_walker_s1 | cuda:1: exp_009e_008d_walker_s1 |
|---|---|---|
| PID | 122271 | 119108 |
| 运行时间 | 1h06m | 1h55m |
| 进程状态 | Rl+ (正常运行) | Rl (正常运行) |
| 显存 | 4163 MiB / 97887 MiB (4.3%) | 2753 MiB / 97887 MiB (2.8%) |
| GPU 利用率 | 33% | 18% |
| 训练步数 | 32K / 500K (6.4%) | 48K / 105K (45.7%) |
| 最新 train_return | ~400-493 | ~95-255 |
| metrics 最后写入 | 刚刚 (活跃) | ~5 分钟前 (活跃) |

**低利用率原因：正常。** DreamerV3 是 CPU/GPU 交替式训练（环境交互在 CPU，模型训练在 GPU），加上这两块 RTX PRO 6000 Black 各有 98GB 显存，DreamerV3 的小模型只用几 GB，显存占比和 GPU 平均利用率天然就低。两个实验都在正常推进，无需干预。

---
