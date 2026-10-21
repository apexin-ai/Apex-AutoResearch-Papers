# analysis 14b sft no evidence eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b_sft_no_evidence_eval_r2_20260519T125642_result.json`
- **Structured JSON:** [`f52ae2f47eb267e95476.json`](../../sessions/f5/f52ae2f47eb267e95476.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success.

## 结果汇总

**plan017_14b_sft_no_evidence_eval_r2** — DONE (success)

| Metric | Value |
|--------|-------|
| **ign_f1** | **0.5510** |
| ign_precision | 0.5149 |
| ign_recall | 0.5926 |
| f1 | 0.5649 |
| format_compliance_rate | 0.9868 |
| n_truncated | 105 |
| n_predictions | 15605 |
| inference_time_seconds | 14497.8 |

Settings verified: `no_evidence=true`, `quantize=false`.

## Evidence Tax

**无法计算** — `plan017_14b_sft_eval_r2` (with-evidence) 仍在运行，进度 411/493 batches (83%)，预计还需 ~50 分钟完成。

等 with-evidence eval 完成后可计算：
- tax = with_evidence_ign_f1 - 0.5510 (no_evidence)

参考其他 scale 的 evidence tax：4B 为 0.4721 - 0.3974 = +7.47pp（with-evidence 更高，因为 evidence 帮助关系预测）。14B no-evidence ign_f1=0.5510 已高于 8B SFT mean (0.4866)，表明 14B 规模提升显著。

---
