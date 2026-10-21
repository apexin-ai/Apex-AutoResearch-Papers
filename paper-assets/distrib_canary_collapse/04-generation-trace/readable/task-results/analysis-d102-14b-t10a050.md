# analysis d102 14b t10a050

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-14b-t10a050_20260522T174243_result.json`
- **Structured JSON:** [`4e411e620bffdc369f79.json`](../../sessions/4e/4e411e620bffdc369f79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇报：

```
PermG fwd: 3/8  (FDR-corrected)
PermG rev: 0/8
Method comparison:
  naive_xcorr_D111:     4/8
  diff_xcorr_fdr:       0/8
  threshold_onset:      0/8
  PermG_fdr:            3/8
  TY_granger:           1/8
K≥3 consensus:          0/8
```

**PermG FDR p-values (forward):**

| Pair | F-stat | p_raw | p_fdr | sig_fdr |
|------|--------|-------|-------|---------|
| token_entropy→distinct_1 | 367.36 | 0.0302 | 0.0604 | No |
| token_entropy→distinct_2 | 107.64 | 0.0486 | 0.0604 | No |
| token_entropy→distinct_3 | 22.02 | 0.0558 | — | No |
| token_entropy→mauve | 0.22 | 0.6697 | — | No |
| ece→distinct_1 | 448.69 | 0.0036 | **0.0144** | **Yes** |
| ece→distinct_2 | 443.09 | 0.0044 | **0.0144** | **Yes** |
| ece→distinct_3 | 69.41 | 0.0068 | **0.0144** | **Yes** |
| ece→mauve | 0.19 | 0.7211 | — | No |

**关键发现 — onset boundary 在 1.4B 不一致：**

- **410M α=0.50 s42**: PermG fwd = **6/8**, K≥3 = robust
- **1.4B α=0.50 s42**: PermG fwd = **3/8**, K≥3 = **0/8**

仅 ece→distinct_{1,2,3} 通过 FDR 校正（全部来自 ece canary）。token_entropy 两个 pair 原始 p 值 <0.05 但 FDR 后失去显著性。threshold_onset 全部失败（downstream 均无 3σ 突破）。mauve pair 完全无信号。

**解读**：1.4B 在 α=0.50 处信号显著弱于 410M——α_c(onset) 随 scale 上移。这意味着更大模型对 50% 合成数据混合更具抗性，onset boundary 不是 scale-invariant 的。

---
