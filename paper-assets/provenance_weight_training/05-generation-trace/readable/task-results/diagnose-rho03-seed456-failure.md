# diagnose rho03 seed456 failure

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_rho03_seed456_failure_20260523T031441_result.json`
- **Structured JSON:** [`775e81318e109352b797.json`](../../sessions/77/775e81318e109352b797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败原因：磁盘满 (No space left on device)

`/root/autodl-tmp` 250GB **100% 已用**，仅剩 1.9MB。四个实验全部在保存 checkpoint 时因磁盘写满崩溃。

| 实验 | 崩溃位置 | 错误 |
|------|---------|------|
| rho03_adaptive_seed456 | step 1000 (16%) | 写 optimizer.pt 时 iostream error |
| rho03_uniform_seed456 | step 1500 (25%) | 写 model.safetensors 时 `os error 28` |
| bs8_nmin4_adaptive_seed123 | step 1000 (16%) | 同上 `os error 28` |
| bs8_nmin4_uniform_seed123 | step 1000 (16%) | 同上 `os error 28` |

### B=8 实验状态

**也挂了**，同样是磁盘满。4 块 GPU 全部空闲（0% 利用率，0 MiB 显存）。

### Checkpoint 可恢复性

| 实验 | 可用 checkpoint | 状态 |
|------|----------------|------|
| rho03_adaptive_seed456 | checkpoint-500 ✅, checkpoint-1000 ✅ | 1000 完整（model 1.1GB + optimizer 673MB） |
| rho03_uniform_seed456 | checkpoint-500 ✅, checkpoint-1000 ✅ | **checkpoint-1500 损坏**（model 仅 36KB） |
| bs8_nmin4_adaptive_seed123 | 未检查 | — |
| bs8_nmin4_uniform_seed123 | 未检查 | — |

### 下一步

必须先清理磁盘空间才能恢复。建议：
1. 删除损坏的 checkpoint（uniform_seed456/checkpoint-1500）
2. 清理旧的/不需要的 checkpoint 和模型文件释放空间
3. 从 checkpoint-1000 恢复所有实验（`--resume_from_checkpoint`）
4. 考虑减少 checkpoint 频率或只保留最近 N 个 checkpoint（`save_total_limit`）

需要我查看磁盘占用大户并制定清理方案吗？

---
