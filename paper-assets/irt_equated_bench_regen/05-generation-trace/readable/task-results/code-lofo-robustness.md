# code lofo robustness

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lofo_robustness_20260522T071721_result.json`
- **Structured JSON:** [`586fff222ebce9c60f6d.json`](../../sessions/58/586fff222ebce9c60f6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LOFO 分析完成。结果摘要：

| Family | N removed | C% LOFO | ΔC% |
|--------|----------|---------|-----|
| mistral | 547 (51% of ref) | 22.47% | −8.85 |
| llama-3 | 315 (39% of foc) | 24.06% | −7.26 |
| llama-2 | 161 (15% of ref) | 31.48% | +0.16 |
| mixtral | 120 (15% of foc) | 34.26% | +2.93 |
| solar | 91 (11% of foc) | 31.01% | −0.31 |

Full baseline C% = 31.32%（与已知 31.3% 一致）。

**核心发现**：占 cohort ≤15% 的家族移除后 |ΔC%| ≤ 2.93pp，C% 稳定。mistral/llama-3 的大幅下降是 **composition effect**（各自占 cohort >30%），不是 DIF 信号脆弱的证据。

输出已保存到 `artifacts/lofo_robustness/` 并注册。

---
