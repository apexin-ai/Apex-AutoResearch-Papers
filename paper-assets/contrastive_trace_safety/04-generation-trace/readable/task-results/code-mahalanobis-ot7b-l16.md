# code mahalanobis ot7b l16

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mahalanobis_ot7b_l16_20260517T131912_result.json`
- **Structured JSON:** [`348bdca979afc2ab5933.json`](../../sessions/34/348bdca979afc2ab5933.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

## 结果总结

**Mahalanobis distance 在 OT-7B 上同样失败，失败模式与 R1-8B 完全一致。**

### MD 分布统计 (pca_64)

| 指标 | R1-8B | OT-7B |
|------|-------|-------|
| safe_md_mean | 6.66 | 7.68 |
| post_md_mean | 6.73 (jb_pre) / 6.64 (jb_post) | 7.71 |
| **separation** | **~0.07** | **~0.03** |

### 跨所有 PCA 维度的 separation

| PCA dim | safe MD | post MD | separation |
|---------|---------|---------|-----------|
| 16 | 3.85 | 3.80 | **-0.048** |
| 32 | 5.46 | 5.48 | +0.012 |
| 64 | 7.68 | 7.71 | +0.031 |
| 128 | 10.70 | 10.71 | +0.004 |
| 256 | 14.90 | 14.80 | **-0.093** |

### False Alarm vs True Positive (pca_64, k=3)

| Threshold | False Alarm Rate | True Positive Rate |
|-----------|-----------------|-------------------|
| p50 | **87.2%** | 38.5% |
| p75 | **57.4%** | 23.1% |
| p90 | **17.0%** | 15.4% |
| p95 | **4.3%** | 0.0% |

False alarm rate ≥ true positive rate at **every** threshold — detector 在 pre-commitment 段比 post-commitment 段触发更频繁。

### 结论

1. OT-7B 上 Mahalanobis 完全无判别力（separation ≈ 0）
2. 失败原因与 R1-8B 一致：判别信号在 PCA minor components 中，principal directions 无法捕获
3. 表面上的高 crossing rate (p50) 纯粹是长序列 + 低阈值的统计伪影

结果已保��至 `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mahalanobis_ot7b/results.json`

---
