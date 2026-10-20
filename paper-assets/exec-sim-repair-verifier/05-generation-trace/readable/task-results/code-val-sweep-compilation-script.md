# code val sweep compilation script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_val-sweep-compilation-script_20260515T163904_result.json`
- **Structured JSON:** [`83d804a1dd76752f72e4.json`](../../sessions/83/83d804a1dd76752f72e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本工作正常。结果汇总：

- **已完成**：9 个 checkpoint（8 个来自之前 sweep@seq8192，1 个来自当前 sweep@seq2048）
- **缺失**：20 个 checkpoint（2000-5800，sweep 正在进行中）
- **当前 Top-1**：ckpt-1000 88.23%（seq8192）
- **ckpt-1800**（首个 seq2048 结果）：82.99% — 注意 seq_length 从 8192 降到 2048 会影响精度，两段数据不完全可比

CSV、PDF/PNG 曲线图已生成。图表中用不同 marker 区分了 seq8192（方块）和 seq2048（圆点）两段数据，并用虚线桥接。

当前 sweep 刚跑完第 1 个 checkpoint（1800/21），剩余 20 个还在排队。

---
