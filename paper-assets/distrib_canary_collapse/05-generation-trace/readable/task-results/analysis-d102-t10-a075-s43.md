# analysis d102 t10 a075 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t10-a075-s43_20260522T070343_result.json`
- **Structured JSON:** [`0cb2afbf72ae198d8fe6.json`](../../sessions/0c/0cb2afbf72ae198d8fe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 分析完成。Registry 已有记录（之前已标记 DONE/success），artifact 已注册。

## 结果

| Method | Forward | Reverse |
|--------|---------|---------|
| **PermG FDR** | **6/8** | 0/8 |
| Diff xcorr FDR | 7/8 | 7/8 |
| Threshold onset | 0/8 | — |
| TY Granger | 0/8 | — |
| Robust (≥3/5) | 4/8 | — |

**Cross-seed 一致**：s43 PermG=6/8 完全匹配 s42 基准。6 个显著 pair 均为 distinct_1/2/3（mauve 对两个 canary 都不显著），fwd≫rev 方向性不对称保持。

---
