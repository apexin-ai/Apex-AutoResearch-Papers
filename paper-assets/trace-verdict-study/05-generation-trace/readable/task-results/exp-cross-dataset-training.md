# exp cross dataset training

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross_dataset_training_20260522T042845_result.json`
- **Structured JSON:** [`928bf57f3c3471c8130a.json`](../../sessions/92/928bf57f3c3471c8130a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**已完成：**
- 修改 `train_sft.py` 和 `evaluate.py` 的 `--condition` choices，新增 4 个 cross-dataset 条件
- 创建串行脚本 `/root/trace-verdict-study/scripts/run_cross_dataset.sh`（4 个实验依次训练+评测）
- 注册 4 个实验（PREPARING）并设置 hypothesis
- 通过 `submit_training_job` 提交到 cuda:1，tmux session: `cross_dataset_batch`

**当前状态：** 脚本正在等待 cuda:1 释放。deepseek_loop_only 在 step 148/444（~33%），预计还需 ~2 小时。等它结束后，4 个 cross-dataset 实验会自动依次执行。

**预计训练时长：**
- HE→MBPP（1640 train samples）：3 epochs ≈ 16 steps/epoch × 3 = ~15 min/experiment
- MBPP→HE（4270 train samples）：3 epochs ≈ 40 steps/epoch × 3 = ~40 min/experiment
- 加上 eval：总计约 2-3 小时

**日志：** `tail -f /root/runs/trace-verdict-study/cross_dataset_batch.log` 或 `/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log`

---
