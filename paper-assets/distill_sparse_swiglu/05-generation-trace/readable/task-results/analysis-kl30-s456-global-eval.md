# analysis kl30 s456 global eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl30_s456_global_eval_20260517T141851_result.json`
- **Structured JSON:** [`4d5f404f89fa8705325a.json`](../../sessions/4d/4d5f404f89fa8705325a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的 registry 已全部更新。摘要如下：

## kl30 Global (30% sparsity) — 3-seed 对比

| Metric | s42 | s123 | **s456** |
|---|---|---|---|
| MMLU | 0.2527 | 0.3807 | **0.4382** |
| PPL | — | — | **8.93** |
| ARC-C | — | — | **0.4633** |
| WinoGrande | — | — | **0.7111** |
| GSM8K | — | — | **0.0758** |

s456 的 MMLU=0.4382 远高于 s42 (0.2527) 和 s123 (0.3807)。30% global allocation 下三个 seed 的 MMLU 方差极大（range 0.186），表明该配置下 seed sensitivity 是一个严重问题。

## kl50 Global (50% sparsity) — 3-seed 对比

| Metric | s42 | s123 | **s456** |
|---|---|---|---|
| MMLU | 0.2789 | 0.2752 | **0.2794** |
| PPL | — | — | **11.81** |
| ARC-C | — | — | **0.3319** |
| WinoGrande | — | — | **0.6488** |
| GSM8K | — | — | **0.0212** |

s456 的 MMLU=0.2794 与 s42 (0.2789) 和 s123 (0.2752) 高度一致（range 仅 0.004）。50% global allocation 的 seed variance 极小，结果稳定。

## 关键发现

- **50% global**: seed variance 可忽略 (MMLU std ~0.002)，三个 seed 收敛到相近水平
- **30% global**: seed variance 异常大 (MMLU range 0.186)，s456 甚至比 s42 高 18.5 个百分点。这对论文中 30% 配置的可信度构成挑战，可能需要讨论或额外分析

---
