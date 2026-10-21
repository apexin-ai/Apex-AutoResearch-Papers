# extract cheetah 5seed baseline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_cheetah-5seed-baseline_20260519T235931_result.json`
- **Structured JSON:** [`d242f46eaf800a89f4a7.json`](../../sessions/d2/d242f46eaf800a89f4a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Per-seed ve_ratio (mean, 35K+)**:
| Seed | Rows | Step range | Mean ve_ratio |
|------|------|-----------|---------------|
| s0 | 21 | 5K–205K | 0.5313 |
| s1 | 21 | 5K–205K | 0.5386 |
| s2 | 21 | 5K–205K | 0.6352 |
| s3 | 21 | 5K–202K | 0.5430 |
| s4 | 32 | 5K–302K | 0.6557 |

注：s3 在 145K 后 step 偏移 +7K，s4 在 75K 后偏移 -1K 且 extended 到 302K。已用 10K rounding 对齐。

**5-seed mean profile (aligned, key checkpoints)**:
| Step | mean_ve_ratio | std | mean_eval_return |
|------|--------------|-----|-----------------|
| 40K | 0.1257 | 0.0160 | 302.9 |
| 60K | 0.3593 | 0.0921 | 319.1 |
| 80K | 0.4341 | 0.0403 | 420.7 |
| 100K | 0.5690 | 0.0748 | 428.2 |
| 120K | 0.6289 | 0.1377 | 457.5 |
| 140K | 0.6395 | 0.0908 | 498.5 |
| 160K | 0.6469 | 0.0674 | 528.7 |
| 180K | 0.6962 | 0.0426 | 539.0 |
| 200K | 0.7481 | 0.2126 | 549.0 |

**Exact @65K (all 5 seeds have this step)**:
- 5-seed mean ve_ratio: **0.3918 ± 0.0285**

**exp_026 NVE @65K**:
- exp_026_s0: **21.85x**
- exp_026_s1: **27.67x**

输出文件：
- `artifacts/cheetah_baseline_{s0,s1,s2,s3,s4}_ve_profile.csv` — per-seed profiles
- `artifacts/cheetah_5seed_mean_ve_ratio.csv` — 5-seed aligned mean

---
