# analysis epoch scierc rho text based

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epoch_scierc_rho_text_based_20260518T145948_result.json`
- **Structured JSON:** [`2a9e642817e8dbc6ee36.json`](../../sessions/2a/2a9e642817e8dbc6ee36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Text-based rho(LP, F1) 结果 (tab:epoch_scierc 更新值):**

| Epoch | median ρ | mean ρ | %pos | n_valid/n_total |
|-------|---------|--------|------|-----------------|
| 3-epoch | 0.3192 | 0.2726 | 76.4% | 495/551 |
| 5-epoch | 0.2624 | 0.1791 | 64.1% | 435/551 |
| 10-epoch | 0.1116 | 0.0660 | 54.0% | 276/551 |

**与 tab:within_rho 交叉验证**: 5-epoch 值 0.2624 → 四舍五入 0.262，与 tab:within_rho 一致。

**与旧 span-based 值差异**: 最大偏差 0.015 (5-epoch)，趋势不变 (3 > 5 > 10)。

脚本: `code/compute_epoch_scierc_rho_textbased.py`，独立实现 text-based F1，不依赖 evaluation.py。

---
