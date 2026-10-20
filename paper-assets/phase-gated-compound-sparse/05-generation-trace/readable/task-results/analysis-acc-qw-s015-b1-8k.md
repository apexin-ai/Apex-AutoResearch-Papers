# analysis acc qw s015 b1 8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s015_b1_8k_20260516T011221_result.json`
- **Structured JSON:** [`1d8f9167ed20c16559cd.json`](../../sessions/1d/1d8f9167ed20c16559cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析摘要：

---

**acc_qw_s015_b1_8k 结果：23/50 = 0.46**

- **8k vs 2k batch1 对比**：s015 从旧值 17/50 (0.34) 跳到 23/50 (0.46)，差异 +6 题。但截断无法解释这个差异——仅 3 题 gen_length > 2048，且这 3 题在 8k 下仍全部答错。1 题撞到 8192 上限（truncation_rate=2%）。差异更可能来自 GPU 浮点非确定性导致的采样路径分叉。
- **与 s020 rescore 的对比异常**：s020 8k rescore 结果不变 (13/50)，s015 却变化 +6，不一致。这暗示 s015 的 ±6 波动属于采样噪声而非系统性截断修复。
- **对 dose curve 的影响**：若采信新值，combined s015 = (23 + 19) / 100 = 0.42，反超 dense (0.40)，dose curve 在 s015 处出现非单调上凸，不合理。**建议不更新权威值**，而是将此结果视为 batch1 采样方差的证据，保留原 combined 值 0.36 或考虑对 s015 做第三次独立 batch 来降低方差。

---
