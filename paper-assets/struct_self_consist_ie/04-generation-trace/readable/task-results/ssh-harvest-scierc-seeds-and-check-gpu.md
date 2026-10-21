# ssh harvest scierc seeds and check gpu

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_scierc_seeds_and_check_gpu_20260522T113747_result.json`
- **Structured JSON:** [`4214138de7ad6de9f390.json`](../../sessions/42/4214138de7ad6de9f390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are all results.

---

## Task 1: SciERC Seed Experiment Results

### exp_scierc_n8_s123 (seed=123)

| Metric | Value |
|--------|-------|
| greedy_f1 | 0.6613143027059174 |
| oracle_f1 | 0.779398630544805 |
| oracle_headroom | 0.11808432783888756 |
| fleiss_kappa_mean | 0.3847084061790966 |
| soft_jaccard_mean | 0.6978851614644095 |
| sample_f1_mean | 0.6100783062719641 |
| sample_f1_pct_zero | 12.38% |
| structural_beats_surface | true |
| rho_advantage (soft_jaccard − fleiss) | 0.11861520862736091 |
| verdict | MARGINAL |

**QE signal correlations (full / conditional):**
- soft_jaccard vs f1: ρ=0.3776 / ρ=0.3031
- fleiss vs f1: ρ=0.2590 / ρ=0.1686

**Logprob baseline (full / conditional):**
- ρ=0.2245 / ρ=0.1461
- AUROC=0.5839 / AUROC=0.5455

### exp_scierc_n8_s456 (seed=456)

| Metric | Value |
|--------|-------|
| greedy_f1 | 0.6656751933372993 |
| oracle_f1 | 0.7733095025320226 |
| oracle_headroom | 0.10763430919472328 |
| fleiss_kappa_mean | 0.3863805377206285 |
| soft_jaccard_mean | 0.6939011351696471 |
| sample_f1_mean | 0.6055179678981888 |
| sample_f1_pct_zero | 12.88% |
| structural_beats_surface | true |
| rho_advantage | 0.10038657925575883 |
| verdict | MARGINAL |

**QE signal correlations (full / conditional):**
- soft_jaccard vs f1: ρ=0.3795 / ρ=0.3379
- fleiss vs f1: ρ=0.2791 / ρ=0.1846

**Logprob baseline (full / conditional):**
- ρ=0.2269 / ρ=0.1741
- AUROC=0.5869 / AUROC=0.5587

**Note:** `report.json` does not contain `mv_strict_f1`, `mv_delta_strict_pp`, `degeneracy_rate`, or `lp_selection_f1`. These metrics may require a separate MV analysis step that hasn't run yet.

### Cross-seed stability (seed 123 vs 456)

| Metric | s123 | s456 | Δ |
|--------|------|------|---|
| greedy_f1 | 0.6613 | 0.6657 | +0.0044 |
| oracle_f1 | 0.7794 | 0.7733 | −0.0061 |
| soft_jaccard ρ (full) | 0.3776 | 0.3795 | +0.0019 |
| logprob ρ (full) | 0.2245 | 0.2269 | +0.0024 |

Very tight across seeds — reproducible.

---

## Task 2: GPU Status

| GPU | Status | Memory | Util | Process |
|-----|--------|--------|------|---------|
| cuda:0 | **FREE** | 2MiB / 32607MiB | 0% | — |
| cuda:1 | **FREE** | 2MiB / 32607MiB | 0% | — |
| cuda:2 | BUSY | 30192MiB / 32607MiB | 90% | VLLM::EngineCore (PID 136811) |
| cuda:3 | BUSY | 30234MiB / 32607MiB | 86% | VLLM::EngineCore (PID 138176) |

cuda:0 and cuda:1 are free.

---

## Task 3: 5-Epoch LP Experiment (exp_fewnerd_5epoch_lp_s42)

- **PID 137895**: running, elapsed **21:58**
- **Progress**: 51744 / 301184 prompts = **17.2%**
- **Speed**: ~7068 toks/s input, ~3764 toks/s output
- **ETA**: ~1h38m–2h30m remaining (fluctuating)
- Using vLLM engine on cuda:3 (PID 138176) — also has a vLLM engine on cuda:2 (PID 136811), likely the same experiment using 2 GPUs

---
