# code director kill cleanup v4

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_director-kill-cleanup-v4_20260521T080440_result.json`
- **Structured JSON:** [`d034fbdea4f26d9b82e4.json`](../../sessions/d0/d034fbdea4f26d9b82e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 步执行完毕。汇总如下。

---

## 最终 GPU 状态

| GPU | PID | 任务 | 显存 | Util |
|-----|-----|------|------|------|
| cuda:0 | 103287 | **s6 eval** (loading model) | 8568 MiB | 92% |
| cuda:1 | 103888 | **s9 train** (36/939 steps) | 27988 MiB | 96% |
| cuda:2 | 97791 | **GRPO** (397/14042 steps) | 9070 MiB | 73% |
| cuda:3 | 102570 | **s7 train** (175/939 steps) | 34834 MiB | 95% |

**注意**: s8 (PID 99807) 在执行前已自行结束，不在进程列表中。s7 因 cuda:0 被 s5 eval 占用，改为在 cuda:3 启动。

---

## GRPO 进度 (cuda:2)

- **Step**: 397/14042 (3%)
- **Epoch**: 0.0235
- **Speed**: ~5.16s/step (ETA ~19.5h)
- **Reward**: 最近 mean 在 0.1–0.4 间波动，entropy ~0.88

---

## s4/s5 Eval 结果 (clean baseline seeds)

| Condition | Accuracy | lz* | theta_MLE | n_items |
|-----------|----------|-----|-----------|---------|
| **clean_s4** | **67.86%** | 8.967 | -0.109 | 14042 |
| **clean_s5** | **67.87%** | 8.532 | -0.088 | 14042 |

两个 clean seed 的 accuracy 高度一致 (~67.9%)，lz* 都很大 (8.5–9.0)，说明 clean SFT 模型的答题模式与 IRT 预测偏差较大但一致。

---

## HT Post-RL 结果

| Stage | Accuracy (Overall) | Accuracy (Seen) | Accuracy (Unseen) | lz* (Overall) | lz* (Seen) | lz* (Unseen) |
|-------|-------|------|--------|------|------|------|
| **Base** | 70.24% | 70.04% | 70.27% | 5.970 | 2.498 | 5.427 |
| **SFT** | 73.39% | **83.10%** | 71.67% | 2.914 | **-0.395** | 3.278 |

SFT 后 seen items accuracy 从 70.04% → 83.10% (+13pp)，而 unseen 仅 70.27% → 71.67% (+1.4pp)。lz* seen 从 2.50 降到 **-0.40**（变为负值，说明 seen items 的答题模式变得"过于合理"——与 contamination 信号一致）。

---
