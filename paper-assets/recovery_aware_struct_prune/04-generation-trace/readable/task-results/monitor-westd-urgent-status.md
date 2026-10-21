# monitor westd urgent status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd_urgent_status_20260516T180049_result.json`
- **Structured JSON:** [`46dceaea983c8abf87f5.json`](../../sessions/46/46dceaea983c8abf87f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 GPU 状态总览

### GPU 占用表

| GPU | VRAM 占用 | PID | 实验名 | 状态 |
|-----|-----------|-----|--------|------|
| cuda:0 | 12,663 / 97,887 MiB (92% util) | 30610 | eval_sft_rasp_rlvr_20_qwen_math (greedy) | Running |
| cuda:1 | 0 / 97,887 MiB (0% util) | — | 空闲 | Idle |
| cuda:2 | 29,171 / 97,887 MiB (91% util) | 25442 | eval_pass_k8_rasp_20_sft_qwen_math | Running (1h17m) |
| cuda:3 | 29,621 / 97,887 MiB (91% util) | 25538 | eval_pass_k8_rasp_20_grpo_qwen_math | Running (1h16m) |

### RLVR Pipeline (cuda:0)
- PID 28243 已不存在（原 RLVR 训练已结束）
- tmux session `eval_sft_rasp_rlvr_20_qwen_math` 存在，正在运行 greedy eval
- PID 30610 正在评估 `sft_rasp_rlvr_20_qwen_math` 模型（greedy，无 pass@k）

### pass@k 评估状态
- **cuda:2** (PID 25442): `sft_qwen_math_rasp_20` pass@8 评估中，已跑 1h17m
- **cuda:3** (PID 25538): `grpo_rasp_qwen_math` pass@8 评估中，已跑 1h16m
- 两个均未产出结果文件

### 已完成的 pass@k 结果

| 模型 | pass@8 | accuracy | stderr |
|------|--------|----------|--------|
| grpo_unpruned_v2 (baseline) | **0.965** | 0.965 | ±0.013 |

（`eval_pass_k8_unpruned_qwen_math.json` — 200 problems, temp=0.7, k=8）

### 总结
- **cuda:1 完全空闲**，可立即使用
- 3 个评估任务并行运行中（1 greedy + 2 pass@k），预计 pass@k 还需一段时间完成

---
