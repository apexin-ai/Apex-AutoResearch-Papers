# check exp1 training status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp1-training-status_20260514T230823_result.json`
- **Structured JSON:** [`4387309f1a5e0b1fd09f.json`](../../sessions/43/4387309f1a5e0b1fd09f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 状态报告

**进程**
- `exp1_isr_b03_s43` (PID 963576): **DEAD** — 训练完成（reward_log 到 step 500，full model weights 已保存）
- `exp1_random_b03_s43` (PID 963653): **ALIVE** — etime 01:16:37, reward_log 到 step 339/500（约 68%）

**GPU**
- GPU 0: 0%, 0 MiB — 空闲（ISR 已完成释放）
- GPU 1: 94%, 83123/97887 MiB — Random 训练中

**Checkpoints/Output**
- ISR: 完整 model-{1..4}-of-4.safetensors + checkpoint-500/trainer_state.json + reward_log.jsonl（step 500 完整）
- Random: 仅 checkpoint-300/trainer_state.json + reward_log.jsonl（运行中，下一个保存点 checkpoint-400）
- 无独立 eval_*.json 文件

**磁盘**
- /root/autodl-tmp: 150G/250G, **60%** — 健康

**tmux**: 工具限制（read-only 模式禁止 tmux 命令），无法直接列出 session

**ETA**: Random 当前 step 339，按 ISR 完成节奏（500 步约 1h17min），剩余 161 步约 ~33 分钟完成。

---
