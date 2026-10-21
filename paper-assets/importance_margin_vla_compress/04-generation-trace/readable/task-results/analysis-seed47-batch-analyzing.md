# analysis seed47 batch analyzing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed47_batch_analyzing_20260529T081508_result.json`
- **Structured JSON:** [`c201b8431b5dcec3866e.json`](../../sessions/c2/c201b8431b5dcec3866e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验 registry 已更新完毕。汇总：

| exp_id | SR | 5-seed ref | 偏差 | 状态 |
|--------|-----|------------|------|------|
| `eval_pi05_random_k095_long_seed47_cqa1` | **62.0%** | 61.2±0.7 | +1.1σ | ✓ 正常完成 |
| `eval_pi05_random_k09_long_seed47_cqa1` | **30.8%** | 33.6±1.2 | **-2.3σ** | ✓ 正常完成 |
| `eval_pi05_random_k085_long_seed47_cqa1` | **43.4%** | 44.9±1.3 | -1.2σ | ✓ 正常完成 |
| `eval_pi05_l2norm_k085_long_seed47_w38` | **77.8%** | 78.1±1.0 | -0.3σ | ✓ 正常完成 |

Random k=0.9 seed47 (30.8%) 偏离 5-seed mean 超过 2σ，加入 6-seed 后会拉低该条件的均值至约 33.1%。其余三个实验均在正常方差范围内。

---
