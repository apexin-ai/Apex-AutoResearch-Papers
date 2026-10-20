# run fewnerd t ablation collect and next

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fewnerd_t_ablation_collect_and_next_20260521T004210_result.json`
- **Structured JSON:** [`362d4688f4c065822716.json`](../../sessions/36/362d4688f4c065822716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。4 GPU 均已加载模型（~30GB 显存各），开始推理。

---

**Phase 1 汇总 — seed=42 FewNERD T-ablation 结果：**

| Metric | T=0.5 | T=0.8 | T=1.2 |
|--------|-------|-------|-------|
| greedy_f1 | 0.788 | 0.788 | 0.789 |
| oracle_f1 | 0.857 | 0.875 | 0.875 |
| oracle_headroom | 6.85% | 8.66% | 8.62% |
| degeneracy_rate | 14.6% | 19.0% | 28.2% |
| rho_SJ_F1 (full) | **0.267** | 0.206 | 0.136 |
| rho_SJ_F1 (cond) | **0.299** | 0.225 | 0.213 |
| rho_advantage (SJ−Fleiss) | 0.044 | **0.102** | 0.076 |
| logprob_baseline rho | 0.356 | 0.232 | 0.103 |

**Phase 2 — 已启动 4 个新实验（autodl-5090-b）：**

| 实验 | GPU | Seed | T | ETA |
|------|-----|------|---|-----|
| exp_fewnerd_t05_s123 | cuda:0 | 123 | 0.5 | ~18min |
| exp_fewnerd_t08_s123 | cuda:1 | 123 | 0.8 | ~18min |
| exp_fewnerd_t12_s123 | cuda:2 | 123 | 1.2 | ~18min |
| exp_fewnerd_t08_s456 | cuda:3 | 456 | 0.8 | ~18min |

---
