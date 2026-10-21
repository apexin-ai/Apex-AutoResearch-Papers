# critical literature verification

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_literature-verification_20260516T053828_result.json`
- **Structured JSON:** [`17e404d3d42b9a91092a.json`](../../sessions/17/17e404d3d42b9a91092a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| # | arXiv ID | 作者 | 标题 | 状态 | 说明 |
|---|----------|------|------|------|------|
| 1 | `2510.03313` | Subramanyam, Chen & Grossman | Scaling Laws Revisited: Modeling the Role of Data Quality in LM Pretraining | ✅ 已确认 | arXiv 存在 + [OpenReview](https://openreview.net/forum?id=x54wwB6QvL) 确认 ICLR 2026 accepted。报告称 "under review" 实为已录用 |
| 2 | `2502.08924` | Amin et al. (Google/USC) | Escaping Collapse: The Strength of Weak Data for LLM Training | ✅ 已确认 | arXiv 存在 + [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/115205) 确认 |
| 3 | `2602.22954` | Martino & Elvira | Effective Sample Size Approximations as Entropy Measures | ✅ 已确认 | arXiv 存在 + [Springer](https://link.springer.com/article/10.1007/s00180-025-01665-8) 确认 Computational Statistics 2025 |
| 4 | `2510.01631` | Kang et al. (Meta/Virginia Tech) | Demystifying Synthetic Data in LLM Pre-training | ✅ 已确认 | arXiv 存在 + [ACL Anthology](https://aclanthology.org/2025.emnlp-main.544/) 确认 EMNLP 2025 |
| 5 | `2410.16713` | Kazdan, Schaeffer, Donoho et al. | Collapse or Thrive? Perils and Promises of Synthetic Data | ✅ 已确认 | arXiv 存在 + [PMLR](https://proceedings.mlr.press/v267/kazdan25a.html) + [ICML.cc](https://icml.cc/virtual/2025/poster/44713) 确认 ICML 2025 |
| 6 | `2410.03735` | Grangier, Fan, Seto & Ablin | Task-Adaptive Pretrained LMs via Clustered-Importance Sampling (CRISP) | ✅ 已确认 | arXiv 存在 + [Semantic Scholar](https://www.semanticscholar.org/paper/3390fdab6dbe8d7cca75336522c85e33e47f31d0) 确认 ICLR 2025 |

## 需要替代引用的论文

无。6/6 全部通过验证。

## 修正项

- Subramanyam et al.：报告写 "under review, ICLR 2026 OpenReview"，实际已被 ICLR 2026 接收（OpenReview 状态为 conference paper）。已在 yaml 中修正为 "ICLR 2026"。

## literature_map.yaml 更新

新增 6 条：
- `subramanyam_2025_scaling_quality` → theoretical-foundation
- `amin_2025_escaping_collapse` → theoretical-foundation
- `martino_2025_ess_entropy` → theoretical-foundation
- `grangier_2025_crisp` → method-component
- `kang_2025_demystifying_synthetic` → background
- `kazdan_2025_collapse_thrive` → background

---
