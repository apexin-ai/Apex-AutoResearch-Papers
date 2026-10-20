# analysis temperature stratified

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_temperature_stratified_20260521T042035_result.json`
- **Structured JSON:** [`bb562f5eb5afe4bada0e.json`](../../sessions/bb/bb562f5eb5afe4bada0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果已保存。

---

**PART 1 — Stratified G coefficients:**

| Temperature | G(correct) | G(text) | Mean(correct) | Mean(text) |
|---|---|---|---|---|
| T=0.0 | 0.7605 | 0.0085 | 0.6987 | 0.9653 |
| T=0.3 | 0.6105 | 0.0673 | 0.6795 | 0.1524 |
| T=0.7 | 0.5492 | 0.0218 | 0.6699 | 0.0222 |

`correct` 指标：温度固定后 G 从全量的 0.007 恢复到 0.55–0.76，T=0.0 最高（76%方差来自 item_id）。随温度升高，residual 和 seed:item_id 交互增大（T=0.7 时 seed:item_id 占 14.8%），G 下降——采样随机性在侵蚀信号。

`text_exact_match`：即使分层后 G 仍极低（0.008–0.067）。T=0.0 时 precision 占 52.5%（float32 vs bf16/fp16 的文本匹配率差异巨大）；T=0.3/0.7 时 residual 占 75–82%，说明文本匹配在非零温度下几乎是纯噪声。

---

**PART 2 — Practical D-study（precision + temperature 固定）:**

- G(correct) = 0.6595，item_id 占 61.08%，delta 占 31.54%
- G(text_exact_match) = 0.0598（不可用）
- **Minimum items for G≥0.80 = 10**（D-study 反转：当前 200 items 远超所需，G 随 n_items 减少反而升高，因为 item variance 被放大）

---

**PART 3 — precision:temperature 交互:**

- `correct`: **0.05%** — 几乎不存在交互，precision 对准确率的影响不随温度变化
- `text_exact_match`: **4.15%** — 存在实质性交互

Cell means 揭示了交互本质：
- bf16/fp16 在 T=0.0 时文本匹配率 99.96%，到 T=0.7 骤降至 0.6%
- float32 在 T=0.0 时只有 74.09%，但 T=0.7 时仍有 5.39%（下降更平缓）

float32 的 KV cache 精度更高，在有采样随机性时反而保留了更多文本一致性。这就是 precision:temperature 交互的来源。

---
