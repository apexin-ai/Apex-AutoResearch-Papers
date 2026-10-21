# setup qwen3 8b traj func

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_qwen3-8b-traj-func_20260517T124501_result.json`
- **Structured JSON:** [`7a5eec2d80fb89da9f7c.json`](../../sessions/7a/7a5eec2d80fb89da9f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 准备完成，汇总报告

### 1. 模型路径
`/home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-8B/` (snapshot `b968826d`)
- HF name: `Qwen/Qwen3-8B`

### 2. 数据路径和数据量
`/home/sonny/exec-sim-repair-verifier/data/`
| Split | File | Samples |
|-------|------|---------|
| Train | `traj_train.jsonl` | 8,052 |
| Val | `traj_val.jsonl` | 1,001 |
| Test | `traj_test.jsonl` | 1,032 |

序列长度: Mean=220, P95=420, P99=578, Max=1253 tokens. 0% truncation at 2048.

### 3. 训练脚本
`/home/sonny/exec-sim-repair-verifier/train_traj_verifier.py`

### 4. Training Commands

**Seed 42:**
```bash
cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py \
  --data_dir data \
  --model_name Qwen/Qwen3-8B \
  --output_dir checkpoints_traj_8b_seed42 \
  --run_name traj-qwen3-8b-lora-s42 \
  --seed 42 \
  --batch_size 2 \
  --grad_accumulation 16 \
  --epochs 3 \
  --lr 2e-4 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --max_seq_length 2048
```

**Seed 123:**
```bash
cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py \
  --data_dir data \
  --model_name Qwen/Qwen3-8B \
  --output_dir checkpoints_traj_8b_seed123 \
  --run_name traj-qwen3-8b-lora-s123 \
  --seed 123 \
  --batch_size 2 \
  --grad_accumulation 16 \
  --epochs 3 \
  --lr 2e-4 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --max_seq_length 2048
```

### 5. Dry-run 结果
- bs=2, max_steps=2: **成功**，4.27 s/step
- Attention: SDPA (flash_attn 未安装)
- Trainable params: 15.3M / 8.2B (0.19%)
- Gradient checkpointing: enabled

### 6. 预估训练时间
- 756 steps/run (252 steps/epoch × 3 epochs)
- ~4.3 s/step → **~54 min/run**
- 两个 seed 共 ~108 min

### 7. Blockers
无。所有组件就绪，dry-run 通过。

---
