# analysis eval gsm8k sft rasp 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144_result.json`
- **Structured JSON:** [`0a473c86aa8b29bac79c.json`](../../sessions/0a/0a473c86aa8b29bac79c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md`。

**关键数据**:
- SFT RASP 20% 1.5B GSM8K accuracy: **26.91%** (355/1319, greedy)
- Checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`
- GRPO delta = 26.16% - 26.91% = **-0.75 pp** (negative)

**结论**: Negative result。GRPO (26.16%) 未超越 SFT baseline (26.91%)，差距在 stderr (±1.22%) 范围内，两者本质上无显著差异。

---
