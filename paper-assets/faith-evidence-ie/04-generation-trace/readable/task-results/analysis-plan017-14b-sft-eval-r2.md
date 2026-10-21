# analysis plan017 14b sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan017_14b_sft_eval_r2_20260519T135510_result.json`
- **Structured JSON:** [`f3e5490171efd935f1e6.json`](../../sessions/f3/f3e5490171efd935f1e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。结果汇总：

**plan017_14b_sft_eval_r2 — 14B SFT baseline eval (bf16, no quantize)**

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.5507** |
| ign_precision | 0.5268 |
| ign_recall | 0.5768 |
| f1 | 0.5611 |
| format_compliance_rate | 1.0 |
| n_truncated | 139 / 985 |
| inference_time | 18011s (~5h) |
| evi_f1 | 0.8292 |
| evi_f1_joint | 0.4453 |
| edcr | 0.597 |

**Scale 对比（SFT baseline ign_f1）：**
- 1.7B: 0.4464
- 4B: 0.4358
- 8B: 0.4866
- **14B: 0.5507** (+13.2% over 8B mean)

**对比 14B no-evidence (0.551)：** 两者几乎持平（0.5507 vs 0.551），evidence tax 极小（-0.05%），说明 14B 模型在输出 evidence 的同时几乎不牺牲关系抽取性能。

Conclusion: **success**。14B 在 4 个 scale 档中最强，且 evidence tax 接近零。

---
