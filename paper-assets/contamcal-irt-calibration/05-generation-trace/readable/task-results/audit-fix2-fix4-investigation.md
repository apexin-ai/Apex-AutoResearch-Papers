# audit fix2 fix4 investigation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_fix2-fix4-investigation_20260523T102829_result.json`
- **Structured JSON:** [`d1532db49ab231feee38.json`](../../sessions/d1/d1532db49ab231feee38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/audit_fix2_fix4_investigation.md`。

**Fix-2 结论**:
- **d = −1.98 (d100)**: 已溯源，来自 `exp008_v4_results.json` S2_MinKPP 三 benchmark 均值 (MMLU −1.22 / GSM8K −2.67 / ARC −2.05 → mean −1.978)。审计之前只看到了 MMLU 单值。
- **|d| > 1.4 (d005)**: MMLU d005 |d|=1.386，差 0.014 不满足。introduction.tex 的 "across benchmarks" 措辞技术上不正确。建议改为 "|d| > 1.2" 或删除 "across benchmarks"。

**Fix-4 结论**:
- "+10.1pp" 已不在当前论文中（已被改为 +11.1pp），原值 = mean(s42=11.07, s123=9.18) 已被旧审计验证正确。
- 当前 +11.1pp 是 s42 单种子值，但 Range ±0.9 仍按双种子均值计算，存在不一致。
- results.tex:57 "d005 yields +11.1pp" 有歧义 — d005 GSM8K Δ 实际是 +6.37pp，+11.1pp 是 d100 值。

---
