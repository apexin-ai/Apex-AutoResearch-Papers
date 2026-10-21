# audit data table1 dose response

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-table1-dose-response_20260522T033442_result.json`
- **Structured JSON:** [`3136044f0d4347575d2e.json`](../../sessions/31/3136044f0d4347575d2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

64 个数据点全部核对完毕。核心结论：

**所有基线和 Δacc 数值与源数据一致，无数据错误。** 发现 3 个小问题：

1. **Gemma-2 "mono." 标签**（Table 1 Peak 列）：d050 (64.01%) 低于 d025 (64.56%)，不严格单调。整体趋势向上但有 0.55pp 回落。

2. **OLMo-2 s123 符号**（Table 2）：Δ=-0.55pp，按文中定义 |Δ|<1pp 应标 "0" 而非 "−"。影响 OLMo-2 的 cross-seed 模式从 "+/−/+" 变为 "+/0/+"。

3. **GSM8K 脚注标签**（tab:gsm8k_transfer）：OLMo-2 脚注写 "Seed=42: +2.1pp"，实际是 mean(s42=+1.74, s123=+2.43)=+2.09pp。行文中 "OLMo-2's gain is seed-sensitive (+2.1pp at s42)" 同样受影响。

报告已注册为 artifact `art_20260522_12d7cc`。

---
