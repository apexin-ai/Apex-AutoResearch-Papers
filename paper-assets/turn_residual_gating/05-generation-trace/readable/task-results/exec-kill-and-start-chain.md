# exec kill and start chain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_kill_and_start_chain_20260523T075318_result.json`
- **Structured JSON:** [`fec6fb87abf88d823ec4.json`](../../sessions/fe/fec6fb87abf88d823ec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **PID 84029 (split-softmax eval)**: 已成功 kill
- **GPU 空闲**: **No** — GPU 显存当前 0MiB，但有一个刚启动的训练进程正在占用 CPU/内存，即将占用 GPU：
  - **PID 84793** — `train_phase2_v8b.py`，参数 `--gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123`，已运行约 14 秒，占用 1.3% 内存（~14GB RAM），CPU 212%
- **其他进程**: tensorboard (PID 895) 和 jupyter-lab (PID 898)，系统服务，无需处理

**结论**: GPU 物理上空闲但 PID 84793 的训练进程刚启动、即将占用 GPU。**不能立即启动 gpu_chain_next.sh**，除非先 kill 84793。需要你确认 84793 是否要保留。

---
