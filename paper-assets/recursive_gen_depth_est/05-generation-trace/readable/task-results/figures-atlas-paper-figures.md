# figures atlas paper figures

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figures_atlas_paper_figures_20260515T040104_result.json`
- **Structured JSON:** [`70be8f2fa9a818fe978b.json`](../../sessions/70/70be8f2fa9a818fe978b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张论文级图表全部完成并注册。

**产出汇总：**

| 图 | 文件 | 内容 |
|---|---|---|
| Fig 1 | `fig1_auc_decay.{pdf,png}` | AUC 衰减曲线，9 条线，EDD 阈值 τ=0.75，2/9 配置 EDD=4（Pythia/OLMo topk），7/9 未饱和 |
| Fig 2 | `fig2_feature_trajectory.{pdf,png}` | Feature 轨迹面板，3 模型 × 5 features（P90 PPL, P75 PPL, Var Surprisal, Mean Surprisal, TTR），全部单调递减 |
| Fig 3 | `fig3_confusion_matrix.{pdf,png}` | 混淆矩阵对比：best（GPT-2 XL temp, 85.4%）vs worst（Pythia topk, 69.6%），d2 最难分类 |
| Fig 4 | `fig4_atlas_heatmap.{pdf,png}` | 3×3 Atlas 热力图，GPT-2 XL > OLMo > Pythia，topk 策略最差 |

**数据说明：**
- Figure 2 用 `type_token_ratio` 替换了 `mean_ppl`（后者因 outlier 导致均值随 depth 暴增，不适合归一化可视化）
- Figure 3 的混淆矩阵用 5-fold stratified CV 的 OOF 预测生成
- GPT-2 XL topk50 的 4-class RF accuracy 为 76.6%（registry 实测值），非任务描述中的 74.5%

---
