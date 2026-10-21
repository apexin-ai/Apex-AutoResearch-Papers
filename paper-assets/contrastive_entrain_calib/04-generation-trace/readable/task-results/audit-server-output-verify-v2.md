# audit server output verify v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_server-output-verify-v2_20260523T192805_result.json`
- **Structured JSON:** [`96cc0be02e1764b3e8eb.json`](../../sessions/96/96cc0be02e1764b3e8eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，开始编写报告。

---

## 服务器端验证报告

### ✅ 已确认

**1. 训练数据样本数**
- train_split.jsonl: **292** 行 ← `/root/contrastive_entrain_calib/data/train_split.jsonl`
- eval_split.jsonl: **70** 行 ← `/root/contrastive_entrain_calib/data/eval_split.jsonl`
- eval_held_out.jsonl: **70** 行 ← `/root/contrastive_entrain_calib/data/eval_held_out.jsonl`
- calibration_v2_1_expanded.jsonl: **362** 行 (= 292+70，完整校准集)

全部与论文声称的 292 train / 70 eval / 70 held-out 一致。

**2. Checkpoint 存在性**
- ACT-s1-ckpt8000: ✅ EXISTS ← `backups/act-s1/checkpoint-8000/`
- ACT-s2-ckpt8000: ✅ EXISTS ← `autodl-tmp/.../exp-004-act-baseline-s2/checkpoint-8000/`
- R3-s1-ckpt6500: ✅ EXISTS ← `autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-6500/` (含 500~8000 + final)
- R3-s2: ✅ EXISTS ← `autodl-tmp/checkpoints/exp003_r3only_seed2/` (含 500~8000 + final)
- Reduced-lora: ✅ EXISTS ← `backups/reduced-lora/checkpoint-{7000,7500,8000}/`

**3. 评估结果文件（关键指标）**

| 模型 | 数据集 | ToF | NoF | SYCONScore | 来源 |
|------|--------|-----|-----|------------|------|
| Vanilla baseline | calibration (362) | 0.8177 | 0.663 | 0.7323 | `results/vanilla_baseline_eval/...report.json` |
| Vanilla baseline | held-out (70) | 0.0286 | 1.0 | 0.0556 | `backups/eval_results_28034/heldout_vanilla_baseline/` |
| R3-only s2 ckpt4000 | calibration | 0.0773 | 0.9448 | 0.1430 | `results/exp003_d027_eval/` |
| R3-only s2 ckpt7500 | calibration | 0.0663 | 0.9724 | 0.1241 | `results/exp003_d027_eval/` |
| R3-only s2 ckpt8000 | calibration | 0.0663 | 0.9613 | 0.1240 | `results/exp003_d027_eval/` |
| R3-only ckpt6500 | held-out | 0.0571 | 0.9714 | 0.1079 | `backups/eval_results_28034/heldout_r3only_ckpt6500/` |
| ACT s1 ckpt8000 | held-out | 0.1714 | 0.8286 | 0.2841 | `backups/eval_results_28034/heldout_act_s1_ckpt8000/` |
| ACT s2 ckpt5000 | calibration | 0.1436 | 0.9061 | 0.2480 | `backups/eval_results_28034/exp-004-s2-eval-ckpt5000` |
| Reduced-lora ckpt7000 | calibration | 0.2044 | 0.8011 | 0.3257 | `backups/eval_results_28034/exp004_rl_ckpt7000` |
| Reduced-lora ckpt8000 | calibration | 0.1602 | 0.8066 | 0.2673 | `backups/eval_results_28034/exp004_reduced_lora_ckpt8000` |
| Retrain ckpt500 | held-out | 0.1143 | 0.9714 | 0.2045 | `backups/eval_results_28034/heldout_retrain_ckpt500/` |
| Retrain ckpt1000 | held-out | 0.1143 | 0.9429 | 0.2039 | `eval_results/heldout_retrain_ckpt1000/` |
| Retrain ckpt2000 | held-out | 0.0857 | 0.9143 | 0.1567 | `eval_results/heldout_retrain_ckpt2000/` |

**6. Direction quality AUROC 0.827 来源确认**
- ✅ 来自 `results/exp001/evaluation_report.json` → 5-fold CV mean_auroc = **0.826887** ≈ 0.827
- Full data best layer 19, AUROC = 0.81594
- Bootstrap 95% CI: [0.7698, 0.8589]

**Probe ablation (d_syc 质量)**
- Multi-layer d_syc AUROC = **0.8349** ← `results/probe_ablation_AB/results.json`
- Best single layer (19) = 0.8166
- Random direction = 0.7265
- Δ(d_syc vs random) = +0.1084

---

### ⚠️ 不一致 / 需注意

**Vanilla baseline 在不同数据集上表现差异巨大：**
- calibration (362 samples): ToF=0.8177, SYCONScore=0.7323
- held-out (70 samples): ToF=0.0286, SYCONScore=0.0556
- 差距极大，论文引用这两组数据时需确认使用了哪个数据集的结果。

**ACT lora_alpha 不一致（reduced-lora vs full ACT）：**

| 配置 | r | lora_alpha | target_modules | adapter_config 验证 |
|------|---|-----------|----------------|---------------------|
| ACT (s1/s2) | 64 | **128** (r×2) | 7 modules (attn+MLP) | ✅ confirmed |
| Reduced-lora | 64 | **64** | 4 modules (attn only) | ✅ confirmed |
| R3-only GRPO | 64 | **64** | 4 modules (attn only) | ✅ confirmed |

reduced-lora 的 "reduced" 体现在 target_modules 从 7→4 和 lora_alpha 从 128→64，不只是模块数。论文 Table 6 需确认这两个差异都有标注。

---

### ❌ 找不到

- **exp008v3 评估结果**：`results/exp008v3_ckpt1500_eval/` 和 `results/exp008v3_ckpt2000_eval/` 目录存在但**为空**
- **ACT s1 在 calibration data 上的评估结果**：backups 中只有 held-out 评估，未找到 ACT-s1 在完整 362 样本上的评估 JSON
- **R3-only seed1 评估结果**：仅 held-out (ckpt6500) 有评估，seed1 在 calibration data 上的评估结果未找到
- **Figure 绘图脚本**：服务器上无 `fig_*.py` / `plot_*.py` / `*figure*.py`，figures/ 目录仅有 `fig_teaser.pdf/png`
- **Reduced-lora 训练脚本**：无独立脚本，推测通过命令行参数修改 ACT 脚本运行（`--lora-rank 64` 但 alpha 设为 64 而非 rank*2）

---

### Figure 源数据映射

| Figure | 源数据 | 状态 |
|--------|--------|------|
| Fig 2 (direction quality / AUROC per layer) | `results/exp001/evaluation_report.json` (per-layer AUROC) + `results/probe_ablation_AB/results.json` (ablation A/B) | ✅ 数据存在 |
| Fig 3 (cosine failure) | `training/run_exp002v2_dcgrpo_cosine.py` / `run_exp002v3_dcgrpo_scaled_cosine.py` 相关实验 | ⚠️ 只有训练脚本，无产出的结果数据文件 |
| Fig 4 (trajectory / SYCONScore) | 各 checkpoint 评估结果散落在 `results/exp003_d027_eval/` 和 `backups/eval_results_28034/` | ⚠️ 需从多个 JSON 文件手动汇总 |
| Probe trap (exp-008) | `training/run_exp008_binary_probe_penalty.py` | ⚠️ eval 目录为空，无产出数据 |

---

### 超参数验证

| 参数 | ACT (exp-004) 脚本实际值 | R3-only (exp-003) 脚本实际值 | exp-008 (Probe-Penalty) |
|------|------------------------|---------------------------|------------------------|
| lr | 5e-5 | 5e-5 | 5e-5 |
| effective batch | 1 × 16 (grad_accum) | 1 × 16 | 1 × 16 |
| max_steps | 8000 | 8000 | 8000 |
| warmup | 200 | 100 | 200 |
| scheduler | linear | cosine | linear |
| lora_r | 64 | 64 | 64 |
| lora_alpha | 128 (r×2) | 64 | 128 |
| target_modules | 7 (attn+MLP) | 4 (attn only) | 7 (attn+MLP) |
| lambda_l2 / lambda_reward | 0.1 | — | 0.1 |
| lambda_probe | — | — | 1.0 |
| seed | 42 (s1), 43 (s2) | 42 | 42 |
| r1/r2/r3 weights | — | 0/0/1.0 | — |
| beta (GRPO) | — | 0.04 | — |
| num_generations | — | 2 | — |
| temperature | — | 0.7 | — |
| save_steps | 500 | 500 | 500 |
| lora_dropout | 0.05 (adapter_config) | 0.0 (adapter_config) | — |
| TARGET_LAYERS (ACT) | [19,20,24,27,32,33,35] | — | [19,20,24,27,32,33,35] |

请核对论文 Table 6 中的值是否与上表一致，特别注意：
1. **warmup steps**: ACT=200 vs R3-only=100，是否在论文中区分
2. **scheduler**: ACT=linear vs R3-only=cosine
3. **lora_alpha**: ACT=128 vs R3-only=64
4. **target_modules**: ACT 7个 vs R3-only 4个
5. **lora_dropout**: ACT=0.05 vs R3-only=0.0

---
