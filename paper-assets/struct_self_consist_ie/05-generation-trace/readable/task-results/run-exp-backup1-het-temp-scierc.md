# run exp backup1 het temp scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_backup1_het_temp_scierc_20260520T181112_result.json`
- **Structured JSON:** [`761a17656d421c672148.json`](../../sessions/76/761a17656d421c672148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE (negative)。

**总结**: het_temp 实验 6 组全部跑完（~2 分钟 wall clock）。**Negative result** — 混合温度采样在 SciERC 上无法一致性提升 F1。所有 best mix 的 Δ 均在 ±0.005 以内且方向不一致。虽然混合有效降低 degeneracy（T=0.5 从 ~35% 降到 ~17%），但 diversity 的增加并不转化为更好的 construction F1。这进一步证实采样层面的干预不是当前瓶颈。

---
