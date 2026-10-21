# ops status check all 4gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-all-4gpu_20260519T000124_result.json`
- **Structured JSON:** [`fb3af345f9abb46e3d6a.json`](../../sessions/fb/fb3af345f9abb46e3d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. c1_ablation_30pct_s42 (westd-34887, GPU 0) — **FAILED**
- tmux session: 不存在
- 错误: `python: can't open file '/root/distill_sparse_swiglu/src/train_bce_kl_targets.py': [Errno 2] No such file or directory`
- EXIT_CODE=2, 无 checkpoint 生成

### 2. kl30_uniform_hellaswag_piqa_v2 (westd-34887, GPU 1) — **RUNNING**
- tmux session: 存在
- 均匀稀疏度 30.1%/layer, model-level 0.300
- hellaswag 已完成 map, 正在跑 loglikelihood requests: ~97% (38933/40168)
- piqa 尚未开始（或在 hellaswag 之后）
- 预计还需几分钟完成

### 3. kl30_s42_global_mmlu_recheck (westd-41718, GPU 1) — **COMPLETED**
- tmux session: 不存在（正常退出）
- **MMLU acc = 0.2527** (stderr = 0.00364)
- 这基本等于随机猜测（4 选 1 = 0.25），说明 KL predictor global_topk 在 30% 稀疏度下 MMLU 崩了
- 结果已保存: `/root/distill_sparse_swiglu/results/benchmark/kl30_s42_global_mmlu_recheck/results.json`

### 4. kl50_global_hellaswag_piqa_v2 (westd-41718, GPU 0) — **RUNNING**
- tmux session: 存在
- 全局稀疏度分配: 0.301~0.701/layer, model-level 0.500
- loglikelihood requests: ~94% (37969/40168)
- 预计还需几分钟完成

### GPU 利用率

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| westd-34887 | **0%, 0 MiB** (空闲) | **100%, 48577/97887 MiB** (kl30_uniform) |
| westd-41718 | **98%, 48577/97887 MiB** (kl50_global) | **0%, 0 MiB** (空闲) |

### 需要关注

1. **c1_ablation** 脚本路径错误 (`train_bce_kl_targets.py` 不存在)，需要修复后重跑
2. **MMLU recheck = 0.2527** 本质上是随机水平，KL predictor global_topk @30% 在 MMLU 上完全失效
3. westd-34887 GPU 0 和 westd-41718 GPU 1 当前空闲，可以安排新任务

---
