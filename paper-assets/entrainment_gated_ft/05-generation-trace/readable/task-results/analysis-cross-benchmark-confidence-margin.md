# analysis cross benchmark confidence margin

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-benchmark-confidence-margin_20260520T140423_result.json`
- **Structured JSON:** [`6b30d16ac01604d9d45f.json`](../../sessions/6b/6b30d16ac01604d9d45f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### Cross-Benchmark Confidence Margin Analysis

**C2 (helped vs stayed-wrong，pure-wrong 内部)** — 全部 6 个条件显著，medium effect：

| Benchmark | Arch | Cohen's d | p |
|-----------|------|-----------|---|
| ARC-Easy | GDN | -0.60 | 1.0e-13 |
| ARC-Easy | RetNet | -0.51 | 5.3e-10 |
| ARC-Easy | HGRN2 | -0.53 | 5.4e-10 |
| HellaSwag | GDN | -0.52 | 1.3e-20 |
| HellaSwag | RetNet | -0.48 | 2.5e-17 |
| HellaSwag | HGRN2 | -0.51 | 6.3e-18 |

Helped 样本的 |loglik| 更低（near-miss wrong），结论一致。

**C1 (hurt vs stayed-right，pure-correct 内部)** — 4/6 显著，effect size 弱于 LAMBADA：

| Benchmark | Arch | Cohen's d | p | Sig? |
|-----------|------|-----------|---|------|
| ARC-Easy | GDN | 0.26 | 3.2e-4 | Yes |
| ARC-Easy | RetNet | 0.22 | 2.8e-3 | Yes |
| ARC-Easy | HGRN2 | 0.13 | 0.145 | **No** |
| HellaSwag | GDN | 0.09 | 0.109 | **No** |
| HellaSwag | RetNet | 0.21 | 1.5e-3 | Yes |
| HellaSwag | HGRN2 | 0.28 | 2.5e-5 | Yes |

**对比 LAMBADA**：LAMBADA 的 C1 d=0.83-0.92、C2 d=0.73-0.77 远强于 MC 任务。MC 任务中 C2 效应稳健（d≈0.5），C1 效应较弱（d≈0.1-0.3），2 个条件不显著。这可能是因为 MC 任务的 confidence proxy（raw loglik of correct option）受选项长度影响，noise 更大；而 LAMBADA 是单 token 预测，confidence 信号更干净。

Artifact 已注册为 `art_20260520_db0c2c`。

---
