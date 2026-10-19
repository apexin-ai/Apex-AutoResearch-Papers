# ops prepare kl25 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-kl25-eval_20260518T185256_result.json`
- **Structured JSON:** [`65c0e55cdc02100bc90c.json`](../../sessions/65/65c0e55cdc02100bc90c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息汇总：

### 1. Checkpoint 确认
`/root/distill_sparse_swiglu/checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt` — 145MB, May 19 00:29

### 2. westd-41718 GPU 状态
**两块 GPU 都完全空闲**（0MiB, 0%）。GPU 0 可用。

### 3. Actual Sparsity
Registry `kl_sparsity25_s42` 记录：`sparsity_actual = 0.23`（target 0.25）

### 4. 完整 Eval 命令
```bash
bash -c "source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.23 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0"
```

### 5. C1 v2 状态
**PID 93700 已死**。41718 上无任何 GPU 进程，也无 C1 v2 相关日志。Registry 标记 `c1_ablation_bce_kl_targets_s123_v2` 为 RUNNING，但实际进程已不存在，属于 stale entry。

### 附加发现
westd-34887 GPU 0 正在运行 `kl_sparsity35_s42_eval_teal_uniform`（PID 47633, ~4 分钟前启动），GPU 1 空闲。

---
