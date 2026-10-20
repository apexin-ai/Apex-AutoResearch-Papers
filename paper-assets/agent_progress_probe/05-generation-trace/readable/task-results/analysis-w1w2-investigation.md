# analysis w1w2 investigation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w1w2-investigation_20260515T012354_result.json`
- **Structured JSON:** [`f88ad35348e24438c72f.json`](../../sessions/f8/f88ad35348e24438c72f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。

## 结果摘要

### W1: Probe ZS macro_f1 (0.581 vs 0.5984)

**Root cause: 评估范围不同。**
- 0.581 = error analysis 对全部 43,366 conf≥2 windows 的 macro_f1
- 0.5984 = cross-agent-eval / openhands-fewshot-probe 对 15% test split (~6,122 windows) 的 macro_f1
- 同一 checkpoint (`checkpoints/best_model.pt`, probe_001)，同一 embeddings，1.74pp 差异来自子集组成不同
- **论文使用 0.5984 是正确的**（与 few-shot 实验方法论一致）

### W2: Overlap 覆盖率 28% (12,328 / 43,366)

**Root cause: report.md 是 stale 的。**
- 当前代码和 JSON 输出已正确匹配 43,366/43,366 windows（**100% 覆盖率**）
- 12,328 来自旧脚本版本的 key 匹配 bug，已修复
- 修正后 overlap: probe 6,005 errors, struct 57 errors, both wrong = 31, overlap rate = 0.52%
- 核心发现不变：两个模型的错误几乎不重叠

### 注意

服务器上 `embeddings_fixed.pt`（May 15）和 `checkpoints/best_model.pt`（May 14）已被重建，当前运行结果 macro_f1=0.7588 与论文数据不一致。JSON 中的绝对数字不可用于论文，但 overlap 覆盖率修复（代码逻辑层面）可信。

---
