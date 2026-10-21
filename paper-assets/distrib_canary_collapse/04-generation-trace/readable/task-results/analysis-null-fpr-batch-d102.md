# analysis null fpr batch d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_fpr_batch_d102_20260524T061916_result.json`
- **Structured JSON:** [`488eddc2122453cc4371.json`](../../sessions/48/488eddc2122453cc4371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## Null FPR D102 分析结果（α=0.00, pythia-410m, T=10）

| Seed | PermG fwd | PermG rev | Robust K≥3 |
|------|-----------|-----------|------------|
| s46  | 0/6       | 0/6       | 1/6        |
| s48  | 0/6       | 0/6       | 0/6        |
| s49  | 0/6       | 0/6       | 0/6        |
| s50  | **2/6**   | 0/6       | **2/6**    |

**Pooled PermG forward FPR**: 2/24 = 8.3%（仅 s50 贡献，token_entropy→distinct_1 和 token_entropy→distinct_2 各 3/5 votes）

**Pooled Robust K≥3 FPR**: 3/24 = 12.5%

s50 是异常值——两对 token_entropy→distinct_{1,2} 在 perm+ty+naive 三法一致显著，可能值得进一步审视。

## gpt2m 进度
- s42: gen_0–gen_7（8/11）
- s43: gen_0–gen_7（8/11）
- 仍在训练中

## 已完成
- 4 个 JSON 已保存到本地 artifacts/
- 4 个 artifact 已 register
- Registry 4 条已更新为 DONE(success)

---
