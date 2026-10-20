# ssh registry sync gpu status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_registry_sync_gpu_status_20260521T174803_result.json`
- **Structured JSON:** [`fbf4dd8f5ec6863f4376.json`](../../sessions/fb/fbf4dd8f5ec6863f4376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report.

---

## Part A: GPU 状态

### autodl-5090 (4× RTX 5090)

| GPU | 利用率 | 显存使用 | 状态 |
|-----|--------|----------|------|
| 0 | 85% | 30152/32607 MiB | **忙** — `fewnerd_n16_s456` 推理 (qwen3-8b-fewnerd-exp021-merged, FT model) |
| 1 | 0% | 2/32607 MiB | **空闲** |
| 2 | 0% | 2/32607 MiB | **空闲** |
| 3 | 85% | 29946/32607 MiB | **忙** — `e2_pretrained_fewnerd_s456` 推理 (Qwen2.5-7B-Instruct, pretrained baseline) |

运行进程：
- GPU 0: `run_mvp_pilot.py` — fewnerd n16 s456, FT model, PID 54277
- GPU 3: `run_mvp_pilot.py` — e2_pretrained_fewnerd_s456, pretrained model, PID 47635

### autodl-5090-c (4× RTX 5090)

| GPU | 利用率 | 显存使用 | 状态 |
|-----|--------|----------|------|
| 0 | 0% | 0/32607 MiB | **空闲** |
| 1 | 0% | 0/32607 MiB | **空闲** |
| 2 | 0% | 0/32607 MiB | **空闲** |
| 3 | 0% | 0/32607 MiB | **空闲** |

无 Python/训练进程运行。**全部 4 卡空闲。**

---

## Part B: 已完成实验指标

所有实验位于 **autodl-5090-c** 的 `/root/autodl-tmp/struct_self_consist_ie/output/` 下。

### 1. scierc_n16_s456 (FT model, SciERC NER, n=16)
- **路径**: `output/scierc_n16_s456/`
- **行数**: 551 (samples.jsonl)
- **greedy_f1**: 0.6641
- **oracle_f1**: 0.8076
- **oracle_headroom**: 0.1435
- **mv_f1**: 未记录
- **verdict**: MARGINAL

### 2. e2_pretrained_conll_s42 (Pretrained, CoNLL NER, n=8)
- **路径**: `output/e2_pretrained_conll_s42/`
- **行数**: 3453 (samples.jsonl)
- **greedy_f1**: 0.5363
- **oracle_f1**: 0.6299
- **oracle_headroom**: 0.0936
- **mv_f1**: 未记录
- **verdict**: MARGINAL

### 3. e2_pretrained_conll_s123_v2 (Pretrained, CoNLL NER, n=8)
- **路径**: `output/e2_pretrained_conll_s123_v2/`
- **行数**: 3453 (samples.jsonl)
- **greedy_f1**: 0.5364
- **oracle_f1**: 0.6257
- **oracle_headroom**: 0.0893
- **mv_f1**: 未记录
- **verdict**: MARGINAL

### 4. e2_pretrained_scierc_s42_v2 (Pretrained, SciERC NER, n=8)
- **路径**: `output/e2_pretrained_scierc_s42_v2/`
- **行数**: 551 (samples.jsonl)
- **greedy_f1**: 0.2434
- **oracle_f1**: 0.3888
- **oracle_headroom**: 0.1454
- **mv_f1**: 未记录
- **verdict**: FAIL
- **警告**: >30% samples F1=0, 建议 T=0.7 重跑

### 5. scierc_n16_s42 (FT model, SciERC NER, n=16)
- **路径**: `output/scierc_n16_s42/`
- **行数**: 551 (samples.jsonl)
- **greedy_f1**: 0.6631
- **oracle_f1**: 0.8086
- **oracle_headroom**: 0.1455
- **mv_f1**: 未记录
- **verdict**: MARGINAL

### 补充：scierc_n16_s123 (FT model, SciERC NER, n=16)
- **路径**: `output/scierc_n16_s123/`
- **行数**: 551 (samples.jsonl)
- **greedy_f1**: 0.6619
- **oracle_f1**: 0.8127
- **oracle_headroom**: 0.1508
- **mv_f1**: 未记录
- **verdict**: PASS

---

## Part C: FewNERD 训练配置

### 核心配置文件（autodl-5090）

**原始 3-epoch 配置**: `train_config_fewnerd_exp021.yaml`

```yaml
model_name_or_path: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
stage: sft
finetuning_type: lora
lora_rank: 32
lora_alpha: 64
lora_target: all
template: qwen3
enable_thinking: false

dataset_dir: /root/autodl-tmp/struct_self_consist_ie/data
dataset: fewnerd_uie_train
eval_dataset: fewnerd_uie_dev

per_device_train_batch_size: 2
gradient_accumulation_steps: 8
learning_rate: 2.0e-4
num_train_epochs: 3.0
lr_scheduler_type: cosine
warmup_ratio: 0.1
bf16: true
gradient_checkpointing: true
cutoff_len: 2048
seed: 42

output_dir: .../output/exp_021_fewnerd_full
```

**已有 5-epoch 配置**: `train_config_fewnerd_5epoch.yaml` — 与 exp021 完全相同，仅 `num_train_epochs: 5.0`，输出到 `checkpoints/qwen3-8b-fewnerd-5epoch-lora`。

### 对应 export 配置: `export_config_fewnerd_5epoch.yaml`（推测存在）

### 训练命令

5-epoch 训练已有现成配置，直接用：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/struct_self_consist_ie
CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_fewnerd_5epoch.yaml
```

合并 LoRA：
```bash
llamafactory-cli export export_config_fewnerd_5epoch.yaml
```

### Checkpoint 位置
- **3-epoch merged**: `checkpoints/qwen3-8b-fewnerd-exp021-merged/` (当前推理用的模型)
- **5-epoch LoRA**: `checkpoints/qwen3-8b-fewnerd-5epoch-lora/` (已存在，训练已完成)
- **基座模型**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`

---
