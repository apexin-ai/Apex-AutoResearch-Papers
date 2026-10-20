# ssh p0 5epoch s456 recompute and progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_5epoch_s456_recompute_and_progress_20260521T211909_result.json`
- **Structured JSON:** [`28e5d6cb72858f25ec94.json`](../../sessions/28/28e5d6cb72858f25ec94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Recompute 完成。

## P0: 5-epoch s456 MV recompute

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.7978 |
| mv_strict_f1 | 0.7950 |
| MV Δ (pp) | -0.28pp |
| degeneracy_rate | 25.9% |
| alpha_crit_eff_strict | 0.8903 |
| oracle_f1 | 0.8793 |

## 5-epoch 3-seed summary

| seed | greedy_f1 | mv_strict_f1 | MV Δ | degen | α_crit_eff |
|------|-----------|-------------|-------|-------|------------|
| s42 | 0.7980 | 0.7935 | -0.45pp | 25.7% | 0.5369 |
| s123 | 0.7976 | 0.7941 | -0.35pp | 27.1% | 0.5468 |
| s456 | 0.7978 | 0.7950 | -0.28pp | 25.9% | 0.8903 |
| **Mean±Std** | **0.7978±0.0002** | **0.7942±0.0008** | **-0.36±0.09pp** | **26.2±0.7%** | **0.6580±0.2039** |

注意：s456 的 α_crit_eff_strict (0.8903) 远高于 s42/s123 (~0.54)，差异显著。可能需要核实 s42/s123 的 α_crit 是否用了相同版本的 recompute 脚本（v4 strict >N/2 vs 旧版本）。

## P4: 5090-c GPU 进度

| GPU | 实验 | PID | 运行时间 | 状态 | 进度 |
|-----|------|-----|---------|------|------|
| cuda:0 | 5-epoch s456 (完成) | — | — | 空闲 | ✅ |
| cuda:1 | mf4v2_s123_v3 | 357394 | 1h35m | 运行中 (89% GPU) | 目录空，尚未写出 samples.jsonl |
| cuda:2 | mf4v2_s456_v3 | 357662 | 1h35m | 运行中 (84% GPU) | 目录空，尚未写出 samples.jsonl |
| cuda:3 | pretrained_s42_v2 | 346388 | 3h07m | 运行中 (81% GPU) | 目录空，尚未写出 samples.jsonl |

三个推理任务都在正常运行，GPU 利用率 80%+。输出目录已创建但 samples.jsonl 尚未写入（可能是写完后一次性输出，或进度还较早）。

---
