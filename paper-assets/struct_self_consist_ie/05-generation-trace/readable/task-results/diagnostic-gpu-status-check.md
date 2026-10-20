# diagnostic gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_gpu_status_check_20260518T123758_result.json`
- **Structured JSON:** [`1603a5f49845bda4c972.json`](../../sessions/16/1603a5f49845bda4c972.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状态汇总

### 各 GPU 状态

| GPU | 显存 | GPU-Util | 温度 | 状态 |
|-----|------|----------|------|------|
| 0 | 2MiB / 32607MiB | 0% | 30°C | **空闲** |
| 1 | 30888MiB / 32607MiB | 94% | 80°C | **忙碌** — LLaMA Few-NERD 训练 |
| 2 | 2MiB / 32607MiB | 0% | 28°C | **空闲** |
| 3 | 2MiB / 32607MiB | 0% | 27°C | **空闲** |

### LLaMA Few-NERD 训练

- **PID**: 137865
- **启动时间**: 今天 17:31（已运行约 3 小时）
- **命令**: `llamafactory-cli train train_config_llama_fewnerd.yaml`
- **运行脚本**: `run_llama_fewnerd_train_single_gpu.sh`（通过 tmux pts/3）
- **显存占用**: 30878MiB（GPU 1 几乎满载）
- **进度**: **9% (423/4706 steps)**，约 ~8.5 it/s，预计还需约 8 分钟完成当前 epoch
- **日志**: `logs/llama_fewnerd_train.log`

### tmux sessions

可见有活跃的 tmux session：
- `exp_001_n16_seed456` — 之前的 pilot 实验 session（挂着但进程似乎已完成，只有 bash shell）
- pts/3 — LLaMA 训练正在跑

### 孤儿进程

无孤儿进程。所有 Python 进程都有明确的父进程和用途：
- LLaMA 训练（PID 137865）— 正常运行
- Jupyter Lab / TensorBoard / supervisord — 系统服务，正常

### 结论

GPU 0/2/3 空闲可用。GPU 1 正在跑 LLaMA Few-NERD 单卡训练，进度 9%，运行正常。

---
