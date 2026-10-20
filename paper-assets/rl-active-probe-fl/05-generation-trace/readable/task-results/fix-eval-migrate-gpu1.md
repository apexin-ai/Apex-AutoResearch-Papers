# fix eval migrate gpu1

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-migrate-gpu1_20260514T111547_result.json`
- **Structured JSON:** [`4fdba96f5c48c7510619.json`](../../sessions/4f/4fdba96f5c48c7510619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Eval 进程 kill + 重启
- 原 eval (PID 30633) 已 kill
- 首次重启时发现 **evaluate.py 第 243 行会用 `--gpu` 参数覆盖 `CUDA_VISIBLE_DEVICES`**，导致外部设 `CUDA_VISIBLE_DEVICES=1` 无效，进程跑到了 GPU 0 上
- 紧急 kill 后改用 `--gpu 1` 重启，新进程 PID 32728 正确运行在 GPU 1 上，当前 5/202 样本，~9s/sample

### 2. GRPO reward 值
GRPO 仅完成 1/73 步（~12:37/step），`logging_steps=5`，**reward 数据尚未输出**。预计 step 5 日志约在 ~20:00 出现。暂无 error/traceback。

### 3. GPU 双卡分配确认
| GPU | 进程 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 (cd33e1aa) | GRPO (PID 30171) | 22698 MiB / 97887 MiB | 39% |
| 1 (51df6041) | Eval (PID 32728) | 17174 MiB / 97887 MiB | 68% |

### 4. 注意事项
- `evaluate.py` 内部覆盖 `CUDA_VISIBLE_DEVICES`（第 243 行），以后启动 eval 应直接用 `--gpu <物理GPU编号>`，不要依赖外部环境变量

---
