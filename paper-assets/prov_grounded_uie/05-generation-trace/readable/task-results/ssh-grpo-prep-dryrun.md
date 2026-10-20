# ssh grpo prep dryrun

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-prep-dryrun_20260512T164845_result.json`
- **Structured JSON:** [`282f2322351948aeb6dc.json`](../../sessions/28/282f2322351948aeb6dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。汇总结果：

---

## 验证结果

| 检查项 | 状态 |
|--------|------|
| 文件存在（train_grpo.py / rewards.py / config.py / data_utils.py） | ✓ |
| `max_prompt_length` 已从 GRPOConfig 构造中移除 | ✓ |
| NLI 模型路径可通过 `--nli_model_name` CLI 覆盖 | ✓ |
| `--help` 正常输出 | ✓ |
| Config 解析 + 数据加载 dry-run | ✓ |

## Dry-run 输出
```
Parsed OK: sft_checkpoint=./outputs/sft/merged
NLI model: /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large
Reward weights: prov=0.4, struct=0.4, fmt=0.2
Dataset loaded: 2 samples
Keys: ['prompt', 'gold_relations', 'sentences', 'document_text']
DRY-RUN PASSED: config parsing + data loading OK
```

## 关键超参默认值
- `num_generations`: 4, `temperature`: 0.7, `beta`: 0.05
- `lr`: 5e-6, `batch_size`: 2/device, `grad_accum`: 8
- `max_completion_length`: 2048, `max_prompt_length`: 2048
- `reward weights`: prov=0.4, struct=0.4, fmt=0.2
- `LoRA`: rank=32, alpha=64, dropout=0.05

## 推荐启动命令

**双卡 DDP（推荐）：**
```bash
cd /root/autodl-tmp/prov_grounded_uie
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

accelerate launch --num_processes 2 --mixed_precision bf16 train_grpo.py \
  --sft_checkpoint ./outputs/sft/merged \
  --nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large \
  --num_generations 4 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 8 \
  --learning_rate 5e-6 \
  --num_train_epochs 1 \
  --report_to wandb \
  --run_name provuie-grpo
```

**单卡 fallback：**
```bash
CUDA_VISIBLE_DEVICES=0 python train_grpo.py \
  --sft_checkpoint ./outputs/sft/merged \
  --nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large \
  --num_generations 4 \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --learning_rate 5e-6 \
  --num_train_epochs 1 \
  --report_to wandb \
  --run_name provuie-grpo
```

## 注意事项
1. **vLLM 版本警告**：服务器 vLLM 0.18.1 超出 TRL 支持范围（0.11-0.17.1），但 GRPO 训练不直接依赖 vLLM，只是 TRL 的 import warning，不影响训练
2. 当前两个 GPU 在跑 eval，GRPO 训练需等 eval 完成后启动

---
