# exp null seeds fpr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_null_seeds_fpr_20260524T015443_result.json`
- **Structured JSON:** [`966e3c0e7719dcdf59ff.json`](../../sessions/96/966e3c0e7719dcdf59ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行，GPU 0-3 占用 ~6.5GB，已进入 Generation 0 训练。

## 汇报

| exp_id | Seed | GPU | tmux session | 状态 |
|--------|------|-----|-------------|------|
| null_fpr_s46_fp32 | 46 | 0 | null_s46 | 运行中 (Gen 0) |
| null_fpr_s48_fp32 | 48 | 1 | null_s48 | 运行中 (Gen 0) |
| null_fpr_s49_fp32 | 49 | 2 | null_s49 | 运行中 (Gen 0) |
| null_fpr_s50_fp32 | 50 | 3 | null_s50 | 运行中 (Gen 0) |

**已存在（跳过）**：s45, s47（gen_0-10 完整，EXIT_CODE=0）

实际只需跑 4 个新 seed（46, 48, 49, 50），加上已有的 s45, s47，共 6 个 null seeds。

**预估时间**：基于 README 的 ~27.5 min/gen × 10 gen ≈ **4.6h**

**训练命令**（所有 seed 相同参数）：
```
python -u iterative_train.py \
  --model_name EleutherAI/pythia-410m \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.00 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --output_dir results/alpha_sweep/a000_s{seed}_fp32 \
  --seed {seed} --batch_size 4 --max_length 512 \
  --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 \
  --top_p 0.95 --optim adamw_torch
```

**日志**：`/tmp/null_fpr_s{seed}.log`
**服务器**：westd-17855，GPU 4-5 空闲可用于其他任务。

---
