# writing results skeleton

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_results-skeleton_20260514T054026_result.json`
- **Structured JSON:** [`0f230593034386174522.json`](../../sessions/0f/0f230593034386174522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Section 5 Results 骨架已写入 `artifacts/_project/paper/results.tex`，provenance 已注册。

结构总览：

- **§5.1 Phase-Modulated Severity Gradient** — Table 1 (main results: 8 行, 4 sparsity × 2 strategy)、Figure 1 (hero line plot)、Table 2 (bootstrap CI: paired + unpaired)、Figure 4 (forest plot)，叙述 gradient 单调递增 + sub-exponential 增长率递减 + median 选择理由
- **§5.2 Strategy-Dependent Crossover** — Figure 2 (crossover heatmap)，叙述 direction reversal（非 magnitude 差异）+ crossover onset 的 phase transition 含义，forward reference §6 mechanism
- **§5.3 Cross-Model Replication** — Table 3 (DeepSeek vs Qwen)、Figure 5 (cross-model comparison)，全部 `\placeholder{}`，结论句 framing 为 "emergent property" 而非 model-specific artifact

所有数字均为 `\placeholder{}`，无 fp16 数据泄漏。每个 claim 旁有 `% Evidence:` 注释。Framing 遵守 D015 硬约束（emergent phase-strategy interaction，未使用 "importance metric limitation"）。

---
