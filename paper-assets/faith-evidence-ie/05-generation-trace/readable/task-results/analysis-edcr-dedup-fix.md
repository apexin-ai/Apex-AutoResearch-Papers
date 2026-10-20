# analysis edcr dedup fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_dedup_fix_20260518T084728_result.json`
- **Structured JSON:** [`bd3a8639c897c656318d.json`](../../sessions/bd/bd3a8639c897c656318d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

## 7 个独立方法数据表

| Method | Rel-F1 | Evi-F1 | EDCR |
|---|---|---|---|
| SFT_baseline | 0.4049 | 0.7986 | 0.6982 |
| RSFT_CED (s44) | 0.4621 | 0.8050 | 0.6350 |
| RSFT_flatNLI | 0.4561 | 0.8076 | 0.6505 |
| RSFT_topk3 | 0.4454 | 0.8088 | 0.6635 |
| DPO_1ep | 0.4034 | 0.8088 | 0.7139 |
| SFT_no_evidence | 0.4893 | 0.0000 | 0.0000 |
| CED_reranker | 0.4864 | 0.8188 | 0.6156 |

## Spearman 相关

**EDCR vs Rel-F1 (n=7): ρ = -1.0000, p = 0.000**

比预期的 ρ=-0.8929 更强 — 7 个方法的 EDCR 排名与 Rel-F1 排名完全单调反序：EDCR 越低，Rel-F1 越高，无一例外。

同时 EDCR vs Evi-F1 相关性很弱 (ρ=0.25, p=0.59)，说明 EDCR 捕捉的信息与 Evi-F1 正交。

脚本已更新到 `/root/autodl-tmp/scripts/edcr_dedup_correlation.py`。

---
