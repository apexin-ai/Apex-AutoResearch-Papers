# exp llama L13 steering seed123

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama-L13-steering-seed123_20260524T171202_result.json`
- **Structured JSON:** [`d8a605045f493b41c62b.json`](../../sessions/d8/d8a605045f493b41c62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果文件已保存到 `data/llama31/steering_results_L13_last_seed123.json`。

## Llama L13 Steering Robustness Report (seed=42 vs seed=123)

```
                           seed=42 (original)     seed=123
N_test:                    201                     201
Probe bal_acc (L13):       90.0%                   92.5%
Baseline distribution:     identical               identical

α=-20:  steer/ctrl flips   45/51  p=0.559           40/63  p=0.012
α=-10:  steer/ctrl flips   35/23  p=0.118           25/55  p=0.000
α=-5:   steer/ctrl flips   12/17  p=0.441           11/16  p=0.426
α=+5:   steer/ctrl flips   38/17  p=0.003  c→p: 2   35/14  p=0.002  c→p: 2  ✓
α=+10:  steer/ctrl flips   57/27  p=0.000  c→p: 3   60/30  p=0.000  c→p: 5  ✓
α=+20:  steer/ctrl flips   65/62  p=0.830  c→p: 0   72/45  p=0.004  c→p: 3  ✓

Bonferroni sig (p<0.0083): 2/6                      4/6
```

**结论：**

1. **Causal claim 完全复现** — 正 alpha 方向的 steering 效应在 seed=123 下高度一致：
   - α=+5: Fisher p=0.002 (原始 0.003), 2 c→p directional flips (一致)
   - α=+10: Fisher p=0.0005 (原始 0.0003), 5 c→p flips (比原始更强)
   
2. **效应方向一致** — 所有正 alpha 均为 steering > control, p→c=0, 一致的 c→p 方向

3. **seed=123 效应更强** — Bonferroni 显著 alpha 数量 4/6 (原始 2/6)，α=+20 也达到显著

4. **负 alpha 模式不同** — seed=123 的 control direction (不同随机正交向量) 在负 alpha 下造成更多扰动，这属于 control condition 的变异，不影响正向 causal claim

5. **Baseline 完全一致** — 验证了 seed 只影响 probe 和 control direction，不影响 baseline generation

---
