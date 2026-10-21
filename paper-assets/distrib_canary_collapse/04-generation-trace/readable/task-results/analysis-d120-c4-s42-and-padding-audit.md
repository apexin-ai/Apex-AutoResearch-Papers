# analysis d120 c4 s42 and padding audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d120_c4_s42_and_padding_audit_20260520T060208_result.json`
- **Structured JSON:** [`4e622b51de3551ebb956.json`](../../sessions/4e/4e622b51de3551ebb956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 个实验全部 D120 重算，registry 已更新，报告已注册。

### 结果摘要

| Experiment | α | PermG_fwd | PermG_rev | K≥3 | K≥4 |
|---|---|---|---|---|---|
| c4_a025_s42 | 0.25 | 0/8 | 0/8 | 0/8 | 0/8 |
| c4_a050_s42 | 0.50 | 8/8 | **7/8** | 4/8 | 0/8 |
| c4_a075_s42 | 0.75 | 8/8 | 0/8 | 8/8 | 0/8 |
| padding_a100_s42 | 1.0 | 6/8 | 0/8 | 6/8 | 0/8 |

### 关键发现

1. **C4 dose-response 确认**: K3 从 0→4→8 随 α 递增，与 wiki domain 一致
2. **C4 α=0.50 双向 PermG**: rev=7/8，wiki 域从未出现。可能反映 C4 跨域环境下更强的双向反馈
3. **Padding 审计通过**: K3=6/8 与 wiki baseline (`generalize_pythia410m_wiki_a100_s42`) 完全一致。Padding side 对 lead-lag 无影响。2 个失败 pair 均为 mauve
4. **TY Granger 在 17855 上不可用**: `signonly` API error，导致所有 K≥4=0/8。K≥3 不受影响

---
