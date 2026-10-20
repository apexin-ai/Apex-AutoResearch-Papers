# ssh check 25pct pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_25pct_pipeline_20260521T013830_result.json`
- **Structured JSON:** [`59a0ac892844aa69f729.json`](../../sessions/59/59a0ac892844aa69f729.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结果

### 1. 25% Pruned Model — 已存在

两种模式的 pruned model 均完整：

| 路径 | 文件 |
|------|------|
| `/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25/` | config.json, model.safetensors, pruning_metadata.pt, tokenizer files |
| `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25/` | 同上 |

Qwen-Math 变体也存在：`pruned_standard_25_qwen_math/`, `pruned_rasp_25_qwen_math/`

### 2. 25% SFT & GRPO — 也已完成

完整 pipeline（prune → SFT → GRPO）已跑完：
- `sft_standard_25/`, `sft_rasp_25/`
- `grpo_standard_25/`, `grpo_rasp_25/`
- Qwen-Math 变体：`sft_qwen_math_standard_25/`, `sft_qwen_math_rasp_25/`, `grpo_standard_25_qwen_math/` (目录名 `grpo_rasp_25_qwen_math` 未在列表中，但 `grpo_rasp_25` 本体存在)

### 3. 脚本路径 & 参数

**Pruning**: `/root/recovery_aware_struct_prune/src/prune.py`
```
--model_path (dense模型路径)
--mode {standard, rasp, rasp-rlvr, cka_only, random}
--sparsity 0.25
--alpha 1.0
--output_path (输出路径)
--importance_path / --cka_path (可选)
--seed 42 --dtype bfloat16
```

**SFT**: `/root/recovery_aware_struct_prune/src/sft_recovery.py`
```
--model_path (pruned模型路径)
--output_dir (输出路径)
--gpu 0
--num_train_epochs 2 --learning_rate 2e-5
--batch_size 1 --gradient_accumulation_steps 8
--max_seq_length 2048 --seed 42
```

**GRPO**: `/root/recovery_aware_struct_prune/src/train_grpo_v5.py`
```
--model_path sft_standard_25 --output_dir grpo_standard_25
--max_steps 100 --seed 42
```

### 4. Dense Base Model

`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`

### 5. 磁盘空间

```
/dev/md0  619G  557G  63G  90%  /root/autodl-tmp
```

63GB 可用，足够跑新实验（单个 SFT/GRPO checkpoint ~15GB）。

### 结论

25% pipeline 已完整存在，无需重新跑 pruning 或 SFT。如果要启动新的 25% 实验（如不同 seed、不同超参），可直接基于现有 pruned model 开始。

---
