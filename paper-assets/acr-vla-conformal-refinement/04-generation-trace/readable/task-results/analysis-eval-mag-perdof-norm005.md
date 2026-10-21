# analysis eval mag perdof norm005

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-perdof-norm005_20260515T165447_result.json`
- **Structured JSON:** [`38d9187ebcda51e01bf9.json`](../../sessions/38/38d9187ebcda51e01bf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已正常完成（EXIT_CODE=0），10/10 tasks 全部跑完，无 W&B run。

## eval-mag-perdof-norm005 最终结果

**Benchmark: spatial | Mode: acr_vla | max_correction_norm: 0.05 | CRM: perdof v3-norm**

| Task | Description | SR |
|------|------------|-----|
| T0 | bowl between plate and ramekin → plate | **50%** (5/10) |
| T1 | bowl next to ramekin → plate | **100%** (10/10) |
| T2 | bowl from table center → plate | **0%** (0/10) |
| T3 | bowl on cookie box → plate | **30%** (3/10) |
| T4 | bowl in top drawer → plate | **0%** (0/10) |
| T5 | bowl on ramekin → plate | **0%** (0/10) |
| T6 | bowl next to cookie box → plate | **100%** (10/10) |
| T7 | bowl on stove → plate | **0%** (0/10) |
| T8 | bowl next to plate → plate | **30%** (3/10) |
| T9 | bowl on wooden cabinet → plate | **0%** (0/10) |

**平均 SR: 31.0% (31/100)**

- 正常完成: 10/10 tasks, EXIT_CODE=0
- W&B: 无
- output_file: 命令中 `--output_file` 未生效（JSON 文件不存在）

## Magnitude sweep 汇总（perdof CRM v3-norm, spatial）

| norm | SR | 状态 |
|------|-----|------|
| 0.03 | 30.0% | FINAL |
| **0.05** | **31.0%** | **FINAL** |
| 0.1 | 35.0% | FINAL |
| 0.2 | 28.3% | 6t partial |
| 0.3 | 32.9% | 7t partial |

perdof CRM 在所有 norm 值下表现高度平稳（28-35%），对 correction magnitude 不敏感。

---
