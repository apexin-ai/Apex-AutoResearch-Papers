# analysis diversity quantification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diversity_quantification_20260515T042244_result.json`
- **Structured JSON:** [`e8cfc05ed081d5a52d81.json`](../../sessions/e8/e8cfc05ed081d5a52d81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/diversity_analysis.json`。

关键发现：

**Diversity 排序（高→低）：Qwen SciERC > LLaMA SciERC > WNUT-17 > Qwen CoNLL > LLaMA CoNLL**

| Config | Unique Frac (mean) | F1 Std | Pairwise SJ (mean) | Logprob Std |
|--------|-------------------|--------|---------------------|-------------|
| Qwen SciERC | 0.433 | 0.144 | 0.703 | 0.0205 |
| LLaMA SciERC | 0.389 | 0.127 | 0.744 | 0.0188 |
| WNUT-17 (Qwen) | 0.224 | 0.100 | 0.823 | 0.0215 |
| Qwen CoNLL | 0.235 | 0.092 | 0.869 | 0.0256 |
| LLaMA CoNLL | 0.147 | 0.020 | 0.972 | 0.0069 |

核心观察：
1. **SciERC diversity 远高于 CoNLL/WNUT** — SciERC 实体边界模糊（科学术语），导致输出变化大；CoNLL/WNUT 是标准 NER（人名/地名），大部分 instance 8 个 sample 完全一致（unique=1 占 57%-88%）
2. **LLaMA CoNLL 几乎无 diversity** — 88% instance 的 8 个 sample 完全相同（unique=1=2421/2756），pairwise SJ 中位数=1.0，constrained decoding 对简单 NER + 强模型的输出高度确定
3. **Qwen 比 LLaMA 在同一数据集上 diversity 更高** — SciERC 上 0.433 vs 0.389，CoNLL 上 0.235 vs 0.147，说明 Qwen 在 constrained decoding 下产生更多样化的输出
4. **WNUT-17 注意**：原始数据有 N=16 samples，这里截取前 8 个分析

---
