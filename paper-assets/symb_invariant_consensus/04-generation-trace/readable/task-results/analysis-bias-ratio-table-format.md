# analysis bias ratio table format

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bias-ratio-table-format_20260520T113129_result.json`
- **Structured JSON:** [`d1286a6f0d1f4c040f11.json`](../../sessions/d1/d1286a6f0d1f4c040f11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过（Mistral BR_err=4.24 与已有数据精确匹配）。LLaMA-3.1-8B 的 exp034 实验没跑完（python not found），用 Gemma-2-7B 替代作为第三个模型家族。

结果如下：

### Table 1: Confirmation Bias

| Model | N | Errors | BR_err | Wrong% | BR_cor | Gold% | Δ |
|-------|---|--------|--------|--------|--------|-------|---|
| Mistral-7B | 204 | 83 | 4.24 | 80.9% | 2.63 | 72.4% | +1.61 |
| Qwen2.5-14B | 204 | 52 | 3.69 | 78.7% | 7.87 | 88.7% | -4.18 |
| Gemma-2-7B | 204 | 40 | 4.06 | 80.3% | 8.34 | 89.3% | -4.28 |

- **BR_err** = 非 gold 权重 / gold 权重（错误题），越高越 biased
- **Wrong%** = 错误题中约束权重流向非 gold 答案的比例
- **BR_cor** = gold 权重 / 非 gold 权重（正确题）
- 三个模型的错误题 BR 都在 3.7–4.2，说明 confirmation bias 是跨模型一致的现象

### Table 2: SICA vs SC Agreement

| Model | SICA Acc | SC Acc | SICA=SC | SICA⊳SC | SC⊳SICA |
|-------|----------|--------|---------|---------|---------|
| Mistral-7B | 59.3% | 54.4% | 91.7% | 12 | 2 |
| Qwen2.5-14B | 74.5% | 75.0% | 96.6% | 2 | 3 |
| Gemma-2-7B | 80.4% | 80.9% | 99.5% | 0 | 1 |

LaTeX 版本已在脚本输出中，可直接复制。脚本路径：`/root/symb_invariant_consensus/scripts/gen_bias_tables_v2.py`

---
