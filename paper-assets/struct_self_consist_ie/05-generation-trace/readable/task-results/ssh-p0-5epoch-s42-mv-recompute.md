# ssh p0 5epoch s42 mv recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_5epoch_s42_mv_recompute_20260521T203850_result.json`
- **Structured JSON:** [`f154ac1686de1c97e0dd.json`](../../sessions/f1/f154ac1686de1c97e0dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 recompute 全部完成。

---

## P0: 5-epoch s42 MV recompute
- samples.jsonl: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_s42/samples.jsonl`, 37648 lines
- greedy_f1: **0.7980**
- mv_strict_f1: **0.7935**
- MV Δ (strict): **-0.45pp**
- degeneracy_rate: **25.7%**
- alpha_crit_eff_strict: **0.5369**
- oracle_f1: **0.8781**
- **与 3-epoch 对比**: degeneracy 8.8% → 25.7% (大幅恶化 +16.9pp), MV Δ -2.74pp → -0.45pp (改善，但 degeneracy 飙升导致 MV 仍为负)

## P2: e2_pretrained_s456 MV recompute
- samples.jsonl: `/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd_s456/samples.jsonl`, 37648 lines
- greedy_f1: **0.5373**
- mv_strict_f1: **0.5738**
- MV Δ (strict): **+3.65pp**
- degeneracy_rate: **11.8%**
- alpha_crit_eff_strict: **0.3047**
- oracle_f1: **0.6460**
- 注：pretrained (未 finetune) 模型 greedy 只有 0.54，但 MV 有正向增益 +3.65pp，degeneracy 低

## 5-epoch s123 MV recompute
- samples.jsonl: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_s123/samples.jsonl`, 37648 lines
- greedy_f1: **0.7976**
- mv_strict_f1: **0.7941**
- MV Δ (strict): **-0.35pp**
- degeneracy_rate: **27.1%**
- alpha_crit_eff_strict: **0.5468**
- oracle_f1: **0.8814**
- 与 s42 一致：5-epoch degeneracy ~26-27%，MV Δ 约 -0.4pp

---

**关键发现**: 5-epoch 两个 seed (s42/s123) 表现高度一致——greedy ~0.798, degeneracy ~26-27%, MV Δ 约 -0.4pp。相比 3-epoch (degeneracy 8.8%, MV Δ -2.74pp)，5-epoch greedy 微升但 degeneracy 飙升近 3 倍，说明过拟合导致采样多样性坍塌。MV Δ 的绝对值反而缩小，但这是因为 MV 和 greedy 都在退化（采样输出趋同）。

---
