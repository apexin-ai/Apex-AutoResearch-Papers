# audit data provenance full v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_provenance_full_v2_20260523T112056_result.json`
- **Structured JSON:** [`0e089ae029894776347a.json`](../../sessions/0e/0e089ae029894776347a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/data_provenance_audit.md`。

**核心发现**:

- **52/63 数据点验证通过** — Table 1 核心数字、全部 12 个 Wilson CI、Fisher 显著性方向、Proposition 2 预测、binomial test、ScienceWorld、Abstract/Intro/Conclusion 引用均正确。

**需修复的 2 个 P0 问题**:
1. **seed5 step10**: 论文写 25.37% (34/134)，但 registry 记录 29.10% (39/134)，差 5 tasks。Registry 有 verification note 确认 29.10% 正确。
2. **Window sweep 混用评估集**: 图标题写 "OOD success"，但 h=10 (6.25%=2/32) 和 h=20 (15.6%=5/32) 来自 32-task ID 集，episode (23.88%=32/134) 来自 134-task OOD 集。

**3 个 P1 问题**: seed8 OOD 差 2 tasks (11.94% vs 13.43%)；seed2048/seed42/seed2 共 3 个 seed 的 OOD eval 在 registry 中无可追溯条目。

**2 个 P2 问题**: seed2 的 p=0.02 实为 chi-squared 值而非 Fisher exact；8B Cell A "1.5%" 实为 1.5625%。

---
