# analysis r11 relative tost

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-relative-tost_20260521T114139_result.json`
- **Structured JSON:** [`bd8a12b5e9abcada7dde.json`](../../sessions/bd/bd8a12b5e9abcada7dde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Absolute ±2pp → Relative ±5% SC：4/16 条件分类变化，全部从 underpowered 翻转为 equivalent。**

| 指标 | Abs ±2pp | Rel ±5% SC |
|------|----------|------------|
| Equivalent | 4 | **8** |
| Different | 2 | 2 |
| Underpowered | 10 | **6** |

变化的 4 个条件（都是高 SC 模型，margin 从 2pp 放大到 ~3-4pp）：
- Qwen2.5-14B FOLIO (ICL): margin 2→3.72pp
- Qwen2.5-14B FOLIO: margin 2→3.65pp
- Qwen2.5-7B FOLIO: margin 2→2.97pp
- Qwen3-14B FOLIO: margin 2→3.48pp

2 个 different（Mistral-7B PW-D5、Qwen2.5-14B PW-D5）不变——它们的 margin 变化不足以改变显著性方向。

核心发现：relative margin 对强模型更宽容（SC 高→margin 大→更容易判定等价），强化了论文"SICA 与 SC 等价"的结论。已注册 artifact `r11_relative_tost`。

---
