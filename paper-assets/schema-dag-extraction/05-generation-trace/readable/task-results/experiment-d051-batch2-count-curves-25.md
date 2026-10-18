# experiment d051 batch2 count curves 25

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d051_batch2_count_curves_25_20260516T184749_result.json`
- **Structured JSON:** [`f69313dff7feb46fface.json`](../../sessions/f6/f69313dff7feb46fface.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并在运行。汇总：

---

**实验状态：RUNNING**

| 项目 | 详情 |
|------|------|
| tmux session | `d051_batch2` |
| 服务器 | cqa1-38874 |
| 当前进度 | Part A: RE count_16 推理中（192 samples/batch × 25 batches） |

**实验结构：**

| Part | 任务 | 数据集 | Batches | Seeds | 预估时间 |
|------|------|--------|---------|-------|----------|
| A | R6-W3 Count Curves | FewRel | 175 (7 levels × 25) | 42 | ~2h |
| A | R6-W3 Count Curves | Few-NERD | 150 (6 levels × 25) | 42 | ~3h |
| B | R8-W2 3-Seed | FewRel | 175 × 2 seeds | 123, 456 | ~4h |
| B | R8-W2 3-Seed | Few-NERD (key levels) | 75 × 2 seeds | 123, 456 | ~2h |

**预估总运行时间：8-12 小时**

**产出路径：**
- `artifacts/d051_fewrel_n25_s{42,123,456}/count_curve_summary.json`
- `artifacts/d051_fewnerd_n25_s{42,123,456}/count_curve_summary.json`

**脚本路径：**
- `/root/schema-dag-extraction/scripts/run_d051_count_curves_25.py`
- `/root/schema-dag-extraction/run_d051_batch2.sh`

**检查进度：**
```bash
ssh connect.cqa1.seetacloud.com 'tail -5 /root/schema-dag-extraction/artifacts/d051_batch2.log'
ssh connect.cqa1.seetacloud.com 'ls /root/schema-dag-extraction/artifacts/d051_fewrel_n25_s42/results_count_*.jsonl'
```

---
