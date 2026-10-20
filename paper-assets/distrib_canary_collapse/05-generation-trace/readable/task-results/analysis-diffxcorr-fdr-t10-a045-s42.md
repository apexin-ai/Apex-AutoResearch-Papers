# analysis diffxcorr fdr t10 a045 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diffxcorr-fdr-t10-a045-s42_20260523T214417_result.json`
- **Structured JSON:** [`0aef4dd00c9b01510eda.json`](../../sessions/0a/0aef4dd00c9b01510eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果总结

**α=0.45, s42, T=10, Pythia-1.4B** 标准 5-method 分析（true_3sigma_d105, FDR 校正）：

| 方法 | Forward | Reverse |
|------|---------|---------|
| DiffXCorr (FDR) | **8/8** | **8/8** |
| PermG (FDR) | 0/8 | 0/8 |
| Threshold Onset | 0/8 | — |
| TY Granger | 2/8 | — |
| Naive XCorr | 2/8 | — |
| **Robust pairs (≥3/5)** | **0/8** | |

**关键发现**：DiffXCorr 8/8 经 BH-FDR 校正后仍全部显著（p_fdr 范围 0.024–0.038），不像 α=0.50 s42 校正后从 8/8 降到 4/8。但 DiffXCorr **正反向均 8/8**（双向对称），说明是并发共变而非因果领先，且无其他方法支持——robust pairs = 0/8。此实验在 phase diagram 中应归类为**无可靠 lead-lag 信号**。

产出已写入：
- `artifacts/D102_14b_t10_a045_s42_fp32_d3.json`
- `artifacts/_project/diffxcorr_fdr_t10_a045_s42_20260523.md`
- Registry `scale_14b_t10_a045_s42_fp32` metrics 已更新

---
