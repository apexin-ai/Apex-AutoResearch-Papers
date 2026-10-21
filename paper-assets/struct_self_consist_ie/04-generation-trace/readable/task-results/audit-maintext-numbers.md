# audit maintext numbers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_maintext-numbers_20260524T042759_result.json`
- **Structured JSON:** [`d1dd80d8f98fee973cdc.json`](../../sessions/d1/d1dd80d8f98fee973cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。发现 14 个问题：

**3 个严重问题（跨表不一致）：**
- **#5**: Tab selection vs Tab fewnerd SciERC 基线不一致（Greedy .645 vs .663，LP Δ +0.2pp vs +0.61pp）— 同一设置两个表不同数字
- **#10**: SciERC EM AUROC 论文 .631 vs registry .7493 — registry 和 provenance 从未更新
- **#11**: LP ρ 在两个表间不一致（SciERC .205 vs .159）

**主要中等问题：**
- Construction +1.40pp (4-seed non-CV) vs +0.88pp (5-fold CV) 在同一段落混用未说明
- LP selection +1.39pp 主种子 registry 显示 1.36pp
- 多个数字无法从 registry 追溯（appendix 来源或统计计算）

**7 个 bug-prone 数字全部正确** ✅（.631 不是 .749、13.0pp 不是 11.4pp、+0.6pp 不是 +0.61pp 等）

报告已写入 `artifacts/audit_maintext_numbers.md` 并注册。

---
