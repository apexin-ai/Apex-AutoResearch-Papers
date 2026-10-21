# ssh p3 scierc pretrained mv retry

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p3_scierc_pretrained_mv_retry_20260521T205948_result.json`
- **Structured JSON:** [`aa0562b65998aafbcf7f.json`](../../sessions/aa/aa0562b65998aafbcf7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件均已生成。

## SciERC Pretrained MV Recompute — 3-Seed

| seed | greedy_f1 | mv_strict_f1 | MV Δ (pp) | degeneracy | α_crit_eff_strict | n_instances |
|------|-----------|-------------|-----------|------------|-------------------|-------------|
| s42  | 0.2475 | 0.2618 | +1.43 | 0.9% | 0.1520 | 529 |
| s123 | 0.2436 | 0.2548 | +1.12 | 0.6% | 0.1468 | 529 |
| s456 | 0.2436 | 0.2642 | +2.06 | 0.9% | 0.1537 | 529 |
| **Mean±Std** | 0.2449±0.0023 | 0.2603±0.0048 | +1.54±0.48 | 0.8%±0.2% | 0.1508±0.0036 | 529 |

## 产出文件
- s42: `/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc_s42_v2/recompute_mv_results.txt` (894 bytes)
- s123: `/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc_s123/recompute_mv_results.txt` (899 bytes)
- s456: `/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc_s456/recompute_mv_results.txt` (894 bytes)

---
