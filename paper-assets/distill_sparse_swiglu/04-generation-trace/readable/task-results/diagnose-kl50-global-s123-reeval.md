# diagnose kl50 global s123 reeval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_kl50_global_s123_reeval_20260517T174942_result.json`
- **Structured JSON:** [`92d6ee4daafa321de382.json`](../../sessions/92/92d6ee4daafa321de382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因

```
FileNotFoundError: [Errno 2] No such file or directory: 
'/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt'
```

Checkpoint 文件只存在于 **westd-34887**（145MB），从未同步到 **westd-41718**。实验在 westd-41718 上启动，模型加载成功后尝试加载 predictor checkpoint 时因文件不存在而崩溃。

### GPU 状态
- westd-41718 cuda:0 空闲（0MiB），cuda:1 被另一进程占用（61.6GB/96%利用率）
- 如果重跑需要用 `--gpu 0`

### 修复方案

先将 checkpoint 从 westd-34887 同步到 westd-41718，然后重跑：

```bash
# Step 1: 在 westd-41718 上创建目录并从 westd-34887 拷贝 checkpoint
mkdir -p /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/
# 需要 scp/rsync 从 westd-34887 复制 predictor_kl_normalized.pt

# Step 2: 重跑（命令不变，用 gpu 0）
cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_global_s123_reeval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
```

是否需要我执行 checkpoint 同步和重跑？

---
