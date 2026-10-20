# ops exp026 exit diagnosis v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026-exit-diagnosis-v2_20260518T111833_result.json`
- **Structured JSON:** [`437dfa607e1f90dda031.json`](../../sessions/43/437dfa607e1f90dda031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_026 诊断结果

**完成状态**: 15/15 runs 全部完成

**退出码**: no_filter=0, binary=0, graduated=0 (全部正常退出)

**GPU 状态**: 3 块 4090D 全部空闲 (0 MiB / 0% utilization)

### 各 Strategy 评估结果 (5 seeds, mean±std)

| Strategy | MMLU | HellaSwag |
|---|---|---|
| no_filter | 0.5899±0.0008 | 0.6600±0.0002 |
| binary | 0.5876±0.0004 | 0.6642±0.0004 |
| graduated_a09 | 0.5900±0.0011 | 0.6599±0.0003 |

**结论: SUCCESS**

三种 filtering strategy 在 MMLU 和 HellaSwag 上差异极小（MMLU 差距 <0.003, HellaSwag 差距 <0.005），std 也很低，说明结果稳定。binary filtering 在 HellaSwag 上略优 (+0.004)，但 MMLU 略低 (-0.002)；graduated 与 no_filter 几乎无差异。

---
