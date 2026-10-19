# code exp004 heldout prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004-heldout-prep_20260523T022814_result.json`
- **Structured JSON:** [`1217c8eef990e38243af.json`](../../sessions/12/1217c8eef990e38243af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 脚本路径
`/root/contrastive_entrain_calib/training/run_exp004_heldout.py` (315 行)

### 2. 数据文件
- 路径: `/root/contrastive_entrain_calib/data/train_split.jsonl`
- 行数: **292** (146 pairs)
- 字段: `pair_id, condition, domain, ground_truth, wrong_answer, pressure_answer, evidence_strength, turns, gt_verified`

### 3. 模型路径
`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`

### 4. cuda:1 状态
**被占用。** PID 553700 正在运行 `run_exp003_len512_r3only.py`，占用 41337 MiB。cuda:0 也被占用（PID 516696, `run_exp003_gs8_r3only.py`）。需要等现有实验完成后才能启动。

### 5. 推荐启动命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python training/run_exp004_heldout.py
```

### 6. 与原始 exp-004s2 脚本的差异

| 项目 | 原始 (run_exp004s2_act.py) | heldout 版 |
|------|---------------------------|------------|
| docstring | exp-004-s2 seed 2 | exp-004-heldout train split |
| `--data-path` | `data/calibration_v2_1_expanded.jsonl` | `data/train_split.jsonl` |
| `--output-dir` | `outputs/exp-004-act-baseline-s2` | `/root/autodl-tmp/.../exp004_heldout/` |
| `--seed` | 43 | **42** |
| parser description | "exp-004-s2 ACT seed 2" | "exp-004-heldout ACT on train split" |

其余参数完全一致：LoRA r=64/alpha=128/7 modules/dropout=0.05, lr=5e-5, warmup=200, max_steps=8000, grad_accum=16, lambda_l2=0.1, save_steps=500, max_seq_len=1024, AdamW weight_decay=0.01, grad_clip=1.0, bfloat16, gradient_checkpointing.

### 7. 注意事项
- **两块 GPU 都被占用**，需等 exp003_len512 或 exp003_gs8 完成后腾出 GPU 才能启动
- 输出目录已创建: `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp004_heldout/`

---
