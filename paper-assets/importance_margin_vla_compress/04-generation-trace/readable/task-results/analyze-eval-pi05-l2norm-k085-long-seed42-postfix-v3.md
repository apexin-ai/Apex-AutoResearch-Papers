# analyze eval pi05 l2norm k085 long seed42 postfix v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k085_long_seed42_postfix_v3_20260525T110233_result.json`
- **Structured JSON:** [`f1421060d23cb652f130.json`](../../sessions/f1/f1421060d23cb652f130.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: `eval_pi05_l2norm_k085_long_seed42_postfix_v3`

| 指标 | 值 |
|------|-----|
| **overall_sr** | **78.0%** |
| **elapsed_min** | 206.2 |
| **wandb_run_id** | 无 |
| **异常** | 无（EXIT_CODE=0） |

### Per-task SR

| Task | Description | SR |
|------|-------------|-----|
| T0 | put both the alphabet soup and the tomat… | 98% |
| T1 | put both the cream cheese box and the bu… | 94% |
| T2 | turn on the stove and put the moka pot o… | 82% |
| T3 | put the black bowl in the bottom drawer | 100% |
| T4 | put the white mug on the left plate and… | 72% |
| T5 | pick up the book and place it in the bac… | 96% |
| T6 | put the white mug on the plate and put t… | 8% |
| T7 | put both the alphabet soup and the cream… | 80% |
| T8 | put both moka pots on the stove | 56% |
| T9 | put the yellow and white mug in the micr… | 94% |

配置: `l2norm pruning, keep=217/256 tokens (85%)`, 模型参数 4143.4M。结果已保存至 `eval_results/pi05_l2norm_k0.85_libero_10_seed42.json`。T6 成功率极低 (8%) 是主要拖累项。

---
