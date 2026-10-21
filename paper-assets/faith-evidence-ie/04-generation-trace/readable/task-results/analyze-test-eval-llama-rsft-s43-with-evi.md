# analyze test eval llama rsft s43 with evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_llama_rsft_s43_with_evi_20260523T091042_result.json`
- **Structured JSON:** [`23d3c3302f45a461409b.json`](../../sessions/23/23d3c3302f45a461409b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已有 conclusion=success。更新完成。

## 分析总结

**核心指标（s43 with-evi）：**

| 指标 | s43 | s42 | 差异 |
|------|-----|-----|------|
| ign_f1 | 0.3488 | 0.3599 | -1.11pp |
| f1 | 0.3488 | 0.3599 | -1.11pp |
| precision | 0.4834 | 0.4790 | +0.44pp |
| recall | 0.2728 | 0.2882 | -1.54pp |
| evi_f1 (DREEAM) | 0.2514 | 0.2509 | +0.05pp |
| edcr | 0.8425 | 0.8391 | +0.34pp |

**与 s42 对比：** ign_f1 差 -1.11pp，在 ±3pp 范围内，结论 success。s43 precision 略高但 recall 明显低，导致 f1 下降。Evidence 相关指标（evi_f1, edcr）两个 seed 几乎一致。

**LLaMA 8B multi-seed variance（s42, s43）：**
- ign_f1: **mean = 0.3544 ± 0.0056**（std）
- f1: mean = 0.3544 ± 0.0056
- evi_f1: mean = 0.2512 ± 0.0003

两 seed 方差较小（std ~0.56pp），LLaMA 8B RSFT with-evi 在 test set 上表现稳定。

---
