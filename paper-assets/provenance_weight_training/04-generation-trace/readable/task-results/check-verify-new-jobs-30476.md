# check verify new jobs 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify_new_jobs_30476_20260518T142856_result.json`
- **Structured JSON:** [`9ac59f9709959751d5de.json`](../../sessions/9a/9ac59f9709959751d5de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-30476 状态报告

### tmux sessions
- `detect_remove_q07_seed42_r2` — **存在，运行中**
- `detect_remove_q03_seed42` — **不存在**
- `detect_remove_q01_seed42` — **不存在**
- `epoch_matched_dr_seed123` — **不存在**
- `epoch_matched_dr_seed456` — **不存在**

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 MiB | 0% |
| 1 | 0 MiB | 0% |
| 2 | 41757 MiB | 99% |
| 3 | 0 MiB | 0% |

只有 GPU 2 在跑（`detect_remove_q07_seed42_r2`），GPU 0/1/3 空闲。

### 新 job 启动状态

**4 个 job 全部启动失败**，log 内容均为：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

失败的 job：
- `detect_remove_q03_seed42` (GPU 2)
- `detect_remove_q01_seed42` (GPU 3)
- `epoch_matched_dr_seed123` (GPU 0)
- `epoch_matched_dr_seed456` (GPU 1)

原因：启动脚本用了 `python` 而不是 `python3`，或未激活 conda/venv 环境。

### 唯一在跑的实验：detect_remove_q07_seed42_r2
- 进度：**4287 / 6103 steps (70%)**
- Epoch：0.37
- Loss：weighted_loss ~1.69-3.16（波动正常）
- 速度：~2.10 s/it
- 预计剩余：**~1h04m**

### 结论
需要修复 4 个失败 job 的启动命令（python 路径问题），然后重新提交到 GPU 0/1/3。GPU 2 当前被 q07_r2 占用，q03 需要等它跑完或改到其他 GPU。

---
