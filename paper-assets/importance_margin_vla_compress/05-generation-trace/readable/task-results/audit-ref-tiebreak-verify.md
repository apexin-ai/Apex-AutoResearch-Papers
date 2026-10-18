# audit ref tiebreak verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_tiebreak_verify_20260529T070204_result.json`
- **Structured JSON:** [`1996c631819c6840b08f.json`](../../sessions/19/1996c631819c6840b08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部证据已收集，以下是最终判定：

---

### [khaki2025sparsevila] 最终判定: ✗需修复
- **证据**: arXiv 页面 ([2510.17777](https://arxiv.org/abs/2510.17777)) 和 [HTML 全文](https://arxiv.org/html/2510.17777) 标题均为 **"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference"**，是动名词 "Decoupling"，不是过去分词 "Decoupled"。Worker A+C 正确。
- **修复建议**: `title` 字段 "Decoupled" → "Decoupling"

### [wang2025specprunevla] 最终判定: ✓当前 bib 正确（保持 arXiv preprint）
- **证据**: 该论文的 [OpenReview 页面](https://openreview.net/forum?id=t85Ni0LwjC) 显示 venue 为 **"Submitted to ICLR 2026"**（非 ICML、非 ICRA）。ICLR 2026 已于 2026 年 3 月底出结果（[官方博客](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)），该论文仍显示 "Submitted to" 而非被接收，说明**未被 ICLR 2026 接收**。无证据表明被 ICML 2026 或 ICRA 2026 接收。Worker B (ICML) 和 Worker C (ICRA) 均不正确。
- **修复建议**: 无需修改，保持 `arXiv preprint arXiv:2509.05614, year=2025`

### [black2024pi0] 最终判定: ✗需修复
- **证据**: RSS 官网 proceedings 页面明确列出 [π₀: A Vision-Language-Action Flow Model for General Robot Control](https://roboticsconference.org/program/papers/10/) 为 RSS 2025 接收论文（Paper #10）。Worker B 正确。
- **修复建议**: `booktitle` 改为 `{Robotics: Science and Systems (RSS)}`，`year` 改为 `2025`，删除 `journal={arXiv preprint}` 字段

---
