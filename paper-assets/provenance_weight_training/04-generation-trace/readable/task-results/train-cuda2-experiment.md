# train cuda2 experiment

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cuda2_experiment_20260524T155714_result.json`
- **Structured JSON:** [`a7c9847ddf16b12921de.json`](../../sessions/a7/a7c9847ddf16b12921de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册。

**汇报：**
- **exp_id**: `detect_remove_q05_seed42`
- **GPU**: cuda:2 (RTX PRO 6000 98GB), westd-41312
- **方法**: 硬过滤 q_score > 0.5 的样本，剩余 153,725 样本 uniform 训练
- **速度**: ~2.24s/step, 6103 steps
- **预计时长**: ~3.8 小时
- **tmux session**: `detect_remove_q05_seed42`
- **日志**: `/root/provenance_weight_training/logs/detect_remove_q05_seed42.log`
- **注意**: wandb 未配置，本次无 wandb 追踪，训练日志写到本地文件

---
