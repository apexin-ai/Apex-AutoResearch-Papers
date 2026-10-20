# code mf2 practical significance v3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf2_practical_significance_v3_20260522T021536_result.json`
- **Structured JSON:** [`eb30ad2e6693d6bc837d.json`](../../sessions/eb/eb30ad2e6693d6bc837d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF2 完成。结果：

| Benchmark | %C | Spearman ρ | Flip Rate |
|---|---|---|---|
| TruthfulQA | 29.7% | 0.9971 | 2.07% |
| ARC | 26.9% | 0.9962 | 2.31% |
| WinoGrande | 30.3% | 0.9943 | 2.84% |
| GSM8K | 18.9% | 0.9993 | 0.78% |
| HellaSwag | 17.9% | 0.9986 | 1.39% |
| MMLU | 31.3% | 0.9965 | — |

**Mean ρ = 0.9971**，移除 DIF-biased items 后模型排名几乎不变。所有 p 值 ≈ 0。

产出在 `artifacts/mf2_practical_significance/`（`benchmark_rho_summary.csv` + `mf2_report.md`），已注册。

---
