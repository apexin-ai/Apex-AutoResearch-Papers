# prep seed45 training commands

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_seed45_training_commands_20260515T211123_result.json`
- **Structured JSON:** [`6fc663c070d7756db4fe.json`](../../sessions/6f/6fc663c070d7756db4fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，汇报如下。

---

## 确认结果

| 项目 | 路径 | 样本数 | 状态 |
|------|------|--------|------|
| flat-NLI RSFT 数据 | `/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl` | 2691 | ✓ |
| CED RSFT 数据 | `/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` | 2718 | ✓ |
| SFT adapter | `/root/autodl-tmp/sft_output/adapter_model.safetensors` | - | ✓ |
| 输出目录 s45 | `rsft_output_flat_nli_s45` / `rsft_output_ced_s45` | - | 不存在 (CLEAN) |

CED RSFT 参数来源：`mvp2_rsft_train_r1_s44` — "Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples)"。与 flat-NLI RSFT 超参完全一致，仅数据不同。

---

## 训练命令

### flat-NLI RSFT seed=45

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed45 --seed 45"
```

### CED RSFT seed=45

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_seed45 --seed 45"
```

---

## 预计时间

- flat-NLI RSFT seed=45: ~2h (2691 samples, 507 steps × 3ep，参考 seed=43 的 6880s)
- CED RSFT seed=45: ~2h (2718 samples, ~510 steps × 3ep，样本量接近)

---

## GPU 状态（阻塞）

4 卡全部在用：
| GPU | 显存占用 | 当前任务 |
|-----|---------|---------|
| 0 | 18.3/32.6 GB | eval_plan_001_flat_nli_s43 |
| 1 | 15.8/32.6 GB | plan_011_bf16_g8_step_eval |
| 2 | 19.5/32.6 GB | eval_plan_012_dpo_ced_1ep |
| 3 | 15.6/32.6 GB | eval_plan_008_rsft_topk3 |

RSFT 训练需要 ~16-19GB 单卡，无法与现有任务共用。需等当前 eval 完成后才能提交。

---
