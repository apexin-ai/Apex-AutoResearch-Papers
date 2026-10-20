# knowledge compile final figure data

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_compile_final_figure_data_20260516T015234_result.json`
- **Structured JSON:** [`280deb419fb651d17c95.json`](../../sessions/28/280deb419fb651d17c95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/dose_curve_figure_data.json` 并注册为 `art_20260516_f78c80`。

内容概要：
- **ds_accuracy**: 5-point dose curve (dense→s030), 含 accuracy/correct/truncation_rate/non_truncated_accuracy，所有值来自 `acc_ds_*_8k_v2` 系列
- **qw_accuracy**: 5-point dose curve，含 batch1/batch2/combined 三层数据 (n=100)，来自 `acc_qw_*_b1_8k` + `acc_qw_*_n100` 系列
- **ii_dose_curves**: 4 条 II dose curve
  - `ds_n50_bf16` / `qw_n50_bf16`: bf16 精度 n=50 paired-test 结果 + random baseline
  - `ds_n500` / `qw_n500`: 大规模验证 (n=496/475)，含 importance/random median II、Wilcoxon p、Cohen's d_z、Bonferroni 校正

---
