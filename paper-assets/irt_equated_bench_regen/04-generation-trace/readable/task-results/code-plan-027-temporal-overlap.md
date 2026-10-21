# code plan 027 temporal overlap

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_027_temporal_overlap_20260521T082014_result.json`
- **Structured JSON:** [`b2fe614a38648b4915f9.json`](../../sessions/b2/b2fe614a38648b4915f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Part 1 — 分布统计**
- 2023 (N=1080): mean=0.5814, SD=0.1405
- 2024 (N=807): mean=0.6068, SD=0.1556
- Cohen's d = −0.17, overlap coefficient = 0.764, Bhattacharyya = 0.961

**Part 2 — Restricted C%**

| Restriction | N_ref | N_foc | Cohen's d | C% |
|---|---|---|---|---|
| Full population | 1080 | 807 | −0.173 | 31.3 |
| Score-range overlap | 1080 | 787 | −0.149 | 30.9 |
| 1:1 NN matching (mean of 5 seeds) | 638 | 638 | −0.010 | 28.9 |

NN matching 将 d 降至 ≈0，C% 仅从 31.3% 降至 28.9%（相对降 7.7%）。能力混淆最多解释 ~2.4 个百分点。

**Part 3 — 与 Llama-2 vs 3 对比**
- Llama: d=−0.99, overlap=0.18, full C%=61.3% → matched C%=28.3% (降 54%)
- Temporal: d=−0.17, overlap=0.76, full C%=31.3% → matched C%=28.9% (降 7.7%)

Temporal cohort 的能力差异比 Llama 小 5.7×，matching 后 C% 几乎不变，确认 31.3% 的 temporal DIF 是真实的 item-level 差异，而非 ability confound。

---
