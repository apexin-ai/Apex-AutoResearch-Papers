# fix table3 and 944 urgent

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table3-and-944-urgent_20260523T111430_result.json`
- **Structured JSON:** [`b31467edcd8e92b640cf.json`](../../sessions/b3/b31467edcd8e92b640cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

---

### 已修复

**Task 1 — SC Baseline**:
- 论文的错误 SC 值来自 finetuned 实验（72.50%），被误用到 zero-shot Table 3
- 正确值：LLaMA 70.00%、Qwen2.5 73.50%、Qwen3 85.00%（均来自各自 combo 结果文件的 `sc_baseline` 字段）
- 修正了 solutions.tex Table 3、appendix.tex Table 28 的全部 SC/Gap/Δ/p/BH 值

**Task 2 — 94.4%**:
- diagnosis.tex 中 "94.4%" 无法追溯到任何结果文件，可能是早期计算残留
- 已改为引用 tab:ablation 的实际数据（">96%"）
- analysis.tex 此前已独立修正为 "≥99%"（引用 tab:alpha-ablation），无需改动

**Task 3 — 文件修改**:
- `solutions.tex`: Table 3 数据 + 两处正文引用
- `appendix.tex`: Table 28 全表 + 叙述文字 + caption
- `diagnosis.tex`: 94.4% → >96%
- `figures/gen_capability_gap_scatter.py`: 3 个数据点坐标

**Task 4 — 验证**:
- grep 确认无旧值残留（72.50% 仅存于 finetuned 表和注释中，均正确）
- 修复报告已写入 `artifacts/table3_fix_report.md` 并注册

### 需 Director 决策的级联影响

1. **Figure 7 需重新生成**（脚本已更新，PDF 需重跑）
2. **LLaMA w=1 现在 BH 显著**（p_BH=0.0048），原论文 "only Mistral gains significantly" 的叙事需要调整——显著条件从 2→3 个
3. **Qwen3 SC=85.83% 在 experiments.tex/diagnosis.tex 的 SICA 主表中可能也有误**（exp033 数据显示 sc=85.00%），建议单独核查
4. **Spearman ρ=1.0** 排序仍单调递减（6.67>3.33>1.17>1.00），但具体统计值建议用新数据重算

---
