# analysis sft 1000 s43 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft-1000-s43-s44_20260515T132650_result.json`
- **Structured JSON:** [`a83cb18aa782214e489a.json`](../../sessions/a8/a83cb18aa782214e489a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 均已更新。汇总如下：

## SFT 1000步 3-seed 完整结果

| Metric | s42 | s43 | s44 | Mean ± Std |
|--------|-----|-----|-----|------------|
| prove_rate | 0.13 | 0.11 | 0.15 | **0.130 ± 0.016** |
| n_proved | 13 | 11 | 15 | 13.0 ± 1.63 |
| mean_isr | 0.0738 | 0.0699 | 0.0884 | **0.077 ± 0.008** |
| proved_only_mean_isr | 0.568 | 0.635 | 0.589 | 0.597 ± 0.028 |
| genuine_count | 12 | 10 | 14 | **12.0 ± 1.63** |
| genuine_rate | 0.923 | 0.909 | 0.933 | **0.922 ± 0.010** |
| h7_strict | 0 | 0 | 0 | 0 |
| h1_strict | 1 | 1 | 1 | 1 (同一样本 folio_167) |
| h8_conj_collapse | 0 | 0 | 0 | 0 |
| content_independent | 0 | 0 | 0 | 0 |
| isr_1_count | 0 | 1 | 0 | 0.33 |
| train_final_loss | 0.0168 | 0.0167 | 0.0171 | 0.0169 ± 0.0002 |

**结论**: SFT 1000步 3-seed 均 genuine_rate > 90%，zero h7/h8 hacking，仅 1 个 h1 样本（同一道题 folio_167）。SFT 无 Goodhart collapse，可作为 GRPO 对照基线。

**Checkpoint 路径**:
- s43: `/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/checkpoint-1000`
- s44: `/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/checkpoint-1000`

---
