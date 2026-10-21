# ops check status westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_status_westd_20260516T092924_result.json`
- **Structured JSON:** [`65876a24159831ba1ff5.json`](../../sessions/65/65876a24159831ba1ff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 实验状态汇总

### GPU 状态
| GPU | 型号 | 状态 | 显存占用 |
|-----|------|------|----------|
| cuda:0 | RTX PRO 6000 (96GB) | **空闲** | 0 MiB |
| cuda:1 | RTX PRO 6000 (96GB) | **空闲** | 0 MiB |

无 Python 训练进程运行，无 tmux session。

### 实验状态

| 实验 | 状态 | Checkpoint |
|------|------|------------|
| sft_qwen_math_rasp_20 (RASP 20%) | **已完成** | `model.safetensors` (11.5GB), 写入时间 16:58 |
| sft_qwen_math_standard_20 (Standard 20%) | **已完成** | `model.safetensors` (11.4GB), 写入时间 16:59 |

两个 checkpoint 目录均包含完整模型文件（config.json, model.safetensors, tokenizer, training_args.bin）。

实际路径为：
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/`
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/`

### 训练 Metrics
**无法获取最终 loss/token accuracy。** 训练脚本使用了 `save_strategy="no"` + `report_to="none"`，没有保存 trainer_state.json，也没有 wandb 记录。stdout 输出未被重定向到文件，训练进程已退出，日志已丢失。

### 磁盘空间

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根分区) | 30G | 5.0G | 26G | 17% |
| /root/autodl-tmp (数据盘) | 250G | 248G | **2.3G** | **100%** |

**数据盘几乎满了，仅剩 2.3G。** 后续实验（eval/GRPO）前需要清理空间。

---
