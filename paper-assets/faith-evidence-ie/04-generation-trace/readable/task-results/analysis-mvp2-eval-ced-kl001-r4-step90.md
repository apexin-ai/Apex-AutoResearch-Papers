# analysis mvp2 eval ced kl001 r4 step90

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931_result.json`
- **Structured JSON:** [`3d7a8a18fb9a09950cb3.json`](../../sessions/3d/3d7a8a18fb9a09950cb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step-90 Eval Results
- F1: 0.2108
- Evi-F1: 0.5666
- EDCR: 0.8584
- pred_count: 11160 (unique matched: 7543)
- truncated: 22/985 (2.2%)
- format_ok: 100%

## vs SFT Baseline
- F1: 0.2108 vs 0.4057 (diff: **-19.49 pp**, 52.0% of SFT)
- Evi-F1: 0.5666 vs 0.7979 (diff: **-23.13 pp**)
- EDCR: 0.8584 vs 0.7118 (diff: +14.66 pp)
- pred_count: 11160 vs ~12150 (~-8.1%)
- truncated: 2.2% vs 37.3% (大幅下降)

## vs Other Checkpoints

| ckpt | F1 | Evi-F1 | pred_count | EDCR | truncated |
|------|------|--------|------------|------|-----------|
| 10 | 0.0030 | 0.7200 | 11621 | 0.9983 | 24 (2.4%) |
| 50 | 0.1563 | 0.5643 | 9250 | 0.8858 | 11 (1.1%) |
| **90** | **0.2108** | **0.5666** | **11160** | **0.8584** | **22 (2.2%)** |
| 100 | 0.217* | — | — | — | — |

\* ckpt-100 from prior context, full metrics not in this eval run.

## Conclusion
**negative** — 两个 pass criteria 均不满足：

1. Evi-F1 差异 = -23.13pp（要求 ≥ +2pp）→ **FAIL**
2. F1 = 0.2108 < 0.3557 = SFT_F1 - 5pp → **FAIL**

Step-90 尽管 training reward=1.370 为全程最高，F1 仅为 SFT 的 52%。与 step-100 (F1=0.217) 接近，说明 step 90-100 已进入平台期。全程 trajectory (0.003→0.156→0.211→0.217) 表明模型从灾难性遗忘中部分恢复，但远未达到 SFT 水平。EDCR 高达 0.858（SFT 仅 0.712）佐证了 reward hacking：模型学会了 CED reward 的 shortcut（高 evidence 精度 + 保守预测），而非提升关系抽取能力。

---
