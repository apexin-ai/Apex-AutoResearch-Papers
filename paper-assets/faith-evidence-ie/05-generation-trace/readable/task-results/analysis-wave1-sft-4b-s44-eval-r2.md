# analysis wave1 sft 4b s44 eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wave1_sft_4b_s44_eval_r2_20260518T220104_result.json`
- **Structured JSON:** [`e6ec7dcbf9ffff46dc2d.json`](../../sessions/e6/e6ec7dcbf9ffff46dc2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（status=DONE, conclusion=success 已由 hook 设置）。

## wave1_sft_4b_s44_eval_r2 结果

| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.4734** |
| F1 | 0.4838 |
| Ign-Precision | 0.4676 |
| Ign-Recall | 0.4794 |
| Evi-F1 (DREEAM/joint) | 0.3820 |
| Evi-F1 (TP) | 0.7875 |
| EDCR | 0.6581 |
| Format OK | 982/985 (99.7%) |
| Truncated | 249/985 |
| Predictions | 16,143 |

**对比 canonical 4B SFT s42 (ign_f1 ≈ 0.505)：s44 低约 3.2 个点。** seed 间波动偏大，可能与 249/985 truncation（25.3%）有关。

---
