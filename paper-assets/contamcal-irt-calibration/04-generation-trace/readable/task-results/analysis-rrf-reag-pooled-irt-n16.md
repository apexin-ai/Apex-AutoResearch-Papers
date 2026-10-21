# analysis rrf reag pooled irt n16

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rrf_reag_pooled_irt_n16_20260516T153922_result.json`
- **Structured JSON:** [`de16b357463f3e32dddb.json`](../../sessions/de/de16b357463f3e32dddb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册 (`art_20260516_d5cac1`)。

## 完整结果

| Benchmark | N | γ̂ | 95% CI | CI excl. 0 | PPP | ΔMAE | R̂ |
|-----------|---|------|--------|------------|------|------|------|
| MMLU | 16 | 0.6551 | [−0.41, 1.74] | No | 0.192 | 0.0085 | 1.007 |
| ARC | 16 | 0.7269 | [0.02, 1.44] | **Yes** | 0.003 | 0.0136 | 1.007 |
| GSM8K | 24 | 0.0639 | [−0.36, 0.49] | No | 0.541 | 0.1632 | 1.008 |

关键发现：
- **ARC 是唯一 CI 排除零的 benchmark**（γ̂=0.73），contamination signal 统计显著
- **MMLU** γ̂=0.66 但 CI 跨零，方向一致但不显著
- **GSM8K** γ̂≈0，无 contamination signal；ΔMAE=0.163 主要来自 IRT 校准本身（N=24 包含 0.5B 模型，accuracy 跨度大）
- 所有 benchmark 收敛良好：R̂<1.01，ESS>1300，divergences=0

---
