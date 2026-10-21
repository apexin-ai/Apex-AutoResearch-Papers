# ssh collect westd 41718 results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_westd_41718_results_20260520T132333_result.json`
- **Structured JSON:** [`8dfff115470ddb7e2ec6.json`](../../sessions/8d/8dfff115470ddb7e2ec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 实验结果汇总

### GPU 状态

| GPU | 型号 | 温度 | 功耗 | 显存 | 利用率 | 进程 |
|-----|------|------|------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 29°C | 33W/600W | 0/97GB | 0% | 空闲 |
| 1 | RTX PRO 6000 Blackwell | 79°C | 601W/600W | 64/97GB | 100% | PID 254228 |

Python 进程仅 PID 254228 (c4_ood_downstream_kl30)。

---

### 1. BCE+STE (PID 249688) — **已完成** ✓

配置：checkpoint=`bce_ste_s42`, sparsity_target=0.5, allocation=uniform

| 指标 | 值 |
|------|-----|
| **model_level_sparsity** | 0.495 |
| **PPL (WikiText-2)** | 60.54 |
| **ARC-c (acc_norm)** | 0.2321 |
| **WinoGrande (acc)** | 0.5185 |
| **MMLU (acc)** | 0.2898 |
| **GSM8K (exact_match)** | 0.0182 |
| **HellaSwag (acc_norm)** | 0.3446 |
| **PIQA (acc_norm)** | 0.6273 |

完成时间：2026-05-20 19:53:20，耗时 4297.5s (~72min)

---

### 2. C4 OOD Downstream KL30 (PID 254228) — **运行中** ⏳

配置：checkpoint=`kl_sparsity30_s42_v3`, sparsity_target=0.3, allocation=uniform, calibration=c4

| 信息 | 值 |
|------|-----|
| **model_level_sparsity** | 0.295 |
| **当前进度** | 20% (8145/40168 loglikelihood requests) |
| **速度** | ~20.47 it/s |
| **预计剩余** | ~26 min |
| **已完成任务** | arc_challenge (样本已加载) |
| **待完成** | winogrande, mmlu, gsm8k, hellaswag, piqa 的 loglikelihood 评估中 |

此实验无 PPL 评估。之前独立跑的 C4 OOD PPL 结果 (`c4_ood_ppl.json`)：

| 模型 | C4 OOD PPL |
|------|-----------|
| Dense | 9.21 |
| KL predictor 50% | 18.40 |
| TEAL vanilla 50% | 38.75 |

---
