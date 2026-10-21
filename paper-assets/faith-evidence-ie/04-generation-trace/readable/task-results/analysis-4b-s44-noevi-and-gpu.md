# analysis 4b s44 noevi and gpu

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-s44-noevi-and-gpu_20260523T140431_result.json`
- **Structured JSON:** [`75336883b43ffa05fff1.json`](../../sessions/75/75336883b43ffa05fff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

test_summary.json 已有 metrics，不需要 batch_eval。结果如下：

## 4B s44 no-evi r2 (test_revised)

| metric | value |
|--------|-------|
| ign_f1 | **0.2671** |
| precision | 0.3444 |
| recall | 0.2182 |
| no_evidence | true ✓ |

### 3-seed evidence tax 汇总

| seed | with-evi | no-evi | tax |
|------|----------|--------|-----|
| s42 | 0.2503 | 0.2654 | +1.51pp |
| s43 | 0.2503 | 0.2702 | +1.99pp |
| s44 | 0.2525 | 0.2671 | **+1.46pp** |
| **avg** | **0.2510** | **0.2676** | **+1.66pp** |

Evidence tax 在 3 个 seed 上一致为正（+1.46 ~ +1.99pp），均值 +1.66pp。

## DPO 3ep eval (dev)

| metric | DPO 1ep | DPO 3ep | Δ |
|--------|---------|---------|---|
| ign_f1 | 0.3223 | **0.3076** | **-1.47pp** |
| evi_f1 | — | 0.8484 | |
| evi_f1_joint | — | 0.2451 | |
| edcr | — | 0.7503 | |

DPO 3ep 相比 1ep 下降 1.47pp，过拟合明显。1ep 仍是最优。

## GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 MiB / 97887 MiB | 0% |
| 1 | 50311 MiB / 97887 MiB | 97% |
| 2 | 0 MiB / 97887 MiB | 0% |
| 3 | 0 MiB / 97887 MiB | 0% |

GPU 0/2/3 空闲，GPU 1 有任务在跑。

---
