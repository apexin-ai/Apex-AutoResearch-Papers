# analysis pending experiments cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pending_experiments_cleanup_20260519T002629_result.json`
- **Structured JSON:** [`bb484ca9fe1af145766e.json`](../../sessions/bb/bb484ca9fe1af145766e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验数据已获取。汇总如下：

| exp_id | 当前状态 | conclusion | 建议 | 原因 |
|--------|----------|------------|------|------|
| `dgs_pilot` | PENDING | — | **cancel** | DGS 已降级为 explored heuristic，无结果无执行记录，已被 exp_epoch_dgs_analysis 等替代 |
| `mbr_pilot` | PENDING | — | **cancel** | MBR 标记为全面 negative，连 hypothesis 都未填，未执行 |
| `exp_030_conll_t12` | PREPARING | killed | **archive** | 已有详细 failure_reason（N=8 vs 基准 N=16 不一致），Director 已决定不重跑 |
| `exp_031_fewnerd_t12` | PREPARING | killed | **archive** | 三重不一致已记录（测试集/N/分析管道），Director 已决定不重跑 |
| `hidden_state_probe_conll_v2` | PREPARING | killed | **cancel** | 无 hypothesis、无 failure_reason，早期探索已废弃 |
| `hidden_state_probe_conll_full` | PREPARING | killed | **cancel** | 同上 |

需要执行的更新：
- **cancel (4个)**: dgs_pilot, mbr_pilot, hidden_state_probe_conll_v2, hidden_state_probe_conll_full → status=DONE, conclusion=killed
- **archive (2个)**: exp_030_conll_t12, exp_031_fewnerd_t12 → status=DONE（conclusion=killed 已设置）

是否执行这些更新？

---
