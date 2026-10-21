# code exp45 multiseed n10

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp45_multiseed_n10_20260522T083802_result.json`
- **Structured JSON:** [`f9fa165606ecc04fa9df.json`](../../sessions/f9/f9fa165606ecc04fa9df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。**三 seed N=10 汇总：**

| Metric | Seed 42 | Seed 123 | Seed 456 | Mean ± Std |
|--------|---------|----------|----------|------------|
| WC FPR | 0.000 | 0.000 | 0.000 | **0.000 ± 0.000** |
| IID F1 | 1.000 | 1.000 | 1.000 | **1.000 ± 0.000** |
| DD F1 | 1.000 | 1.000 | 1.000 | **1.000 ± 0.000** |
| AA F1 | 1.000 | 0.971 | 0.971 | **0.981 ± 0.016** |
| FITD F1 | 1.000 | 1.000 | 1.000 | **1.000 ± 0.000** |

结论：N=10 结果 multi-seed 稳健。FPR 三个 seed 均为 0%，DD/FITD F1 均为完美 1.0。唯一的微小波动在 AA F1（seed 123/456 各漏检 3 个 ActorAttack 样本，AA recall=96.25%），但 F1 仍 >0.97。

产出文件：
- 服务器：`results/exp45_benign_n10_seed{123,456}.json` + `results/exp45_benign_n10_multiseed_summary.json`
- 本地 artifact：`art_20260522_29ae86`

---
