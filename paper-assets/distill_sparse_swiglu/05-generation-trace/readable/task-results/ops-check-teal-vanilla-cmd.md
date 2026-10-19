# ops check teal vanilla cmd

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-teal-vanilla-cmd_20260516T094054_result.json`
- **Structured JSON:** [`fb86531cf5f28a4e7be8.json`](../../sessions/fb/fb86531cf5f28a4e7be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。

## 回答

### 1. 不传 `--checkpoint` 不会自动用 magnitude-based sparsity

`main()` 中有显式校验（第~290行）：如果 `--dense`、`--checkpoint`、`--baseline_mode` 都没传，直接报错退出。

### 2. TEAL vanilla 用 `--baseline_mode teal_vanilla`

这是独立于 `--sparsity_mode` 的参数。`--sparsity_mode` 仅用于 predictor 模式（`per_token` / `teal_global`），而 `--baseline_mode` 用于无 predictor 的 training-free baselines。

`teal_vanilla` 内部调用 `_collect_swiglu_magnitudes` 收集 activation magnitudes，然后 `vanilla_teal_global_masks` 做 global top-k mask。

### 3. 完整命令

**bench_teal30** (cuda:0):
```bash
bash -c 'cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 nohup python -u src/benchmark_eval.py --exp_id bench_teal30 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 > logs/bench_teal30.log 2>&1 &'
```

**bench_teal50** (cuda:1):
```bash
bash -c 'cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 nohup python -u src/benchmark_eval.py --exp_id bench_teal50 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.5 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 > logs/bench_teal50.log 2>&1 &'
```

注意：`CUDA_VISIBLE_DEVICES=1` + `--gpu 0` 的组合让 PyTorch 在可见的唯一 GPU（实际 cuda:1）上以 `cuda:0` 索引运行，两个实验可并行。需确保 `logs/` 目录存在。

---
