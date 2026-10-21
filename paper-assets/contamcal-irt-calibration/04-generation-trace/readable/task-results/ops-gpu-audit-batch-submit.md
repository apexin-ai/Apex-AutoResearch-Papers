# ops gpu audit batch submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-batch-submit_20260515T032323_result.json`
- **Structured JSON:** [`c3eb58f3c567d05d0e20.json`](../../sessions/c3/c3eb58f3c567d05d0e20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 4 进程已启动（PID 493617，模型加载中）。全部 6 张卡满载。

## GPU 映射 (最新)

| GPU | 显存占用 | PID | 实验 |
|-----|----------|-----|------|
| 0 | 8976/24564 MiB | 477489 | exp_001_eval_3B_d100_v2_aligned_v2 |
| 1 | 6782/24564 MiB | 492660 | exp_001_eval_3B_d000_v2_s123_aligned |
| 2 | 7530/24564 MiB | 492733 | exp_001_eval_3B_d000_v2_s123_para_aligned |
| 3 | 17644/24564 MiB | 466755 | exp_001_sft_d025_3B_v2 |
| 4 | 1302/24564 MiB | 493617 | **exp_001_sft_05B_d025_s123** ← 本次提交 |
| 5 | 17972/24564 MiB | 471296 | exp_001_sft_3B_d100_s123 |

## 本次提交

| exp_id | GPU | 类型 | 说明 |
|--------|-----|------|------|
| exp_001_sft_05B_d025_s123 | cuda:4 | SFT | 0.5B d025 seed=123, lr=2e-4, lora_alpha=32, r=16 |

## 仍然空闲的 GPU
无。6 张卡全部占满。

## 发现
- **0.5B d005 s123 SFT**: ✅ 完成（adapter 35MB, checkpoint-3177）
- **1.5B d100 s123 SFT**: ✅ 完成（adapter 73MB, checkpoint-4159）
- **3B d000 v2 s123 SFT**: ✅ 完成（adapter 119MB, checkpoint-3125）
- **0.5B d005 s123 eval**: ✅ 已完成（eval_results.json 存在）
- **1.5B d100 s123 eval**: ✅ 已完成（eval_results.json 存在）
- **3B d000 v2 s123 eval**: 🏃 已有人提交到 GPU 1（aligned）+ GPU 2（para_aligned），无需重复
- GPU 1/2 的 eval 完成后可释放，届时提交剩余 SFT：**1.5B d005 s123, 1.5B d025 s123, 3B d005 s123**

---
