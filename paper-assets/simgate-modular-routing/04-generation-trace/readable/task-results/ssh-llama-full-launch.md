# ssh llama full launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-full-launch_20260519T022055_result.json`
- **Structured JSON:** [`be1faf76d682371aa807.json`](../../sessions/be/be1faf76d682371aa807.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张卡都在正常推理，vLLM 运行流畅。

## 产出报告

| 项目 | 值 |
|---|---|
| **模型** | `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct` (实际路径 `LLM-Research/Meta-Llama-3___1-8B-Instruct`) |
| **GPU 0** | RTX 5090, 28017/32607 MiB, 100% 利用率, vLLM PID 277224 |
| **GPU 1** | RTX 5090, 28017/32607 MiB, 100% 利用率, vLLM PID 277468 |
| **tmux session** | `llama-full-gpu0` (6 tasks), `llama-full-gpu1` (5 tasks) |
| **脚本** | 已有 `scripts/run_llama_full_gpu0.sh` 和 `run_llama_full_gpu1.sh`，未做修改 |
| **配置** | 11 tasks × 20 episodes × 2 conditions, seed=42, max_steps=30 |
| **Dry-run** | `llama_cross_model_full_dryrun/freeze/` 1 episode 成功完成，输出格式正确 |
| **日志** | `results/llama_cross_model_full/gpu0.log`, `gpu1.log` |
| **预估完成时间** | GPU 0: ~9.4h (6 tasks), GPU 1: ~7.8h (5 tasks) → 约 5/19 20:00 前完成 |

**注意**: 之前 `llama-dry30` 因 vLLM EngineDeadError 崩溃，已清理。当前全量实验两卡同时跑，推理速度 ~90 toks/s output，运行正常。

---
