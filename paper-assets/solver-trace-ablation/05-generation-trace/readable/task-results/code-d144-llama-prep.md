# code d144 llama prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d144-llama-prep_20260519T115929_result.json`
- **Structured JSON:** [`5d05ed17a39dabc8d478.json`](../../sessions/5d/5d05ed17a39dabc8d478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速率约 1.7 MB/s，预计还需 ~30-40 分钟。tmux session `llama_dl` 在后台运行。

汇报总结：

---

## D144 LLaMA-3.2-3B 准备状态

### 1. 下载状态：进行中
- 源: `unsloth/Llama-3.2-3B` via hf-mirror.com（huggingface.co 不通）
- 路径: `/root/autodl-tmp/models/Llama-3.2-3B`
- 进度: ~780MB / 6.4GB，预计 ~30-40 分钟完成
- 后台运行: tmux session `llama_dl`
- 检查命令: `tmux has-session -t llama_dl && echo running || echo done`

### 2. 模型路径
`/root/autodl-tmp/models/Llama-3.2-3B`

### 3. Tokenizer 兼容性
| 属性 | LLaMA-3.2-3B | Qwen3-4B |
|------|-------------|----------|
| pad_token | `<\|finetune_right_pad_id\|>` (已有) | `<\|endoftext\|>` |
| eos_token | `<\|end_of_text\|>` | `<\|im_end\|>` |
| vocab_size | 128,000 | — |
| chat_template | **手动设置** (标准 Llama 3 格式) | 自带 |
| enable_thinking | 静默忽略 (OK) | 生效 |

**已完成修复**: base model 无 chat_template，已将标准 Llama 3 chat template 写入 `tokenizer_config.json`，验证通过。

### 4. 代码适配：**无需修改**
- `train_grpo.py`: 只需 `--model_path /root/autodl-tmp/models/Llama-3.2-3B`
- `eval_sta.py`: 同上
- `enable_thinking=False`: Jinja2 静默忽略，不影响 LLaMA
- `strip_thinking()`: 匹配不到 `&lt;think>` 标签，无害跳过
- TRL GRPOTrainer 自动处理 pad_token（line 62-63）

### 5. 显存预估
| 项目 | LLaMA-3.2-3B | Qwen3-4B |
|------|-------------|----------|
| 实际参数 | ~4.0B | ~4B |
| BF16 权重 | ~8 GB | ~8 GB |
| 训练估算 | ~63 GB | ~64 GB |
| GPU 容量 | 98 GB (充裕) | 98 GB |

注意：尽管名字是 3B，实际参数量约 4.0B，与 Qwen3-4B 非常接近。

### 6. Dry-run
GPU 当前空闲（0 MiB），但权重文件未下载完成，无法做 dry-run。下载完成后可立即验证。

### 7. 训练启动命令（下载完成后）
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
python scripts/train_grpo.py \
    --model_path /root/autodl-tmp/models/Llama-3.2-3B \
    --data_path data/train_500_seed42.jsonl \
    --reward_mode execution_only \
    --output_dir outputs/d144_llama_exec_only \
    --num_steps 500 \
    --wandb_project solver-trace-ablation
```

---
