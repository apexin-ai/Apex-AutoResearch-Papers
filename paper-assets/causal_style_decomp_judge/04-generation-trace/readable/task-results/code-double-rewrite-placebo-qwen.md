# code double rewrite placebo qwen

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_double_rewrite_placebo_qwen_20260521T132436_result.json`
- **Structured JSON:** [`67bc46c0791e1c97ad35.json`](../../sessions/67/67bc46c0791e1c97ad35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 已 kill，结果已保存到 `data/double_rewrite_placebo_qwen32b.json`。

## 结果

Placebo test **未通过** — Qwen3-32B 对 double_rewrite 有强烈偏好，而非预期的 ~50%：

| Axis | n_pairs | n_consistent | consistency | original win rate | p-value |
|------|---------|-------------|-------------|-------------------|---------|
| **Formality** | 81 | 45 | 55.6% | **26.7%** [13.3%, 40.0%] | 0.0025 |
| **Verbosity** | 43 | 36 | 83.7% | **0.0%** [0.0%, 0.0%] | ≈0 |

**解读**：
- Judge 强烈偏好 double_rewrite（经过两轮 LLM 改写的文本）而非原始文本
- Verbosity 轴尤为极端：36/36 一致性判断全部选 double_rewrite
- Formality 轴 consistency 仅 55.6%（几乎等于随机），说明判断本身很噪
- 这意味着 pairwise format 确实会从 rewriting artifact 产生 bias — **MF1 防御不成立**，rewriting 过程本身引入了 LLM 偏好的文本特征（更平滑、更结构化），judge 能区分并偏好 LLM 改写版本

---
