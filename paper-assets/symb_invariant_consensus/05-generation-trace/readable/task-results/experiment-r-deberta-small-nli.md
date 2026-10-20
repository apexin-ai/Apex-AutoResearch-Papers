# experiment r deberta small nli

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r-deberta-small-nli_20260520T103141_result.json`
- **Structured JSON:** [`f8db873f142ec735337d.json`](../../sessions/f8/f8db873f142ec735337d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成！4.3 秒跑完 204 题。结果非常有意义：

## Direction R 结果：DeBERTa-Large-MNLI 外部验证器

| Strategy | Acc | Correct | Delta vs SC |
|---|---|---|---|
| SC baseline (Mistral-7B K=12) | 54.41% | 111 | — |
| NLI standalone | 49.51% | 101 | -4.90% |
| NLI-as-verifier | 49.51% | 101 | -4.90% |
| **NLI-SICA-combo** | **57.84%** | **118** | **+3.43%** |

### Per-label 分析

| Label | NLI Acc | SC Acc | 观察 |
|---|---|---|---|
| True (n=72) | 59.72% | 55.56% | NLI 略强 |
| **False (n=63)** | **71.43%** | **38.10%** | **NLI 大幅领先 (+33pp)** |
| Unknown (n=69) | 18.84% | 68.12% | NLI 极弱 (-49pp) |

### 关键发现

1. **NLI 在 contradiction 检测上碾压 LLM**：False label 上 NLI 71.43% vs SC 38.10%，差距 33 个百分点。这正是 NLI 模型训练的强项。

2. **NLI 几乎无法处理 Unknown/neutral**：仅 18.84%。NLI 模型倾向于给出 entailment 或 contradiction，很少预测 neutral——这与 FOLIO 的三值逻辑不匹配。

3. **NLI-as-verifier 策略失败**：因为 NLI 和 SC 只有 45% 一致率，disagreement 时 NLI 仅 34% 正确(38/112)，直接替换反而更差。

4. **NLI-SICA-combo 最佳**（+3.43%）：NLI 作为额外 1 票加入 12 票 SC 中，在 False 类问题上修正了 SC 的错误，同时在 Unknown 上 SC 多数票能压过 NLI 的错误预测。

5. **互补性明确**：NLI 擅长 False（contradiction），LLM 擅长 Unknown（逻辑推理中的不确定性）。两者结构性互补。

---
