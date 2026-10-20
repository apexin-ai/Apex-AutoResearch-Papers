# ops check s0 training progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-s0-training-progress_20260520T195051_result.json`
- **Structured JSON:** [`67162fa0ded5529740d1.json`](../../sessions/67/67162fa0ded5529740d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

### westd-29999 (RTX PRO 6000 Black ×4, 96GB each)
| GPU | 状态 | 详情 |
|-----|------|------|
| cuda:0 | **空闲** | 0 MiB, 0% util |
| cuda:1 | **Gemma-2 d050 s0 训练** | PID 406532, 95.4/97.9 GB, 97% util |
| cuda:2 | **空闲** | 0 MiB, 0% util |
| cuda:3 | **Qwen-14B d025 s0 eval** | PID 420512, 32.7/97.9 GB, 97% util |

### cqa1-21977 (RTX 4090D ×1, 24GB)
| GPU | 状态 | 详情 |
|-----|------|------|
| cuda:0 | **Qwen-7B d100 s0 训练** | PID 389216, 20.1/24.6 GB, 93% util |

## 训练进度

| 实验 | 服务器 | GPU | Step | 进度 | ETA | 当前 Loss | 备注 |
|------|--------|-----|------|------|-----|-----------|------|
| Qwen2.5-7B d100 s0 | cqa1 | cuda:0 | 1454/4159 | **35%** | ~2h55m | 0.83–1.12 (epoch 0.35) | 正常训练中 |
| Gemma-2-9B d050 s0 | westd | cuda:1 | 2646/3642 | **73%** | ~44min | 1.06–1.30 (epoch 0.62) | 正常训练中 |
| Qwen2.5-14B d025 s0 | westd | cuda:3 | 3384/3384 | **训练完成** | — | 最终 ~0.88–1.06 | 已转入 MMLU eval: 4429/14042 (31%), ETA ~13min |

**注意：PID 均已变化**（cqa1: 313407→389216, westd: 311554→420512, 314029→406532），进程应是重启过或 sweep 自动轮转。

**westd cuda:0 和 cuda:2 均空闲，可调度新任务。**

---
