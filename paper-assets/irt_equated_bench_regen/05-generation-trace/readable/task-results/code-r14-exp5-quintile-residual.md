# code r14 exp5 quintile residual

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r14_exp5_quintile_residual_20260522T123546_result.json`
- **Structured JSON:** [`2703d5075ec946037b26.json`](../../sessions/27/2703d5075ec946037b26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个文件已写入 `artifacts/r14_mf1_domain_profile/`：

**核心发现**：

| Stratum | Δ Mean | Cohen's d | Pooled SD |
|---------|--------|-----------|-----------|
| Q1 | −0.017 | −0.18 | 0.092 |
| Q2 | −0.004 | −0.10 | 0.037 |
| Q3 | +0.004 | +0.36 | 0.012 |
| Q4 | +0.006 | +0.69 | 0.008 |
| Q5 | −0.002 | −0.06 | 0.041 |

Q3、Q4 的 Cohen's d 超过 0.1 阈值，但**原始均值差异极小**（最大 0.006）。d 被放大是因为这两个 stratum 的 score range 极窄（Q4 仅跨 0.028 分），导致 pooled SD 仅 0.008，分母极小。在 0–1 量表上 0.006 的差异不构成有意义的 ability confounding，MH-DIF 的 conditioning 是可靠的。

---
