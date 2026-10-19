# ops bjb1 v6 check and eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_v6_check_and_eval_20260522T151148_result.json`
- **Structured JSON:** [`0b983cc66099ca7148bf.json`](../../sessions/0b/0b983cc66099ca7148bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正在 cuda:0 上加载模型（9.2GB VRAM），运行正常。

---

## 汇总

### 1. v6 状态：已崩溃
- **错误**：`HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface'`
- SFT checkpoint `qwen3_scienceworld_sft` 已被删除，v6 config 中的 model_path 指向了一个带 `/huggingface` 后缀的路径，被 HF 误当成 repo_id 而非本地路径
- EXIT_CODE=1

### 2. 可用 checkpoint 列表

| Checkpoint | 最新 Step | HF 格式 | 大小 |
|---|---|---|---|
| `exp029-seed4` | **15** (完成) | **有** (`global_step_15_hf`, 3.8G) | - |
| `exp029-seed42` | 5 | 无 (FSDP only) | - |
| `exp029-seed7-high-kl` | 7 | 无 (FSDP only) | - |
| `exp029_intervention_c_prime` | 7 | 无 (FSDP only) | - |
| 已有 HF 转换 | `exp029_seed42_step5_hf`, `exp029_seed7_high_kl_step5_hf`, `exp029_seed7_high_kl_step7_hf`, `c_prime_step5_hf` | - | - |

**seed2 checkpoint 不存在于 bjb1 上。**

### 3. Eval 已启动
- **Config**: `_alfworld_exp029_seed4_ood_step15.yaml`
- **Checkpoint**: `exp029-seed4/global_step_15_hf` (symlink: `qwen_exp029_seed4_step15_hf`)
- **GPU**: cuda:0, 模型加载中 (9.2GB)
- **设置**: seed.val=321, val_only=True, 134 OOD tasks, enable_response_mask=false
- **日志**: `/root/autodl-tmp/logs/exp029_seed4_ood_step15.log`
- **W&B**: `exp029-seed4-ood-step15`

### 4. ScienceWorld SFT checkpoint
bjb1 上未找到任何 `*scienceworld*sft*` 或 `*qwen3_scienceworld*` 目录。已完全删除。

---
