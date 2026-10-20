# analysis table1 nve integrity check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1-nve-integrity-check_20260516T202231_result.json`
- **Structured JSON:** [`4bbd917eda3a04657fa2.json`](../../sessions/4b/4bbd917eda3a04657fa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结论：

**Reviewer 的质疑完全正确。** 008d 和 009e 的 NVE ���在 25K-55K bit-for-bit 相同，原因是 009e 命名为 "s1" 但实际使用了 seed=0（configs.yaml 默认值），与 008d 相同。这不是 checkpoint 恢复（train_eps 日期不同），而是相同 seed + 确定性环境产生了完全一致的训练轨迹。

关键影响：
- 009e 不是独立 seed，effective n=1 而非 n=2
- NVE threshold 分析已正确排除 009e（只用 008d + 009b）
- 论文 Table 1 如果引用了 009e 作为 "seed 1"，需要删除并修正
- 008d 配置当前真正独立的 seeds 只有 {0, 2}，n=2

报告已保存至 `artifacts/analysis/table1_integrity_check.md`（服务器和本地各一份）。

---
