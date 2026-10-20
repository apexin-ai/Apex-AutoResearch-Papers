# audit rebuttal artifacts

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_rebuttal_artifacts_20260515T150610_result.json`
- **Structured JSON:** [`ac1e2d2f9ff2d041a571.json`](../../sessions/ac/ac1e2d2f9ff2d041a571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Artifact 验证

| 实验 | 状态 | 详情 |
|------|------|------|
| EXP-A | **存在** | 目录，含 4 子目录 (olmo_qwen_cont, olmo_qwen_rw, pythia_qwen_cont, pythia_qwen_rw) + run.log (1.07MB)，May 15 18:59 |
| EXP-B | **存在** | exp_B_14d_ablation.json, 2242B, May 15 18:28 |
| EXP-C | **存在** | exp_C_permutation_10k.json, 3558B, May 15 18:37 |
| EXP-D | **存在** | exp_D_obd_n500_v2.json, 789B, May 15 18:47 |
| EXP-E | **存在** | exp_E_paired_stats.json, 39807B, May 15 22:21 |

全部 5 个已注册实验的 artifact 均存在。

## exp_kstar_theta

- **产出文件**:
  - `artifacts/kstar_theta_curve.pdf` — 32KB, 生成于 2026-05-15 21:18
  - `artifacts/kstar_theta_curve.png` — 335KB, 生成于 2026-05-15 21:18
- **生成脚本**: `scripts/plot_kstar_theta.py`
- **内容摘要**: K*(θ) 曲线图，绘制 4 个模型 (Qwen-rewrite, Pythia, OLMo, Qwen-cont) 在 5 个 depth pair (0v1, 1v2, 2v3, 3v4, 4v5) 上的分类准确率衰减。所有模型在 0v1 准确率 ≥0.993，到 4v5 衰减至 ~0.50–0.53（接近随机）。

## 未注册的 artifact

以下文件在 `artifacts/` 中存在但无 registry entry：

| 文件 | 大小 | 日期 | 描述 |
|------|------|------|------|
| `bootstrap_ci_4model.json` | 5.2KB | May 13 | 4模型 bootstrap CI |
| `bootstrap_ci_results.json` | 3.9KB | May 13 | bootstrap CI 结果 |
| `cross_transfer_matrix.csv` | 806B | May 13 | 跨模型迁移矩阵 |
| `cross_transfer_matrix.json` | 5.8KB | May 13 | 同上 JSON 格式 |
| `exp003_analysis.json` | 4.7KB | May 14 | exp003 分析 |
| `exp003_decoding_ablation.pdf` | 21KB | May 14 | decoding 消融图 |
| `exp003_decoding_ablation.png` | 54KB | May 14 | 同上 PNG |
| `exp003_decoding_ablation.tex` | 628B | May 14 | 同上 LaTeX |
| `exp011_analysis.json` | 1.8KB | May 13 | exp011 分析 |
| `exp011_results_claude_opus_4_6.jsonl` | 58KB | May 13 | exp011 Claude 结果 |
| `exp011_results_gpt_5_5.jsonl` | 54KB | May 13 | exp011 GPT 结果 |
| `exp011_samples.jsonl` | 496KB | May 13 | exp011 样本数据 |
| `exp015_dryrun.json` | 1.2KB | May 14 | exp015 dry run |
| `exp015_neural_probe_results.json` | 12KB | May 15 | exp015 neural probe |
| `exp_D_mcnemar.json` | 788B | May 15 | McNemar 检验（初版） |
| `exp_D_mcnemar_comprehensive.json` | 1.6KB | May 15 | McNemar 检验（综合版） |
| `exp_D_mcnemar_final.json` | 1.4KB | May 15 | McNemar 检验（最终版） |
| `exp_D_mcnemar_fixed.json` | 1.3KB | May 15 | McNemar 检验（修复版） |
| `exp_D_obd_n500.json` | 648B | May 15 | OBD n500 v1 |
| `kstar_theta_curve.pdf` | 32KB | May 15 | K*(θ) 曲线 |
| `kstar_theta_curve.png` | 335KB | May 15 | K*(θ) 曲线 |
| `ordinal_comparison_results.json` | 3.8KB | May 13 | 序数比较结果 |
| `figures/auc_heatmap.pdf` | 34KB | May 13 | AUC 热力图 |
| `figures/feature_importance.pdf` | 20KB | May 13 | 特征重要性图 |
| `figures/jsd_decay.pdf` | 24KB | May 13 | JSD 衰减图 |

共 25 个未注册文件/目录。其中 `exp_D_mcnemar*` 系列有 4 个迭代版本，建议只保留 `exp_D_mcnemar_final.json` 并注册。`kstar_theta_curve` 也应注册。

---
