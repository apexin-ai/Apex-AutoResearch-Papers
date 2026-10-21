# analysis 2seed nve robustness

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_2seed-nve-robustness_20260519T150234_result.json`
- **Structured JSON:** [`9557f2ae83df1de446a8.json`](../../sessions/95/9557f2ae83df1de446a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。

## 1. Baseline VE_Ratio 对比 (35K-105K)

| Step | s1_ve | s2_ve | s2/s1 |
|------|-------|-------|-------|
| 35K | 0.2412 | 0.3096 | 1.283 |
| 45K | 0.3310 | 0.4872 | 1.472 |
| 55K | 0.4035 | 0.5681 | 1.408 |
| 65K | 0.5629 | 0.8983 | **1.596** |
| 75K | 0.7194 | 0.5788 | 0.805 |
| 85K | 0.7007 | 0.6805 | 0.971 |
| 95K | 0.6320 | 0.7641 | 1.209 |
| 105K | 0.6564 | 0.7423 | 1.131 |

s2 在 65K 处 ve_ratio 远高于 s1（0.898 vs 0.563），导致 s2 归一化分母更大、NVE 更低。这是 flip 的主要原因。

## 2. 1.5× Threshold 分类结果

| 统计项 | 值 |
|--------|-----|
| 总 configs | 53 |
| s1 归一化 CIVO | 19 |
| s2 归一化 CIVO | 14 |
| **分类翻转** | **5** |

## 3. 5 个翻转 configs（全部 s1=CIVO → s2=OK）

| Config | NVE_s1 | NVE_s2 |
|--------|--------|--------|
| exp_008d_civo_trigger_s1 | **2.093** | 1.422 |
| exp_008d_civo_trigger_s3 | **1.528** | 1.427 |
| exp_009b_008d_walker_s2 | **1.619** | 1.100 |
| exp_018v2_full_sgs_walker_s1 | **1.661** | 1.374 |
| exp_024b_cheetah_no_dt_emb_s1 | **1.742** | 1.237 |

所有 flip 方向一致：s1 判 CIVO、s2 判 OK。原因是 s2 在 45K-65K 的 ve_ratio 分母偏高（尤其 65K 的 0.898 spike），使 NVE 被压低。

## 4. 被关注的 configs

| Config | NVE_s1 | NVE_s2 | 状态 |
|--------|--------|--------|------|
| **exp_009b_008d_walker_s2** | 1.619 (CIVO) | 1.100 (OK) | **FLIP** |
| **exp_008d_civo_trigger_s3** | 1.528 (CIVO) | 1.427 (OK) | **FLIP** |
| exp_008f_no_dt_emb_s4 | 1.415 (OK) | 1.457 (OK) | 稳定 OK（双边均 <1.5） |
| exp_015b_frozen_dt_emb | 1.454 (OK) | 1.303 (OK) | 稳定 OK |

008f_s4 和 015b 在两个 seed 下都低于 1.5，分类一致。009b 和 008d_s3 在 s1 下刚过线、s2 下刚不过线，是典型边界 case。

---
