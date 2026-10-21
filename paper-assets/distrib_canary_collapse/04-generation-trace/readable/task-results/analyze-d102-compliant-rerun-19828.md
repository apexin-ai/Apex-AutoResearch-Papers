# analyze d102 compliant rerun 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d102-compliant-rerun-19828_20260521T233647_result.json`
- **Structured JSON:** [`e242e58d546df416ca85.json`](../../sessions/e2/e242e58d546df416ca85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### D102 脚本版本确认
19828 上 `run_5method_analysis_d102.py` 已存在且合规：
- DOWNSTREAMS = `["distinct_1", "distinct_2", "distinct_3", "mauve"]`（无 perplexity）
- threshold = `true_3sigma_d105`（非 3x_sigma_drift）

### 输出文件确认
- JSON: `threshold_criterion: "true_3sigma_d105"` ✓
- downstreams 列表包含 mauve，无 perplexity ✓

### 结果

| 方法 | Forward sig | /8 |
|------|-----------|-----|
| Perm Granger (FDR) | 6/8 |
| Diff XCorr (FDR) | 6/8 |
| Threshold Onset | 6/8 |
| TY Granger | 6/8 |
| **Robust (≥3/5)** | **6/8** |

Reverse: 0/8（全部不显著，符合预期方向性）

### Significant pairs 完整列表

| Pair | Consensus | Methods |
|------|-----------|---------|
| token_entropy→distinct_1 | 4/5 | diff, threshold, perm, ty |
| token_entropy→distinct_2 | 4/5 | diff, threshold, perm, ty |
| token_entropy→distinct_3 | 4/5 | diff, threshold, perm, ty |
| token_entropy→mauve | 0/5 | — |
| ece→distinct_1 | **5/5** | naive, diff, threshold, perm, ty |
| ece→distinct_2 | **5/5** | naive, diff, threshold, perm, ty |
| ece→distinct_3 | **5/5** | naive, diff, threshold, perm, ty |
| ece→mauve | 1/5 | naive only |

旧的 perplexity+3x_sigma_drift 分析 PermG=8/8 确认无效。D102 合规重跑结果：**PermG fwd 6/8, rev 0/8, robust 6/8**。mauve 两对 pair 均不显著。

---
