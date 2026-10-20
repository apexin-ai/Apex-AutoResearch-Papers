# analysis failure mode smollm3 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_failure_mode_smollm3_14b_20260520T080348_result.json`
- **Structured JSON:** [`15ba146bb14c21196605.json`](../../sessions/15/15ba146bb14c21196605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**不是 scale 效应。** Pythia-6.9B (7/8 sig) 和 Qwen-0.8B (8/8 sig) 表明大模型可以保留 MMCT 信号。两个"失败"模型有各自不同的根因：

1. **SmolLM3-3B — Entropy-Diversity Decoupling**：entropy 轨迹呈强 U 型（gen 0→2 骤降至 0.94，gen 10 反弹至 1.70），与 distinct_1 的单调下降走向相反，破坏了 Granger 因果关系。ECE 通道完好 (3/3 distinct pairs 显著)。

2. **Pythia-1.4B s42 — Entropy 早期饱和 + 种子不幸**：entropy gen 2 后锁定在 ~1.28 几乎不动，变异量被噪声淹没。但 s43 种子 robust_pairs=7，证明非系统性问题。

3. **Mauve 跨所有模型系统性弱**（Qwen-0.8B 除外），根因是动态范围仅 ~0.01、T=11 统计功效不足。

报告已保存至 `artifacts/failure_mode_analysis/report.md` 并注册。

---
