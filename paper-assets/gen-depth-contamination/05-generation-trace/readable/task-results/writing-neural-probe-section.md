# writing neural probe section

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_neural-probe-section_20260514T040621_result.json`
- **Structured JSON:** [`5cd915d68c5300f65b12.json`](../../sessions/5c/5cd915d68c5300f65b12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/drafts/neural_probe_section.md`。

结构：Motivation → Method → Results（含 LaTeX 表格代码和 Pythia/OLMo placeholder）→ Interpretation。关键内容：

- **2v3 是翻转边界**：neural probe $0.6195 \pm 0.0094$ > $\theta$（PASS），LightGBM $0.5609$（FAIL），$K^*$ 从 2 升到 3
- **1v2 margin 从 0.0114 扩大到 0.0983**，说明 15D 投影确实丢信息
- **Interpretation 的核心论点**：$K^*=2$ 是测量工具的限制而非数据本身的极限，但 100× 维度增长只提升 1 级 $K^*$，lossy channel 叙事不变
- **两个 caveats**：单数据集 + self-recognition 可能膨胀区分度
- Pythia/OLMo 预留了注释掉的表格行和显式 placeholder 文字

---
