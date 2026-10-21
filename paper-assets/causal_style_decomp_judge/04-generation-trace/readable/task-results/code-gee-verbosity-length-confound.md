# code gee verbosity length confound

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gee_verbosity_length_confound_20260521T061342_result.json`
- **Structured JSON:** [`fce6a78fbe743781c0e5.json`](../../sessions/fc/fce6a78fbe743781c0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰，直接汇总：

## Verbosity Length Confound — 结果

**结论：Verbosity style effect 在控制 text length 后完全存活，OR 几乎不变。Length bias 假说不成立。**

### Qwen3-32B (86 pairs, 172 obs)

| Model | Style OR | Style p | Length OR | Length p |
|-------|----------|---------|-----------|----------|
| A: No length | 13.10 | 2.60e-09 | — | — |
| B: + length_ratio | 13.10 | 2.56e-09 | 1.03 | 0.424 |
| C: + length_diff | 13.32 | 2.37e-09 | 0.85 | 0.276 |
| D: + log_length_ratio | 13.13 | 2.60e-09 | 0.98 | 0.901 |

Style OR 变化：最大 +1.7%，所有模型 p < 3e-09。Length 本身完全不显著（p=0.28–0.90）。

### GPT-4o (85 pairs, 170 obs)

| Model | Style OR | Style p | Length OR | Length p |
|-------|----------|---------|-----------|----------|
| A: No length | 10.97 | 1.74e-08 | — | — |
| B: + length_ratio | 10.97 | 1.74e-08 | 1.03 | 0.478 |
| C: + length_diff | 11.02 | 1.69e-08 | 0.90 | 0.520 |
| D: + log_length_ratio | 11.03 | 1.81e-08 | 1.14 | 0.320 |

Style OR 变化：最大 +0.5%，所有模型 p < 2e-08。Length 同样完全不显著。

### 关键数字（给 rebuttal 用）

- 控制 length 后 Style OR 变化 < 2%，p-value 量级不变（10⁻⁸ ~ 10⁻⁹）
- Length covariate 本身在所有模型中均不显著（p > 0.27）
- 这说明 verbose/concise 的 **风格特征**（而非单纯字数差异）驱动了 judge 偏好
- Verbose 文本平均长 4.7x（median 2.0x），字符差 ~500 chars——length variation 很大，但对 judge 选择无预测力

脚本已保存在 `csd_pipeline/verbosity_length_confound.py`。

---
