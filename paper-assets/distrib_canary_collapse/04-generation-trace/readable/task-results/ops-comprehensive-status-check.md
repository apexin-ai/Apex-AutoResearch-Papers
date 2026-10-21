# ops comprehensive status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_comprehensive_status_check_20260521T023659_result.json`
- **Structured JSON:** [`23a7be80efa30889792d.json`](../../sessions/23/23a7be80efa30889792d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westd-17855 (6× A100 97GB)

**GPU 状态：**

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 98% | 28.5 / 97.9 GB |
| 1 | 59% | 14.5 / 97.9 GB |
| 2 | 67% | 14.5 / 97.9 GB |
| 3 | 92% | 71.0 / 97.9 GB |
| 4 | 72% | 7.5 / 97.9 GB |
| 5 | 84% | 7.5 / 97.9 GB |

**实验：**

| 实验 | 状态 | 进度 |
|------|------|------|
| alpha_sweep_a046_s42_fp32 | RUNNING | gen 0/10 (baseline, 刚启动) |
| alpha_sweep_a048_s42_fp32 | RUNNING | gen 1/10 (training 95%, 4762/5000 steps) |
| alpha_sweep_a052_s42_fp32 | RUNNING | gen 0/10 (baseline, 刚启动) |
| alpha_sweep_a070_s42_fp32 | RUNNING | gen 3/10 (generating synthetic data) |
| t20_a025_s42_fp32 | RUNNING | gen 15/20 (generating synthetic data), 16 gen dirs |
| scale_69b_a100_s43_bf16 | RUNNING | gen 3/10 (generating synthetic data) |

**C4 Monte Carlo：** RUNNING — scenario 4/12, elapsed ~14.7min

**Conditional Granger v2 JSON：** NOT FOUND

---

### westd-19828 (2× A100 97GB)

**GPU 状态：**

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 空闲 |
| 1 | 97% | 24.3 / 97.9 GB |

**实验：**

| 实验 | 状态 | 进度 |
|------|------|------|
| generalize_pythia1b_c4_a100_s43_v2 | RUNNING | gen 6/10 (training ~33-43%, 7 gen dirs) |
| scale_14b_a050_s42_bf16 | NOT FOUND | 无日志、无 gen 目录 |

---

**要点：** 17855 全部 6 卡满载跑 6 个实验；19828 仅 GPU1 在跑 pythia1b C4 泛化实验，GPU0 完全空闲。14b 实验未部署。

---
