# ssh prepare next eval batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_next_eval_batch_20260523T205105_result.json`
- **Structured JSON:** [`6882f054525a6a919489.json`](../../sessions/68/6882f054525a6a919489.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息齐备。汇总如下：

---

## Checkpoint 状态表

| # | Checkpoint | 服务器 | 状态 | 有 model.safetensors |
|---|-----------|--------|------|---------------------|
| 1 | `sft_rasp_alpha0p5_20` | westd | ✅ Found | ✅ |
| 2 | `sft_rasp_alpha2p0_20` | westd | ✅ Found | ✅ |
| 3 | `sft_alpha4_20` | westd | ✅ Found | ✅ |
| 4 | `grpo_cka_only_25` | westd | ✅ Found | ✅ |
| 5 | `sft_cka_only_25` | westd | ✅ Found | ✅ |
| 6 | `grpo_rasp_alpha3p0_20_v2` | westd | ⚠️ 无模型文件 | ❌ 只有 README+completions |
| 7 | `grpo_random_20` | westd | ⚠️ 无模型文件 | ❌ 只有 README+completions+config |
| 7' | `grpo_random_20_seed123_v2` | westd | ✅ Found | ✅ |
| 7'' | `grpo_random_20_retrain` | westb | ✅ Found | ✅ |

---

## 可立即启动的 Eval 命令（westd-32935）

**P0 — dose-response SFT：**

```bash
# 1. sft_rasp_alpha0p5_20
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha0p5_20_fixed.json --seed 42 --dtype bfloat16"

# 2. sft_rasp_alpha2p0_20
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20_fixed.json --seed 42 --dtype bfloat16"

# 3. sft_alpha4_20
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_alpha4_20_fixed.json --seed 42 --dtype bfloat16"
```

**P1 — 25% sparsity：**

```bash
# 4. grpo_cka_only_25
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_25_fixed.json --seed 42 --dtype bfloat16"

# 5. sft_cka_only_25
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_25_fixed.json --seed 42 --dtype bfloat16"
```

**P1 — grpo_random 替代：**

```bash
# 7'. grpo_random_20_seed123_v2 (westd)
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_seed123_v2_fixed.json --seed 42 --dtype bfloat16"
```

**westb-23072 单独跑：**

```bash
# 7''. grpo_random_20_retrain (westb)
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_retrain_fixed.json --seed 42 --dtype bfloat16"
```

---

## 缺失/需重训

| Checkpoint | 问题 |
|-----------|------|
| `grpo_rasp_alpha3p0_20` | v2 目录存在但无模型权重（只有 README+completions），**需重训** |
| `grpo_random_20` | 原始目录无模型权重。可用替代：`grpo_random_20_seed123_v2`（westd）或 `grpo_random_20_retrain`（westb），二选一即可 |

---
