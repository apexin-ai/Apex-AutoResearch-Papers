# ops results summary and citation check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_results_summary_and_citation_check_20260517T191933_result.json`
- **Structured JSON:** [`19179cc07e01f9fe52fb.json`](../../sessions/19/19179cc07e01f9fe52fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

### 任务 A：results_summary.json

已写入 `/artifacts/results_summary.json`，包含 12 个 section：
- **core_matrix_3x3**：9 cells 均来自 plan_012 标准化评估（RF 4-class acc + CI + d1v2/d2v3 AUC）
- **instruct_model / learned_estimator_120k / baseline_comparison / prompted_gen / wild_data_fpr / downstream_train_loss / theory_auc_values / cross_model_loo / depth_extension_edd**：按模板填入
- **supplementary**：额外收录了 cross_strategy_loo、granularity_ablation、mlp_19feat、per-model finetune losses、depth extension binary pairwise 的详细数据

注意 core_matrix_3x3 数据与原始实验存在微小差异（如 GPT-2 XL nucleus 0.8393 vs 原始 0.833），因为 plan_012 是统一重评估。

---

### 任务 B：Pareek & Sanghavi (2024) 引用核实

**论文真实存在，但作者名有误。**

- **正确标题**：*Understanding the Gains from Repeated Self-Distillation*
- **正确作者**：**Divyansh Pareek, Simon S. Du, Sewoong Oh**（非 Sanghavi）
- **Venue**：NeurIPS 2024 Main Conference（确认）
- **问题**："Sanghavi" 不是本文作者。Sanghavi（Sujay Sanghavi）出现在 Das & Sanghavi 的 **prior work** 中（研究 one-step self-distillation），Pareek et al. 的论文引用并扩展了他们的结果，可能导致混淆。

**修正建议**：引用改为 `Pareek et al. (2024)` 或 `Pareek, Du, & Oh (2024)`。

Sources:
- [NeurIPS 2024 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0eb1ac7551ddbae575415aa5183a88be-Abstract-Conference.html)
- [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/94147)
- [OpenReview](https://openreview.net/forum?id=gMqaKJCOCB)

---
