# ops westd full eval collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-full-eval-collect_20260515T213655_result.json`
- **Structured JSON:** [`dd24dc97db54a06e7a6d.json`](../../sessions/dd/dd24dc97db54a06e7a6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## N=1319 Full Eval Results (westd)

| Model | N | Accuracy | Stderr | EOS Rate | Avg Len |
|-------|---|----------|--------|----------|---------|
| Standard SFT | 1319 | 59.29% | ±1.35% | 98.03% | 226.7 |
| RASP SFT | 1319 | 61.49% | ±1.34% | 98.26% | 216.5 |

**Δ(RASP - Standard) = +2.20pp, z = 1.154, p-value = 0.248, 95% CI = [-1.53, +5.93]pp**

差异不显著 (p=0.248 > 0.05)，95% CI 跨越零点。

### Cross-server comparison
| Setting | N | Standard | RASP | Δ(RASP-Std) |
|---------|---|----------|------|-------------|
| westb N=100 | 100 | 64% | 57% | -7pp |
| westd N=100 | 100 | 63% | 67% | +4pp |
| **westd N=1319** | **1319** | **59.29%** | **61.49%** | **+2.20pp** |

Full eval 显示 RASP 有微弱优势（+2.2pp），但统计上不显著。N=100 时看到的 ±7pp 波动确认为小样本噪声——full eval 把差异压缩到了 CI 内。

---
