# ops diagnose lora only failure

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_lora_only_failure_20260519T124535_result.json`
- **Structured JSON:** [`a9a86fce4413474202b4.json`](../../sessions/a9/a9a86fce4413474202b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Checkpoint 状态

| Checkpoint | 状态 | 文件 | 大小 |
|---|---|---|---|
| `epoch_0/lora/` | **完整** | adapter_config.json + adapter_model.safetensors (19.3MB) + README.md | 保存于 17:14 |
| `epoch_1/lora/` | **完整** | 同上 | 保存于 19:09 |
| `epoch_2/` | **不存在** | 训练在 Epoch 2 中途被 kill，未完成保存 | — |

### 最后记录的 Training Metrics

- **Epoch 0 done**: Avg Loss=1.0154, L_NTP=0.9809, L_GAR=0.0345
- **Epoch 1 done**: Avg Loss=0.9462, L_NTP=0.9450, L_GAR=0.0012
- **Epoch 2 最后一条日志**: Step 6700, L_NTP=0.8149, L_GAR=0.0003, Loss=0.8152
- Gate 值全程固定 1.0000（所有 28 层），符合 LoRA-only baseline 预期

### GPU 状态

**GPU 正在被占用**：PID 46085 (python), 显存 91312 MiB / 97887 MiB (93%), GPU 利用率 99%。有其他训练任务在跑，当前不可用于重启训练。

### 磁盘

根分区 30G，已用 16G，剩余 15G (51%)。空间充足。

### 结论

- epoch_0 和 epoch_1 的 LoRA checkpoint 完整可用，可从 epoch_1 恢复训练（只需跑完 Epoch 2）
- Epoch 2 跑到 Step 6700（日志中 step 编号是全局的，每 epoch ~3000 步，已完成 ~70% of Epoch 2）
- GPU 当前被另一进程占满，需等其结束或 kill 后才能恢复训练

---
