# research fl comparison data conflict

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fl-comparison-data-conflict_20260525T095915_result.json`
- **Structured JSON:** [`d04e15b965bcef1fa169.json`](../../sessions/d0/d04e15b965bcef1fa169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/fl_comparison_investigation.md`。

核心结论：

1. **0.064 不是 bug** — 远程服务器 CSV 验证：Global 0.06432, HB EC-HTE 0.06427，三位小数均为 0.064
2. **"+0.006, +0.001" 也不是 bug** — 对应 `mean_bias`（有符号），z=0 和 z=1 的偏差方向相反，在 subgroup 内抵消；表格的 `|Bias|` 是 `mean_abs_bias`（无符号），不会抵消
3. **0.064 vs 0.008 是不同 DGP** — FL comparison 用 τ(0)=0, τ(1)=0.3（小效应），Table 1 用 τ̄=0.5, Δτ≈1.0（大效应），处理效应越大 EC-HTE 改善越显著
4. **本地无生成脚本**，CSV 仅存于远程 `results/exp_fl_comparison*.csv`

修复：仅需改 appendix.tex 3 处文字——区分 signed/unsigned bias 口径、标注 DGP 差异、在 caption 注明 Oracle floor。无需重跑实验。

---
