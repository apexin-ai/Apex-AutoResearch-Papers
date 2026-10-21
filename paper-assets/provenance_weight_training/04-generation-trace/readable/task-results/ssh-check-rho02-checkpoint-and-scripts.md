# ssh check rho02 checkpoint and scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_rho02_checkpoint_and_scripts_20260517T060549_result.json`
- **Structured JSON:** [`de12688a284f79130d65.json`](../../sessions/de/de12688a284f79130d65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. checkpoint-3000 完整路径
`/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/checkpoint-3000/`

### 2. optimizer.pt 或 optimizer_states/
**NO** — 目录中不存在 `optimizer.pt` 也不存在 `optimizer_states/` 目录。

### 3. scheduler.pt
**NO** — 不存在 `scheduler.pt`。

### 4. 完整文件列表

| 文件 | 大小 |
|------|------|
| added_tokens.json | 707 B |
| chat_template.jinja | 4.2 KB |
| config.json | 1.4 KB |
| generation_config.json | 188 B |
| merges.txt | 1.6 MB |
| model.safetensors | **1.19 GB** |
| special_tokens_map.json | 613 B |
| tokenizer.json | 11.4 MB |
| tokenizer_config.json | 5.4 KB |
| trainer_state.json | 4.2 MB |
| training_args.bin | 5.9 KB |
| vocab.json | 2.8 MB |

这是一个 **inference-only checkpoint**（仅含模型权重和 tokenizer，无训练状态），无法用于 resume training。

### 5. grid_b0_3 脚本 eval 参数检查
**CLEAN** — 两个脚本 (`run_grid_b0_3_seed123.sh`, `run_grid_b0_3_seed456.sh`) 中 grep `eval_steps` 和 `eval_data_path` 均无匹配输出。

---
