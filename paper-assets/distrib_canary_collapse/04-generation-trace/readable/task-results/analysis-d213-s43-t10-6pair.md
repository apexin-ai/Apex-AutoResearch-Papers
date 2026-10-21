# analysis d213 s43 t10 6pair

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d213_s43_t10_6pair_20260524T005010_result.json`
- **Structured JSON:** [`19332aa17e31b0c5c004.json`](../../sessions/19/19332aa17e31b0c5c004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**4 个实验中只有 1 个完成了分析，其余 3 个数据目录不存在：**

| T | α | Seed | PermG_fwd | PermG_rev | Robust_K3 | 状态 |
|---|------|------|-----------|-----------|-----------|------|
| 10 | 0.45 | s43 | 1/6 | 0/6 | 2/6 | ✓ 完成 |
| 10 | 0.50 | s43 | — | — | — | ✗ 目录不存在（仅 s42/s44 有 14b） |
| 10 | 0.60 | s43 | — | — | — | ✗ 目录不存在（仅 s42/s44 有 14b） |
| 10 | 0.75 | s43 | — | — | — | ✗ 目录不存在（`t10_a075_s43_fp32` 是 GPT-2 small） |

**a045 s43 细节**：6 pair 中仅 ece→distinct_1 (3/5: naive+diff+perm) 和 ece→distinct_3 (3/5: naive+diff+ty) 达到 robust consensus。token_entropy 的 3 个 pair 均只有 diff_xcorr 显著。PermG FDR 校正后仅 ece<distinct_1 通过。

**缺失的 3 个 s43 T=10 1.4B 实验尚未训练**，两台服务器（17855、19828）上均无对应目录。需要先训练这些实验才能完成完整的 s43 T=10 6-pair 转换。

---
