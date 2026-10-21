# analysis verify ced s45 params

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_ced_s45_params_20260516T001824_result.json`
- **Structured JSON:** [`ce15cc7381e14835e1cf.json`](../../sessions/ce/ce15cc7381e14835e1cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**两个训练的超参数完全一致，无需重启。**

### 关键发现

argparse 中**不存在** `--batch`、`--grad_accum`、`--lr`、`--epochs` 这些参数名（第 254-257 行），只有：
- `--per_device_batch_size` (default=4)
- `--gradient_accumulation_steps` (default=4)
- `--learning_rate` (default=2e-5)
- `--num_epochs` (default=3)

### 实际运行参数对比

s43 的 `ps` 输出显示实际命令**没有传 batch/grad_accum 参数**，全部走默认值：

| 参数 | s43 (默认值) | s45 (显式传入) |
|------|-------------|---------------|
| per_device_batch_size | **4** | 4 |
| gradient_accumulation_steps | **4** | 4 |
| effective batch size | **16** | 16 |
| learning_rate | **2e-5** | 2e-5 |
| num_epochs | **3** | 3 |
| lora_rank | **64** | 64 |
| lora_alpha | **128** | 128 |
| bf16 | True | True |
| weighted_sampling | True | True |

两者都是 510 steps（2718 samples × 3 epochs / 16 = 510），进一步确认 effective batch size 一致。

任务描述中 s43 的 `--batch 1 --grad_accum 16` 参数名在脚本中不存在——实际运行的 s43 用的是默认值 batch=4、accum=4。

### 进程状态

| PID | 运行时间 | 状态 |
|-----|---------|------|
| 275269 (s43) | 8h21m | 存活，约 84/510 steps (16%) |
| 276143 (s45) | 1h53m | 存活，约 15/510 steps (3%) |

**结论：两组训练参数完全一致（仅 seed 不同），满足 paired t-test 要求，不需要重启。**

---
