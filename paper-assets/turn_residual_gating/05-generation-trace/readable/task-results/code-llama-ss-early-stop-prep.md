# code llama ss early stop prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_ss_early_stop_prep_20260524T121021_result.json`
- **Structured JSON:** [`47efd5466dca14c671ca.json`](../../sessions/47/47efd5466dca14c671ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 1. Checkpoint 机制确认

| 项目 | 结果 |
|------|------|
| Per-epoch checkpoint | **有**，每 epoch 结束后自动保存到 `{output_dir}/epoch_{N}/` |
| 保存内容 | `lora/` (LoRA weights) + `gate_params.pt` (gate + turn_embedding) |
| Epoch 0 | 已保存 (`runs/p1_llama_ss_s42/epoch_0/`, 4.4MB gate_params.pt) |
| Epoch 1 | 训练完成后会自动保存到 `epoch_1/` |
| Epochs 参数 | `--epochs 3`，在 `p1_llama_ss_train.sh` 中 |

## 2. 早停方案：Scheme B (watcher)

已创建 **`scripts/epoch2_watcher.sh`**：
- 每 5 分钟检查日志是否出现 `"Checkpoint saved to runs/p1_llama_ss_s42/epoch_1"`
- 检测到后等 10 秒确保磁盘 I/O 完成，验证 checkpoint 文件完整
- SIGTERM 杀 python 子进程，5 秒后仍存活则 SIGKILL
- 如果训练进程提前退出也能优雅处理

**启动方式**（需要时执行）：
```bash
nohup bash scripts/epoch2_watcher.sh > logs/epoch2_watcher.log 2>&1 &
```

## 3. Eval 脚本

已创建 **`scripts/p1_llama_ss_eval.sh`**：
- Checkpoint 自动检测，优先 `epoch_1` (2-epoch 早停)
- TF eval: Base + SS × GAR-ours + GAR-Dongre (4 组)
- AR eval: SS β=0/3/5 N=50 + Base β=0 N=50 (2 组)
- 自带 Bootstrap 95% CI 统计
- 输出到 `results/llama_ss_eval/`

---
