# code threshold q03 prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threshold_q03_prep_20260516T054228_result.json`
- **Structured JSON:** [`02e1e9c6d24f43eabb63.json`](../../sessions/02/02e1e9c6d24f43eabb63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。与 detect_remove_baseline 对比：超参数完全一致，唯一差异是过滤阈值 0.3 vs 0.5。

**结果：**

```
COMMAND: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && nohup bash scripts/run_threshold_q03.sh > logs/threshold_q03_seed42.log 2>&1 &
FILTERED_COUNT: 116,935 / 371K (31.5%, 过滤掉了 68.5% 的数据)
```

脚本变更摘要：
- 移除了 `WANDB_MODE=offline`，W&B 在线记录
- 加入了与 detect_remove 一致的自动过滤逻辑（`filter_high_qscore.py --threshold 0.3`）
- 过滤后数据文件 `scored_data_filtered_q03.jsonl` 已存在（116,935 条）
- 清理了之前失败运行的输出目录（只跑了 92 步）

---
