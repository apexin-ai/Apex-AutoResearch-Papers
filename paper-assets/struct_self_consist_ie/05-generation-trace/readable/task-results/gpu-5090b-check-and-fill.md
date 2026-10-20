# gpu 5090b check and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090b_check_and_fill_20260521T081102_result.json`
- **Structured JSON:** [`d900c09c151c4d56100d.json`](../../sessions/d9/d900c09c151c4d56100d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 experiments running:
- **cuda:0**: exp_conll_mf4_v2_s123 — 30GB, 86% util, processing prompts (CoNLL 3453 instances × 8 samples)
- **cuda:1**: exp_conll_mf4_v2_s456 — 30GB, 86% util, processing
- **cuda:2**: exp_fewnerd_mf4_v2_s456 — 30GB, rendering prompts (FewNERD 37648 instances × 8 samples)
- **cuda:3**: idle, no PREPARING/QUEUED experiments available to fill

## 汇报

### 已完成实验（已更新 registry → DONE）

| 实验 | greedy_f1 | oracle_f1 | rho_SJ_full | rho_SJ_cond | verdict |
|------|-----------|-----------|-------------|-------------|---------|
| exp_fewnerd_mf4_v2_s42 (MF4v2) | 0.788 | 0.878 | 0.163 | 0.199 | FAIL |
| exp_fewnerd_t12_s456 (T=1.2) | 0.789 | 0.878 | 0.290 | 0.254 | FAIL |
| exp_fewnerd_n16_s42 (N=16) | 0.789 | 0.906 | 0.211 | 0.212 | FAIL |
| exp_fewnerd_n16_s123 (N=16) | 0.789 | 0.915 | 0.352 | 0.282 | MARGINAL |

### 新启动实验

| GPU | 实验 | Dataset | Config | PID |
|-----|------|---------|--------|-----|
| cuda:0 | exp_conll_mf4_v2_s123 | CoNLL | N=8 T=1.0 s=123 | 334013 |
| cuda:1 | exp_conll_mf4_v2_s456 | CoNLL | N=8 T=1.0 s=456 | 334155 |
| cuda:2 | exp_fewnerd_mf4_v2_s456 | FewNERD | N=8 T=1.0 s=456 | 334423 |
| cuda:3 | — | — | 空闲 | — |

CoNLL 实验约 3453 instances，预计 ~1h 完成；FewNERD 37648 instances，预计 ~3-4h。

---
