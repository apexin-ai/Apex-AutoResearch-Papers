# analysis a050 postd093 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a050_postd093_s42_20260520T030638_result.json`
- **Structured JSON:** [`a08528a746cf3fddb693.json`](../../sessions/a0/a08528a746cf3fddb693.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis 完成，`5method_leadlag.json` 已生成。

## 结果报告

### PermG Forward: **6/8** (与 pre-D093 一致)

| pair | p_fdr | sig | dir |
|------|-------|-----|-----|
| token_entropy→distinct_1 | 0.0016 | **Yes** | fwd |
| token_entropy→distinct_2 | 0.0054 | **Yes** | fwd |
| token_entropy→distinct_3 | 0.0136 | **Yes** | fwd |
| token_entropy→mauve | 0.3983 | No | fwd |
| ece→distinct_1 | 0.0008 | **Yes** | fwd |
| ece→distinct_2 | 0.0076 | **Yes** | fwd |
| ece→distinct_3 | 0.0036 | **Yes** | fwd |
| ece→mauve | 0.2312 | No | fwd |

### 5-Method Summary

| Method | fwd sig / total |
|--------|----------------|
| naive_xcorr | 3/8 |
| diff_xcorr | 2/8 |
| threshold_onset | 8/8 |
| perm_granger | **6/8** |
| ty_granger | 4/8 |

**结论**: PermG 6/8 ≥ 6/8 阈值达标。D093 padding side 变更（left→right）未影响 onset 判定——两个 mauve pair 不显著的模式与 pre-D093 一致，6 个 distinct pair 全部 fwd 显著。C006 混杂可降级。

---
