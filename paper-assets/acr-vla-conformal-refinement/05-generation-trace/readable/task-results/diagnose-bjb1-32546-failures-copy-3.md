# diagnose bjb1 32546 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-failures_20260521T003058_result.json`
- **Structured JSON:** [`35968d4021522dab4af3.json`](../../sessions/35/35968d4021522dab4af3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因：`python` 命令不存在

两个实验（seed62、seed63）都在启动瞬间失败，日志各只有一行：

```
nohup: failed to run command 'python': No such file or directory
```

日志文件仅 65 字节，进程从未真正启动过。

**原因**：该服务器使用 conda 环境，`python` 只存在于 `/root/miniconda3/bin/python`，系统 PATH 下没有 `/usr/bin/python` 或 `/usr/bin/python3`。启动命令用的 `nohup python ...` 没有先激活 conda，所以找不到 `python`。

### 磁盘 / GPU 状态

- 磁盘正常：`/root/autodl-tmp/` 218G 可用（13%），根分区 21G 可用（33%）
- GPU 正常：6x RTX 4090 全部空闲，仅 GPU 2 有一个进程在用

### seed49-r2（PID 720058）状态

**已死亡**，进程不存在。GPU 2 上当前运行的是另一个实验：

```
PID 712964 | 运行 42 分钟 | RSS 10.3GB | GPU 2
python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 61 
  --max_correction_norm 0.05  (norm005_seed61)
```

### 重跑建议

需要重跑 seed62、seed63，以及确认 seed49-r2 是否也需要重跑。重跑前修复启动命令，改为以下任一方式：

1. `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u src/evaluate.py ...`
2. 直接用绝对路径 `/root/miniconda3/bin/python -u src/evaluate.py ...`

---
