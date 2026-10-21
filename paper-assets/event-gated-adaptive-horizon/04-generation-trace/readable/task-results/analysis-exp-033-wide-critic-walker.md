# analysis exp 033 wide critic walker

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_033_wide_critic_walker_20260521T120408_result.json`
- **Structured JSON:** [`b55b111dfcdcc9921b92.json`](../../sessions/b5/b55b111dfcdcc9921b92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_033 结果总结

**Conclusion: success（hypothesis validated）**

Wide single critic（2.89M params）**未能阻止 CIVO**：
- VE ratio 在 45-55K 飙升至 **4.7**（exp_032 dual-critic 最高仅 0.099，相差 47 倍）
- CIVO alert 在 step 105K 正式触发
- 不稳定期持续 ~75K steps（占总训练量 36%）
- 训练最终恢复，final eval **407.9**，但仍低于 dual-critic 的 **787.7/551.8**（差距 26-48%）

### 2×2 Factorial 更新

| | Single critic | Dual critic (min) |
|--|--------------|-------------------|
| ~1.2M | 008d: CIVO persistent | exp_035: running |
| ~2.9M | **exp_033: CIVO triggered, transient** | exp_032: CIVO prevented |

**核心结论**：dual-critic 的 min 操作通过悲观 value 正则化从根本上阻止 CIVO 发生；单纯增加参数量只能在 CIVO 发生后帮助恢复，不能预防。

Registry 已更新为 DONE(success)，报告已注册。

---
