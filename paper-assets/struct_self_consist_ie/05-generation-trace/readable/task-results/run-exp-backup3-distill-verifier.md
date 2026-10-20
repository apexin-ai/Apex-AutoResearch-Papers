# run exp backup3 distill verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_backup3_distill_verifier_20260520T184111_result.json`
- **Structured JSON:** [`4e363a407fa720d7b432.json`](../../sessions/4e/4e363a407fa720d7b432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**总结**：`exp_backup3_distill_verifier` 实验完成，conclusion = **negative**。

- Entity-level AUROC 不错（~0.875），说明分类器能区分 gold/non-gold entities
- 但转化为下游 F1 时，ΔF1 极小（最好的 MLP 仅 +0.0011），说明 weighted MV 无法持续超越 standard MV
- 核心原因：agreement_ratio 是压倒性强特征（LR coef ~1.6），而这本质上就是 MV 的投票频率——分类器学到的主要就是"同意率高的 entity 更可能正确"，跟 MV 做的事情一样
- 结果文件在 `/root/autodl-tmp/struct_self_consist_ie/output/distill_verifier/distill_verifier_results.json`

---
