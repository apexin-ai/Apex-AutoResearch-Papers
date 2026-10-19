# analysis nested cv

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nested_cv_20260519T112959_result.json`
- **Structured JSON:** [`027f4f6960ba39d1eb49.json`](../../sessions/02/027f4f6960ba39d1eb49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Nested 5-fold CV 全部完成。结果如下：

## R1-8B (209 traces, 9667 steps)

| Fold | Best Layer | W_hs | HS Prec | Text Prec | Δ Prec |
|------|-----------|------|---------|-----------|--------|
| 0 | L12 | 3 | 0.6634 | 0.4427 | +0.2206 |
| 1 | L12 | 3 | 0.5701 | 0.4257 | +0.1444 |
| 2 | L12 | 5 | 0.5437 | 0.3688 | +0.1750 |
| 3 | L13 | 5 | 0.5786 | 0.4082 | +0.1704 |
| 4 | L14 | 3 | 0.4580 | 0.2985 | +0.1595 |
| **Mean** | | | **0.563 ± 0.066** | **0.389 ± 0.051** | **+0.174 ± 0.026** |

## OT-7B (228 traces, 18260 steps)

| Fold | Best Layer | W_hs | HS Prec | Text Prec | Δ Prec |
|------|-----------|------|---------|-----------|--------|
| 0 | L23 | 5 | 0.3755 | 0.2432 | +0.1323 |
| 1 | L21 | 5 | 0.5327 | 0.3184 | +0.2143 |
| 2 | L27 | 5 | 0.4455 | 0.2577 | +0.1877 |
| 3 | L26 | 5 | 0.3806 | 0.2543 | +0.1263 |
| 4 | L26 | 5 | 0.3715 | 0.2134 | +0.1581 |
| **Mean** | | | **0.421 ± 0.062** | **0.257 ± 0.034** | **+0.164 ± 0.033** |

**HS > Text in 10/10 outer folds (both models)**, precision advantage consistent and substantial.

结果已保存到服务器：
- `artifacts/nested_cv/results.json` (完整 JSON)
- `artifacts/nested_cv/report.txt` (可读报告)

关键发现：
- R1-8B 稳定选择 early layers (L12-14)，OT-7B 稳定选择 deep layers (L21-27)
- OT-7B 的 W_hs 全部选了 5，W_txt 全部选了 3，超参选择高度一致
- Δ precision 标准差小 (R1-8B: 0.026, OT-7B: 0.033)，说明 HS 优势不是 hyperparameter overfitting 造成的

---
