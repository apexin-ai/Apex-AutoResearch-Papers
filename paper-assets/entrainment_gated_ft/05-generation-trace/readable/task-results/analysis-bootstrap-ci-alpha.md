# analysis bootstrap ci alpha

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-alpha_20260521T130458_result.json`
- **Structured JSON:** [`981623209c0c680a15fc.json`](../../sessions/98/981623209c0c680a15fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 benchmarks × 5 ratios = 20 组 bootstrap 95% CI 全部计算完毕，结果摘要：

| Benchmark | α 范围 | CI 宽度 |
|-----------|--------|---------|
| **PIQA** (n=1838) | 0.132–0.143 | ~0.031 |
| **HellaSwag** (n=10042) | 0.146–0.150 | ~0.014 |
| **ARC-Easy** (n=2376) | 0.201–0.226 | ~0.032 |
| **LAMBADA** (n=5153) | 0.294–0.316 | ~0.025 |

关键观察：α 在不同 attention ratio 之间变化很小（各 benchmark 内 CI 大量重叠），说明 ambiguity 主要是 benchmark-driven 而非 architecture-driven。LAMBADA 的 α 最高（~30%），HellaSwag 的 CI 最窄（得益于 10K 样本量）。

Artifact 已注册：`art_20260521_31b294`。

---
