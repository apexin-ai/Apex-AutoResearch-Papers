# ops s2ext full ve profile

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s2ext-full-ve-profile_20260519T181637_result.json`
- **Structured JSON:** [`1da8180cc734693fd122.json`](../../sessions/1d/1da8180cc734693fd122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**数据来源**：tensorboard tfevents（metrics.jsonl 只有 train_return 等基础字段，无 value_mean）。用 tbparse 提取 `scalars/value_mean` + `scalars/eval_return`。

**s1 不存在**，只有 s2/s3/s4。

### @105K ve_ratio 三 seed 对比

| Seed | eval_return | value_mean | ve_ratio |
|------|------------|------------|----------|
| s2 | 443.46 | 329.16 | **0.7423** |
| s3 (102K) | 869.03 | 577.36 | **0.6644** |
| s4 | 922.82 | 576.07 | **0.6243** |

### s2 ve_ratio 收敛 profile（关键节点）

| Step | eval_return | value_mean | ve_ratio |
|------|------------|------------|----------|
| 35K | 250.88 | 77.66 | 0.310 |
| 65K | 205.84 | 184.90 | 0.898 |
| 105K | 443.46 | 329.16 | 0.742 |
| 202K | 932.12 | 627.96 | 0.674 |
| 302K | 960.76 | 664.71 | 0.692 |
| 402K | 862.93 | 663.90 | 0.769 |
| 512K | 945.68 | 664.53 | 0.703 |

s2 收敛后 ve_ratio 稳定在 **0.69–0.77** 区间（value_mean 饱和在 ~665，eval_return 波动造成 ve_ratio 抖动）。

CSV 已保存到 artifacts/:
- `exp_001_baseline_s2_ve_profile_full.csv` (49 rows, 35K–512K)
- `exp_001_baseline_s3_ve_profile_full.csv` (41 rows, 35K–430K)
- `exp_001_baseline_s4_ve_profile_full.csv` (36 rows, 35K–382K)

---
