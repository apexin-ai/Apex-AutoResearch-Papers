# ops recovery paired data prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recovery-paired-data-prep_20260516T020034_result.json`
- **Structured JSON:** [`185afb79276caaa41212.json`](../../sessions/18/185afb79276caaa41212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。以下是结果汇总：

---

## 1. recovery_paired.jsonl 数据格式

每行一个 JSON 对象，字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| `inject_id` | str | 注入 ID |
| `source_trajectory_id` | str | 来源轨迹 ID |
| `task_description` | str | 任务描述 |
| `operator` | str | 错误操作符 (e.g. P1_step_order_swap) |
| `error_label` | str | 错误类别标签 |
| `injection_step` / `total_original_steps` | int | 注入位置 |
| `num_error_prefix_steps` / `num_recovery_steps` | int | step 数量 |
| `error_prefix` | list[{messages}] | 错误前缀步骤 (3831 steps total) |
| `recovery_continuation` | list[{messages, is_recovery, recovery_step}] | 恢复步骤 (5408 steps total) |
| `api_usage_estimate` | dict | token 用量估计 |

每个 step 的 `messages` = `[{role: "user", content: ...}, {role: "assistant", content: ...}]`，与 sft_taxei_v4 格式一致。

## 2. 格式转换

**需要转换**。recovery_paired.jsonl 是嵌套结构，swift SFT 需要扁平的 `{"messages": [...]}` 格式。

转换脚本：`scripts/convert_recovery_paired_to_sft.py`（支持 3 种模式：recovery_only / all_steps / multi_turn）

使用 `recovery_only` 模式，仅提取 recovery_continuation 步骤（error_prefix 已包含在 TaxEI 基础数据中）。

## 3. TaxEI-RP 合并样本数

| 组成 | 样本数 |
|------|--------|
| TaxEI (clean + error injection) | 9,029 |
| Recovery continuation steps | 5,408 |
| **TaxEI-RP 总计** | **14,437** |

文件：`data/recovery_paired/sft_taxei_rp.jsonl` (30MB)

## 4. Dry-run 结果 ✓

5 步全部完成，loss 稳步下降：

| Step | Loss | Grad Norm | Token Acc | Memory |
|------|------|-----------|-----------|--------|
| 1 | 4.019 | 4.962 | 0.637 | 34.0 GiB |
| 2 | 3.440 | 4.318 | 0.620 | 34.8 GiB |
| 3 | 3.270 | 5.796 | 0.610 | 34.8 GiB |
| 4 | 2.695 | 3.204 | 0.626 | 34.8 GiB |
| 5 | 2.424 | 2.993 | 0.654 | 35.5 GiB |

峰值显存 35.5 GiB（RTX 5090 32GB × 1 卡），稍超 VRAM。实际训练时显存波动正常，如果 OOM 可降 max_length 到 2048。

速度：~2.68 s/it，bs=4, ga=2 → effective batch=8。

## 5. 正式训练命令

3 seeds × 单卡训练，分别在 cuda:0-2 上并行：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Seed 42 on cuda:0
CUDA_VISIBLE_DEVICES=0 nohup swift sft \
  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 42 --data_seed 42 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch \
  > /tmp/taxei_rp_s42.log 2>&1 &

# Seed 123 on cuda:1
CUDA_VISIBLE_DEVICES=1 nohup swift sft \
  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 123 --data_seed 123 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch \
  > /tmp/taxei_rp_s123.log 2>&1 &

# Seed 456 on cuda:2
CUDA_VISIBLE_DEVICES=2 nohup swift sft \
  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s456 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 456 --data_seed 456 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch \
  > /tmp/taxei_rp_s456.log 2>&1 &
```

预估每个 seed 训练时间：14,437 samples × 3 epochs / (effective_bs=8) × 2.68s ≈ ~4 小时。cuda:3 保留用于评估或备用。

---
