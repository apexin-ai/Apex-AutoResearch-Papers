# code traj level data prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_traj-level-data-prep_20260512T034232_result.json`
- **Structured JSON:** [`6f988b4a7a6b3dd73dcb.json`](../../sessions/6f/6f988b4a7a6b3dd73dcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`train_trace_judge.py` is currently training on the GPU (running 3m41s). Scripts are all created and data is built. The dry-run can't proceed until that finishes.

---

### 汇报

**1. 数据统计**

| Split | Trajectories | Resolved | Unresolved | Avg tests/traj |
|-------|-------------|----------|------------|----------------|
| train | 8,052 | 3,764 (46.7%) | 4,288 (53.3%) | 1.9 |
| val | 1,001 | 457 (45.7%) | 544 (54.3%) | 1.9 |
| test | 1,032 | 479 (46.4%) | 553 (53.6%) | 1.8 |

0% truncation at max_seq_length=2048.

**2. Dry-run**

无法执行 — `train_trace_judge.py` 正在占用 GPU（27GB/32GB, PID 2310157, 已运行 ~4 分钟）。需等该任务结束后再 dry-run。

**3. 已创建的脚本**
- `build_traj_data.py` — 已执行，数据在 `data/traj_{train,val,test}.jsonl`
- `train_traj_verifier.py` — prompt 用 `[Code]`/`[Test Summary]` 格式，label 为 resolved/unresolved
- `eval_traj_verifier.py` — 含 per-test 一致性分析

**4. 完整训练命令**
```bash
cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py \
  --data_dir data/ --model_name Qwen/Qwen3-4B \
  --output_dir checkpoints_traj/ \
  --batch_size 2 --grad_accumulation 16 --lr 2e-4 \
  --epochs 3 --seed 42 --run_name traj-qwen3-4b-lora
```

**5. 完整 eval 命令**
```bash
cd /home/sonny/exec-sim-repair-verifier && python3 eval_traj_verifier.py \
  --data_dir data/ --checkpoint_dir checkpoints_traj/best \
  --model_name Qwen/Qwen3-4B --output eval_traj_results.json
```

---
