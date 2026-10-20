# ops mistral theta fixed n10

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mistral-theta-fixed-n10_20260522T082124_result.json`
- **Structured JSON:** [`6b0ae8e9677731eeadf6.json`](../../sessions/6b/6b0ae8e9677731eeadf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果汇总：

## Mistral θ-fixed Recomputation (n=10 theta)

### θ_fixed
| | n=6 (旧) | n=10 (新) |
|---|---|---|
| θ_fixed | -1.0652 | **-1.0876** |

### 10 个 clean theta_MLE
| Seed | theta_MLE |
|------|-----------|
| s1 | -1.156851 |
| s2 | -0.962674 |
| s3 | -0.973253 |
| s4 | -1.169343 |
| s5 | -1.100047 |
| s6 | -1.140540 |
| s7 | -1.075488 |
| s8 | -1.145650 |
| s9 | -1.124025 |
| s10 | -1.028590 |

### 6 个 clean lz*_fixed (θ=-1.0876)
| Seed | lz\*\_fixed |
|------|------------|
| s1 | 5.3714 |
| s2 | -1.3154 |
| s3 | 3.0571 |
| s8 | 5.7690 |
| s9 | 3.5155 |
| s10 | 3.3474 |
| **mean** | **3.2908** |
| **std** | **2.5217** |

### Contam lz*_fixed
| Condition | lz\*\_fixed |
|-----------|------------|
| contam_15 | -3.4813 |
| contam_50 | -11.3279 |

### Cohen's d 对比

| | 旧 (n=6) | 新 (θ from n=10) |
|---|---|---|
| contam_15 d | 2.59 [1.45, 9.00] | **2.69 [1.53, 9.06]** |
| contam_50 d | 5.60 [3.71, 18.16] | **5.80 [3.87, 18.45]** |

### 重要说明
s4-s7 的 response vectors 随 19912 服务器释放而丢失（checkpoints 未迁移到 35694）。当前 Cohen's d 的分母仍基于 **6 个** clean seed 的 lz\*_fixed 分布，θ_fixed 则确实用了全部 10 个 theta_MLE 的均值。

结果已保存到 `/root/autodl-tmp/ctrl_contam_mistral/results/theta_fixed_n10_recompute.json`。

---
