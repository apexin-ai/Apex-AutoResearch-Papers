# ssh eval all 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_all_30476_20260517T220036_result.json`
- **Structured JSON:** [`a84cd542958edeb55305.json`](../../sessions/a8/a84cd542958edeb55305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU 状态 ===
GPU 0: 占用 (PID 54784, 41757MiB/97887MiB, 97%)  → grid_b0_3_seed456_r2
GPU 1: 占用 (PID 53826, 41757MiB/97887MiB, 98%)  → grid_b0_3_seed123
GPU 2: 占用 (PID 41387, 46505MiB/97887MiB, 99%)  → rho02_adaptive_tau08_seed42
GPU 3: 占用 (PID 48891, 71173MiB/97887MiB, 100%) → batchsize16_nmin8_r2

=== 实验进度 ===
exp_id                      | step/total | 进度  | loss   | 完成?
rho02_adaptive_tau08_seed42 | 5500/6103  | 90.1% | 11.868 | ❌ 即将完成
batchsize16_nmin8_r2        | 3500/6103  | 57.3% | 2.5278 | ❌
grid_b0_3_seed123           | 2500/6103  | 41.0% | 9.2144 | ❌
grid_b0_3_seed456_r2        | 1500/6103  | 24.6% | 8.3447 | ❌
```

**关键发现：**

1. **rho02_adaptive_tau08_seed42** 还剩 603 步，预计 ~25 分钟内完成。
2. **batchsize16_nmin8_r2** 注意：输出目录是 `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2`（不是 `/root/autodl-tmp/output/models/`）。
3. **grid_b0_3_seed123** 从 checkpoint-1000 恢复后继续训练。
4. **尚无实验完成**，无法立即 eval。

**eval 脚本就绪：** `/root/provenance_weight_training/eval_perplexity.py`

rho02_adaptive_tau08_seed42 完成后可执行：
```bash
cd /root/provenance_weight_training
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
  --model_path /root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/final_checkpoint \
  --eval_data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 --stride 1024 --fp16
```

---
