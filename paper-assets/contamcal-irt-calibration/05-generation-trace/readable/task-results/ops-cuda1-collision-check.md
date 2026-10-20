# ops cuda1 collision check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-collision-check_20260518T165127_result.json`
- **Structured JSON:** [`b9dbd774a7ed0ec62e12.json`](../../sessions/b9/b9dbd774a7ed0ec62e12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**cuda:1 无冲突，但情况与预期不同：**

| 项目 | 状态 |
|---|---|
| **PID 42743 (d025_s123)** | **存在且活跃** — 正在 cuda:1 跑 `train_sft.py --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-7B_d025_s123 --seed 123 --lora-alpha 32`，占用 62GB VRAM，GPU util 98% |
| **d100_s123** | **不存在** — 无对应 tmux session，无任何相关进程。`submit_training_job` 提交可能失败或未实际执行 |
| **tmux sessions** | 仅 `wait_d025`（内容为空） |
| **cuda:1 进程数** | 仅 1 个（PID 42743），无冲突 |

**关键问题：**
1. **Director 说 cuda:1 空闲（0% util, 0 MiB）是错误的** — 实际 98% util、62GB 占用，d025_s123 一直在跑
2. **d100_s123 提交到了一个已被占用的 GPU** — 但幸运的是该提交似乎没有成功启动，所以没有造成实际冲突
3. 需要检查 `submit_training_job` 的返回/日志，确认 d100_s123 为什么没有启动

---
