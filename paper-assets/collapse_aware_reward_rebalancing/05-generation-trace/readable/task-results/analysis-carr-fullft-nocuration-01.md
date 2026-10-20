# analysis carr fullft nocuration 01

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_fullft_nocuration_01_20260516T233611_result.json`
- **Structured JSON:** [`9c8437aa11962a7ef48a.json`](../../sessions/9c/9c8437aa11962a7ef48a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE，memory 已写入。结果汇总：

**实验 carr_fullft_nocuration_01 结果：**

| Gen | mean_quality | vendi_score | self_bleu | perplexity | mean_nn_distance | complexity_mean |
|-----|-------------|-------------|-----------|-----------|-----------------|----------------|
| 0 | 0.1126 | 107.17 | 0.0045 | 8.77 | 0.7061 | 2.847 |
| 1 | 0.1111 | 107.87 | 0.0047 | 8.70 | 0.7094 | 2.793 |
| 2 | 0.1117 | 108.64 | 0.0065 | 8.82 | 0.7114 | 2.820 |

- **vendi_decline_pct**: +1.38% (diversity 上升，无 collapse)
- **checkpoint**: `/root/autodl-tmp/carr/outputs_fullft_nocuration/gen_2/condition_0/merged`
- **结论**: success (baseline 正常完成，符合预期：no_curation 不产生 collapse)

与 LoRA no-curation baseline 对比：LoRA +3.13% vs Full-FT +1.38%，Full-FT 增长更温和但趋势一致。

---
