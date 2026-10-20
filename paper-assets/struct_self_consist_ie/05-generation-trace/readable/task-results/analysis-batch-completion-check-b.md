# analysis batch completion check b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch_completion_check_b_20260516T140055_result.json`
- **Structured JSON:** [`ee8f839236f6e3325088.json`](../../sessions/ee/ee8f839236f6e3325088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个实验均已完成，报告已写入 `artifacts/batch_completion_check_b.md`。

核心发现：
- **exp_026_t05** (T=0.5): 完成，verdict=FAIL，SJ ρ=0.297，oracle headroom 仅 0.078
- **exp_026_t08** (T=0.8): 完成，verdict=MARGINAL，SJ ρ=0.359，headroom 更大(0.105)，T=0.8 各项指标优于 T=0.5
- **Trained verifier (exp_019 LR, N=8)**: LR selection F1 仅比 greedy +0.0011，oracle gap closure 0.8%，VC 系数独大(0.75)，信号高度冗余
- **exp_027 MLP/RF (N=16)**: MLP/RF 均无法超越 LR，所有监督方法的 selection F1 甚至不如 greedy。**结论：特征是瓶颈而非模型容量**

---
