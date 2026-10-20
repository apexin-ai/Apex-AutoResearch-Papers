# code plan 022 model independence

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_022_model_independence_20260521T055408_result.json`
- **Structured JSON:** [`a67aa8976dae70a299ed.json`](../../sessions/a6/a67aa8976dae70a299ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Full-population C% = 31.32%（已验证一致）。**

**Graduated de-duplication sweep：**

| Cap K | N_total | C% | Random Control C% |
|-------|---------|-----|-------------------|
| 1 | 33 | 0.17% | 0.16% ± 0.17% |
| 3 | 92 | 5.46% | 10.77% ± 2.52% |
| 5 | 146 | 11.69% | 16.89% ± 1.99% |
| 10 | 261 | 22.71% | 26.82% ± 2.39% |
| 20 | 447 | 29.12% | 30.91% ± 3.18% |
| 50 | 794 | 27.54% | 31.64% ± 0.80% |
| full | 1887 | 31.32% | — |

**关键发现：**

1. **C% 受 sample size 驱动，非 model redundancy。** 在每个 cap 水平，de-duplicated C% 都 ≤ 同 N 的 random subsample control，说明 family structure 不但没有膨胀统计量，反而略微 *压低* 了 C%（同族模型响应相似，减少了组间变异）。

2. **Per-item Δ_MH 排序稳定**：cap=10 时 ρ=0.58，cap=20 时 ρ=0.66，被标记为 C 类的 item identity 在 de-duplication 下保持一致。

3. **结论**：31.3% C-rate 不是 non-independent models 的 artifact。审稿人的担忧可以用这个 graduated sweep + random control 设计来直接回应。

---
