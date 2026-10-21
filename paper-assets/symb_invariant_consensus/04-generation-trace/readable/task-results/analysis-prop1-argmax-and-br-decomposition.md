# analysis prop1 argmax and br decomposition

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prop1-argmax-and-br-decomposition_20260523T094713_result.json`
- **Structured JSON:** [`ad681881f9f168b79bb2.json`](../../sessions/ad/ad681881f9f168b79bb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果如下：

## Argmax Agreement

| Condition | Agreement Rate | N problems |
|-----------|---------------|------------|
| Mistral-7B × FOLIO | 92.2% | 204 |
| Mistral-7B × PW | 90.2% | 600 |
| Qwen2.5-14B × FOLIO | 97.5% | 204 |
| Qwen2.5-14B × PW | 93.2% | 600 |
| LLaMA-8B × FOLIO | 87.3% | 204 |
| LLaMA-8B × PW | 87.3% | 600 |
| **OVERALL** | **90.8%** | **2412** |

## BR Decomposition (SC-incorrect problems only)

| Condition | Observed BR | Base-rate BR | Excess | Pearson r | N valid |
|-----------|------------|-------------|--------|-----------|---------|
| Mistral-7B × FOLIO | 2.19 | 3.85 | −1.65 | 0.70 | 85 |
| Mistral-7B × PW | 2.46 | 4.44 | −1.98 | 0.52 | 318 |
| Qwen2.5-14B × FOLIO | 2.05 | 4.37 | −2.31 | 0.58 | 33 |
| Qwen2.5-14B × PW | 1.53 | 3.79 | −2.25 | 0.24 | 139 |
| LLaMA-8B × FOLIO | 2.14 | 3.71 | −1.57 | 0.56 | 65 |
| LLaMA-8B × PW | 1.49 | 2.83 | −1.35 | 0.63 | 174 |

## Bonus: When SICA ≠ SC, who is correct?

| Condition | Disagree | SICA correct | SC correct | Both wrong |
|-----------|----------|-------------|-----------|------------|
| Mistral-7B × FOLIO | 16 | 10 | 3 | 3 |
| Mistral-7B × PW | 59 | 10 | 32 | 17 |
| Qwen2.5-14B × FOLIO | 5 | 1 | 3 | 1 |
| Qwen2.5-14B × PW | 41 | 10 | 25 | 6 |
| LLaMA-8B × FOLIO | 26 | 9 | 16 | 1 |
| LLaMA-8B × PW | 76 | 13 | 58 | 5 |

## 已有 Shuffle Control（来自 `br_shuffle_control_results.json`）

| Condition | Original BR | Shuffle Null BR | p-value | Cohen's d |
|-----------|------------|----------------|---------|-----------|
| Qwen3-FOLIO-2x2 | 5.70 | 6.16 | 0.783 | −0.78 |
| GPT4o-FOLIO | 6.32 | 6.89 | 0.822 | −0.93 |
| Mistral7B-FOLIO | 3.16 | 3.31 | 0.706 | −0.62 |

### 关键发现

1. **Argmax Agreement 90.8%** — SICA 评分的 argmax 与 trace count 的 argmax 在超过 90% 的问题上一致，支持 degeneration 论点。

2. **Excess BR 始终为负** — 出乎意料的方向：observed BR（SICA score ratio）低于 base-rate predicted BR（trace count ratio）。这表明 SICA 评分不是放大 trace count 偏差，而是对其进行了压缩，但 Pearson r 在 0.24–0.70 之间说明 trace count ratio 仍是 SICA score ratio 的强预测因子。

3. **Disagreement 不对称** — 除 Mistral×FOLIO 外，当 SICA 和 SC 不一致时，SC 的正确率一致高于 SICA（SC 139 vs SICA 53），进一步说明约束提取引入噪声而非信息。

数据来源文件：Mistral PW 用的是 `multi_seed/mistral_pw_seed42`，如需用其他 seed 或 canonical 版本请指定。结果已保存至 `/root/symb_invariant_consensus/results/r17_argmax_br_metrics.json`。

---
