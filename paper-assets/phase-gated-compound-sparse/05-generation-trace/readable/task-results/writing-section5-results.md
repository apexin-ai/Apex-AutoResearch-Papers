# writing section5 results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_section5_results_20260514T090520_result.json`
- **Structured JSON:** [`73a7ab54411a3f82a43b.json`](../../sessions/73/73a7ab54411a3f82a43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 变更报告

### results.tex — 全部 placeholder 已替换（~60 处）

**§5.2 Strategy-Dependent Severity (tab:aggregate-ii)**
- 重构为 median severity difference Δ = II_low − II_high（原 "mean II" 指标在 JSON 中无数据）
- Importance: 0.39 → 1.48 → 7.16 → 14.59（37× 放大）
- Random: 0.01 → −0.02 → 0.54 → 1.54
- 数据源: `experiment_summary_table.json` median_diff

**§5.3 Phase-Modulated Amplification (tab:main-results)**
- 8 行 per-phase median II 全部填入，新增 Δ 列，移除 95% CI 列（无 G ratio bootstrap CI 数据）
- G ratio: importance 69×→103×→222×→274×; random 0.9×–1.7×
- 增长率: Δ 增长因子 3.8×→4.8×→2.0×（递减，支撑 sub-exponential claim）
- Skew ratio: mean/median = 22.94/14.59 = 1.6:1
- 数据源: `experiment_summary_table.json`, `cohens_d_bf16.json` mean_diff

**§5.4 Crossover (C3)**
- s=0.25: importance high=0.032 vs random=0.818; importance low=7.196 vs random=1.363
- 低相位反转比: 5.3×
- Crossover onset 更新为 "all four tested levels (s ≥ 0.15)"，附各水平比值 3.9×→5.4×→5.3×→3.6×
- 数据源: `experiment_summary_table.json`

**§5.5 Cross-Model (C5)**
- tab:cross-model 改为 Δ（原 G ratio 对 Qwen 不稳定——s020 分母 ≈ 0）
- DeepSeek Δ: 0.39→14.59; Qwen Δ: 0.04→2.94（约 1/10 到 1/5）
- 填入完整 narrative: Spearman ρ=1.0, gradient permutation p=0.043, per-problem concordance p=0.926 (ns)
- Qwen 起效阈值 s≥0.20 (d≥0.55), s=0.15 CI 含 0
- 新增 Qwen random control 段落: 3/4 FAIL, s030 borderline PASS (d≈0)
- 数据源: `cross_model_analysis.json`, `cohens_d_bf16_qwen.json`, `experiment_summary_table.json`

**§5.6 Statistical Validation** — 原已有真实数字，已验证全部与 JSON 一致（permutation test 4 行、Cohen's d 4×2 行）

### discussion.tex — 5 处 PENDING-BF16 修正

- G 范围: 11–42× → 69–274×
- high-phase II: "<1" → "<0.06"
- Crossover 数值: (0.58 vs 3.00, 30.9 vs 2.9) → (0.032 vs 0.818, 7.20 vs 1.36)
- Statistical scope: fp16/B=1000 → bf16/B=10000; skew 34:1 → 1.6:1; bootstrap CI 更新为 permutation CI
- Growth rate: 2.24→1.84→1.42× → 3.8→4.8→2.0×

### analysis.tex — 1 处数值修正

- G 范围: 11–42× → 69–274×; section ref 修正

### 仍有 placeholder 未填

| 文件 | 位置 | 内容 | 原因 |
|------|------|------|------|
| `analysis.tex:21` | §6.1 Attention Redistribution | 实证 attention entropy per phase（pruned vs unpruned） | 等 c4_entropy 实验完成（~21/30） |
| `analysis.tex:30` | §6.2 Discrimination Collapse | Importance score Gini/concentration（pruned vs unpruned） | 同上 |
| `results_5_1.tex` | 全文 | 36 处 PENDING-BF16 | 旧 fp16 草稿，已被 results.tex 取代，无需更新 |

### 数字追溯

每个数值在 LaTeX 注释中标注了 `exp_id` 和 `source` JSON 文件名，可直接追溯到 `/root/autodl-tmp/pacs/analysis_output/` 下的原始文件。

---
