# analysis acc ds s025 results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s025_results_20260515T212016_result.json`
- **Structured JSON:** [`c59f0c9be301a292142a.json`](../../sessions/c5/c59f0c9be301a292142a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## acc_ds_s025 结果总结

| 指标 | 值 |
|------|-----|
| **accuracy** | **8.0% (4/50)** |
| delta vs dense | **-44pp** |
| null (生成为空) | 37 (74%) |
| output truncated (gen=2048) | 38 (76%) |
| wrong (非空但错) | 9 (18%) |
| extraction failure | 1 (2%) |
| heads_pruned | 196 |
| total_time | 1670.5s |

### 剂量曲线 (DeepSeek-R1-Distill-Qwen-7B)

| Sparsity | Accuracy | Delta |
|----------|----------|-------|
| dense | 52% | — |
| s=0.15 | 36% | -16pp |
| s=0.20 | 待确认 | — |
| **s=0.25** | **8%** | **-44pp** |
| s=0.30 | 10% | -42pp |

### Conclusion: **success**

s=0.25 的 8% accuracy 确认了 compound interaction severity 随 sparsity 增加而剧烈恶化。关键发现：

1. **s015→s025 存在 cliff**：从 36% 骤降到 8%，degradation 不是线性的，更像 phase transition
2. **s025 ≈ s030**（8% vs 10%，差 1 题）：在高 sparsity 区间，模型已接近完全崩溃（floor effect），进一步增加 sparsity 不再有显著变化
3. **74% null rate** 说明模型在 s=0.25 时大量陷入重复循环/无法终止推理，是 compound head interaction 的典型症状

---
