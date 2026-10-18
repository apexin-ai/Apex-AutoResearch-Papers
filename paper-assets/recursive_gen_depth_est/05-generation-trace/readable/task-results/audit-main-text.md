# audit main text

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_main-text_20260525T194442_result.json`
- **Structured JSON:** [`715217b9f2f43063f4c8.json`](../../sessions/71/715217b9f2f43063f4c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/audit_main_text.md`。

**核心结论：119 个数字中 100 个精确匹配 registry，0 个内部矛盾。**

**5 个不一致（均为小幅偏差）：**
1. AUC-excess contraction ratio 0.80 → registry 计算为 0.759（theory.tex:10）
2. AUC-excess contraction ratio 0.69 → registry 计算为 0.646（theory.tex:10）
3. Top-5 accuracy 76.5% → registry 为 76.8%（atlas.tex:52）
4. "d2 F1 ≤ 0.26" → RoBERTa d2 F1 = 0.261 略超（discussion.tex:6）
5. 14B self-ref "EDD=0" 表述模糊 — 仅 nucleus 确认 EDD=0（generalization.tex:83）

**需重点关注：** AUC-excess contraction ratios（#1, #2）偏差最大（约 5%），建议核实计算方法是否与 `depth_extension_binary_pairwise_002` 的 AUC 值一致。

14 个无出处数字均为 derived metrics（如 d1-d3 balanced accuracy 45.9%、VIF 计数、per-depth feature medians），registry 通常只记录原始指标，可从实验数据直接计算。Table 1、Table 2、Table 3 的所有数字均通过验证。

---
