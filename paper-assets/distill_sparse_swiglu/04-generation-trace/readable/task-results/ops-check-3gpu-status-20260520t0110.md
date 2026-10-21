# ops check 3gpu status 20260520T0110

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_3gpu_status_20260520T0110_20260520T013543_result.json`
- **Structured JSON:** [`7deffb2400114aa62f77.json`](../../sessions/7d/7deffb2400114aa62f77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. bench_teal50_uniform_gsm8k — ✅ 已完成
- **服务器**: westd-41718 cuda:1（已释放，GPU 空闲 0%）
- **耗时**: ~23 min
- **结果**:

| Metric | Value |
|--------|-------|
| GSM8K exact_match (flexible) | **1.74%** ± 0.36% |
| GSM8K exact_match (strict) | 0.15% ± 0.11% |

8B TEAL 50% uniform 在 GSM8K 上几乎完全崩溃（dense 基线通常 ~50%+）。

---

### 2. qwen14b_kl30_uniform_hspiqa — 🔄 运行中
- **服务器**: westd-41718 cuda:0（GPU 98%, 68.7/97.9 GB）
- **已运行**: 41 min
- **当前进度**: HellaSwag loglikelihood **65%**（26185/40168），12.55 it/s
- **预估剩余**: HellaSwag ~19 min + PIQA ~8 min ≈ **~27 min**

---

### 3. qwen14b_teal30_uniform_hspiqa — 🔄 运行中
- **服务器**: westd-34887 cuda:0（GPU 100%, 40.0/97.9 GB）
- **已运行**: 40 min
- **当前进度**: HellaSwag loglikelihood **63%**（25297/40168），12.47 it/s
- **预估剩余**: HellaSwag ~20 min + PIQA ~8 min ≈ **~28 min**

---
