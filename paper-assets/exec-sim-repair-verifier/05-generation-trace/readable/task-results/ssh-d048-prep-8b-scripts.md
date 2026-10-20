# ssh d048 prep 8b scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d048-prep-8b-scripts_20260513T085459_result.json`
- **Structured JSON:** [`5832c2c07bbba3cc9505.json`](../../sessions/58/5832c2c07bbba3cc9505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 1. 创建结果

| 文件 | 状态 |
|------|------|
| `train_repo_verifier_8b.py` | ✓ 创建成功 |
| `train_cwm_baseline_8b.py` | ✓ 创建成功 |

## 2. 语法验证

- `CLS_8B_SYNTAX_OK` ✓
- `CWM_8B_SYNTAX_OK` ✓

## 3. 关键参数差异 (4B vs 8B)

| 参数 | 4B (verifier) | 8B (verifier) | 4B (cwm) | 8B (cwm) |
|------|-----------|-----------|--------|--------|
| model_name | Qwen/Qwen3-4B | Qwen/Qwen3-8B | Qwen/Qwen3-4B | Qwen/Qwen3-8B |
| batch_size | 2 | **1** | 2 | **1** |
| grad_accumulation | 16 | **32** | 16 | **32** |
| effective batch | 32 | 32 | 32 | 32 |
| output_dir | checkpoints_repo_cls_home/ | checkpoints_repo_cls_**8b**_home/ | checkpoints_cwm/ | checkpoints_cwm_**8b**/ |
| run_name | repo-cls-qwen3-**4b**-lora-home | repo-cls-qwen3-**8b**-lora-home | cwm-qwen3-**4b**-lora | cwm-qwen3-**8b**-lora |
| lr | 5e-5 | 5e-5 | 2e-4 | 2e-4 |
| warmup_ratio | 0.05 | 0.05 | 0.1 | 0.1 |
| gradient_checkpointing | True | True | True | True |

## 4. 显存估算

- 模型权重 (bf16): ~16GB
- LoRA 参数: ~50MB
- 优化器状态: ~100MB
- 激活值 (gradient_checkpointing): ~4-6GB
- **总计: ~20-22GB → 32GB 5090 可行 (batch_size=1)**

---
