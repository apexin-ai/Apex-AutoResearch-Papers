# analysis exp017 3seed completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp017_3seed_completion_20260514T202124_result.json`
- **Structured JSON:** [`ed4651e6ab23f7377799.json`](../../sessions/ed/ed4651e6ab23f7377799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**seed456 5信号评估 (N=16 full ρ)**
| Signal | ρ | AUROC | ECE |
|--------|------|-------|------|
| SJ | 0.455 | 0.729 | 0.113 |
| FK | 0.448 | 0.725 | 0.109 |
| EM | 0.452 | 0.728 | 0.108 |
| voting_conf | 0.457 | 0.735 | 0.086 |
| logprob | 0.308 | 0.761 | 0.129 |

**3-seed 汇总 (full ρ mean±SD)**
| Signal | Mean | SD | CV% |
|--------|------|----|-----|
| SJ | 0.463 | 0.007 | 1.6% |
| FK | 0.455 | 0.006 | 1.3% |
| EM | 0.460 | 0.008 | 1.7% |
| voting_conf | 0.458 | 0.003 | 0.7% |
| logprob | 0.310 | 0.006 | 1.8% |

- structural > surface: **3/3 seeds** (full + conditional)
- CV 全部 <2%，比 Qwen SciERC (CV=6%) 稳定得多
- N-scaling: 结构信号 Δ≈+0.03，logprob 基本不变
- Registry: 三个 seed 全部标记为 DONE/success
- Artifact 已注册: `llama_conll_n16_3seed_5signal_summary`

---
