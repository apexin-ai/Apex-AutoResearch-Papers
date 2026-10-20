# audit ref check B

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-check-B_20260526T101811_result.json`
- **Structured JSON:** [`7b4fa79210ad386e27d3.json`](../../sessions/7b/7b4fa79210ad386e27d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/ref_audit_worker_B.md`。

核心发现：
- **64 篇论文全部真实存在，无 hallucinated citations**
- **4 条必须修复**：`kang2025selfcertainty`（NeurIPS volume 38→39）、`yee2019noisy`（缺作者 Nathan Ng）、`shinn2023reflexion`（缺作者 Edward Berman）、`li2023stepaware`（标题多了 "Large"）
- **3 条建议修复**：`dong2024xgrammar`（应更新为 MLSys 2025）、`fleiss1971agreement`（缺 volume/pages）、`geifman2017selective`（NIPS/NeurIPS 命名）
- **3 条未使用 entry** 可清理：`holm1979simple`、`li2024simple`、`xiao2022uncertainty`

---
