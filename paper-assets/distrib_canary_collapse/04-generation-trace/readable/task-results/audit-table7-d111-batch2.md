# audit table7 d111 batch2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table7_d111_batch2_20260520T010742_result.json`
- **Structured JSON:** [`a14b2492a1f93b81ac35.json`](../../sessions/a1/a14b2492a1f93b81ac35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/table7_d111_audit_batch2.md`。

核心发现：

| 实验 | K≥3 old→D111 | K≥4 old→D111 |
|------|-------------|-------------|
| GPT-2m s42 | 6/8 → **5/8** | 2/8 → **0/8** |
| GPT-2m s43 | 6/8 → **1/8** | 4/8 → **0/8** |
| OPT-1.3B s42 | 6/8 → **3/8** | 2/8 → **0/8** |
| Padding s42 | 6/8 → **6/8** | 6/8 → **0/8** |

**K≥4 全部归零** — 所有 4 个实验的 32 个 diff_xcorr forward peak_lag 无一 > 0，D111 方向检查将 diff_xcorr 完全排除出 K 计算。K≥3 影响因实验而异：Padding 最稳健（thresh+permG+TY 撑住 6/8），GPT-2m s43 最严重（threshold_onset 只有 1/8 显著，可能是旧版阈值计算的问题）。PermG 不受影响，仍为 6/8。

---
