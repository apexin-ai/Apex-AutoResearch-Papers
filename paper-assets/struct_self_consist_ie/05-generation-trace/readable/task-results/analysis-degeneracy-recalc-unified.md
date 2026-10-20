# analysis degeneracy recalc unified

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_degeneracy_recalc_unified_20260518T203519_result.json`
- **Structured JSON:** [`12a2231e6a4eda973671.json`](../../sessions/12/12a2231e6a4eda973671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 JSON 文件。以下是完整的退化率重算对比表：

```
Label                                                       N  Degen%(unified)  OldPctZero   Delta
─────────────────────────────────────────────────────────────────────────────────────────────────────
Qwen3-8B / SciERC / T=1.0 / seed=42                       529            17.8%       12.6%    +5.2
Qwen3-8B / SciERC / T=1.0 / seed=123                      529            17.2%       11.7%    +5.5
Qwen3-8B / SciERC / T=1.0 / seed=456                      529            20.4%       13.3%    +7.2
Qwen3-8B / CoNLL / T=1.0 N=16 / seed=42                  2756            48.4%        7.6%   +40.9
Qwen3-8B / CoNLL / T=1.0 N=16 / seed=123                 2756            47.1%        7.5%   +39.5
Qwen3-8B / CoNLL / T=1.0 N=16 / seed=456                 2756            55.4%        7.0%   +48.4
Qwen3-8B / FewNERD / T=1.0 / seed=42                     4351             7.1%         N/A     N/A
Qwen3-8B / FewNERD / T=1.0 / seed=123                   32565            13.1%       20.4%    -7.3
Qwen3-8B / FewNERD / T=1.0 / seed=456                   32565            12.1%       19.3%    -7.2
LLaMA3.1-8B / SciERC / T=1.0 / seed=42                    529            24.9%       11.4%   +13.5
LLaMA3.1-8B / SciERC / T=1.0 / seed=123                   529            26.6%       11.1%   +15.6
LLaMA3.1-8B / SciERC / T=1.0 / seed=456                   529            27.4%       11.7%   +15.8
LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=42               2756            86.5%        4.3%   +82.2
LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=123              2756            86.4%        4.3%   +82.1
LLaMA3.1-8B / CoNLL / T=1.0 N=16 / seed=456              2756            86.7%        4.3%   +82.4
Qwen3-8B / SciERC / T=0.5 / seed=42 (ablation)            529            41.4%       10.3%   +31.1
Qwen3-8B / SciERC / T=0.8 / seed=42 (ablation)            529            23.8%       11.2%   +12.7
Qwen3-8B / SciERC / T=1.2 / seed=42 (ablation)            529            14.9%       13.9%    +1.1
Qwen3-4B / SciERC / T=1.0 / seed=42                       529            10.4%       11.4%    -1.0
Qwen3-4B / CoNLL / T=1.0 / seed=42                       2756            90.6%        4.4%   +86.2
```

**关键发现：**

1. **CoNLL 差异最大**：旧值 ~7% 实际 ~48-55% (Qwen3-8B)、~86% (LLaMA)。差距高达 +40~+86pp。因为 CoNLL 高性能 → 大量实例 N 个 sample 的 F1 完全相同（constant-F1），但 sample_f1_pct_zero 只统计 F1=0 的。

2. **SciERC T=0.5 差异大**：旧值 10.3%，真实 41.4%。低温下多样性低 → 高退化率，符合预期。

3. **FewNERD 反向偏差**：unified 定义 (7-13%) 比 old_pct_zero (19-20%) 更低。因为 FewNERD 难度适中，F1=0 的 sample 多但实例级 constant-F1 少。

4. **T 消融趋势反转**：旧指标下 T=0.5 (10.3%) < T=1.2 (13.9%)，unified 下 T=0.5 (41.4%) > T=1.2 (14.9%)。退化率随温度升高单调下降，这才是正确的物理直觉。

5. **FewNERD seed=123/456 注意**：N=32565 实例 (n8 实验)，远多于 seed=42 的 4351 (n16 实验)，数据集版本不一致。

结果 JSON 已保存至 `/root/autodl-tmp/struct_self_consist_ie/output/unified_degeneracy_audit/degeneracy_recalc_results.json`。

---
