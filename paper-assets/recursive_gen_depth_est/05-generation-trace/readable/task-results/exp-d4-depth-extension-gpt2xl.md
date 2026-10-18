# exp d4 depth extension gpt2xl

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d4_depth_extension_gpt2xl_20260518T183412_result.json`
- **Structured JSON:** [`16f2614782d7f9630d9a.json`](../../sessions/16/16f2614782d7f9630d9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

**d4 depth extension (GPT-2 XL nucleus) 结果**

| 指标 | 值 |
|---|---|
| **5-class RF accuracy (d0-d4)** | **74.03%** [73.90, 74.17] (chance=20%) |
| **d3 vs d4 pairwise AUC** | **0.7273** |
| **d4 recall** | 63.86% |

**Per-class recall**: d0=98.4%, d1=87.3%, d2=71.8%, d3=48.7%, d4=63.9%

d3 recall 从 4-class 的 ~80% 降到 5-class 的 48.7%，因为 d3/d4 相互混淆。d4 recall (63.9%) 高于 d3，说明 d4 有自己的特征模式。

**Feature trends (d0→d4)**:
- **p90_ppl**: 483.7 → 128.1 → 73.8 → 57.6 → 49.2 (单调递减 ✓)
- **var_surprisal**: 6.50 → 3.62 → 3.07 → 2.47 → 2.22 (单调递减 ✓)
- **mean_ppl**: 25K → 54K → 678K → 1076K → **928K** (d4 处打破单调性)

mean_ppl 在 d4 出现下降 (1076K→928K)，p90_ppl 和 var_surprisal 保持单调。这说明递归生成到 d4 时，文本熵进一步压缩（surprisal 下降），但平均 PPL 的极端值趋于稳定。

产出文件在 `/root/autodl-tmp/recursive_gen_depth_est/results/d4_extension_gpt2xl/`：
- `features_d4.jsonl` (5000 条 d4 特征)
- `d4_extension_results.json` (完整评估结果)

---
