# ssh check s456 completion and recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_s456_completion_and_recompute_20260521T190118_result.json`
- **Structured JSON:** [`c434618729698d536a9f.json`](../../sessions/c4/c434618729698d536a9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## e2_pretrained_fewnerd_s456 结果

| 指标 | 值 |
|------|-----|
| **greedy_f1** | 0.5373 |
| **mv_strict_f1** | 0.5738 |
| **mv_incl_f1** | 0.5611 |
| **oracle_f1** | 0.6460 |
| **mv_delta_strict_pp** | **+3.65pp** |
| **degeneracy_rate** | 11.8% |
| **alpha_crit_eff (strict)** | 0.3047 |
| **mv_capture_rate** | (0.5738 - 0.5373) / (0.6460 - 0.5373) = **33.6%** |
| **gold_nonempty** | 32565 ✓ |

### 三 seed 对比

| seed | greedy_f1 | mv_strict_f1 | Δ (pp) | degen | capture_rate |
|------|-----------|-------------|--------|-------|-------------|
| 42 | 0.5384 | 0.5788 | +4.03 | 12.2% | 37.6% |
| 123 | 0.5381 | 0.5783 | +4.02 | 11.2% | 36.8% |
| **456** | **0.5373** | **0.5738** | **+3.65** | **11.8%** | **33.6%** |

s456 的 MV gain 略低于其他两个 seed（+3.65 vs ~+4.0pp），greedy baseline 也略低。三 seed 均值：Δ_strict ≈ +3.90pp，degen ≈ 11.7%。

---
