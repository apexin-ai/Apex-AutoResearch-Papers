# extract s4 ve profile

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_s4_ve_profile_20260519T230704_result.json`
- **Structured JSON:** [`1c6aa7741474ea4215db.json`](../../sessions/1c/1c6aa7741474ea4215db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 seed 的 ve_ratio profile CSV 全部就位：

| 文件 | 行数 | Step 范围 |
|------|------|-----------|
| `exp_001_baseline_s1_ve_profile_full.csv` | 已有 | — |
| `exp_001_baseline_s2_ve_profile_full.csv` | 52 | 5,000 – 512,000 |
| `exp_001_baseline_s3_ve_profile_full.csv` | 52 | 5,000 – 510,000 |
| `exp_001_baseline_s4_ve_profile_full.csv` | 52 | 5,000 – 512,000 |

所有 CSV 保存在 `artifacts/` 目录下。s3 最终 step 为 510K（比其余少 2K），其余三个都跑到 512K。末期 ve_ratio 均收敛到 ~0.69–0.71 区间。

---
