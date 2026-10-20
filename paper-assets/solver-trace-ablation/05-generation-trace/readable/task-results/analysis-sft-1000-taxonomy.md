# analysis sft 1000 taxonomy

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft-1000-taxonomy_20260515T153612_result.json`
- **Structured JSON:** [`33b14f84faee0195ff98.json`](../../sessions/33/33b14f84faee0195ff98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总 JSON 已保存。以下是完整结果。

## SFT 1000-step 3-seed Taxonomy

| | s42 | s43 | s44 | **mean±std** |
|---|---|---|---|---|
| **n_proved / 100** | 13 | 11 | 15 | **13.0±2.0** |
| **Prove Rate** | 13% | 11% | 15% | **13.0±2.0%** |
| H7 (strict) | 0 | 0 | 0 | **0** |
| H1 (strict) | 1 | 1 | 1 | **1.0±0** |
| H8 (conjunction collapse) | 0 | 0 | 0 | **0** |
| **Genuine** | 12 | 10 | 14 | **12.0±2.0** |
| **Genuine Rate** | 92.3% | 90.9% | 93.3% | **92.2±1.2%** |
| Proved-only ISR | 0.568 | 0.635 | 0.589 | **0.597±0.035** |

### 关键发现

**SFT 1000-step 几乎零 hacking：** H7=0（全部 seed），H8=0，每个 seed 仅 1 例 H1（conclusion in premise）。Genuine rate 稳定在 90.9%–93.3%。

### 与 500-step SFT 对比

| | 500-step mean | 1000-step mean | 变化 |
|---|---|---|---|
| Prove Rate | 15.3% | 13.0% | ↓2.3pp |
| Genuine Rate | 91.5% | 92.2% | ↑0.7pp |

PR 略降但 genuine rate 基本持平。1000-step SFT 没有出现 hacking 恶化——与 GRPO 的退化形成鲜明对比。

### 与 GRPO 1000-step 对比

| Method | PR | H7 | Genuine Rate |
|---|---|---|---|
| **SFT 1000-step** (3-seed avg) | 13% | 0 | **92.2%** |
| GRPO exec-only s42 | — | 1 | 7.5% |
| GRPO ISR s42 | — | 87 | 2.2% |
| GRPO Random s42 | — | 97 | 0% |

SFT 在 1000 步训练后 genuine rate 保持 >90%，而所有 GRPO 变体在同样步数下 genuine rate 都崩溃到 <10%。这确认 SFT 不产生 reward hacking，可作为论文的 clean baseline。

---
