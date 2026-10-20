# gpu e2 pretrained fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_e2_pretrained_fill_20260521T105606_result.json`
- **Structured JSON:** [`dd11d0eb41ea38ed502a.json`](../../sessions/dd/dd11d0eb41ea38ed502a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已经存在且已完成，无需重新启动：

**exp_e2_pretrained_conll** — status: DONE, conclusion: **success**
- server: autodl-5090, cuda:2
- wall clock: ~97min (1.62 GPU-hours)

**exp_e2_pretrained_scierc** — status: DONE, conclusion: **negative**
- server: autodl-5090-c, cuda:3
- wall clock: ~112min (1.86 GPU-hours)
- greedy_f1=0.242, oracle_f1=0.389, oracle_headroom=0.147
- rho_SJ_full=0.219, rho_kappa_full=0.252
- verdict: FAIL (>30% samples F1=0, structural_beats_surface=false)

两个实验都已跑完并写入了 registry，不需要重复提交。

---
