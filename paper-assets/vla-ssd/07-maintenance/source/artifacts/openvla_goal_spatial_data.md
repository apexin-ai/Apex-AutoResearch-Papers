# OpenVLA Goal & Spatial 实验数据汇总

## 数据来源映射

| 目录/文件 | 对应 Suite | 内容 |
|-----------|-----------|------|
| `trained/action_prediction/` | LIBERO-Long | R² probing (非 Goal/Spatial) |
| `functional_validation/action_probe_libero_spatial.json` | LIBERO-Spatial | R² probing (trained+untrained, 33层) |
| `attention/l1_attention_trained_summary.json` | LIBERO-Goal | L1 attention per-task |
| `attention/l1_attention_untrained_summary.json` | LIBERO-Goal | L1 attention aggregate |
| `attention/full_32layer_attention_summary.json` | LIBERO-Goal | 全层 attention (含 n_instruction_dominant) |
| `cross_instruction/classification_results.json` | LIBERO-Goal | Cross-instruction classification |
| `cross_instruction_spatial/classification_results.json` | LIBERO-Spatial | Cross-instruction classification |
| `counterfactual_10tasks/` | LIBERO-Goal | CF (trained model only) |
| `counterfactual_spatial/` | LIBERO-Spatial | CF (trained model only) |

---

## OpenVLA Spatial

### R² Probing (from `action_probe_libero_spatial.json`)

| Condition | Representation | Peak Layer | Peak R² | Exit (L32) R² |
|-----------|---------------|------------|---------|---------------|
| Trained | image_mean | L13 | 0.696 | — |
| Trained | last_preaction | L21 | 0.675 | — |
| Untrained | image_mean | L0 | 0.673 | 0.621 |
| Untrained | last_preaction | L1 | 0.635 | 0.621 |

Bootstrap trained vs untrained (image_mean, best-vs-best): Δ=0.023, p=0.0, CI=[0.012, 0.036]

### L1 Attention

**无 Spatial 专用 L1 attention 数据。** `attention/` 目录下的数据是 Goal 任务。

### Cross-Instruction Classification (from `cross_instruction_spatial/`)

| Condition | Representation | L1 | L4 | L8 | L16 | L24 | L31 |
|-----------|---------------|-----|-----|-----|------|------|------|
| Trained | last_preaction | 0.989 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Trained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.101 |
| Untrained | last_preaction | 0.995 | 0.862 | 0.683 | 0.765 | 0.777 | 0.754 |
| Untrained | image_mean | 0.1 | 0.1 | 0.101 | 0.1 | 0.1 | 0.1 |

Chance = 0.1 (10-class)

### Counterfactual (from `counterfactual_spatial/`, trained model only)

| Condition | Cohen's d (token-level) | Paired MSE | Token Divergence Rate |
|-----------|------------------------|------------|----------------------|
| empty | 0.942 | 0.0659 | 0.914 |
| wrong | 0.851 | 0.0580 | 0.865 |
| shuffled | 0.833 | 0.0570 | 0.877 |
| paraphrased | 0.806 | 0.0547 | 0.799 |

Top condition: **empty** (d=0.942)

---

## OpenVLA Goal

### R² Probing

**无 Goal 专用 R² probing 数据。** `trained/action_prediction/` 的数据是 LIBERO-Long (复合多步任务)，非 Goal。

附 LIBERO-Long 数据供参考：
- Trained: peak R²=0.683 (L19, per_task_mean), overall_r2=0.677
- Untrained: peak R²=0.616 (L32, per_task_mean), overall_r2=0.607

### L1 Attention (from `full_32layer_attention_summary.json` + `l1_attention_*_summary.json`)

| Condition | Instruction-Dominant Heads | Total Heads | Mean Text Attn | Mean Image Attn |
|-----------|---------------------------|-------------|---------------|----------------|
| Trained | 24 | 32 | 0.573 | 0.217 |
| Untrained | 0 | 32 | 0.117 | 0.878 |

Trained 任务：open_the_middle_drawer, push_the_plate_to_the_front, put_the_wine_bottle_on_top 等 LIBERO-Goal 任务。

### Cross-Instruction Classification (from `cross_instruction/`)

| Condition | Representation | L0 | L8 | L16 | L24 | L31 |
|-----------|---------------|-----|-----|------|------|------|
| Trained | last_preaction | 0.1 | 1.0 | 1.0 | 1.0 | 1.0 |
| Trained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.096 |
| Untrained | last_preaction | 0.1 | 0.982 | 0.923 | 0.864 | 0.82 |
| Untrained | image_mean | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |

Chance = 0.1 (10-class)

### Counterfactual (from `counterfactual_10tasks/`, trained model only)

**Token-level:**

| Condition | Cohen's d | Paired MSE | Token Divergence Rate |
|-----------|----------|------------|----------------------|
| empty | 0.978 | 0.0691 | 0.913 |
| wrong | 0.924 | 0.0647 | 0.908 |
| shuffled | 0.763 | 0.0512 | 0.871 |
| paraphrased | 0.707 | 0.0462 | 0.830 |

**Trajectory-level (from `trajectory_level_cohens_d.json`):**

| Condition | Cohen's d | 95% CI | Mean MSE |
|-----------|----------|--------|----------|
| empty | 3.848 | [3.409, 4.440] | 0.0691 |
| wrong | 2.992 | [2.634, 3.491] | 0.0647 |
| paraphrased | 2.353 | [2.092, 2.678] | 0.0462 |
| shuffled | 2.127 | [1.857, 2.459] | 0.0512 |

Top condition: **empty** (token d=0.978, trajectory d=3.848)

---

## NORA Spatial Untrained CF 状态

**缺失。** `/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained/` 目录下仅有：
- `action_r2_probing.json` ✓
- `l1_attention_profile.json` ✓ (14/16 instruction-dominant heads)
- `cross_instruction_classification.json` ✓ (all layers ≈ 1.0)
- `counterfactual_combined.json` ✗ **不存在**

NORA Spatial untrained 的 cross-instruction 数据显示所有层 image_mean ≈ 0.999, last_preaction = 1.0，说明 SigLIP 视觉编码器提供了极强的任务可分性，但 CF 需要单独运行。

---

## 可直接填入汇总表的数据行

### OpenVLA Spatial

| Metric | Trained | Untrained |
|--------|---------|-----------|
| R² peak (image_mean) | 0.696 (L13) | 0.673 (L0) |
| R² peak (last_preaction) | 0.675 (L21) | 0.635 (L1) |
| L1 instr-dominant heads | N/A (no spatial data) | N/A |
| Cross-inst peak acc | 1.0 (L4+) | 0.995 (L1) |
| Cross-inst exit acc (L31) | 1.0 | 0.754 |
| CF top condition | empty | — |
| CF top Cohen's d | 0.942 | — |

### OpenVLA Goal

| Metric | Trained | Untrained |
|--------|---------|-----------|
| R² peak (image_mean) | N/A (no goal data) | N/A |
| L1 instr-dominant heads | 24/32 | 0/32 |
| Cross-inst peak acc | 1.0 (L8+) | 0.995 (L1) |
| Cross-inst exit acc (L31) | 1.0 | 0.82 |
| CF top condition | empty | — |
| CF top Cohen's d (token) | 0.978 | — |
| CF top Cohen's d (traj) | 3.848 | — |
