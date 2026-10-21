# ssh comprehensive harvest

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_comprehensive_harvest_20260522T061526_result.json`
- **Structured JSON:** [`a0d4f6e3d17b904a8730.json`](../../sessions/a0/a0d4f6e3d17b904a8730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/full_results_harvest_20260522.md`。

---

## 汇总

### Part 1: nvidia-smi
- **autodl-5090**: 4× RTX 5090 全部空闲
- **autodl-5090-c**: GPU 0/1/3 繁忙 (~80% util, ~30GB), GPU 2 空闲

### Part 2: Finetuned N-scaling (seed=42, unified baseline)

**SciERC** (LP baseline = 63.48%):

| N | Greedy | MV strict | MV Δ | LP-best | LP Δ | Degen% | Oracle |
|---|--------|-----------|------|---------|------|--------|--------|
| 8 | 66.83 | 65.58 | −1.24 | 66.51 | +3.03 | 13.4 | 78.40 |
| 16 | 66.51 | 66.22 | −0.29 | 66.35 | +2.87 | 7.6 | 81.79 |
| 32 | 66.29 | 67.06 | +0.78 | 67.08 | +3.60 | 3.6 | 83.99 |
| 64 | 66.73 | 67.35 | +0.63 | 67.12 | +3.64 | 2.1 | 86.26 |

**CoNLL** (LP baseline = 88.63%):

| N | Greedy | MV strict | MV Δ | LP-best | LP Δ | Degen% | Oracle |
|---|--------|-----------|------|---------|------|--------|--------|
| 8 | 91.23 | 91.01 | −0.22 | 89.81 | +1.18 | 60.1 | 95.38 |
| 16 | 91.28 | 91.48 | +0.19 | 89.18 | +0.55 | 49.7 | 96.36 |
| 32 | 91.20 | 91.66 | +0.46 | 89.23 | +0.60 | 40.5 | 96.90 |
| 64 | 91.20 | 91.84 | +0.64 | 88.89 | +0.26 | 30.6 | 97.51 |

### Part 3: N=32 multi-seed

**SciERC** — mean MV Δ = +0.24pp (不稳定):

| Seed | MV Δ(pp) | Greedy | Degen% |
|------|----------|--------|--------|
| 42 | +0.78 | 66.29 | 3.6 |
| 123 | +0.12 | 66.63 | 5.1 |
| 456 | −0.17 | 66.61 | 4.0 |

**CoNLL** (seed 456 缺失):

| Seed | MV Δ(pp) | Greedy | Degen% |
|------|----------|--------|--------|
| 42 | +0.46 | 91.20 | 40.5 |
| 123 | +0.55 | 91.23 | 37.9 |

### Part 4: Pretrained N-scaling

**SciERC pretrained** — MV 增益大且稳定:

| N | Greedy | MV strict | MV Δ | Degen% | Oracle |
|---|--------|-----------|------|--------|--------|
| 8 | 24.75 | 26.18 | +1.43 | 0.9 | 39.51 |
| 16 | 24.86 | 26.28 | +1.42 | 0.8 | 43.23 |
| 32 | 24.46 | 26.43 | +1.97 | 0.2 | 47.29 |

**CoNLL pretrained** — MV Δ 约 +3pp:

| N | Greedy | MV strict | MV Δ | Degen% | Oracle |
|---|--------|-----------|------|--------|--------|
| 8 | 60.07 | 63.08 | +3.01 | 36.4 | 70.26 |
| 32 | 59.75 | 62.96 | +3.21 | 18.8 | 74.93 |

### 缺失实验
- scierc/conll pretrained N=64: 空目录未完成
- conll pretrained N=16: 无数据
- conll N=32 seed 456: 未找到
- fewnerd pretrained N=16/32: 空目录

---
