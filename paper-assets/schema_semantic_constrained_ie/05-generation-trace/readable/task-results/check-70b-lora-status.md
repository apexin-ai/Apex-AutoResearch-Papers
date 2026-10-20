# check 70b lora status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_70b_lora_status_20260521T122625_result.json`
- **Structured JSON:** [`9621ce7540ff5f8631b2.json`](../../sessions/96/9621ce7540ff5f8631b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中完全没有 loss 输出。原因是脚本没有设置 `log_level="info"`，HF Trainer 的 loss 日志在 INFO 级别被默认 WARNING 级别过滤了。

## 汇报

### 1. SciERC (PID 836206/836212)
- **状态**: 存活，运行 ~23h
- **进度**: step **97/663** (14.6%)，~14.5s/step，预计还需 ~2h15m
- **Loss**: **无法观测** — 脚本未设 `log_level="info"`，Trainer 的 loss 日志被默认 WARNING 级别过滤。日志文件只有启动信息和 tqdm 进度条
- **NaN/Error**: 无异常，AwqGEMMLinear 警告 2 次（正常）
- **Checkpoint**: 尚无（`save_strategy="epoch"`，第 1 个 epoch 在 step 221）

### 2. DocRED (PID 835754)
- **状态**: **已死**
- **tmux session**: docred_70b **不存在**（当前 tmux 有 llama_beam, llama_wikievents, llama_wikievents_full, qwen_wikievents）
- **Checkpoint 目录**: `/root/autodl-tmp/checkpoints/70b_lora_docred/` **为空**（只有目录本身）
- **恢复**: 无 checkpoint，需从头重启

### 3. GPU VRAM
| GPU | 已用 | 总量 | 利用率 |
|-----|------|------|--------|
| GPU0 | 46.6 GB | 97.9 GB | 99% (SciERC) |
| GPU1 | 0 GB | 97.9 GB | 0% (空闲) |

### 4. 建议
- **DocRED**: 需从头重启到 GPU1，建议在新 tmux session 中启动
- **SciERC loss 监控**: 当前无法看到 loss。如需实时监控，可以：
  1. 在脚本 SFTConfig 中加 `log_level="info"` 然后重启（会丢失当前进度，不推荐）
  2. 等第 1 个 epoch 结束后从 `trainer_state.json` 读取完整 loss 历史（推荐，约 ~2h15m 后）

---
