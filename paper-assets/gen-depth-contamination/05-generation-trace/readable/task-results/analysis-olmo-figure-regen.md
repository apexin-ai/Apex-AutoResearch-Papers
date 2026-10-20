# analysis olmo figure regen

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo_figure_regen_20260521T153930_result.json`
- **Structured JSON:** [`46b93a604f9a74dbbb85.json`](../../sessions/46/46b93a604f9a74dbbb85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已更新 (4 个图表)**:
- **Fig2** (`fig2_auc_decay.pdf`): OLMo AUC 曲线更新为 rerun 值 (1v2: 0.6145→0.508)
- **Fig3** (`fig_kstar_theta.pdf`): OLMo K*(θ) 更新，现为 K*=1
- **Fig4** (`fig_jsd_decay.pdf`): 标签修正 "7 models"→"8 models"，OLMo 已正确排除
- **Supplementary** (`fig_s1_auc_decay_ci.pdf`): 自动发现 rerun 数据，已重生成
- **LOFO θ validation**: 更新了 OLMo 数据，输出 JSON + LaTeX table

**不需更新**: `mcnemar_obd_vs_baselines.py` (引用的是 OLMo/Wiki 和 OLMo/arXiv，非 C4)

**需要额外实验**: `transfer_heatmap.py` 的 cross-model transfer 矩阵需要重跑跨模型迁移实验，无法仅从 rerun 数据更新

**注意**: LOFO θ=0.60 共识分析因 OLMo K*=1 而失效，论文正文可能需要修改相关叙述。

报告已写入 `artifacts/olmo_figure_regen_report.md`。

---
