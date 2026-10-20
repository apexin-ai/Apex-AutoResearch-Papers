# analysis re nonzero selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_nonzero_selection_20260515T071419_result.json`
- **Structured JSON:** [`768b672654d9311f3876.json`](../../sessions/76/768b672654d9311f3876.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果写入 `artifacts/re_nonzero_selection_analysis.md`。

关键发现：

- 551 个 instance 中仅 238 个 (43.2%) 有非零 RE greedy F1
- **全部 5 个信号在两个子集上都无法超过 greedy**（所有 gain 为负，p=1.0）
- **非零子集上 selection 更差**，gain 幅度是全集的 5-10 倍（如 VC: -0.1005 vs -0.0325），因为 greedy 在非零子集上已经很强 (F1=0.6743)，信号主动选了更差的样本
- Zero-F1 instance 并未拉低信号表现，反而起到了缓冲作用（选错也无所谓，greedy 本来就是 0）
- Oracle gap 仍然存在 (0.7574 vs 0.6743)，说明有改进空间，但当前信号无法利用

---
