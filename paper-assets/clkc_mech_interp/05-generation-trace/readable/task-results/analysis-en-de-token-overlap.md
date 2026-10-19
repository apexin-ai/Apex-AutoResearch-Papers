# analysis en de token overlap

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_en-de-token-overlap_20260523T044131_result.json`
- **Structured JSON:** [`0ec81385d90479872248.json`](../../sessions/0e/0ec81385d90479872248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 1 完成。结果：

**EN-DE Token Overlap (Llama-3.1-8B-Instruct)**

| 指标 | EN-DE | EN-ZH (参考) |
|------|-------|-------------|
| Type-level Jaccard | 0.4210 | ~0.03-0.04 |
| Per-sample Jaccard mean | **14.77%** | ~3-4% |
| Per-sample Jaccard median | 13.47% | — |
| Per-sample Jaccard std | 7.84% | — |
| Per-sample Jaccard range | [1.3%, 47.3%] | — |
| Overlap/EN | 31.2% | — |
| Overlap/DE | 20.9% | — |

EN-DE 的 token overlap 约为 EN-ZH 的 **4.2x**，符合预期（共享拉丁字母 + 大量 cognate subword）。

- 脚本路径：`/root/clkc_mech_interp/src/token_overlap_en_de.py`
- 结果文件：`/root/clkc_mech_interp/data/llama31/token_overlap_en_de.json`
- Phase 2（correlation）：DE bootstrap 完成后执行 `python src/token_overlap_en_de.py --phase full` 即可

---
