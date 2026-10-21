# investigation auroc pipeline p01

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigation_auroc_pipeline_p01_20260519T140333_result.json`
- **Structured JSON:** [`d7fe5393c806ce569825.json`](../../sessions/d7/d7fe5393c806ce569825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/p01_auroc_investigation_report.md`。

**根因**：Registry (`all_signals_5signal.json`) 和 Paper Table 1 使用了完全不同的 AUROC 定义：
- **Paper Table 1**: `F1 >= median (0.667)` binarization — 正类 301/529
- **Registry**: `F1 >= 1.0` (perfect extraction) binarization — 正类 132/529

**Paper Table 1 是正确的**，与论文 §3 方法描述一致。EM 的 13.5pp 偏差最大是因为 exact match 天然与"完美抽取"强相关，但与"高于中位数"的关系弱得多。LP 巧合匹配是因为其在两种 threshold 下的 discriminative power 恰好相近。

**EM 不是 SciERC AUROC 最高信号**——在论文定义下 VC (.663) 和 SJ (.650) 排前两位，EM (.614) 排第三。

此外，`d114_auroc_investigation/` 目录下已有之前的完整调查记录（包括 `evaluation.py` 的 `>` vs `>=` bug 修复）。

---
