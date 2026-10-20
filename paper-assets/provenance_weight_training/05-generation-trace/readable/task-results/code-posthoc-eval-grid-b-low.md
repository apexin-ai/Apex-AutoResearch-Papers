# code posthoc eval grid b low

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_posthoc_eval_grid_b_low_20260515T083643_result.json`
- **Structured JSON:** [`0c074a359c98f8671a60.json`](../../sessions/0c/0c074a359c98f8671a60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建，参数接口验证通过。

**产出：**
- 脚本路径：`/root/provenance_weight_training/training/run_posthoc_eval_grid_b_low_seed42.sh`
- 参数验证：`eval_perplexity.py --help` 确认 `--checkpoints`、`--data_path`、`--max_docs`、`--output_path` 均匹配
- 结果输出到：`output/eval/posthoc_eval_grid_b_low_seed42.json`

**当前状态：** 训练尚未完成（b=0.1 在跑，b=0.2/0.3 未开始），3 个 `final/` 目录都不存在。脚本有缺失检查，会跳过不存在的 checkpoint 并打印 WARNING，全部缺失则 exit 1。训练完成后运行：

```bash
bash training/run_posthoc_eval_grid_b_low_seed42.sh
```

---
