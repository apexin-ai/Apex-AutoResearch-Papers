# ssh check westd eval progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_eval_progress_20260522T141813_result.json`
- **Structured JSON:** [`99de5164009a75c364b8.json`](../../sessions/99/99de5164009a75c364b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在运行中，汇总如下：

| 实验 | PID | 状态 | 进度 | 当前 acc | GPU |
|------|-----|------|------|----------|-----|
| eval_gsm8k_grpo_rasp_alpha3p0_20 | 43755 | **running** (2h24m) | **1128/1319 (86%)** | 63.0% (↓0.4 from 63.4%) | cuda:0, 99% util, 30GB/98GB |
| eval_gsm8k_grpo_random_20_seed123 | 46229 | **running** (1h42m) | **1190/1319 (90%)** | 51.9% (↓1.1 from 53.0%) | cuda:2, 91% util, 26GB/98GB |

- 两个实验速度约 2-3s/it，预计 **random_20 约 5-8 分钟完成，alpha3p0 约 10-15 分钟完成**
- 磁盘 `/root/autodl-tmp/` 使用 89% (574G/650G)，剩余 77GB 足够
- GPU:1 和 GPU:3 空闲

---
