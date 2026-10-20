# research paper update checklist

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-update-checklist_20260514T183914_result.json`
- **Structured JSON:** [`aa9290ea633222a5abb5.json`](../../sessions/aa/aa9290ea633222a5abb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已生成并注册。总结：

**更新规模**：
- **7 处** "n=50"→"n=500" 文本替换
- **8 个表格**，约 80 个数据单元格需替换（Table 1-2 主结果、Table 3 Cohen's d、cross-model、permutation、discrimination、entropy 共 6 个正文/附录表）
- **5 个图表 PDF** 需用 n=500 数据重新生成（fig1 dose-response、fig2 Cohen's d、fig3 crossover、fig4 forest plot、fig5 cross-model）
- **~55 处**内联统计数值散布在 abstract/intro/results/analysis/discussion/conclusion/appendix 中
- **2 个条件性决策点**：
  1. Qwen s015 CI 是否含零 → 决定 threshold narrative vs full narrative（影响 6 处叙事）
  2. QW rand s030 是否仍 PASS → 决定 "7/8" vs "8/8"（影响 4 处）

**执行顺序**：等 16 conditions 全部完成 → 跑 5 个分析脚本 → 从 JSON 提取数值逐项替换 → 检查 Qwen s015 决策点 → 重编译 LaTeX → grep 残留旧值。

---
