# train imm fullft k07 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_imm_fullft_k07_cqa1_20260516T231150_result.json`
- **Structured JSON:** [`d9377cf46ece6ed1c761.json`](../../sessions/d9/d9377cf46ece6ed1c761.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

## 确认结果

1. **配置文件**：`configs/libero_imm_twostage_fullft_k07.yaml`
   - k_ratio=0.7, delta=0.3, stage1=10K, stage2=20K
   - baseline_checkpoint: `checkpoints/libero_full_ft/step_099999/checkpoint.pt`
   - output_dir: `checkpoints/libero_imm_twostage_fullft_k07`

2. **GPU3 显存**：2881 MiB 占用

3. **训练输出**：
   - Stage 1 已开始，margin_loss=0.2964（正常）
   - ACIS 可训练参数 3.46M (0.76%)，expert 全部冻结
   - tmux session: `libero_imm_fullft_k07`
   - 日志: `~/runs/importance_margin_vla_compress/libero_imm_fullft_k07.log`

（首次启动失败原因：漏了 `source /etc/network_turbo`，第二次已修复。）

---
