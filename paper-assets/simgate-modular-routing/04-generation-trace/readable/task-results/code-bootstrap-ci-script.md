# code bootstrap ci script

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-ci-script_20260520T120423_result.json`
- **Structured JSON:** [`666b5abdf6c0b1b7370b.json`](../../sessions/66/666b5abdf6c0b1b7370b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完毕。结果汇总：

## Aggregate Results (B=10000, seed=42)

| Model | Int DR [95% CI] | Det DR [95% CI] | ΔDR [95% CI] | DAF [95% CI] |
|---|---|---|---|---|
| **Qwen2.5-7B** (245 eps) | 42.9% [36.7, 49.0] | 16.3% [11.8, 21.2] | +26.5 [20.4, 32.7] | 90.4% [81.3, 99.1] |
| **Llama-3.1-8B** (220 eps) | 41.4% [35.0, 47.7] | 11.4% [7.3, 15.9] | +30.0 [23.6, 36.4] | 88.2% [80.2, 95.1] |

**验证点对齐情况**：
- Qwen int_DR = 42.9% ✓, DAF = 90.4% ✓
- Llama int_DR = 41.4% ✓, det_DR = 11.4% ✓, ΔDR = 30.0pp ✓, DAF = 88.2% ✓

**注意**：Qwen det_DR 实际为 **16.3%**（40/245），与你给的"≈4.5%"有较大差异。数据确认过——`plan_c` 11 个 task、245 个有效 episode（排除了 30 个 `always_deep_internal` 的），逐 task det death 都在 10-25%。如果你的 4.5% 来源于不同数据子集或不同定义，需要核实。

输出文件：
- `results/cross_model_bootstrap_cis.json` — 完整数值
- `results/cross_model_bootstrap_cis.tex` — LaTeX tabular，可直接插入 Appendix M

---
