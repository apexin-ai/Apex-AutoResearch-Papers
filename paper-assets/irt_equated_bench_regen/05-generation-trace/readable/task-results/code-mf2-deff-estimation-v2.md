# code mf2 deff estimation v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf2_deff_estimation_v2_20260522T105423_result.json`
- **Structured JSON:** [`3a2188474c7e29e128cd.json`](../../sessions/3a/3a2188474c7e29e128cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF2 完成。核心结果：

| 指标 | 值 |
|------|-----|
| Valid models / families | 2118 / 45 |
| m̄_weighted | 230.53 |
| Mean ICC | 0.0415 |
| **Global DEFF** | **10.54** |
| Effective N | 201 (from 2118) |
| Original C% | 31.3% (3918 items) |
| **Adjusted C%** | **17.5% (2183 items)** |
| C→A reclassified | 1735 |
| B→A reclassified | 2151 |

DEFF 高于 reviewer 预期的 3-5，原因是 family size 极度不均（mistral=547, llama-3=315, median=15），加权 m̄ = Σ(n_f²)/Σ(n_f) = 230.53 远大于简单均值 47。ICC 本身很低（mean=0.04），但乘上大 m̄ 后 DEFF 仍达 10.54。

56% 的 C 类 items 在校正后仍为 C，说明这些 item 的 DIF 信号足够强，即使考虑 family clustering 也显著。

输出位于 `artifacts/mf2_deff_estimation/`：脚本、per-item CSV、summary report。

---
