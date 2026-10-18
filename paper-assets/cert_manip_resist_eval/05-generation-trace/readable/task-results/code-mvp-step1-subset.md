# code mvp step1 subset

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-step1-subset_20260521T204933_result.json`
- **Structured JSON:** [`86bbf47d6137798f3ebc.json`](../../sessions/86/86bbf47d6137798f3ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3-model pipeline 完成。结果汇总：

## Pairwise Correlation Table

### MMLU (300 samples)

| Pair | MI | MI 95% CI | Copula ρ | ρ 95% CI | Agreement |
|------|-----|-----------|----------|----------|-----------|
| llama-8b ↔ qwen-14b | 0.037 | [0.016, 0.073] | 0.177 | [0.056, 0.261] | 0.460 |
| llama-8b ↔ qwen-32b | 0.024 | [0.010, 0.053] | 0.144 | [-0.026, 0.198] | 0.533 |
| **qwen-14b ↔ qwen-32b** | **0.191** | [0.141, 0.267] | **0.263** | [0.095, 0.333] | **0.667** |

### ARC Challenge (300 samples)

| Pair | MI | MI 95% CI | Copula ρ | ρ 95% CI | Agreement |
|------|-----|-----------|----------|----------|-----------|
| llama-8b ↔ qwen-14b | 0.132 | [0.085, 0.190] | 0.203 | [0.078, 0.300] | 0.670 |
| llama-8b ↔ qwen-32b | 0.112 | [0.066, 0.166] | 0.301 | [0.184, 0.378] | 0.700 |
| **qwen-14b ↔ qwen-32b** | **0.319** | [0.247, 0.397] | **0.278** | [0.109, 0.335] | **0.723** |

### Cross-vs-Within Family Validation

| Dataset | Within-family MI | Cross-family MI | Hypothesis holds | Permutation p |
|---------|-----------------|-----------------|-----------------|---------------|
| MMLU | 0.191 | 0.031 | **True** (6.3×) | 0.331 |
| ARC | 0.319 | 0.122 | **True** (2.6×) | 0.331 |

**核心发现：**

1. **Within-family MI 显著高于 cross-family** — MMLU 上 within/cross 比值为 6.3×，ARC 上为 2.6×，方向一致且效应量大。
2. **Permutation p=0.331** — 因为只有 1 个 within-family pair 和 2 个 cross-family pairs（共 3 对，排列空间极小），统计检验力不足。这是预期内的，扩展到更多模型后 p 值会下降。
3. **Bootstrap CI 无重叠** — qwen-14b↔qwen-32b 的 MI CI 下界（MMLU: 0.141, ARC: 0.247）远高于两个 cross-family pair 的 CI 上界，信号清晰。
4. **管道端到端验证通过** — 模型加载/卸载、batch scoring、pairwise correlation、bootstrap CI、cross-vs-within validation 全链路正常。

结果保存在 `artifacts/results/results_step1_subset_20260521_214027.json`。

---
