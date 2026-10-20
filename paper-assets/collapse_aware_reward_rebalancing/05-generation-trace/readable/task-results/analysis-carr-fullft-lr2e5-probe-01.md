# analysis carr fullft lr2e5 probe 01

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_fullft_lr2e5_probe_01_20260517T002512_result.json`
- **Structured JSON:** [`d5fc82819f3bfb100ab1.json`](../../sessions/d5/d5fc82819f3bfb100ab1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

| Metric | Gen 0 | Gen 1 | Gen 2 | Trend |
|--------|-------|-------|-------|-------|
| mean_quality | 0.1130 | 0.1154 | 0.1124 | flat |
| vendi_score | 107.81 | 108.03 | 108.54 | **+0.68%** |
| self_bleu | 0.0046 | 0.0039 | 0.0040 | slight ↓ |
| perplexity | 9.57 | 10.34 | 8.82 | volatile |
| mean_nn_distance | 0.7079 | 0.7107 | 0.7100 | flat |
| complexity_mean | 2.890 | 2.868 | 2.846 | slight ↓ |

**Training loss**: 0.380 → 0.212 → 0.140 (model is fitting harder each gen)

**判定: NEGATIVE**

- Vendi 从 107.81 → 108.54 (+0.68%)，与 baseline (+1.38%) 和 LR=5e-6 (+0.91%) 趋势一致
- 即使 4x 更高的 LR 使 loss 大幅下降（模型确实在更强地 overfit 选定数据），diversity 仍未下降
- 3 代 K=4 ArmoRM top-1 的 reward curation 在 Qwen3-0.6B 上**无法诱导可测量的 collapse**
- Checkpoint: `/root/autodl-tmp/carr/outputs_fullft_lr2e5/gen_2/condition_0/merged`
- 耗时: ~3.7 小时

---
