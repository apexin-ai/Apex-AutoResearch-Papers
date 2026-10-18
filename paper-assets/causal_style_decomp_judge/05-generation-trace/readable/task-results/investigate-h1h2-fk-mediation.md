# investigate h1h2 fk mediation

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_h1h2-fk-mediation_20260525T201059_result.json`
- **Structured JSON:** [`6b944d2c26c01c4e45de.json`](../../sessions/6b/6b944d2c26c01c4e45de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。结论：

**只有 Sobel z 和 p 是错误的，OR 值正确。**

| 指标 | 论文值 | 正确值 |
|------|--------|--------|
| Sobel z | 2.15 | **3.60** |
| Sobel p | .031 | **0.0003** |
| Direct-effect Style OR | 2.15 | 2.15 ✓ |
| Total Style OR | 2.70 | 2.70 ✓ |

**错误机制**：作者将 FK-controlled Style OR=2.15 误写为 Sobel z=2.15，然后从该错误 z 值推导出 p=.031（2×(1-Φ(2.15))=0.031）。p 不是独立错误来源，而是从错误 z 推导的。

**2.15 与 Qwen3 n=355 的巧合**：`gee_n355_results.json` 中 Qwen3 n=355 style_or=2.15 是不同分析的数值巧合，论文中的 2.15 确实来自 `fk_gee_covariate.py` GPT-4o direct effect。

**额外发现**：FK-controlled Style OR=2.15 的 p=0.132（非显著），论文未报告。

修复建议：`(Sobel z = 3.60, p < .001)`

---
