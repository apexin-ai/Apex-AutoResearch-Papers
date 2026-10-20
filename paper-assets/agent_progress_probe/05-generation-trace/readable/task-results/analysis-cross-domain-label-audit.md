# analysis cross domain label audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-domain-label-audit_20260514T220420_result.json`
- **Structured JSON:** [`7add9d35119d653c3d17.json`](../../sessions/7a/7add9d35119d653c3d17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整摘要：

---

## 诊断结果：跨域结构特征数字不一致

### 根因：过时标签（Pre-Relabeling 残留结果）

旧的 v2 paired bootstrap 报告的 GB macro_f1=0.6936 是基于**旧版 `windows_labeled.jsonl`** 计算的。用当前数据重新运行完全相同的 v2 脚本，GB 得分为 **0.9767**。

### 三步诊断详情

**Step 1 — 标签一致性**

| 指标 | embeddings.pt | windows_labeled.jsonl (当前) |
|------|--------------|--------------------------|
| OH 窗口数 | 143,057 | 150,652 (non-abstain) |
| stagnation 数 | 9,390 (6.56%) | 31,440 (20.87%) |
| progress 数 | 133,667 (93.44%) | 119,212 (79.13%) |

- Cohen's kappa = **0.3925**（仅"fair"级别一致性）
- 21,596 个窗口在 embeddings.pt 中标为 progress，但在当前 WL 中标为 stagnation
- 标签分布差异 3.2 倍

**Step 2 — 控制变量 GB 评估（当前数据）**

| 评估集 | N | macro_f1 |
|--------|-------|----------|
| (a) ALL OH non-abstain | 150,652 | 0.973 |
| (b) OH test matched | 20,807 | 0.981 |
| (c) OH non-test | 128,679 | 0.973 |
| (d) OH test all-inst | 21,973 | 0.975 |
| 旧 v2 结果（已废弃） | 20,807 | 0.6936 |
| 新 v2c 运行 | 20,807 | **0.9767** |

所有评估在当前数据上高度一致（0.97-0.98），没有 test split 偏差。

**Step 3 — 窗口数差异**
- 差 7,595 个窗口，全部在 WL 有但 embeddings.pt 无
- 这些窗口都是 progress 标签、conf=1
- 原因：WL 重新标注后增加了窗口，但 embeddings.pt 未重新生成

### 关键结论

1. **0.6936 是无效数字** — 不能在论文中引用
2. **当前一致数字**：GB cross-agent OH 全量 = 0.973，test split = 0.977
3. **embeddings.pt 标签严重过时** — Probe 模型训练在旧标签上，现在评估仅得 0.644
4. **必须行动**：重新生成 embeddings.pt 标签 或 用 WL 标签直接训练 Probe，然后重新跑 paired bootstrap

诊断报告已保存至 `results/cross_domain_label_audit.json`（服务器）和 artifact registry。

---
