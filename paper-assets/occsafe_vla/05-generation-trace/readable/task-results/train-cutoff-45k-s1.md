# train cutoff 45k s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cutoff_45k_s1_20260524T122919_result.json`
- **Structured JSON:** [`8b07b7e5c866271fa2ec.json`](../../sessions/8b/8b07b7e5c866271fa2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cutoff_45k_s1 已启动，训练正常运行。**

总结：
- **服务器**: westd-34685, GPU 0, tmux session `cutoff_45k_s1`
- **PID**: 882188
- **配置**: `--occ_loss_cutoff_step 45000 --occ_loss_cutoff_mode after --seed 43`
- **Trainable params**: 279,977,608 ✓
- **初始 loss**: occ_loss=0.178, action_loss=0.652
- **日志**: `~/runs/occsafe_vla/cutoff_45k_s1.log`
- **Registry**: RUNNING

注意：任务指令中部分路径与实际运行环境不一致，已按 cutoff_15k_s1/cutoff_25k_s1 的实际命令格式修正（`--vla_path`、`--occ_data_dir`、`--occ_loss_cutoff_mode after`）。

---
