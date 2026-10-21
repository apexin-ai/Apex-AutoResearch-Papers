# code stats analysis prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stats-analysis-prep_20260515T133936_result.json`
- **Structured JSON:** [`a7f57e5cd43a6bdad64c.json`](../../sessions/a7/a7f57e5cd43a6bdad64c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完毕，验证通过。

**路径**: `/root/acr-vla-conformal-refinement/scripts/statistical_analysis.py`

**使用方法**:

```bash
# 从 JSON 文件（支持多 seed 合并）
python scripts/statistical_analysis.py \
    --file_a logs/eval_obs_only_s42.json logs/eval_obs_only_s43.json \
    --file_b logs/eval_argmin_s42.json logs/eval_argmin_s43.json \
    --label_a obs_only --label_b argmin

# 从 summary 数据
python scripts/statistical_analysis.py \
    --a_success 70 --a_total 200 --b_success 55 --b_total 200 \
    --label_a obs_only --label_b argmin

# dry-run 验证
python scripts/statistical_analysis.py --dry_run
```

**输出内容**:
- Fisher exact test (p-value, odds ratio)
- Bootstrap 95% CI (success rate 差异)
- Cohen's h effect size
- McNemar's test (paired per-task，需 JSON 输入)
- Per-task breakdown 表格
- 若不显著，估算达到 p<0.05 需要的样本量

---
