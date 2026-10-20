# analysis read exp016 and seed123 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_read_exp016_and_seed123_results_20260514T122622_result.json`
- **Structured JSON:** [`70f9cea726558515cf82.json`](../../sessions/70/70f9cea726558515cf82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 已更新。汇总如下：

---

## 汇总

### exp-016 (Signal Ensemble, autodl-5090) — DONE

**NER** (n=529):
| 指标 | 值 |
|---|---|
| SJ↔logprob 相关 | r=0.567, ρ=0.538 |
| 最优线性组合 | SJ+VotConf α=0.3 → ρ=**0.489** |
| Ensemble AUROC | **0.735** (vs best single VotConf 0.700) |
| 系数排名 | VotConf(0.86) > ExactMatch(0.65) > SJ(0.12) > logprob(0.04) > FK(-0.34) |
| Selection F1 | greedy 0.609 > logprob 0.609 > ensemble 0.604 > oracle 0.769 |

**RE** (n=397):
| 指标 | 值 |
|---|---|
| SJ↔logprob 相关 | r=0.417, ρ=0.489 |
| 最优线性组合 | VotConf+logprob α=0.6 → ρ=**0.429** |
| Ensemble AUROC | **0.719** (vs best single VotConf 0.721) |
| Selection F1 | logprob 0.397 > greedy 0.374 > oracle 0.561 |

关键发现：Ensemble 在 NER 上 AUROC 提升 ~3.5pp，但 **Selection F1 未超过 greedy**。RE 上 Ensemble AUROC 甚至不如单 VotConf。

---

### exp-001 三 seed 对比 (gpu-5090-4x-2) — 全部 DONE, verdict=FAIL

| Seed | NER ρ_sj (cond) | NER advantage | RE ρ_sj (cond) | RE advantage |
|------|----------------|--------------|---------------|-------------|
| 42 (原始) | — | — | — | — |
| **123** | **0.427** | +0.128 | **0.400** | +0.029 |
| **456** | 0.339 | +0.072 | 0.353 | +0.048 |

seed=123 的 NER ρ_sj 最高 (0.427)，RE ρ_sj 刚好触及 0.40 门槛但整体 joint verdict 仍 FAIL。seed=456 数值明显低于 seed=123。

---

### exp-008 (RE N=16, seed=42) — DONE, verdict=FAIL

NER ρ_sj_cond=0.360, RE ρ_sj_cond=**0.398** (接近但未达 0.40)。RE SJ 仅比 FK 高 0.01，几乎无优势。

---

### seed=456 和 exp-008 进度

均已完成（200 samples, report.json 存在），已更新 registry 为 DONE。

---
