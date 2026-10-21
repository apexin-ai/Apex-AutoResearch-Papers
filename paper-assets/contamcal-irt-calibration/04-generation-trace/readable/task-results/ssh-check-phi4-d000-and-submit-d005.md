# ssh check phi4 d000 and submit d005

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-phi4-d000-and-submit-d005_20260519T001817_result.json`
- **Structured JSON:** [`f2faf6347346d6e36205.json`](../../sessions/f2/f2faf6347346d6e36205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## Phi-4 d000 训练状态

| 指标 | 值 |
|------|-----|
| **当前 step** | 1512 / 3125 (48%) |
| **Epoch** | ~0.48 |
| **最近 loss** | 1.09 → 1.24 → 1.17 → 1.14 → 1.19 (step 1470-1510) |
| **Token accuracy** | 72-75% |
| **Learning rate** | 2.85e-05 (正常衰减) |
| **GPU** | cuda:2 (PID 84612), 57884MiB, 93% util |
| **ETA** | ~1h07m |
| **状态** | **正常收敛**，loss 稳定在 1.1-1.25 区间 |

## GPU 占用

| GPU | 进程 | 任务 |
|-----|------|------|
| cuda:0 | PID 84688 | OLMo-2-7B d000 |
| cuda:1 | PID 86378 | gemma-2-9b d025 |
| cuda:2 | PID 84612 | **phi-4 d000** |
| cuda:3 | 空闲 | 0MiB, 0% util |

## d005 提交准备

- 数据文件 `sft_dosage_005.jsonl` 存在 (93MB)
- 输出目录 `phi-4_d005_s42` 不存在，可安全使用
- **cuda:3 空闲，可立即提交**

是否现在提交 Phi-4 d005 到 cuda:3？

---
