# analysis construct divergence

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_construct-divergence_20260522T230958_result.json`
- **Structured JSON:** [`10ee0bf5430ad621dd7e.json`](../../sessions/10/10ee0bf5430ad621dd7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Construct divergence 完整检验不可行** — 缺少 pairwise quality 数据。

### 数据缺口

项目的 pairwise 评分全部是**风格比较**（original vs counterfactual），不存在**质量比较**（LLMBar output_1 vs output_2 哪个更好）。因此无法计算 pairwise agreement with gold labels，也无法做 McNemar 检验。

### 可用的部分分析（Likert 侧）

通过将 100 个 scored entry 匹配回原始 LLMBar 数据，恢复了 output_tag。其中 10 对共享同一 instruction 的 entry 构成了可分析的 LLMBar pairs。

**Pair-level Likert accuracy**（gold-preferred output 得分更高？）：

| Judge | Pairs | Correct | Ties | Wrong | Acc | Mean Δ |
|-------|-------|---------|------|-------|-----|--------|
| Qwen3-32B | 10 | 10 | 0 | 0 | 1.000 | +4.1 |
| GPT-4o | 10 | 10 | 0 | 0 | 1.000 | +4.1 |
| Llama-70B | 9 | 7 | 2 | 0 | 0.778 | +2.7 |
| Gemini Flash | 9 | 7 | 2 | 0 | 0.778 | +4.7 |
| Qwen3-32B (formality) | 10 | 4 | 4 | 2 | 0.400 | +1.0 |

**Entry-level point-biserial** (is_gold_preferred vs score_original)：所有 judge 的 r 在 0.32–0.54 之间，均 p < 0.002。

### 关键发现

Likert 评分确实能区分 gold-preferred 和 non-preferred outputs（r ≈ 0.43–0.54），但 formality rewrite 后同一 judge 的区分力大幅下降（r = 0.32, pair-level acc = 40%）。这暗示**风格操纵压缩了 Likert 的质量区分能力**，间接支持 construct divergence 假设。

### 补全建议

标注为 future work。完整检验需要在 LLMBar 全部 319 pairs 上以 pairwise quality-comparison 模式运行 4 个 judge。

产出已写入 `artifacts/r14_fixes/construct_divergence_test.json`。

---
