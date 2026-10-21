# analysis harvest eval results s123 complete

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_eval_results_s123_complete_20260515T194000_result.json`
- **Structured JSON:** [`5ca793bd9ca4dc874831.json`](../../sessions/5c/5ca793bd9ca4dc874831.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**8 个 canonical eval 目录** 全部完整（d000/d005/d025/d100 × aligned/para_aligned），另有 1 个 d000 non-v2 备选。

**关键发现**：
- GSM8K 污染信号最强：d000=26.8% → d100=73.2%（aligned）
- HumanEval 也有清晰趋势：6.1% → 18.3%
- MMLU/ARC-C 相对稳定，对 dosage 不敏感
- d025 GSM8K aligned（52.5%）低于 d005（63.1%），非单调——值得关注

**Per-item 数据完全可用**：所有目录都有 `correctness_matrix.json`（boolean 数组）和 `item_responses.json`（结构化记录），可直接输入 pooled IRT。每个 aligned 条件有 16,697 items，para_aligned 有 7,547 items。

Artifact 已注册：`art_20260515_2e6035`

---
