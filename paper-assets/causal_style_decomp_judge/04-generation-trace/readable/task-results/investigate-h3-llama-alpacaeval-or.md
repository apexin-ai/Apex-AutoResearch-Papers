# investigate h3 llama alpacaeval or

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_h3-llama-alpacaeval-or_20260525T201117_result.json`
- **Structured JSON:** [`32ecd5c8bf55435e52bc.json`](../../sessions/32/32ecd5c8bf55435e52bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成，报告已写入 `artifacts/investigate_h3_m4.md`。

### H3 结论
OR=7.64 来自 **r14 修正后的 cross-benchmark 分析**（`artifacts/r14_fixes/cross_benchmark_local.json`），经过 NLI≥0.90 过滤后 GEE 正常收敛（VIF=1.51, CI=[3.35, 17.38]）。`data/llama70b_crossbench_summary.json` 是旧版未过滤数据（OR=2.18e+21 degenerate），已被修正版替代。**论文值正确，无需修改。**

### M4 结论
- 论文声明 "all three judges p>0.15" 限定于 **formality** axis，三个 p 值分别为 0.725 / 0.154 / 0.440，全部 > 0.15（Qwen3 仅高出 0.004）。**声明准确。**
- GPT-4o verbosity 100pt（wilcoxon_p=0.067）是独立实验，不在论文 claim 范围内。但主文第 79 行的泛化表述（"unresolved by 100-point continuous scaling"）可能让读者误以为覆盖所有 axis，建议考虑加上 "for formality" 限定词。

---
