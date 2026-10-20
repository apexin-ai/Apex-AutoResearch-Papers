# monitor qwen14b find pid

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_qwen14b-find-pid_20260513T085700_result.json`
- **Structured JSON:** [`f5ed8c3c0cdf43e07f3a.json`](../../sessions/f5/f5ed8c3c0cdf43e07f3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 项目 | 详情 |
|------|------|
| **Eval 进程** | PID **138858** — `python run_mvp_experiment.py --skip-vllm --end-index 20 --num-trials 1 --output-dir .../qwen14b_bcp/run_1 --vllm-port 8005` |
| **Eval 外壳脚本** | PID **138748** — `bash eval_qwen14b_fp16_bcp.sh`（无独立 tmux session，由 nohup 后台启动） |
| **vLLM 进程** | PID **10408** — Qwen2.5-14B-Instruct on port 8005, tensor-parallel=2, GPU 2,3 |
| **Eval 进度** | run_1 下已产生 1 个结果 JSON（range 0-20），eval.log 最新活动 16:57，正在执行中 |
| **GPU 占用** | GPU 0: 21%, 12.6GB (datagen) / GPU 1: 10%, 13.7GB (datagen) / **GPU 2: 45%, 21.9GB (vLLM)** / **GPU 3: 100%, 21.9GB (vLLM)** / GPU 4: 20%, 12.6GB (datagen) / GPU 5: 空闲 |

BCP eval 正在运行中，无需干预。

---
