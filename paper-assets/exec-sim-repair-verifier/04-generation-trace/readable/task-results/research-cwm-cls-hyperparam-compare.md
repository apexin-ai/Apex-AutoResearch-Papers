# research cwm cls hyperparam compare

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cwm-cls-hyperparam-compare_20260514T113411_result.json`
- **Structured JSON:** [`33c18c2db51aa0763684.json`](../../sessions/33/33c18c2db51aa0763684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整对比表。

## CLS vs CWM Repo-level 训练超参对比

### 数据来源
- **CLS 4B**: `train_repo_verifier.py` + `/root/autodl-tmp/checkpoints_repo_cls_v5_conda/` adapter_config
- **CWM 4B**: `train_repo_cwm.py` + `start_seed123_after_eval.sh` 启动命令 + `/root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/` adapter_config
- **CLS 8B**: `train_repo_verifier_8b.py` + `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` adapter_config
- **CWM 8B**: `train_repo_cwm_8b.py` + `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` adapter_config

### 核心超参对比

| 超参 | CLS 4B | CWM 4B | CLS 8B | CWM 8B | 对齐? |
|------|--------|--------|--------|--------|-------|
| base_model | Qwen3-4B | Qwen3-4B | Qwen3-8B | Qwen3-8B | ✅ |
| learning_rate | 5e-5 | 5e-5 | 5e-5 | 5e-5 | ✅ |
| weight_decay | 0.01 | 0.01 | 0.01 | 0.01 | ✅ |
| warmup_ratio | 0.05 | 0.05 | 0.05 | 0.05 | ✅ |
| lora_r | 16 | 16 | 16 | 16 | ✅ |
| lora_alpha | 32 | 32 | 32 | 32 | ✅ |
| lora_dropout | 0.05 | 0.05 | 0.05 | 0.05 | ✅ |
| target_modules | q,k,v,o_proj | q,k,v,o_proj | q,k,v,o_proj | q,k,v,o_proj | ✅ |
| epochs | 3 | 3 | 3 | 3 | ✅ |
| per_device_batch_size | **2** | **1** | 1 | 1 | ⚠️ |
| grad_accumulation | **16** | **32** | 32 | 32 | ⚠️ |
| **effective_batch** | **32** | **32** | **32** | **32** | ✅ |
| total_steps | 6633 | 6633 | 6633 | 6633 | ✅ |
| max_seq_length | 2048 | 2048 | 2048 | 2048 | ✅ |
| seed | **42** | **123** | **42** | **42** | ❌ |
| optimizer | AdamW | AdamW | AdamW | AdamW | ✅ |
| lr_scheduler | linear | linear | linear | linear | ✅ |
| bf16 | True | True | True | True | ✅ |
| gradient_checkpointing | True | True | True | True | ✅ |
| class_weighting | ✅ inverse freq | ✅ inverse freq | ✅ inverse freq | ✅ inverse freq | ✅ |
| dataloader_num_workers | 4 | 4 | 4 | 4 | ✅ |
| train_data | swebench_train (70748) | swebench_train (70748) | swebench_train (70748) | swebench_train (70748) | ✅ |
| val_data | swebench_val (9335) | swebench_val (9335) | swebench_val (9335) | swebench_val (9335) | ✅ |

### 不影响模型质量的差异（无需担心）

| 参数 | CLS | CWM | 说明 |
|------|-----|-----|------|
| eval_steps | 200 | 100 | 只影响 eval 频率，不影响训练 |
| save_steps | 200 | 100 | 只影响保存频率，不影响训练 |
| StderrLogCallback | 有 | 无 | 只影响日志输出 |

### 需要关注的差异

**1. batch_size/grad_accum 拆分不同（CLS 4B: 2×16 vs CWM 4B: 1×32）**
- effective batch size 完全一致（32），学习动力学等价
- 原因：CWM 生成目标更长（execution_output），单条 seq 占显存更多，所以 per-device batch 降到 1，通过加倍 grad_accum 补偿
- **审稿人安全**：可以解释 "We kept effective batch size identical at 32; the micro-batch split differs due to CWM's longer targets requiring more GPU memory per sample"

**2. CWM 4B seed=123，其余三个 seed=42**
- 来源：CWM 4B 通过 `start_seed123_after_eval.sh` 启动，显式传了 `--seed 123`
- **风险**：审稿人可能质疑 seed 不一致。建议统一说明 "seed=42 for main experiments; CWM-4B additionally verified with seed=123" 或者如果有 seed=42 的 CWM 4B 结果也列出
- 如果 CWM 4B seed=42 的早期 run 因 crash 废弃，可补跑一个 seed=42 的 CWM 4B 作为主结果

---
