# analysis seed comparison prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed_comparison_prep_20260516T023404_result.json`
- **Structured JSON:** [`096d698c4e1b88273e48.json`](../../sessions/09/096d698c4e1b88273e48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**3/4 seeds 已就绪**（双方都只缺 s45）：

| Seed | flat-NLI rel_f1 | CED rel_f1 | Δ (fNLI-CED) |
|------|----------------|-----------|---------------|
| s42 | 0.4539 | 0.4504 | +0.0035 |
| s43 | 0.4523 | 0.4683 | -0.0159 |
| s44 | 0.4615 | 0.4655 | -0.0040 |
| Mean | 0.4559±0.0049 | 0.4614±0.0096 | -0.0055 |

**预比较 (N=3):** CED 略优 0.55 个点，但 p=0.4357 远未显著，95% CI [-0.030, +0.019] 跨零。s45 结果出来后用 `python3 scripts/seed_comparison.py` 即可得到完整 paired t-test。

**注意事项：**
- rsft_flat_nli_s44 缺 metrics_v2.json（无 Ign-F1 修正），脚本用 metrics.json 不影响 rel_f1，但 ign_f1 值不准
- rsft_flat_nli_s43 原始结果是坏的（f1=0.002），脚本已正确回退到 reeval 版本

---
