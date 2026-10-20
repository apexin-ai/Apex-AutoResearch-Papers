# diagnose pass k and rlvr status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pass_k_and_rlvr_status_20260516T182246_result.json`
- **Structured JSON:** [`5d94103c8a2fb37e9b40.json`](../../sessions/5d/5d94103c8a2fb37e9b40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### Part 1: pass@k 结果（全部完成，registry 已更新）

| Experiment | pass@8 | stderr |
|---|---|---|
| Unpruned GRPO (baseline) | **0.965** | ±0.013 |
| RASP-20 SFT | **0.935** | ±0.017 |
| RASP-20 GRPO | **0.915** | ±0.020 |

### Part 2: RLVR eval

- `eval_sft_rasp_rlvr_20_qwen_math` — **完成**，greedy accuracy = **0.73** (146/200)
- GRPO 已启动：PID **32087**，tmux session `grpo_rasp_rlvr_20_qwen_math`，cuda:0，正在加载模型

### Part 3: GPU 空闲情况

| GPU | 状态 |
|---|---|
| cuda:0 | GRPO 训练中（刚启动） |
| cuda:1 | **空闲** |
| cuda:2 | **空闲** |
| cuda:3 | **空闲** |

3 张 GPU 可用于下一步实验。

---
