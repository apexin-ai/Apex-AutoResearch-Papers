# code flyingsquid baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flyingsquid-baseline_20260514T110819_result.json`
- **Structured JSON:** [`2f2c7845171a6032a43c.json`](../../sessions/2f/2f2c7845171a6032a43c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Part 1: Filtered Test Set (conf≥2, n=1824)**
- FlyingSquid ≡ Majority Vote — 100% 一致，两者 Macro-F1=1.0（因为 ground truth 就是 majority_label）
- GRU Probe 参考: Macro-F1=0.9055

**Part 2: Full Dataset (n=54,809, 无 conf 过滤)**
- FS vs MV 一致率: 82.04%
- 9,841 个分歧窗口（18%），**全部**是 FS 将 progress 翻转为 stagnation
- MV progress rate: 71.5% → FS progress rate: 53.6%
- FlyingSquid 高度 up-weight outcome_backpropagation 的 stagnation 信号

**结论**: Negative result。FlyingSquid 在高置信度窗口上与 majority vote 完全一致，不提供额外价值。在模糊窗口上引入系统性 stagnation 偏置。作为 Claim 1 的 baseline，说明简单的相关性感知 label model 不能改善标签质量——需要 temporal/sequential 信息（即 GRU probe 的价值所在）。

产出：
- `baseline_flyingsquid.py` 脚本（服务器上）
- `flyingsquid_results.json`（服务器上）
- Registry: `baseline_flyingsquid` (DONE, negative)

---
