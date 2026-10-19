# prep stat testing scripts

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_stat-testing-scripts_20260515T010842_result.json`
- **Structured JSON:** [`bbf7ec6cbb5c47469b9b.json`](../../sessions/bb/bbf7ec6cbb5c47469b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/structfuse/scripts/m2_statistical_analysis.py` 并通过 `--dry-run` 验证。

功能：
- **数据收集**：自动搜索 `full_m2_outputs/` 和 `checkpoints/` 两处目录，从 `train.log` 解析 `New best R@1=`、`[eval@step]`、`[Final eval]` 三种格式，缺失 run 给警告
- **统计检验**：paired t-test、Wilcoxon signed-rank、bootstrap 95% CI (1000 iter)、Cohen's d，按 encoder 分组，paired by seed
- **输出**：JSON (`m2_stats.json`) + Markdown 表格 (`m2_stats.md`)，含 heterogeneity 标注（StarCoder s42 = 3 epochs）
- **`--dry-run`**：mock 数据验证全流程

M2 训练完成后直接跑：
```bash
python /root/structfuse/scripts/m2_statistical_analysis.py
```

---
