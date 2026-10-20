# ops gpqa analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpqa_analysis_prep_20260517T021841_result.json`
- **Structured JSON:** [`0cc16737f87331791829.json`](../../sessions/0c/0cc16737f87331791829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出**: `/root/autodl-tmp/pacs/scripts/analyze_gpqa_results.py`

**功能**:
- `--output_dir &lt;dir>`: 单条件分析 (per-phase median + bootstrap CI, phase gradient, Wilcoxon p, Cohen's d_z)
- `--compare_dir &lt;dir>`: 两条件对比 (importance vs random, 含 d_z ratio 和 interpretation)
- `--output &lt;path>`: JSON 报告输出
- `--dry-run`: 检查数据可用性

**使用方式** (实验完成后):
```bash
# 单条件
/root/miniconda3/bin/python3.12 scripts/analyze_gpqa_results.py --output_dir profiling_output_gpqa_ds_importance_s020

# importance vs random 对比
/root/miniconda3/bin/python3.12 scripts/analyze_gpqa_results.py \
  --output_dir profiling_output_gpqa_ds_importance_s020 \
  --compare_dir profiling_output_gpqa_ds_random_s020 \
  --output artifacts/gpqa_s020_comparison.json
```

---
