# review round7 consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_round7_consistency_20260515T124330_result.json`
- **Structured JSON:** [`8f21816f45957d1a4598.json`](../../sessions/8f/8f21816f45957d1a4598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。总评 **WARNING**，发现：

**1 CRITICAL**：OOD 表 (Appendix Table 9) 的 in-domain 列声称引用 Table 1 (seed=42) 但实际用了 Table 5 的 3-seed 均值。所有 5 个信号的 Δ 被偏移，EM 的 Δ 符号翻转 (+.005 → -.007)。需立即修复。

**3 WARNING**：
- WNUT 表 caption 标注 N=8，但 registry 仅有 N=16 数据，且表中数值与 N=16 registry 精确匹配
- Appendix logprob_ties 节内部矛盾：正文说 59.7%，表格说 60.3%（registry 支持 59.7%）
- Table 1 两个 AUROC 值有末位 rounding 偏差（.693→.694, .600→.601）

**全部硬约束通过**：exp_012 旧数据未被引用、LLaMA 数据来源正确、selection 正确描述为 null result、无 "0.335"、OOD 失败正确归因为 model failure、exp_019 未出现。Table 1 全部 40 个数值与 registry 匹配。

报告已写入 `artifacts/review_reports/round_7_consistency.md`。

---
