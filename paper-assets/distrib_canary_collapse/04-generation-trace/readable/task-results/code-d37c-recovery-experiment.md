# code d37c recovery experiment

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d37c_recovery_experiment_20260521T065841_result.json`
- **Structured JSON:** [`d74e4f18248a42fdaef8.json`](../../sessions/d7/d74e4f18248a42fdaef8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。生成产出总结。

---

## D37-C Recovery Experiments — 产出总结

### 1. 脚本

**远程**: `/root/autodl-tmp/distrib_canary_collapse/recovery_train.py`

关键参数:
```
--resume_from      collapsed checkpoint 路径
--recovery_alpha   恢复期 synthetic ratio (0.0=纯 clean)
--num_recovery_gens  恢复代数 (default 10)
--baseline_metrics   baseline metrics.json 路径（用于 gap 计算）
--dry_run            仅 1 step 验证
```

复用 `iterative_train.py` 的 `generate_synthetic_data`、`mix_datasets`、`train_one_generation` + `metrics.py` 的 `compute_all_metrics`。

### 2. Dry-run 日志

EXIT_CODE=0。验证通过项：
- Checkpoint 加载 ✓（a075_s42/gen_10 → fp32 on cuda:0）
- Baseline metrics 加载 ✓（gap 计算正常）
- Synthetic generation ✓（4 samples）
- Data mix with recovery_α=0.0 ✓（20 samples pure clean）
- Training loop ✓（1 step, loss=2.77）
- Checkpoint 保存 ✓（model.safetensors + tokenizer）
- all_metrics.json 输出 ✓（含 phase/gap 字段）

### 3. 预估

| 项目 | 数值 |
|------|------|
| 每 gen 训练时间 | ~32 min（5000 steps × 0.38s/step on Blackwell） |
| 每 gen 含生成+metrics | ~40 min |
| 每个 condition (10 gen) | ~6-7 GPU-hours |
| 6 conditions 总计 | ~36-42 GPU-hours |
| VRAM 峰值 | ~8-10 GB（410M fp32 + optimizer） |
| 磁盘/condition | ~1.6 GB（含 checkpoint cleanup） |
| 6 conditions 磁盘 | ~10 GB（当前剩余 28GB，可行但需注意） |

### 4. 运行矩阵

| Source Checkpoint | rec_α=0.0 | rec_α=0.25 | rec_α=0.50 |
|---|---|---|---|
| **a075_s42/gen_10** (α=0.75, strongest) | ✓ | ✓ | ✓ |
| **a050_s42/gen_10** (α=0.50, boundary) | ✓ | ✓ | ✓ |

示例运行命令：
```bash
python recovery_train.py \
  --resume_from results/alpha_sweep/a075_s42/gen_10/checkpoint \
  --recovery_alpha 0.0 \
  --output_dir results/recovery/a075_s42_rec000 \
  --baseline_metrics results/alpha_sweep/a000_s42/gen_0/metrics.json \
  --num_recovery_gens 10 --seed 42
```

### 5. 实验假设

| ID | Hypothesis | Expected Outcome |
|---|---|---|
| **H1** | Pure clean recovery (α_rec=0.0) 能完全恢复 boundary collapse (α=0.50) | entropy/distinct 在 5-7 gen 内回到 baseline ±5% |
| **H2** | Strong collapse (α=0.75) 恢复更慢且可能不完全 | α=0.75 → rec_α=0.0 仍有 ~10% residual gap after 10 gen |
| **H3** | 恢复期仍含 50% synthetic (rec_α=0.50) 无法逆转 collapse | metrics 持平或继续恶化 |
| **H4** | Canary metrics (entropy, distinct-n) 比 downstream (ppl, MAUVE) 先恢复 | 与 collapse 时的 early-warning 排序一致 |
| **H5** | 恢复路径与 collapse 路径不对称（hysteresis） | 恢复所需代数 > collapse 发生代数 |

**核心研究问题**: Model collapse 是否可逆？如果是，恢复代价与 collapse 深度的关系是什么？

---
