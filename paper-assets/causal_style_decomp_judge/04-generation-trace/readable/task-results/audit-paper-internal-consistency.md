# audit paper internal consistency

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-internal-consistency_20260525T083230_result.json`
- **Structured JSON:** [`f4aafe791279539dda74.json`](../../sessions/f4/f4aafe791279539dda74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。发现 **3 个 critical 不一致**，需要修复：

1. **Appendix K bootstrap 的 BT 值 (66.5%) 与 Table 1 / Analysis (67.5%) 矛盾** — 同一 n=355 数据，两处报不同 BT
2. **Appendix K bootstrap 表的 d = −0.017 与 Table 1 / Analysis 的 d = −0.025 矛盾** — n=355 行应一致
3. **Table 2 (GEE) 脚注声称所有非 scaled 行 n=88，但 verbosity 行实际 n=86**

另有 4 个 warning（abstract/analysis 中 verbosity 误标 n=88；"8/11" 计数不明；conclusion "6/24" 措辞夸大 Blindspot 范围）和 2 个 info 级精度差异。

无占位符，无 undefined reference，16 组关键数字已验证一致。完整报告已写入 artifacts 并注册。

---
