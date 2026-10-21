# diag kl50 global s123 downstream v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_kl50_global_s123_downstream_v2_20260522T183123_result.json`
- **Structured JSON:** [`a210e62743e107921d94.json`](../../sessions/a2/a210e62743e107921d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**`kl50_global_s123_downstream_v2` 是 cron 监控误报，实验实际已成功完成。**

### 根因
实验以 `WANDB_MODE=disabled` 运行。Cron 健康检查依赖 W&B metrics 或 PID 存活检测——进程正常退出后 PID 消失，且无 W&B 数据可回退验证，连续 5 次检测 "process dead" 后自动判定失败。

### 实际结果（已保存到 results.json）
| Task | Metric | Value |
|------|--------|-------|
| ARC-c | acc_norm | 0.3916 |
| WinoGrande | acc | 0.6401 |
| MMLU | acc | 0.2908 |
| GSM8K | exact_match | 0.0341 |

### 前序实验 `kl50_global_s123_reeval`
最初在 westd-41718 因 CLI 参数不匹配失败（`--predictor_path` vs `--checkpoint`），retry 后成功。结果: ARC-c=0.3635, WG=0.6109, MMLU=0.2834, GSM8K=0.0258。

### 需要的操作
1. Registry 中 `kl50_global_s123_downstream_v2` 的 `conclusion` 需从 `failed` 更新为 `success`，补充 metrics
2. 日志路径在 `/root/distill_sparse_swiglu/logs/`（非 `~/runs/`）——任务描述中的路径有误
3. 长期建议：`WANDB_MODE=disabled` 的实验应在完成时写 sentinel 文件，避免 cron 误报

---
