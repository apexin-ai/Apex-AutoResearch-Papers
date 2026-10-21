# diagnose exp 040 wide dual critic cheetah

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_040_wide_dual_critic_cheetah_20260522T093626_result.json`
- **Structured JSON:** [`497198040f804b44aee4.json`](../../sessions/49/497198040f804b44aee4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 memory.md。

## 总结

**exp_040 没有程序崩溃**（EXIT_CODE=1 信息可能有误）。进程仍在 GPU 上正常运行。

真正的问题是**训练质量崩溃**：
- Eval: 256.4 (peak at 25k) → 41.0 (215k)，持续单调下降
- Gate 锁死 dt=2，entropy=0，从未探索其他 horizon
- 与之前 exp_034 Cheetah dual-critic 结论一致：dual-critic 在 Cheetah 上无效

**建议**：可以让它跑完收集完整数据，但结论已明确 — wide dual-critic 在 Cheetah 上是 negative result。不需要 resume 或修代码。

---
