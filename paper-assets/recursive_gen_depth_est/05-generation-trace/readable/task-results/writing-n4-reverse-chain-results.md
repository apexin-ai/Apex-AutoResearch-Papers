# writing n4 reverse chain results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_n4_reverse_chain_results_20260516T142452_result.json`
- **Structured JSON:** [`324dc90f987ad26fd4f7.json`](../../sessions/32/324dc90f987ad26fd4f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译无错误，18 页（与之前一致）。

完成的修改：

1. **section_appendix.tex** (Appendix): 在 cross-boundary confound discussion 后加入 `\paragraph{Reverse-chain control.}`，含 reverse chain 85.75% [82.0, 89.25] vs forward chain 84.75% [81.0, 88.25] 的结果，论证 architecture confound 不成立。原来的 "Nevertheless, definitive disentanglement requires a reverse-order chain" 改为 "We address this confound directly with a reverse-chain control below."

2. **generalization.tex** (正文): 第 106 行加入 "validated by a reverse-chain control (85.75%)"，仅增加几个词。

3. **abstract.tex**: 将 "cross-model recursive chains...achieve 84.75\% accuracy, providing preliminary evidence" 改为 "bidirectional cross-model recursive chains achieve equivalent accuracy under forward (84.75%) and reverse (85.75%) orderings, providing evidence for a process-level depth signal"——去掉了 "preliminary"，措辞仍然谨慎。

---
