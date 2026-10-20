# ssh n16 fewnerd 3seed mv recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n16_fewnerd_3seed_mv_recompute_20260521T194140_result.json`
- **Structured JSON:** [`0863466d85c6d79dc7de.json`](../../sessions/08/0863466d85c6d79dc7de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 全部完成。汇总结果：

**注意**：脚本输出显示 `need>=5/8`，说明每个 instance 实际有 8 个 samples（而非 16），请确认是否符合预期。

### 各 seed 结果

| Metric | s42 | s123 | s456 |
|--------|-----|------|------|
| n_instances | 32565 | 32565 | 32565 |
| greedy_f1 | 0.7911 | 0.7916 | 0.7910 |
| mv_strict_f1 | 0.7677 | 0.7798 | 0.7767 |
| oracle_f1 | 0.9077 | 0.9150 | 0.9105 |
| degeneracy_rate | 2.4% | 4.8% | 4.8% |
| alpha_crit_eff_strict | 0.4053 | 0.6715 | 0.4154 |
| capture_rate | -0.201 | -0.095 | -0.120 |

### Mean ± Std (3 seeds)

| Metric | Mean ± Std |
|--------|-----------|
| greedy_f1 | 0.7912 ± 0.0003 |
| mv_strict_f1 | 0.7747 ± 0.0063 |
| oracle_f1 | 0.9111 ± 0.0037 |
| degeneracy_rate | 4.0% ± 1.4% |
| alpha_crit_eff_strict | 0.4974 ± 0.1509 |
| capture_rate | -0.139 ± 0.055 |

capture_rate 全部为负，说明 MV strict 在 FewNERD N=16 上低于 greedy baseline（Δ_SC strict 分别为 -2.34pp、-1.18pp、-1.43pp）。

---
