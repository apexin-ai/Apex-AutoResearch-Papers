# analysis claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim_audit_20260519T133313_result.json`
- **Structured JSON:** [`cd031278272c5d576f77.json`](../../sessions/cd/cd031278272c5d576f77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/claim_audit_report.md` 并注册。

核心发现：

**4 个需修复的不一致 (❌)**：
1. WNUT VC ρ 打字错误：experiments.tex:104 写了 0.730，应为 0.724
2. Table 1 SciERC AUROC 列与 registry 系统性偏离（EM: 0.614 vs 0.749），疑似 AUROC 计算管线不同
3. CoNLL LP 选择 Δ：Table 3 写 -0.85pp，附录 cross-selection 表算出 -1.1pp
4. WNUT zero-F1 率在论文内不统一（51% vs 52%）

**6 个存疑/无法验证的声明 (⚠️)**：
- "13–87% degeneracy" 跨 benchmarks → 87% 来自特定 model×N 配置，非跨数据集
- CoNLL 退化率 48.4% 可能是 N=16 值误用于 N=8 表格
- FewNERD 退化率 13.8% 无法从 registry seed 数据复现（3-seed 均值约 11.8%）
- FewNERD LP ρ=.220 种子间方差极大，无法从现有数据验证
- Entity construction 数值因评估协议不同（multi-seed vs 5-fold CV）无法直接对比

**已知矛盾状态**：当前论文版本中未找到 "Discussion +0.1pp" vs "Limitations +0.4pp" 冲突，可能已在编辑中修复。72B 节中 SciERC -0.1pp 和 CoNLL -0.4pp 是不同数据集的结果，非矛盾。

---
