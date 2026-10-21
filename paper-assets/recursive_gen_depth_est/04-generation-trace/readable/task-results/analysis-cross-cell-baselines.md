# analysis cross cell baselines

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_cell_baselines_20260515T035515_result.json`
- **Structured JSON:** [`1f208340e5270c4f285e.json`](../../sessions/1f/1f208340e5270c4f285e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9-cell baseline battery 完成。结果摘要：

**3×3 Best Accuracy Matrix (4-class, paper Table 1):**

|          | nucleus | temp09 | topk50 |
|----------|---------|--------|--------|
| Pythia   | 78.2%   | 77.2%  | 68.8%  |
| OLMo     | 79.6%   | 82.7%  | 75.9%  |
| GPT-2 XL | 84.3%   | 85.3%  | 75.4%  |

**关键发现：**
- 4 种 baselines 性能非常接近（RF ≈ CORAL > DivEye > LR），最大差距 ~4pp
- GPT-2 XL temp09 是最强配置（85.3% RF），GPT-2 XL nucleus 次之（84.3% CORAL）
- Top-k 解码显著削弱深度信号（-9~13pp vs nucleus），但仍远超 chance（25%）
- 模型效应 > 解码策略效应：GPT-2 XL topk50（75.4%）仍优于 Pythia nucleus（78.2%）相当

**产出位置：**
- 完整 JSON: `gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/results/baseline_battery_9cell/all_results.json`
- Artifact: `9cell_baseline_battery_results` (art_20260515_12b98b)

---
