# audit data correctness table10 xref

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-correctness-table10-xref_20260522T022433_result.json`
- **Structured JSON:** [`b2263574c4495be6e60b.json`](../../sessions/b2/b2263574c4495be6e60b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。**55 项核对，54 项正确，1 项不一致。**

唯一问题：**§5.5 的 Δτ = 0.27**。实际计算 B3 Vanilla 2PL 在 RRF 300 items (τ=0.731) vs random 300 items (τ=0.554) 的差值为 0.177，不是 0.27。即使用 B0 Raw τ 比较 (0.767 vs 0.537) 也只得到 0.230。建议核实计算口径或修正为 Δτ ≈ 0.18。

其余所有数字——Table 4 全部 14 个 MAE/τ 值、Table 10 全部 6 个 prior sensitivity 值、§5.7 全部 7 个 domain 内联数字、Limitations 的 LoRA%/+33% 声明、以及 8 组交叉引用——均与源数据一致。

---
