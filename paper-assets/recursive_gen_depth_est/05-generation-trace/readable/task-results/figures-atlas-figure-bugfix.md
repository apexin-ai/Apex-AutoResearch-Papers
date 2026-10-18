# figures atlas figure bugfix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figures_atlas_figure_bugfix_20260515T042039_result.json`
- **Structured JSON:** [`e18d26b4c1067ab36560.json`](../../sessions/e1/e18d26b4c1067ab36560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EDD fix confirmed at line 98: `edd_val = idx`.

---

## 汇报

### Bug 1: EDD 标注修复

`edd_val = idx + 2` → `edd_val = idx`

受影响的 cells（仅 2 个 topk 配置的 d2v3 AUC < 0.75）：

| Cell | d2v3 AUC | 修复前 EDD | 修复后 EDD |
|------|----------|-----------|-----------|
| Pythia-1.4B / topk | 0.6918 | 4 (不可能) | 2 |
| OLMo-1B / topk | 0.7357 | 4 (不可能) | 2 |

其余 7/9 cells 所有 pairs AUC ≥ 0.75，无标注（EDD=3，未饱和）。

### Bug 2: Pythia nucleus features 不存在

**可用的 Pythia features 文件**：
- `data/pythia_temp09/features.jsonl` — temp τ=0.9
- `results/pythia_topk50/features.jsonl` — top-k k=50

**不存在 `data/pythia/` 或任何 `pythia_nucleus*` 目录**。OLMo (`data/olmo/`) 和 GPT-2 XL (`data/gpt2xl/`) 的无后缀目录确认为 nucleus。

由于无法统一数据源，已将 Figure 2 panel 标题改为标注各自实际使用的策略：
- `Pythia-1.4B (temp τ=0.9)`
- `OLMo-1B (nucleus p=0.95)`
- `GPT-2 XL (nucleus p=0.95)`

### 产出

8 个文件已覆盖写入 `/root/autodl-tmp/recursive_gen_depth_est/artifacts/figures/`：
- `fig1_auc_decay.{pdf,png}` — EDD 标注已修正
- `fig2_feature_trajectory.{pdf,png}` — 策略标签已添加
- `fig3_confusion_matrix.{pdf,png}` — 无变化
- `fig4_atlas_heatmap.{pdf,png}` — 无变化

**若需要完全统一 Figure 2 为 nucleus，需先生成 Pythia nucleus p=0.95 的 features 数据。**

---
