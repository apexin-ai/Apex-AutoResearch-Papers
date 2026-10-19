# analysis bce data source verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bce-data-source-verify_20260519T082212_result.json`
- **Structured JSON:** [`0178ab3c0e465bf65347.json`](../../sessions/01/0178ab3c0e465bf65347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**Table 2 "BCE + comp.*" PPL 28.13±0.20** — 数据来源确认为 `bce_isocompute_v3_{s42,s123,s456}_eval`（纯 BCE，2700 steps，无 compensation）。PPL 和全部 4 个 downstream 指标均匹配。

**Table 4 "BCE + Compensation" PPL 25.44** — 数据来源确认为 `bce_comp_staged_s42` 的 `predictor_hard_mask_ppl`，匹配。

**发现的问题：**
1. Table 2 脚注 `$^\ast$` 写的是 "with compensation (67.2M params)"，但实际数据来自无 compensation 的 iso-compute 实验。"comp." 实际含义是 computational budget matching，脚注需修正。
2. MMLU std 实际为 0.44，论文报 0.5（微小的保守取整偏差）。

报告已注册：`artifacts/bce_data_source_verification.md`

---
