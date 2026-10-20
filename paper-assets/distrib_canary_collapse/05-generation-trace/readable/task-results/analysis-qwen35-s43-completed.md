# analysis qwen35 s43 completed

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen35_s43_completed_20260520T080145_result.json`
- **Structured JSON:** [`6ab04476bfe642df2b18.json`](../../sessions/6a/6ab04476bfe642df2b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## qwen35_08b_wiki_a100_s43_fp32 — 5-Method 分析结果

| 指标 | s43 | s42 (parent) |
|------|-----|-------------|
| PermG_fwd (FDR) | **6/8** | 8/8 |
| PermG_rev (FDR) | **0/8** | 0/8 |
| diff_xcorr (FDR) | **8/8** | 8/8 |
| naive_xcorr | **6/8** | 8/8 |
| threshold_onset | **0/8** | 0/8 |
| TY Granger | **0/8** | 6/8 |
| K≥3 (robust pairs) | **6/8** | 6/8 |
| K≥4 | **0/8** | — |

### 逐 pair 共识

| Pair | s43 votes | s43 methods |
|------|-----------|-------------|
| token_entropy→distinct_1 | 3/5 | naive, diff, perm |
| token_entropy→distinct_2 | 3/5 | naive, diff, perm |
| token_entropy→distinct_3 | 3/5 | naive, diff, perm |
| token_entropy→mauve | 0/5 | — |
| ece→distinct_1 | 3/5 | naive, diff, perm |
| ece→distinct_2 | 3/5 | naive, diff, perm |
| ece→distinct_3 | 3/5 | naive, diff, perm |
| ece→mauve | 0/5 | — |

### 对比总结

- **K≥3 一致**：s42 和 s43 均为 6/8，seed 间稳定
- **PermG_fwd**：s43 = 6/8 vs s42 = 8/8，略低但仍强。s43 两个 mauve pair 未过 PermG
- **TY Granger**：s43 = 0/8（全部 PermFDR=0.923，dmax 波动 0/1），符合 C003 预期——T=11 下 TY 不稳定，不作为支撑证据
- **mauve pairs** 在两个 seed 下都是最弱的，这是一致的模式
- **方向性清晰**：PermG reverse = 0/8，确认因果方向 canary→downstream

---
