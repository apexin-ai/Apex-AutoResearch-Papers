# ops check all running status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_running_status_20260521T014054_result.json`
- **Structured JSON:** [`d06495162345cbb68edf.json`](../../sessions/d0/d06495162345cbb68edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### westd-17855 (6x RTX PRO 6000 Blackwell 96GB)

| 实验 | 状态 | 进度 |
|------|------|------|
| `alpha_sweep_a048_s42_fp32` | STILL_RUNNING | Gen 0/10 (baseline training) |
| `t20_a025_s42_fp32` | STILL_RUNNING | Gen 13/20 (generating synthetic data) |
| `alpha_sweep_a070_s42_fp32` | STILL_RUNNING | Gen 0/10 (baseline, saving dataset) |
| `scale_69b_a100_s43_bf16` | STILL_RUNNING | Gen 2/10 (generating synthetic data) |
| `gen_gpt2m_a100_s43` | STILL_RUNNING | Gen 6/10 (training 20%, 1035/5000 steps) |
| `alpha_sweep_a010_s42_bf16` | STILL_RUNNING | Gen 7/10 (generating synthetic data) |

GPU 占用：6 GPU 全部在用（22/15/12/71/15/10 GB），利用率 93/66/0/92/96/45%。GPU2 暂时 0% 可能在生成/评估阶段。

### westd-19828 (2x RTX PRO 6000 Blackwell 96GB)

| 实验 | 状态 | 进度 |
|------|------|------|
| `scale_14b_a050_s42_bf16` | STILL_RUNNING | Gen 5/10 (training 88%, 4381/5000 steps) |
| `generalize_pythia1b_c4_a100_s43_v2` | STILL_RUNNING | Gen 4/10 (training 20%, 983/5000 steps) |

GPU 占用：2 GPU 全部在用（19/24 GB），利用率 95/97%。

### 总结

- **STILL_RUNNING**: 8
- **COMPLETED**: 0
- **FAILED**: 0

所有 8 个实验均在正常运行中。进度最快的是 `t20_a025_s42_fp32`（13/20）和 `alpha_sweep_a010_s42_bf16`（7/10）。两台服务器共 8 GPU，全部满载。

---
