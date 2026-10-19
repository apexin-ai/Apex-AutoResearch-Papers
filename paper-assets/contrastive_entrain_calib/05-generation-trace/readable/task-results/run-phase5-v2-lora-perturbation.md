# run phase5 v2 lora perturbation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase5_v2_lora_perturbation_20260518T102024_result.json`
- **Structured JSON:** [`b52ebd0adccf8baef638.json`](../../sessions/b5/b52ebd0adccf8baef638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 5 Robustness Report

| 指标 | 值 |
|---|---|
| **Original AUROC** | 0.9985 |
| **Perturbed AUROC** | 0.9941 |
| **Delta** | 0.0044 (< 0.05 threshold) |
| **Verdict** | **ROBUST** |
| **Polarity Reversed** | false |
| **Best Layer (perturbed)** | 24 |
| **LoRA Rank** | 16 |
| **Samples** | 640 |

**关键观察**：
- AUROC 仅下降 0.0044，远低于 0.05 阈值
- 无极性反转
- Layer 16-35 在扰动后全部保持 AUROC > 0.985，高层方向高度稳定
- 最佳层从原始的 Layer 27 微移至 Layer 24（AUROC 差异仅 0.001），属于正常波动
- Layer 0 扰动后 AUROC = 0.6927，与原始 0.6897 基本一致

**结论**：Sycophancy direction 在随机 LoRA 扰动下具有鲁棒性，确认其捕获的是模型的稳定内部特征而非权重值的偶然产物。Go/No-Go 通过。

---
