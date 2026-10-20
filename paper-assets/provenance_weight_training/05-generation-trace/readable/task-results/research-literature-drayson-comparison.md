# research literature drayson comparison

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-drayson-comparison_20260514T233124_result.json`
- **Structured JSON:** [`9aa91c35ee55470f1f22.json`](../../sessions/9a/9aa91c35ee55470f1f22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/drayson_comparison.md`。

关键发现：
- **Drayson 的 b 是验证集 empirical 选取，训练中固定**（GPT-2/SmolLM 135M/360M 用 b=10，1.7B 用 b=1），无任何 adaptive 机制
- **你们的 adaptive b\* 在文献中无先例**——没有找到任何工作对 detection-score 权重指数做自适应推导
- 已有 `literature_diff_drayson.md` 包含更详细的策略建议（Angle A+B+C），新文件以更紧凑的格式呈现可直接用于论文的对比表和差异化论点

---
