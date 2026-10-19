# ops v5 div reg progress check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v5-div-reg-progress-check_20260516T031421_result.json`
- **Structured JSON:** [`d3c130ae10e066c04103.json`](../../sessions/d3/d3c130ae10e066c04103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Part 1: 进度快照

| 指标 | 值 |
|------|-----|
| **当前 step** | 5700 / 20000 (28.5%) |
| **速度** | 0.9 steps/s |
| **剩余时间** | ~4.4h (14300 steps ÷ 0.9 s/step) |
| total loss | 0.0257 |
| task_loss | 0.0658 |
| ib_loss | 0.1576 |
| div_loss | -0.4434 |
| scorer_mean | 0.551 |
| scorer_std | 0.441 |
| β | 0.0100 (warmup 已完成，稳定在目标值) |

**进程健康**：PID 682228 运行 1h47m，GPU PID 682233 占用 16214 MiB，正常。

**趋势观察**：β warmup 在 step ~2000 完成后，scorer_mean 从 0.57 缓慢下降到 0.551，scorer_std 从 0.41 上升到 0.441 — 说明 IB loss 在起作用，推动 scorer 向更稀疏的方向分化。task_loss 也在缓慢下降（0.08→0.06 区间）。训练正常。

---

## Part 2: 代码调研表

### 1. ACIB-H (--mode hard) — **已完全实现**

`scorer.py:34-48` 有 `_hard_topk` 实现，使用 straight-through estimator (`mask - soft.detach() + soft`)。`train_acib.py:129` 已支持 `--mode hard`。

启动命令：
```bash
MUJOCO_GL=egl python scripts/train_acib.py \
    --mode hard --top_k_ratio 0.8 \
    --model_id lerobot/smolvla_libero \
    --hidden_dim 64 --alpha 0.01 --beta 0.01 \
    --diversity_lambda 1.0 --lambda_ent 0.1 \
    --steps 20000 --batch_size 64 --lr 1e-4 \
    --output_dir outputs/acib_h_k08 \
    --gpu &lt;GPU> --seed 42 --wandb_project acib
```

### 2. 消融实验 — **纯参数调整，不需要改代码**

Loss 公式：`total = task + α·consistency + β·ib + div_lambda·div + λ_ent·entropy`

| 消融条件 | 参数设置 |
|----------|---------|
| **VIB-only** (去掉 consistency) | `--alpha 0 --beta 0.01` |
| **Consistency-only** (去掉 IB) | `--alpha 0.01 --beta 0` |
| **No div reg** | `--diversity_lambda 0` |
| **No entropy reg** | `--lambda_ent 0` |

### 3. smolvla_libero_plus 作为 model_id — **可以直接换**

`--model_id` 直接传给 `SmolVLAPolicy.from_pretrained(model_id)`，只要 `lerobot/smolvla_libero_plus` 在 HF 缓存中可用即可。`load_normalization_stats` 也通过同一个 `model_id` 获取 normalizer，遵循 lerobot 标准约定。

唯一需要确认：该模型是否已缓存在服务器上（`HF_HUB_OFFLINE=1`），否则需要先下载。

### 4. eval 脚本 — **eval_acib.py 专门评测 ACIB checkpoint**

- `eval_acib.py`：接受 `--checkpoint_dir` + `--base_model`，重建 ACIBPolicy 后跑 lerobot-eval，支持指定 checkpoint step 或自动选 latest
- `eval_baseline.py`：仅评测原始 SmolVLA baseline

两个 eval 脚本覆盖了所有需求。

### 5. 代码缺失项 — **无**

所有后续实验（ACIB-H、消融、换 model_id）均可通过现有代码 + 命令行参数完成，不需要写新代码。

---
