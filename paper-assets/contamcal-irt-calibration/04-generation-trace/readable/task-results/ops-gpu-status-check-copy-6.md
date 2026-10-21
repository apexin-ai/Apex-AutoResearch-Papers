# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T110901_result.json`
- **Structured JSON:** [`a47397ccd6bc7de704a5.json`](../../sessions/a4/a47397ccd6bc7de704a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态摘要

| GPU | 实验 | PID | 运行时间 | 显存 | 进度 | ETA |
|-----|------|-----|---------|------|------|-----|
| 0 | exp-002 0.5B signals | 353390 | 23min | 2GB/24GB | **Task 4/9** (d005/mmlu) | ~1h+ |
| 1 | 1.5B aligned eval | 336765 | 1h51m | 6GB/24GB | GSM8K 75% (994/1319) | ~30min+arc |
| 2 | 0.5B aligned eval | 354435 | 17min | 4GB/24GB | GSM8K_para 84% (191/228) | ~3min+arc |
| 3 | **3B d100 SFT** | 319555 | 4h14m | 13GB/24GB | **Step 3382/4159 (81%)**, loss=1.10 | **~54min** |
| 4 | 3B d005 SFT | 335351 | 1h58m | 22GB/24GB | Step 1663/3177 (52%), loss=1.12 | ~1h38m |
| 5 | 3B d000 aligned eval | 342940 | 1h17m | 9GB/24GB | GSM8K 43% (568/1319) | ~1h30m+arc |

所有 6 个进程均存活。

### cuda:3 — 3B d100 SFT 详情
- 当前 step 3382/4159，**81% 完成**（从上次的 78% 推进了 3%）
- loss 稳定在 ~1.10，token accuracy ~0.73
- 速度 ~4.2s/step，剩余 777 steps ≈ **54 分钟**
- Checkpoint 目录 `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/` 存在但尚无 lora_adapter（应在训练完成时保存）

### 异常发现
**exp-002 signals (cuda:0): Task 2 和 Task 3 失败。** d000_s42/gsm8k 和 d000_s42/arc_challenge 均报错（stderr 显示模型类型列表，疑似模型加载问题）。Task 1 (d000/mmlu) 成功，Task 4 (d005/mmlu) 正在运行。已产出信号文件：d000_s42 有 5 个，d005_s42 有 1 个。需要排查 gsm8k/arc_challenge 的失败原因。

---
