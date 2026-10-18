# analysis r15 mf3 gee n355

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15-mf3-gee-n355_20260523T055128_result.json`
- **Structured JSON:** [`18b76d13222db3e91619.json`](../../sessions/18/18b76d13222db3e91619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

**GEE Decomposition: n=88 → n=355 (Qwen3-32B, Formality)**

| | Style OR | 95% CI | p | Orig OR | 95% CI | p |
|---|---|---|---|---|---|---|
| **n=88** | 4.20 | [1.99, 8.87] | 0.0002 | 4.70 | [2.22, 9.96] | <0.0001 |
| **n=355** | 2.15 | [1.46, 3.16] | <0.0001 | 4.99 | [3.40, 7.34] | <0.0001 |

关键发现：

- **Style OR 缩水 49%**：4.20 → 2.15，确认 n=88 时 Style 效应被高估（小样本偏差）
- **Orig OR 稳定**：4.70 → 4.99，originality preference 不受样本量影响，是稳健效应
- **CI 宽度缩窄约 1.94×**（log-OR 尺度），接近理论值 √(355/88)=2.01
- **Regime 从 Mixed 变为 Orig-Dominated**：n=355 下 Style OR=2.15 远小于 Orig OR=4.99，说明 originality preference 是主导因素
- **Power**：min detectable OR 从 1.56 (n=88) 降至 1.25 (n=355)
- **无 verbosity 轴的 scaled 数据**

产出已保存至 `artifacts/r15_analysis/gee_n355_results.json`。

---
