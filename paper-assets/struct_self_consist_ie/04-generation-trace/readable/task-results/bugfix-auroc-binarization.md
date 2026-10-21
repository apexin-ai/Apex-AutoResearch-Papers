# bugfix auroc binarization

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_auroc_binarization_20260514T142457_result.json`
- **Structured JSON:** [`44d2dd21f9e7a71106a9.json`](../../sessions/44/44d2dd21f9e7a71106a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**Bug 根因**：`compute_auroc` 用 `f > median` 做二值化，WNUT-17 条件集 67.1% 样本 F1=1.0 导致 median=1.0，strict `>` 产生空 pos 集，AUROC 直接返回 0.5。

**修复**：当 `> median` 产生退化分割时，回退到 `>= median` vs `< median`。修改了 4 个文件：`evaluation.py`、`analyze_logprob_baseline.py`、`analyze_exact_match_voting.py`、`analyze_entity_voting.py`。

**修复前后对比**：
- WNUT-17 conditional logprob AUROC: **0.5000 → 0.7092**（唯一受影响的数字）
- WNUT-17 full 和 SciERC 全部不变

**关键发现**：修复后 logprob 在 WNUT-17 条件集上 AUROC=0.7092，高于 SJ 的 0.6535——logprob baseline 在 WNUT-17 上比结构一致性更强，不是随机水平。exp-003 的 `report.json` 中 `logprob_baseline.conditional.auroc` 需更新。

诊断报告已写入 `artifacts/auroc_bug_diagnosis.md`。

---
