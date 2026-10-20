# code plan009 sft setup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-sft-setup_20260514T105605_result.json`
- **Structured JSON:** [`349f5ab102ecf8bf1091.json`](../../sessions/34/349f5ab102ecf8bf1091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型验证通过。现在整理结果。

---

## 报告

### 1. 模型下载路径
`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`

（注意：这是 ModelScope 创建的符号链接，指向 `._____temp` 下的实际文件）

### 2. 模型大小
- 文件大小：**2.9GB**（model.safetensors = 2.88GB）
- 参数量：**~1.5B**
- vocab_size：151643

### 3. train_sft.py 修复确认
第 165 行：`save_total_limit=3` → `save_total_limit=1` ✓（符合 C003 约束）

### 4. train_sft.py 命令行参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--model_path` | str | **必填** | 基座模型路径 |
| `--data_path` | str | **必填** | FOLIO JSONL 训练数据 |
| `--output_dir` | str | **必填** | Checkpoint 输出目录 |
| `--max_steps` | int | 200 | 训练步数 |
| `--num_train_epochs` | int | None | 设置后覆盖 max_steps |
| `--per_device_batch_size` | int | 4 | 每卡 batch size |
| `--gradient_accumulation_steps` | int | 2 | 梯度累积步数 |
| `--learning_rate` | float | 2e-5 | 学习率 |
| `--max_seq_length` | int | 1024 | 最大序列长度 |
| `--seed` | int | 42 | 随机种子 |
| `--warmup_ratio` | float | 0.1 | warmup 比例 |
| `--logging_steps` | int | 10 | 日志间隔 |
| `--save_steps` | int | 50 | 保存间隔 |
| `--wandb_project` | str | None | W&B 项目名 |
| `--wandb_run` | str | None | W&B run 名 |
| `--no_wandb` | flag | False | 禁用 W&B |
| `--bf16` | flag | True | BF16 训练 |

---
