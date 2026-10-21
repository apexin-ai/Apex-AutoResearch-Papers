# exp steering gemma L10 120 v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-gemma-L10-120-v2_20260523T101826_result.json`
- **Structured JSON:** [`1ffba8fb9ef3d8d4bf9b.json`](../../sessions/1f/1ffba8fb9ef3d8d4bf9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个方向实验均已完成。

## Gemma L10 (120)
状态: **完成**

命令:
```
# 正方向
CUDA_VISIBLE_DEVICES=0 python src/steering_experiment.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/gemma2 --peak_layer 10 --alphas 5 10 20 --position last
# 负方向
CUDA_VISIBLE_DEVICES=0 python src/steering_experiment.py --model /root/autodl-tmp/models/gemma-2-9b-it --data_dir data/gemma2 --peak_layer 10 --alphas -5 -10 -20 --position last --output_suffix _L10_neg
```

Probe accuracy: **70.57%**

| | Steering flips | Control flips | Fisher p |
|---|---|---|---|
| Alpha +5 | 3/158 (1.9%) | 2/158 (1.3%) | 1.0000 |
| Alpha -5 | 1/158 (0.6%) | 1/158 (0.6%) | 1.0000 |
| Alpha +10 | 1/158 (0.6%) | 1/158 (0.6%) | 1.0000 |
| Alpha -10 | 2/158 (1.3%) | 4/158 (2.5%) | 0.6845 |
| Alpha +20 | 5/158 (3.2%) | 1/158 (0.6%) | 0.2143 |
| Alpha -20 | 2/158 (1.3%) | 6/158 (3.8%) | 0.2828 |

所有条件 p→c=0, c→p=0（无实质性参数↔上下文翻转）

Bonferroni 显著 (k=6, p<0.0083): **无**

JSON 路径:
- `/root/clkc_mech_interp/data/gemma2/steering_results.json`（正方向）
- `/root/clkc_mech_interp/data/gemma2/steering_results_L10_neg.json`（负方向）

Log 路径:
- `/root/clkc_mech_interp/logs/steering_gemma_L10.log`
- `/root/clkc_mech_interp/logs/steering_gemma_L10_neg.log`

---
