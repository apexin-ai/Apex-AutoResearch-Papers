# audit data integrity

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-integrity_20260525T194250_result.json`
- **Structured JSON:** [`99ab9202c93b1e71586d.json`](../../sessions/99/99ab9202c93b1e71586d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。

**审计结果**: ~210 个数值，~195 个验证通过。

**已修复 (appendix.tex)**:
1. LLM-judge 表 9-class DD: `.994` → `.997`（与 Table 2 一致，源: round7_seed_level_stats.json）
2. E2E 表 frozen 行: DD `.994±.005` → `.997±.005`，AA `.939±.047` → `.972±.026`（源: exp26_frozen_probing.json）
3. E2E Δ 行: `+.006/+.058` → `+.003/+.025`
4. 正文: "+5.8pp" → "+2.5pp"
5. E2E caption: 移除了与 frozen_verify 的冗余对比描述

**需你决定的 2 个 UNVERIFIABLE 项**:
- **TOST 10-seed**: 服务器仅有 5-seed 数据 (d=0.0/DD, d=0.09/AA)，论文声称 10-seed (d=−0.136, d=0.440)。需补做实验或降级为 5-seed。
- **κ=0.78 (n=50)**: 无对应源数据文件。需补充人工标注数据。

审计报告: `artifacts/data_audit_report.md`

---
