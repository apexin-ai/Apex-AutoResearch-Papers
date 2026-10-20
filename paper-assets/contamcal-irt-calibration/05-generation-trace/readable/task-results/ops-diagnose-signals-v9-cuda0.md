# ops diagnose signals v9 cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-signals-v9-cuda0_20260516T034833_result.json`
- **Structured JSON:** [`4623037c773fb17478e3.json`](../../sessions/46/4623037c773fb17478e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

- **v9**: 部分完成。d025_s123 全部信号已就绪。d100_a32_s123 mmlu s4 由 orphan PID 689315 继续（~2.4h），但 gsm8k/arc 需要新提交。
- **cuda:0**: eval + 1.5B signals 共存，内存安全（58%），互相竞争计算但不会崩。1.5B 在 ~45%。
- **cuda:4**: PID 689315 独占，正常运行 d100_a32_s123 mmlu s4。

---
