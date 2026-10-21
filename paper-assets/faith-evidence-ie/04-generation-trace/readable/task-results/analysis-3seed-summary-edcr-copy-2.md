# analysis 3seed summary edcr

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_summary_edcr_20260515T115333_result.json`
- **Structured JSON:** [`ceabbabfca6e1e107d67.json`](../../sessions/ce/ceabbabfca6e1e107d67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成，汇总如下。

---

### 任务 1：3-seed 汇总脚本

脚本已创建在 `/root/autodl-tmp/scripts/summarize_3seed.py`，dry-run 通过（r1+s44 两个 seed 正常加载，s43 跳过）。

当前 2-seed 快照：

| 指标 | Mean | Std | SFT | Delta |
|------|------|-----|-----|-------|
| Rel F1 | 0.4552 | 0.0146 | 0.4057 | **+0.0495** |
| Evi F1 | 0.8137 | 0.0071 | 0.7979 | +0.0158 |
| EDCR | 0.6458 | 0.0152 | 0.7118 | **-0.0660** (↓好) |

s43_r2 完成后直接跑 `python /root/autodl-tmp/scripts/summarize_3seed.py` 即可（会自动检查 `rsft_s43/` 和 `rsft_s43_r2/` 两个路径）。

---

### 任务 2：EDCR 分析核心发现

报告已保存到 `/root/autodl-tmp/eval_results/edcr_analysis_r2b.md`。

**EDCR=0.6609 的根因是 FP triples，不是 evidence 选择质量：**

| 类别 | 三元组数 | Distractor引用数 | 占比 |
|------|---------|-----------------|------|
| A: FP triple（无 gold 匹配）| 8,279 | 14,766 | **90.2%** |
| B: TP + evidence 超集 | 992 | 1,122 | 6.9% |
| C: TP + evidence 部分重叠 | 330 | 367 | 2.2% |
| D: TP + evidence 完全不交 | 77 | 112 | 0.7% |

**关键结论**：90.2% 的 distractor citations 来自 FP triples —— 模型预测了错误的三元组，这些三元组的所有 evidence 都被计为 distractor。TP triples 的 evidence 质量其实很好（只贡献 9.8% distractor）。要降 EDCR，核心是**提升 precision、减少 FP**，而非改善 evidence 选择策略。

---
