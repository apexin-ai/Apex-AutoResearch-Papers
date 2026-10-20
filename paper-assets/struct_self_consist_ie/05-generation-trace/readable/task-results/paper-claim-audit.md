# paper claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim-audit_20260523T183421_result.json`
- **Structured JSON:** [`3fed042b4e26a5f3b472.json`](../../sessions/3f/3fed042b4e26a5f3b472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/claim_audit_report.md`。

核心发现：

**3 处 MISMATCH：**
- **M1** (HIGH): `experiments_main.tex:76` 5-epoch LP Δ 写了 +0.09pp，但同文件 line 107 和 appendix 表格均为 **+0.12pp**（疑似混淆了 footnote 中 corpus micro-F1 的 +0.09 值）
- **M2** (HIGH): `experiments_main.tex:76,107` 5-epoch degeneracy 写了 31%，但 appendix tab:epoch_confound 为 **26.4%**（疑似混淆了 Qwen2.5-7B FT 的 31.7%）
- **M3** (LOW): `experiments_main.tex:91` SciERC degeneracy 13.4% vs 其他表格的 **12.2%**（可能因评估子集不同）

**1 处 UNTRACED：**
- **U1** (MEDIUM): `experiments_main.tex:106` "+5--8pp at 80% coverage" 引用 tab:cross_selection，但该表不含 selective prediction 数据（疑似旧版残留）

其余 55+ 定量声明全部通过交叉验证。M1+M2 在同一句话中，修正影响最小。

---
