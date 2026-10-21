# diagnose cwm8b v4 crash

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm8b-v4-crash_20260515T174735_result.json`
- **Structured JSON:** [`6aad656b5fc7db992ecf.json`](../../sessions/6a/6aad656b5fc7db992ecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总如下：

---

## CWM 8B 训练崩溃诊断报告

### 1. 进程状态
**已死。** PID 266816 不存在，tmux session `repo-level-cwm-8b-conda-v4` 也不在 session 列表中。

### 2. 崩溃原因：`timeout` 超时 (EXIT_CODE=124)
日志末尾明确显示 `EXIT_CODE=124`，这是 bash `timeout` 命令的标准退出码。训练进程被外部 timeout 包装器强制杀死，**不是 OOM、CUDA error 或磁盘满**。佐证：
- dmesg 无 OOM killer 记录
- 磁盘 `/root/autodl-tmp` 剩余 102G（60% 使用率），充足
- 日志中无任何 error/exception/CUDA 错误

训练实际运行了 **~23h54m**，在 step 5273/6633 (79.5%) 处被 timeout 终止。Cron 上报的 step 4013 (60.5%) 是过期数据。

### 3. 最新完整 checkpoint
**checkpoint-5200**（保存于 2026-05-16 01:30）。文件完整：
- `adapter_model.safetensors` (61MB)
- `optimizer.pt` (123MB)
- `scheduler.pt`, `trainer_state.json`, `rng_state.pth` 均存在

丢失了 step 5201-5273 共 73 步进度（~14 分钟训练量）。

### 4. cuda:2 状态
**空闲可用。** 显存 0 MiB / 32607 MiB，利用率 0%。

其他 GPU 仍在使用中：
| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 18477/32607 MiB | 99% |
| 1 | 27313/32607 MiB | 88% |
| 2 | **0/32607 MiB** | **0%** |
| 3 | 22527/32607 MiB | 88% |

### 5. Resume 可行性
**可以直接从 checkpoint-5200 resume。** 剩余 1433 步（~4h45m，按 ~12s/it 估算）。启动时需要：
- 将 timeout 时长设为 ≥8h（给足余量）
- 日志写入正确的 v4 log 文件（当前实际写入了 v2.log）
- `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-5200`

---
