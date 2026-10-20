# monitor gpu status and pending evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu-status-and-pending-evals_20260516T145422_result.json`
- **Structured JSON:** [`6f290872c76aca4a4251.json`](../../sessions/6f/6f290872c76aca4a4251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态

| GPU | 状态 | PID | 进程 | 显存 |
|-----|------|-----|------|------|
| 0 | **空闲** | - | - | 0 MiB |
| 1 | 运行中 | 290182 | `eval/injected_eval.py` vanilla-s123 injected | 16,828 MiB |
| 2 | 运行中 | 277781 | swift sft llama31-taxei-s123 | 31,950 MiB |
| 3 | 运行中 | 277973 | swift sft llama31-random-s123 | 31,950 MiB |

### Clean Eval 结果（已完成，已注册 registry）

| 实验 | success_rate | episodes |
|------|-------------|----------|
| llama31-taxei-s42-clean | **0.766** | 47 |
| llama31-random-s0-clean | **0.745** | 47 |
| llama31-vanilla-s123-clean | **0.723** | 47 |

### Scale-up 数据收集（PID 266813 已结束）

产出在 `data/trajectories_scaleup_p1/`：
- `successful_trajectories.jsonl`: 797 条
- `failed_trajectories.jsonl`: 2,736 条

### Vanilla s123 injected eval

已有另一个 worker 在 cuda:1 启动了正确的命令（PID 290182，运行 2.5 分钟）：
```
python eval/injected_eval.py --model_path output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635 \
  --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --model_variant vanilla --num_episodes 47 --seed 123 \
  --output eval_results/llama31_vanilla_s123_injected.json
```

注意：我之前尝试用 `recovery.py --adapter` 启动失败（参数名不对），但没有影响——因为已有进程在跑。我的错误启动覆盖了 `.log` 文件，但 eval 进程本身正常运行中。

---
