# ssh 5090c full sweep and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_full_sweep_and_fill_20260521T141645_result.json`
- **Structured JSON:** [`fd5b18f15a95e6db2d44.json`](../../sessions/fd/fd5b18f15a95e6db2d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部满载。

## Phase 1: 实验状态

| exp_id | GPU | status | key_metrics |
|--------|-----|--------|-------------|
| exp_fewnerd_n16_s123 | cuda:0 | **RUNNING** (84%, ~40min left) | PID 312685, 37648 instances × 16 samples |
| exp_e2_pretrained_conll_s123 | — | **DONE** ✅ | greedy_f1=0.541, oracle_f1=0.629, rho_sj_cond=0.463, verdict=MARGINAL |
| exp_e2_pretrained_conll_s456 | — | **DONE** ✅ | greedy_f1=0.538, oracle_f1=0.627, rho_sj_cond=0.443, verdict=MARGINAL |
| exp_e2_pretrained_fewnerd_s123 | cuda:3 | **RUNNING** | PID 306642, output dir empty (still generating) |

## Phase 3: GPU 填满

| GPU | new_exp | PID |
|-----|---------|-----|
| cuda:1 | exp_e2_pretrained_scierc_s123 (seed=123) | 326918 |
| cuda:2 | exp_e2_pretrained_scierc_s456 (seed=456) | 327084 |

所有 4 GPU 均在工作：
- **GPU 0**: fewnerd_n16_s123 (84%, 快结束)
- **GPU 1**: e2_pretrained_scierc_s123 (刚启动, 551 instances, ~15min 预计)
- **GPU 2**: e2_pretrained_scierc_s456 (刚启动)
- **GPU 3**: e2_pretrained_fewnerd_s123 (运行中, 4706 instances)

两个已完成的 conll 实验已注册 DONE（metrics 已录入 registry）。

---
