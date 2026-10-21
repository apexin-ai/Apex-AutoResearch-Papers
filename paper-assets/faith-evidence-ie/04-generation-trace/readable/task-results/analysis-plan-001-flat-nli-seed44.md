# analysis plan 001 flat nli seed44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_001_flat_nli_seed44_20260515T232414_result.json`
- **Structured JSON:** [`a136519ae86e3eecbd40.json`](../../sessions/a1/a136519ae86e3eecbd40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总报告：

## plan_001_flat_nli_seed44 训练结果

| 项目 | 值 |
|------|-----|
| 训练时长 | 1h43m (6197s) |
| 总步数 | 507 (3 epochs) |
| 训练样本 | 2691 (CED mean=0.725) |
| Final train loss | 0.6247 |
| Final eval loss | 0.7564 |
| Checkpoint | `/root/autodl-tmp/rsft_output_flat_nli_s44/` (adapter 528MB) |
| W&B | 未启用 |

### Mid-train Task Eval (50 docs)

| Epoch | F1 | Evi-F1 | EDCR | Preds |
|-------|----|--------|------|-------|
| 1 | 0.4306 | 0.7292 | 0.6474 | 883 |
| 2 | 0.4884 | 0.7458 | 0.6317 | 876 |
| 3 | **0.4897** | **0.7800** | **0.6596** | 782 |

### 与其他 seed/方法对比（mid-train 50-doc eval）

| 方法 | rel_f1 | 备注 |
|------|--------|------|
| SFT baseline | 0.4057 | 全量 eval |
| flat-NLI s42 | 0.4539 | 全量 eval |
| flat-NLI s45 | 0.4876 | mid-train eval |
| **flat-NLI s44** | **0.4897** | mid-train eval |
| CED RSFT mean | ~0.4596 | 全量 eval |

s44 的 mid-train F1=0.4897 是三个 flat-NLI seed 中最高的，且 Evi-F1=0.78 也很出色。注意 s44 和 s45 的数值都是 50-doc mid-train eval，需全量 eval 才能与 s42 的 0.4539 直接对比。预期全量 eval 数值会有所变动。

---
