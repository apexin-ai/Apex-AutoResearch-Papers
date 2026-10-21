# analysis algo1 threshold heatmap c3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_algo1-threshold-heatmap-c3_20260521T085541_result.json`
- **Structured JSON:** [`076ec06736ad15d94a9d.json`](../../sessions/07/076ec06736ad15d94a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，跳过注册。

产出写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/threshold_sensitivity/algo1_threshold_heatmap.json`。

**结果摘要**：

| Family | Expected | 原始 30 组合 | 扩展 134 组合 | 最近 transition |
|--------|----------|-------------|--------------|----------------|
| Phi-4 | Immune | 30/30 (100%) | 110/134 (82%) | tau < 0.35 (0.35x default) |
| Qwen2.5-14B | U-collapse | 30/30 (100%) | 134/134 (100%) | tau = 9.40 (9.4x default) |
| Qwen2.5-7B | V-recovery | 30/30 (100%) | 97/134 (72%) | tau = 3.00 (3x default) |
| Gemma-2-9B | Benefit | 30/30 (100%) | 119/134 (89%) | tau = 3.80 (3.8x default) |
| OLMo-2-7B | Benefit-sat | 30/30 (100%) | 110/134 (82%) | tau = 3.25 (3.25x default) |

**W9 可用的核心论据**：在合理参数范围 τ∈[0.5, 2.0]×σ∈[3.0, 7.0]（4× range for τ, 2.3× for σ）内，所有 5 个家族分类 **30/30 完全一致**。最近的 transition point（Qwen2.5-7B at τ=3.0）需要将 3pp 的准确率下降当作噪声处理——这在实践中不合理。分类稳定的根本原因是效应大小本身分离度很高（Phi-4 波动 < 0.4pp vs Qwen-14B 下降 9.4pp）。

---
