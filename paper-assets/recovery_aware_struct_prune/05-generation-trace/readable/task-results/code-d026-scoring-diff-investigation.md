# code d026 scoring diff investigation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d026-scoring-diff-investigation_20260515T094616_result.json`
- **Structured JSON:** [`f0f2d63f0e994da00c26.json`](../../sessions/f0/f0f2d63f0e994da00c26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scoring_diff_investigation.md`。核心结论：

**根因：两台服务器独立计算了 `importance_scores.pt`（md5 不同），不同 driver 版本（595 vs 580）导致浮点非确定性。**

具体机制：
- L20 g27 和 L26 g5 的 importance score 仅差 ~0.00007，calibration noise 翻转了排序
- westb: L26 g5 score 更低 → 被剪 → L26 少 1 group, L20 多 1 group
- westd: L20 g27 score 更低 → 被剪 → L20 少 1 group, L26 多 1 group
- 总剪枝量完全相同（200 MLP groups, sparsity ≈ 19.1%）

**α=0 在代码逻辑上与 standard pruning 完全等价**（`(1-overlap)^0 = 1.0`，乘法不改变 score）。论文表述无需修改。差异纯粹是输入数据不一致，不是算法问题。

**建议：** 如需 ablation 与 baseline 严格一致，所有实验应共享同一份 importance_scores.pt（复制而非重算）。

---
