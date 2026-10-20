# code check stability pid

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_stability_pid_20260517T031858_result.json`
- **Structured JSON:** [`4c2a00bd201db47c67b5.json`](../../sessions/4c/4c2a00bd201db47c67b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Stability test 进程：**
- **PID: 406717**
- 命令: `python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path .../Qwen3-8B --output_path outputs/stability_seed123.jsonl --device cuda:0 --seed 123 --decoding_strategy greedy --temperature 0.0`
- 父进程 PID 406710 (`bash run_stability_test.sh`)，由 PID 406709 启动

**Tmux session：**
- `llama_beam` — 这个跑的是另一个任务（Llama beam search，PID 406047）

**注意：** Stability test 实际运行在 **cuda:0** 而非 cuda:1，且当前只跑了 seed 123（第一个 seed）。它没有在 tmux 里，是通过 nohup 后台启动的，日志在 `outputs/stability_test.log`。

---
