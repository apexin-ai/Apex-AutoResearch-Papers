# code exp 005 trajguard

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_005_trajguard_20260516T203547_result.json`
- **Structured JSON:** [`0154f7a1b93cc60d5b0e.json`](../../sessions/01/0154f7a1b93cc60d5b0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed and registered. Here's the full results summary:

---

## exp-005 TrajGuard Mahalanobis Distance — NEGATIVE RESULT

**核心发现：** Mahalanobis distance 从 safe 参考分布出发无法检测 commitment point。Safe/jailbreak-pre/jailbreak-post 三组的 MD 分布几乎完全相同。

### MD 分布对比 (PCA-64, Layer 14)

| Group | MD Mean | MD Std |
|-------|---------|--------|
| Safe val | 6.66 | 0.79 |
| JB pre-commit | 6.73 | 0.74 |
| JB post-commit | 6.64 | 0.86 |

### 检测结果 (K=5, 标准窗口)

| Config | Pctl | CrossRate | LeadMean |
|--------|------|-----------|----------|
| pca_64 | p75 | 30.2% | +16.4 |
| pca_32 | p75 | 27.9% | +8.8 |
| pca_128 | p75 | 18.6% | +17.2 |
| pca_64 | p85 | 11.6% | +3.4 |
| p90+ thresholds | — | 0-9% | — |

### Delta（相对变化）方法
- 最大 crossing_rate = 2.3%（基本无效）

### 与现有方法对比

| Method | CrossRate | LeadMean |
|--------|-----------|----------|
| Static LR L14 | 46.5% | -2.0 |
| Temporal LR W=15 | 76.7% | -1.1 |
| GRU multi-7L h=256 | 76.7% | +4.7 |
| **TrajGuard best (K=5)** | **30.2%** | **+16.4** |

**结论：** 高 lead time (+16~+30) 说明"检测"发生在 trace 开头（噪声），不是 commitment 转折点。TrajGuard 的无监督 anomaly detection 思路不适用于此数据——commitment 的信号在 supervised 的判别方向上，不在主成分方向上。

---
