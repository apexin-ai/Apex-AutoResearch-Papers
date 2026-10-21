# ssh check westd completed evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_completed_evals_20260522T142520_result.json`
- **Structured JSON:** [`1fadcd5295a51608fae0.json`](../../sessions/1f/1fadcd5295a51608fae0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都仍在运行中。汇报如下：

## 状态汇总

### 1. α=3.0 GRPO eval (PID 43755)
- **状态**: 运行中，88%（1163/1319），已跑 2h26m
- **当前 acc**: **63.04%**（1150 样本时）
- **预估剩余**: ~12 分钟（156 样本 × ~3s/it）
- GPU: cuda:0

### 2. seed123 eval (PID 46229)
- **状态**: 运行中，95%（1249/1319），已跑 1h43m
- **当前 acc**: **52.00%**（1200 样本时）
- **预估剩余**: ~4 分钟（70 样本 × ~2.5s/it）
- GPU: cuda:2

### 3. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 99% | 29.6/97.9 GB |
| 1 | 91% | 12.6/97.9 GB |
| 2 | 99% | 26.2/97.9 GB |
| 3 | 94% | 12.7/97.9 GB |

### 4. 新启动的实验
已有两个新 eval 在跑：
- **depth-first GRPO eval** (PID 51986) — cuda:3，刚启动 ~2min
- **depth-first SFT eval** (PID 52151) — cuda:1，刚启动 ~2min

seed123 预计 ~4 分钟内完成，α=3.0 预计 ~12 分钟内完成。

---
