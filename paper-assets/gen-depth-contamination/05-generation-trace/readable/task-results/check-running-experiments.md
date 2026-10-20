# check running experiments

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_experiments_20260524T095747_result.json`
- **Structured JSON:** [`6b690e847760e209a073.json`](../../sessions/6b/6b690e847760e209a073.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

- **arxiv_multi_source**: **DONE** | PID 165918 已退出
  - K* = 3（max depth with AUC > 0.60）
  - Pairwise AUC: 0v1=0.9948, 1v2=0.8581, 2v3=0.6436, 3v4=0.544, 4v5=0.5299
  - Pairwise JSD: 0v1=0.203, 1v2=0.077, 2v3=0.020, 3v4=0.008, 4v5=0.008
  - Ordinal 6-class: MAE=0.826, Acc=47.7%
  - Top features: freq_entropy, surp_std, surp_mean

- **code_domain_olmo**: **RUNNING** | 已运行 35min | depth 3 生成中 180/344 batches (52%)
  - depth 0-2 已完成，depth 3 进行中，还剩 depth 4-5
  - 速度 ~3.2s/it，depth 3 剩余约 9min，整体预计还需 ~40-50min

- **gemma27b_filtering**: **RUNNING** | 已运行 11min | 3 strategies × 3 seeds = 9 runs
  - 已完成: no_filter_seed42, binary_ours_seed42, graduated_a09_seed42 (3/9)
  - 进行中: no_filter_seed123（训练完成，eval 加载中）(4/9)
  - 剩余: 5 runs，每 run ~4min，预计还需 ~20-25min

## GPU 状态
```
cuda:0:  36% util | 12,139 / 97,887 MiB  (arxiv 已完成，残留显存或其他进程)
cuda:1:  85% util | 14,308 / 97,887 MiB  (code_domain_olmo 活跃)
cuda:2:  36% util |  8,729 / 97,887 MiB  (无实验，可能有其他进程)
cuda:3:  35% util |  8,729 / 97,887 MiB  (gemma27b_filtering 活跃)
```

---
